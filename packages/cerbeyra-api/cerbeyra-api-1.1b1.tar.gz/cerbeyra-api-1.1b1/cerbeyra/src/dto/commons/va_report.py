import csv
import uuid
import shutil
import openpyxl
from typing import Generator, Any, Set, List, Dict
from cerbeyra.src.dto.commons.va_item import VAItem
from cerbeyra.src.dto.factories.factories import VaItemFactory


class VAReport:
    """
    This super class defines a vulnerability assessment report object.
    """

    def __init__(self, csv_file_path: str, queried_fields: list):
        self.csv_file_path = csv_file_path
        self.queried_fields = queried_fields

    def iterate_entries(self) -> Generator[VAItem, Any, None]:
        """
        Reads the report file specified in 'csv_file_path' and returns a generator over report entries.

        :return: a Generator of VaItem objects.
        """
        idx_entry = 0
        with open(self.csv_file_path, 'r') as f:
            report_entries = csv.reader(f, delimiter=',')
            for entry in report_entries:
                if idx_entry > 0:
                    yield VaItemFactory.build_from_row(self.queried_fields, entry)
                idx_entry += 1

    def _get_distinct_field(self, field: str) -> Set[str]:
        """
        Gets a set of items belonging to specific fields.

        :param field: the queried report field.
        :return: a set of value associated to the queried field.
        """
        return set(self._get_field(field))

    def _get_field(self, field: str) -> List[str]:
        """
        Gets a list of all items belonging to specific fields.

        :param field: the queried fields.
        :return: a list of report values.
        """
        return [item.get_field(field) for item in self.iterate_entries()]

    def _group_by_field(self, field: str) -> Dict[str, List[VAItem]]:
        """
        Groups the report items by specific field.

        :param field: the queried field.
        :return: a dictionary containing the grouped items.
        """
        grouped_by_entries = dict()
        for item in self.iterate_entries():
            field_value = item.get_field(field)
            if field_value not in grouped_by_entries.keys():
                grouped_by_entries[field_value] = list()
            grouped_by_entries[field_value].append(item)
        return grouped_by_entries

    def _count_by_field(self, field: str) -> Dict[str, int]:
        """
        Counts report items by specific field.

        :param field: the queried field.
        :return: a dictionary containing the counts.
        """
        grouped_entries = self._group_by_field(field)
        return {k: len(v) for k, v in grouped_entries.items()}

    def save_csv(self, path=None):
        """
        Saves report as .csv file. If the saving path is not specified, then a universally unique identifier
        will be used as file name.

        :param path: the file saving location.
        """
        if not path:
            path = f"{uuid.uuid4()}.csv"
        shutil.copy(self.csv_file_path, path)

    def save_xls(self, path=None):
        """
        Saves report as .xlsx file. If the saving path is not specified, then a universally unique identifier
        will be used as file name.

        :param path: the file saving location.
        """
        if not path:
            path = f"{uuid.uuid4()}.xlsx"
        work_book = openpyxl.Workbook()
        work_sheet = work_book.active
        work_sheet.append(self.queried_fields)
        with open(self.csv_file_path, 'r') as f:
            report_entries = csv.reader(f, delimiter=',')
            idx_entry = 0
            for entry in report_entries:
                if idx_entry > 0:
                    work_sheet.append(entry)
                idx_entry += 1
            work_book.save(path)

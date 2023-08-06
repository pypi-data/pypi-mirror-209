from typing import Set, Dict, List

from cerbeyra.src.dto.commons import VAReport, VAItem
from cerbeyra.src.types import WebReportFields


class WebReport(VAReport):
    """
    Defines a WebReport object. Contains a set of functions to easily manipulate report entries.
    It consists of a VAItems list.
    """

    def __init__(self, csv_file_path, queried_fields):
        super().__init__(csv_file_path, queried_fields)
        self.__check_fields()

    def group_by_threat(self) -> Dict[str, List[VAItem]]:
        """
        Groups the report items by threat.

        :return: a dictionary containing the grouped VAItems.
        """
        if WebReportFields.threat.value not in self.queried_fields:
            return dict()
        return super()._group_by_field(field=WebReportFields.threat.value)

    def get_distinct_hosts(self) -> Set[str]:
        """
        Gets the set of scanned host.

        :return: a set of host.
        """
        if WebReportFields.host.value not in self.queried_fields:
            return set()
        return super()._get_distinct_field(WebReportFields.host.value)

    def get_distinct_urls(self) -> Set[str]:
        """
        Gets the set of scanned urls.

        :return: a set of urls.
        """
        if WebReportFields.url.value not in self.queried_fields:
            return set()
        return super()._get_distinct_field(WebReportFields.url.value)

    def count_by_threat(self) -> Dict[str, int]:
        """
        Counts report items by threat.

        :return: a dictionary containing item counts per threat level.
        """
        if WebReportFields.threat.value not in self.queried_fields:
            return dict()
        return super()._count_by_field(WebReportFields.threat.value)

    def __check_fields(self):
        """
        Checks whether the queried fields correspond to WebReport items.

        :return: None
        """
        for queried_field in self.queried_fields:
            try:
                WebReportFields(queried_field)
            except ValueError:
                raise AttributeError

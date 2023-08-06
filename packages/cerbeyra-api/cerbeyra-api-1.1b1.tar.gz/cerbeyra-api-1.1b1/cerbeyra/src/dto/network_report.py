from typing import Set, Dict, List
from cerbeyra.src.dto.commons import VAReport, VAItem
from cerbeyra.src.types import NetworkReportFields


class NetworkReport(VAReport):
    """
    Defines a NetworkReport object. Contains a set of functions to easily manipulate report entries.
    It consists of a VAItems list.
    """

    def __init__(self, csv_file_path, queried_fields):
        """
        Makes a NetworkReport object from the corresponding csv file.

        :param csv_file_path: a reference for the csv file location.
        :param queried_fields: the list of requested network report fields (through URL params).
        """
        super().__init__(csv_file_path, queried_fields)
        self.__check_fields()

    def group_by_threat(self) -> Dict[str, List[VAItem]]:
        """
        Groups the report items by threat.

        :return: a dictionary containing the grouped VAItems.
        """
        if NetworkReportFields.threat.value not in self.queried_fields:
            return dict()
        return super()._group_by_field(field=NetworkReportFields.threat.value)

    def get_distinct_hosts(self) -> Set[str]:
        """
        Gets the set of scanned host.

        :return: a set of host.
        """
        if NetworkReportFields.host.value not in self.queried_fields:
            return set()
        return super()._get_distinct_field(NetworkReportFields.host.value)

    def count_by_threat(self) -> Dict[str, int]:
        """
        Counts report items by threat.

        :return: a dictionary containing item counts per threat level.
        """
        if NetworkReportFields.threat.value not in self.queried_fields:
            return dict()
        return super()._count_by_field(NetworkReportFields.threat.value)

    def __check_fields(self):
        """
        Checks whether the queried fields correspond to NetworkReport items.

        :return: None
        """
        for queried_field in self.queried_fields:
            try:
                NetworkReportFields(queried_field)
            except ValueError:
                raise AttributeError

from enum import Enum
from typing import List, Union
from cerbeyra.src.dto.commons.collection import AggregationMethods
from cerbeyra.src.dto.network_host_vuln import NetworkHostVuln
from cerbeyra.src.dto.commons.collection import Collection
from cerbeyra.src.dto.web_host_vuln import WebHostVuln


class _VulnFilterFields(Enum):
    THREAT = 'threat'
    VULN_ID = 'vuln_id'
    ASSET_ID = 'asset_id'


class _VulnCollection(Collection):
    def group_by_threat(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, _VulnCollection]]
        """
        return self.group_by(_VulnFilterFields.THREAT.value, aggr=aggr)

    def group_by_vuln(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, _VulnCollection]]
        """
        return self.group_by(_VulnFilterFields.VULN_ID.value, aggr=aggr)

    def group_by_asset(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, _VulnCollection]]
        """
        return self.group_by(_VulnFilterFields.ASSET_ID.value, aggr=aggr)

    def filter_by_threat(self, threat: str):
        """
        :return: _VulnCollection
        """
        return self.filter_by(_VulnFilterFields.THREAT.value, threat)

    def filter_by_vuln(self, vuln_id: int):
        """
        :return: _VulnCollection
        """
        return self.filter_by(_VulnFilterFields.VULN_ID.value, vuln_id)

    def filter_by_asset(self, asset_id: int):
        """
        :return: _VulnCollection
        """
        return self.filter_by(_VulnFilterFields.ASSET_ID.value, asset_id)


class WebVulnCollection(_VulnCollection):

    def __init__(self, vulns: List[WebHostVuln]):
        super().__init__(items=vulns)


class NetworkVulnCollection(_VulnCollection):

    def __init__(self, vulns: List[NetworkHostVuln]):
        super().__init__(items=vulns)

from enum import Enum
from typing import List, Union
from cerbeyra.src.dto.scan_results import NetworkScanResult, WebScanResult
from cerbeyra.src.dto.commons.collection import AggregationMethods
from cerbeyra.src.dto.commons.collection import Collection


class _ResultFilterFields(Enum):
    ASSET = 'asset_id'
    PERIMETER = 'perimeter'
    STATUS = 'status'


class _ScanResultCollection(Collection):

    def group_by_asset(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, _ResultCollection]]
        """
        return self.group_by(_ResultFilterFields.ASSET.value, aggr=aggr)

    def group_by_status(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, _ResultCollection]]
        """
        return self.group_by(_ResultFilterFields.STATUS.value, aggr=aggr)

    def group_by_perimeter(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, _ResultCollection]]
        """
        return self.group_by(_ResultFilterFields.PERIMETER.value, aggr=aggr)

    def filter_by_asset(self, asset_id: int):
        """
        :return: _ResultCollection
        """
        return self.filter_by(_ResultFilterFields.ASSET.value, asset_id)

    def filter_by_status(self, status: str):
        """
        :return: _ResultCollection
        """
        return self.filter_by(_ResultFilterFields.STATUS.value, status)

    def filter_by_perimeter(self, perimeter: str):
        """
        :return: _ResultCollection
        """
        return self.filter_by(_ResultFilterFields.PERIMETER.value, perimeter)


class NetworkScanResultCollection(_ScanResultCollection):

    def __init__(self, results: List[NetworkScanResult]):
        super().__init__(items=results)


class WebScanResultCollection(_ScanResultCollection):
    def __init__(self, results: List[WebScanResult]):
        super().__init__(items=results)

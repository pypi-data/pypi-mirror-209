from enum import Enum
from typing import List, Union

from cerbeyra.src.dto.commons.collection import AggregationMethods
from cerbeyra.src.dto.host import Host
from cerbeyra.src.dto.commons.collection import Collection


class _HostFilterFields(Enum):
    ASSET_ID = 'asset_id'
    TYPE = 'type'
    INDEX = 'index'
    PERIMETER = 'perimeter'
    VISIBILITY = 'visibility'


class HostCollection(Collection):

    def __init__(self, hosts: List[Host]):
        super().__init__(items=hosts)

    def group_by_asset(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, HostCollection]]
        """
        return self.group_by(_HostFilterFields.ASSET_ID.value, aggr)

    def group_by_perimeter(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, HostCollection]]
        """
        return self.group_by(_HostFilterFields.PERIMETER.value, aggr)

    def group_by_index(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, HostCollection]]
        """
        return self.group_by(_HostFilterFields.INDEX.value, aggr)

    def group_by_visibility(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, HostCollection]]
        """
        return self.group_by(_HostFilterFields.VISIBILITY.value, aggr)

    def filter_by_asset(self, asset_id: int):
        """
        :return: HostCollection
        """
        return self.filter_by(_HostFilterFields.ASSET_ID.value, asset_id)

    def filter_by_perimeter(self, perimeter: str):
        """
        :return: HostCollection
        """
        return self.filter_by(_HostFilterFields.PERIMETER.value, perimeter)

    def filter_by_index(self, index: str):
        """
        :return: HostCollection
        """
        return self.filter_by(_HostFilterFields.INDEX.value, index)

    def filter_by_visibility(self, visibility: str):
        """
        :return: HostCollection
        """
        return self.filter_by(_HostFilterFields.VISIBILITY.value, visibility)

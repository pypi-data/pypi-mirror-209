from enum import Enum
from typing import List, Union
from cerbeyra.src.dto.asset import Asset
from cerbeyra.src.dto.commons.collection import AggregationMethods
from cerbeyra.src.dto.commons.collection import Collection
from cerbeyra.src.types import AssetTypes, Perimeters


class _AssetFilterFields(Enum):
    TYPE = 'type'
    PERIMETER = 'perimeter'


class AssetCollection(Collection):

    def __init__(self, assets: List[Asset] = None):
        super().__init__(items=assets)

    def group_by_type(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, AssetCollection]]
        """
        return self.group_by(_AssetFilterFields.TYPE.value, aggr)

    def group_by_perimeter(self, aggr: Union[bool, AggregationMethods, None] = None):
        """
        :param aggr:
        :return: Dict[str, Union[int, AssetCollection]]
        """
        return self.group_by(_AssetFilterFields.PERIMETER.value, aggr)

    def filter_by_type(self, asset_type: AssetTypes):
        """
        :return: AssetCollection
        """
        return self.filter_by(_AssetFilterFields.TYPE.value, asset_type.value)

    def filter_by_perimeter(self, perimeter: Perimeters):
        """
        :return: AssetCollection
        """
        return self.filter_by(_AssetFilterFields.PERIMETER.value, perimeter.value)

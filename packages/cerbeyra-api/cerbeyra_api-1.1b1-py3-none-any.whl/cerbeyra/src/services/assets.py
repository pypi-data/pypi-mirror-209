from cerbeyra.src.dto.collections import AssetCollection, HostCollection
from cerbeyra.src.dto.factories.factories import HostFactory, AssetFactory
from cerbeyra.src.services.base import Base


class Assets(Base):
    __asset_list_uri = 'assets'
    __asset_detail_uri = 'assets/{asset_id}'
    __host_list_uri = 'hosts'

    def get_all_assets(self, client_id: int = None, search: str = None, visibility: str = None,
                       perimeter: str = None, types: list[str] = None) -> AssetCollection:
        params = self.__build_common_filter(search=search, visibility=visibility, perimeter=perimeter)
        if types:
            params['types[]'] = types
        assets_response = self._client.get(self.__asset_list_uri, params=params, client_id=client_id)
        return AssetCollection([AssetFactory.build_from_json(asset) for asset in assets_response.json()])

    def get_all_hosts(self, client_id: int = None, asset_id: int = None, search: str = None, visibility: str = None,
                      perimeter: str = None, host_type: str = None) -> HostCollection:
        params = self.__build_common_filter(search=search, visibility=visibility, perimeter=perimeter)
        if host_type:
            params['type'] = host_type
        url = self.__host_list_uri
        if asset_id:
            url = f"{self.__asset_detail_uri.format(asset_id=asset_id)}/{url}"
        hosts_response = self._client.get(url, params=params, client_id=client_id)
        return HostCollection([HostFactory.build_from_json(host) for host in hosts_response.json()])

    @staticmethod
    def __build_common_filter(search=None, visibility=None, perimeter=None):
        params = {}
        if search is not None:
            params['search'] = search
        if visibility is not None:
            params['visibility'] = visibility
        if perimeter is not None:
            params['perimeter'] = perimeter
        return params

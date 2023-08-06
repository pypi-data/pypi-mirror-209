from cerbeyra.src.dto.collections import NetworkVulnCollection, WebVulnCollection
from cerbeyra.src.dto.factories.factories import NetworkHostVulnFactory, WebHostVulnFactory
from cerbeyra.src.services.base import Base


class Vulnerabilities(Base):
    __vulnerabilities_uri = "vulns/{type}"
    __asset_sub_uri = "/assets/{asset_id}"
    __host_sub_uri = "/hosts/{host}"

    def __build_api(self, vulnerability_type: str, asset_id=None, host_id=None):
        uri = self.__vulnerabilities_uri.format(type=vulnerability_type)
        if asset_id is not None:
            uri += self.__asset_sub_uri.format(asset_id=asset_id)
            if host_id is not None:
                uri += self.__host_sub_uri.format(host_id=host_id)
        return uri

    def get_network_vulns(self, client_id: int = None, asset_id: int = None, host_id: int = None, threat: list = None,
                          exclusion: bool = None, host_visibility: str = None, asset_visibility: str = None,
                          detail: int = None) -> NetworkVulnCollection:

        params = self.__build_common_filter(threat, exclusion, host_visibility, asset_visibility, detail)

        url = self.__build_api('network', asset_id=asset_id, host_id=host_id)
        network_response = self._client.get(url, params=params, client_id=client_id)
        return NetworkVulnCollection([NetworkHostVulnFactory.build_from_json(v) for v in network_response.json()])

    def get_web_vulns(self, client_id: int = None, asset_id: int = None, host_id: int = None, threat: list = None,
                      exclusion: bool = None, host_visibility: str = None, asset_visibility: str = None,
                      detail: int = None) -> WebVulnCollection:

        params = self.__build_common_filter(threat, exclusion, host_visibility, asset_visibility, detail)
        if threat:
            params['threat[]'] = threat
        if detail:
            params['detailLevel'] = detail
        if exclusion:
            params['exclusion'] = 1 if exclusion else 0
        if host_visibility:
            params['hostVisibility'] = host_visibility
        if asset_visibility:
            params['assetVisibility'] = asset_visibility

        url = self.__build_api('web', asset_id=asset_id, host_id=host_id)
        web_response = self._client.get(url, params=params, client_id=client_id)
        return WebVulnCollection([WebHostVulnFactory.build_from_json(v) for v in web_response.json()])

    @staticmethod
    def __build_common_filter(threat: list = None, exclusion: bool = None, host_visibility: str = None,
                              asset_visibility: str = None, detail: int = None):
        params = {}
        if threat is not None:
            params['threat[]'] = threat
        if detail is not None:
            params['detailLevel'] = detail
        if exclusion is not None:
            params['exclusion'] = 1 if exclusion else 0
        if host_visibility is not None:
            params['hostVisibility'] = host_visibility
        if asset_visibility is not None:
            params['assetVisibility'] = asset_visibility
        return params

from cerbeyra.src.services.base import Base
from cerbeyra.src.dto.collections import NetworkScanResultCollection, WebScanResultCollection
from cerbeyra.src.dto.factories.factories import NetworkResultFactory
from cerbeyra.src.dto.factories.factories import WebResultFactory


class ScanResults(Base):
    __scan_results_uri = "scans/{type}/results"
    __asset_sub_uri = "assets/{asset_id}/scans/results"

    def __build_api(self, scan_type: str, asset_id: int = None) -> str:
        uri = self.__scan_results_uri.format(type=scan_type)
        if asset_id is not None:
            uri = self.__asset_sub_uri.format(asset_id=asset_id)
        return uri

    @staticmethod
    def __build_common_params(search: str = None, perimeter: str = None, probe: str = None,
                              include_excluded: bool = None, status: str = None, from_date: str = None,
                              to_date: str = None) -> dict:
        params = {}
        if search is not None:
            params['search'] = search
        if perimeter is not None:
            params['perimeter'] = perimeter
        if probe is not None:
            params['probe'] = probe
        if include_excluded is not None:
            params['includeExcluded'] = 1 if include_excluded else 0
        if status is not None:
            params['status[]'] = status
        if from_date is not None:
            params['fromDate'] = from_date
        if to_date is not None:
            params['toDate'] = to_date
        return params

    def get_network_scans(self, client_id: int = None, asset_id: int = None, search: str = None,
                          perimeter: str = None, probe: str = None, include_excluded: bool = None,
                          status: str = None, from_date: str = None,
                          to_date: str = None) -> NetworkScanResultCollection:

        url = self.__build_api(scan_type='network', asset_id=asset_id)
        params = self.__build_common_params(search, perimeter, probe, include_excluded, status, from_date, to_date)
        network_response = self._client.get(url, params=params, client_id=client_id)
        network_results = [NetworkResultFactory.build_from_json(result)
                           for result in network_response.json() if result.get('type') == 'network']
        return NetworkScanResultCollection(network_results)

    def get_web_scans(self, client_id: int = None, asset_id: int = None, search: str = None,
                      perimeter: str = None, probe: str = None, include_excluded: bool = None,
                      status: str = None, from_date: str = None, to_date: str = None) -> WebScanResultCollection:

        url = self.__build_api(scan_type='web', asset_id=asset_id)
        params = self.__build_common_params(search, perimeter, probe, include_excluded, status, from_date, to_date)
        web_response = self._client.get(url, params=params, client_id=client_id)
        web_results = [WebResultFactory.build_from_json(result)
                       for result in web_response.json() if result.get('type') == 'web']
        return WebScanResultCollection(web_results)

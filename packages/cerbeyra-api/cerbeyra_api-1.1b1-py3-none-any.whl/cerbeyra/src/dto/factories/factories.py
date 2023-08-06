import re
from cerbeyra.src.dto.commons.va_item import VAItem
from cerbeyra.src.dto.cerbeyra_index import CerbeyraIndex
from cerbeyra.src.dto.probe import Probe
from cerbeyra.src.dto.sensor import Sensor
from cerbeyra.src.dto.client import Client
from cerbeyra.src.dto.host import Host
from cerbeyra.src.dto.network_host_vuln import NetworkHostVuln
from cerbeyra.src.dto.web_host_vuln import WebHostVuln
from cerbeyra.src.dto.asset import Asset
from cerbeyra.src.dto.technical_info import TechnicalInfo, HistoryInfo
from cerbeyra.src.dto.scan_results import NetworkScanResult, WebScanResult


def _camel_to_snake(camel_name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_name).lower()


class CerbeyraIndexFactory:
    """
    Defines a factory method for building CerbeyraIndex objects.
    """

    @staticmethod
    def build_from_json(json_file: dict) -> CerbeyraIndex:
        """
        Builds a CerbeyraIndex object from the corresponding json data
        .
        :param json_file: a dictionary containing the CerbeyraIndex data.
        :return: a CerbeyraIndex object.
        """
        json_file['index'] = json_file.pop('cerbeyraIndex')
        json_file = {_camel_to_snake(k): json_file[k] for k in json_file}
        return CerbeyraIndex(**json_file)


class ClientFactory:
    """
     Defines a factory method for building Client objects.
     """

    @staticmethod
    def build_from_json(json_file: dict) -> Client:
        """
        Builds a Client object from the corresponding json data.

        :param json_file: a dictionary containing Client data.
        :return: a Client object.
        """
        json_file['client_id'] = json_file.pop('id')
        return Client(**json_file)


class ProbeFactory:
    """
    Defines a factory method for building Probe objects.
    """

    @staticmethod
    def build_from_json(json_file: dict) -> Probe:
        """
        Builds a Probe object from the corresponding json data.

        :param json_file: a dictionary containing Probe data.
        :return: a Probe object.
        """
        json_file['last_update'] = json_file.pop('lastUpdate')
        json_file['probe_id'] = json_file.pop('id')
        client_obj = None
        if 'client' in json_file:
            client_json = json_file['client']
            json_file.pop('client')
            client_obj = ClientFactory.build_from_json(client_json)
        return Probe(**json_file, client=client_obj)


class SensorFactory:
    """
    Defines a factory method for building Sensor objects.
    """

    @staticmethod
    def build_from_json(json_file: dict) -> Sensor:
        """
        Builds a Sensor object from the corresponding json data.
        :param json_file: a dictionary containing Sensor data.
        :return: a Sensor object.
        """
        json_file['probe_gateway'] = json_file.pop('probeGateway')
        json_file['last_update'] = json_file.pop('lastUpdate')
        client_obj = None
        if 'client' in json_file:
            client_json = json_file['client']
            json_file.pop('client')
            client_obj = ClientFactory.build_from_json(client_json)
        return Sensor(**json_file, client=client_obj)


class VaItemFactory:
    """
    Defines a factory method for building VaItem objects.
    """

    @staticmethod
    def build_from_row(columns: list, entry_data: list) -> VAItem:
        """
        Builds a ReportItem object from key-value pairs specified in columns and
        entry_data respectively.

        :param columns: a list of fields either defined in WebReport or NetworkReport.
        :param entry_data: a list of values whose items are associated to the queried columns.
        :return: a ReportItem object.
        """
        d = {col: entry_data[i] for i, col in enumerate(columns)}
        return VAItem(**d)


class HostFactory:

    @staticmethod
    def build_from_json(json_file: dict) -> Host:
        json_file = {_camel_to_snake(k): json_file[k] for k in json_file}
        return Host(**json_file)


class NetworkHostVulnFactory:

    @staticmethod
    def build_from_json(json_file: dict) -> NetworkHostVuln:
        json_file = {_camel_to_snake(k): json_file[k] for k in json_file}
        return NetworkHostVuln(**json_file)


class WebHostVulnFactory:

    @staticmethod
    def build_from_json(json_file: dict) -> WebHostVuln:
        json_file = {_camel_to_snake(k): json_file[k] for k in json_file}
        return WebHostVuln(**json_file)


class AssetFactory:
    @staticmethod
    def build_from_json(json_file: dict) -> Asset:
        json_file = {_camel_to_snake(k): json_file[k] for k in json_file}
        return Asset(**json_file)


class TechnicalFactory:
    @staticmethod
    def build_from_json(json_file: dict) -> TechnicalInfo:
        history = json_file.get('history', dict())
        return TechnicalInfo(
            history=TechnicalFactory.build_history({_camel_to_snake(k): history[k] for k in history}),
            index=CerbeyraIndexFactory.build_from_json(json_file.get('index')),
            vulnerability_assessment=json_file.get('vulnerabilityAssessment')
        )

    @staticmethod
    def build_history(json_file: dict):
        return HistoryInfo(**json_file)


class NetworkResultFactory:

    @staticmethod
    def build_from_json(json_file: dict) -> NetworkScanResult:
        json_file = {_camel_to_snake(k): json_file[k] for k in json_file}
        return NetworkScanResult(**json_file)


class WebResultFactory:

    @staticmethod
    def build_from_json(json_file: dict) -> WebScanResult:
        json_file = {_camel_to_snake(k): json_file[k] for k in json_file}
        return WebScanResult(**json_file)

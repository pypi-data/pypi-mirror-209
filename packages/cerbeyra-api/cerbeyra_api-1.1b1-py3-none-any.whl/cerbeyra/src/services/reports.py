from cerbeyra.src.dto import NetworkReport, WebReport
from cerbeyra.src.services.base import Base
from cerbeyra.src.types import NetworkReportFields, WebReportFields
from cerbeyra.utils import stream_response_to_temp_file


class Reports(Base):
    __network_report_uri = 'reportnetworkvuln'
    __web_report_uri = 'reportwebvuln'
    __network_default_columns = [
        el.value for el in [
            NetworkReportFields.asset, NetworkReportFields.host, NetworkReportFields.hostname,
            NetworkReportFields.protocol,
            NetworkReportFields.port, NetworkReportFields.threat, NetworkReportFields.cvss,
            NetworkReportFields.vulnerability,
            NetworkReportFields.description, NetworkReportFields.summary, NetworkReportFields.insight,
            NetworkReportFields.impact,
            NetworkReportFields.affected, NetworkReportFields.solution, NetworkReportFields.references,
            NetworkReportFields.vuln_id,
            NetworkReportFields.last_detection, NetworkReportFields.first_detection
        ]
    ]

    __web_default_columns = [
        el.value for el in [
            WebReportFields.asset, WebReportFields.host, WebReportFields.family, WebReportFields.vulnerability,
            WebReportFields.description, WebReportFields.threat, WebReportFields.solution, WebReportFields.url,
            WebReportFields.method, WebReportFields.vuln_id, WebReportFields.last_detection
        ]
    ]

    def get_report_network(self, columns: list[str] = None, client_id: int = None) -> NetworkReport:
        """
        Get the list of every vulnerability detected on your account on every network host.
        you can select a list of columns using the Enum class : types.NetworkReportFields,
        otherwise the API will return a default set of column.
        *For Partners Only:* you can specify a client_id to obtain the information about one of your client.


        :param columns: a list of report fields (defining the query string).
        :param client_id: the unique identifier of a specific client.
        :return: a NetworkReport object.
        """
        if not columns:
            columns = self.__network_default_columns
        params = {'column[]': columns}

        csv_response = self._client.get(self.__network_report_uri, params=params, stream=True, client_id=client_id)
        csv_file = stream_response_to_temp_file(csv_response)
        return NetworkReport(csv_file, columns)

    def get_report_web(self, columns: list[str] = None, client_id: int = None) -> WebReport:
        """
        Get the list of every vulnerability detected on your account on every web host.
        you can select a list of columns using the Enum class : types.WebReportFields,
        otherwise the API will return a default set of column.
        *For Partners Only:* you can specify a client_id to obtain the information about one of your client.

        :param client_id: the unique identifier of a specific client.
        :param columns: a list of report fields (defining the query string).
        :return: a WebReport object.
        """
        if not columns:
            columns = self.__web_default_columns
        params = {'column[]': columns}
        csv_response = self._client.get(self.__web_report_uri, params=params, stream=True, client_id=client_id)
        csv_file = stream_response_to_temp_file(csv_response)
        return WebReport(csv_file, columns)

from typing import List

from cerbeyra.src.dto import Probe, Sensor
from cerbeyra.src.dto.factories.factories import ProbeFactory, SensorFactory
from cerbeyra.src.services.base import Base


class Iot(Base):
    __probes_uri = 'probes'
    __sensors_uri = 'sensors'
    __partner_probes_uri = 'clients/probes'
    __partner_sensors_uri = 'clients/sensors'

    def get_probes(self, status: str = None, client_id: int = None) -> List[Probe]:
        params = {}
        if status:
            params = {'status': status}

        probes_response = self._client.get(self.__probes_uri, params=params, client_id=client_id)
        return [ProbeFactory.build_from_json(probe) for probe in probes_response.json()]

    def get_sensors(self, status: str = None, client_id: int = None) -> List[Sensor]:
        params = {}
        if status:
            params = {'status': status}
        sensors_response = self._client.get(self.__partner_sensors_uri, params=params, client_id=client_id)
        return [SensorFactory.build_from_json(sensor) for sensor in sensors_response.json()]

    def get_all_probes(self, status: str = None) -> List[Probe]:
        """
        *For Partners Only:* gets the list of all probes.
        You can specify a status *(ALIVE, WARNING, DANGER)* to filter away the probes you are not interested on.

        :param status: a probe status (defining the query string).
        :return: a list of Probe objects.
        """
        params = {}
        if status:
            params = {'status': status}

        probes_response = self._client.get(self.__sensors_uri, params=params)
        return [ProbeFactory.build_from_json(probe) for probe in probes_response.json()]

    def get_all_sensors(self, status: str = None) -> List[Sensor]:
        """
        *For Partners Only:* gets the list of all IoT sensors.
        You can specify a status *(ALIVE, WARNING, DANGER)* to filter away the sensors you are not interested on.

        :param status: a sensor status (defining the query string).
        :return: a list of Sensor objects.
        """
        params = {}
        if status:
            params = {'status': status}
        sensors_response = self._client.get(self.__partner_sensors_uri, params=params)
        return [SensorFactory.build_from_json(sensor) for sensor in sensors_response.json()]

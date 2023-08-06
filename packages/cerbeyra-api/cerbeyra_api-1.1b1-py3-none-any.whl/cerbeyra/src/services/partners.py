from typing import List

from cerbeyra.src.dto import Client
from cerbeyra.src.dto.factories.factories import ClientFactory
from cerbeyra.src.services.base import Base


class Partners(Base):
    __clients_uri = 'clients'

    def get_all_clients(self, active: bool = None) -> List[Client]:
        """
        *For Partners Only:* gets the list of all clients.

        :return: a list of Client objects.
        """
        params = {}
        if active:
            params['active'] = 1 if active else 0
        clients_response = self._client.get(self.__clients_uri, params=params)
        try:
            return [ClientFactory.build_from_json(client) for client in clients_response.json()['clients']]
        except KeyError:
            return []

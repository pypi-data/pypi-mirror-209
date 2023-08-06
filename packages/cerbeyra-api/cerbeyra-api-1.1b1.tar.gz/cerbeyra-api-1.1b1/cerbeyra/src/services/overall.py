from cerbeyra.src.dto import CerbeyraIndex
from cerbeyra.src.dto.technical_info import TechnicalInfo
from cerbeyra.src.dto.factories.factories import CerbeyraIndexFactory, TechnicalFactory
from cerbeyra.src.services.base import Base


class Overall(Base):
    __cerbeyra_index_uri = "cerbeyraindex"
    __trend_uri = "technical"

    def get_cerbeyra_index(self, client_id: int = None) -> CerbeyraIndex:
        """
        Returns the *Cerbeyra Index* of the logged user.
        *For Partners Only:* you can specify the client_id to obtain the *Cerbeyra Index* of a specific client.

        :param client_id: the unique identifier of a client.
        :return: a Cerbeyra Index object.
        """
        ci_response = self._client.get(self.__cerbeyra_index_uri, client_id=client_id)
        return CerbeyraIndexFactory.build_from_json(ci_response.json())

    def get_technical_info(self, client_id: int = None, days: int = None) -> TechnicalInfo:
        params = {}
        if days:
            params = {'days': days}
        trend_response = self._client.get(self.__trend_uri, params=params, client_id=client_id)
        return TechnicalFactory.build_from_json(trend_response.json())

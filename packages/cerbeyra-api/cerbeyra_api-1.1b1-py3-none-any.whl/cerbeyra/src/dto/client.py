from dataclasses import dataclass, fields


@dataclass
class Client:
    client_id: int
    name: str
    surname: str
    email: str
    company: str
    active: bool
    expiration_date: str = None

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items() if k in self.fields]

    def __str__(self):
        """
        A string representation of a Client object containing its client_id, name and surname.

        :return: the string representation.
        """
        return f'<Client [{self.client_id}] company={self.company} - ({self.name} {self.surname})>'

    @property
    def fields(self) -> list[str]:
        return [field.name for field in fields(self)]

from dataclasses import dataclass, fields
from cerbeyra.src.dto.client import Client
from cerbeyra.src.types import IoTStatus


@dataclass(kw_only=True)
class Probe:
    name: str
    probe_id: str
    status: IoTStatus
    last_update: str
    client: Client = None

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items() if k in self.fields]
        if self.status is not None:
            self.status = IoTStatus(self.status)

    def __str__(self):
        """
        Defines the string representation for a probe object containing its probe_id and status.

        :return: the string representation.
        """
        if self.client:
            return f'<Probe [{self.probe_id}] {self.name}: {self.status.value} - Client={self.client}>'
        else:
            return f'<Probe [{self.probe_id}] {self.name}: {self.status.value}>'

    @property
    def fields(self) -> list[str]:
        return [field.name for field in fields(self)]

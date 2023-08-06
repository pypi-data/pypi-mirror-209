from dataclasses import dataclass, fields
from cerbeyra.src.dto.client import Client
from cerbeyra.src.types import IoTStatus


@dataclass(kw_only=True)
class Sensor:
    name: str
    probe_gateway: str
    status: IoTStatus
    alarm: str
    last_update: str
    client: Client
    thresholds: list = None
    sensor_id: str = None

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items() if k in self.fields]
        if self.status is not None:
            self.status = IoTStatus(self.status)

    def __str__(self):
        """
        Defines the string representation for a sensor object containing its name and status.

        :return: the string representation.
        """
        if self.client:
            return f'<Sensor [{self.name}] {self.name}: {self.status.value} - Client={self.client}>'
        else:
            return f'<Sensor [{self.name}] {self.name}: {self.status.value}>'

    @property
    def fields(self) -> list[str]:
        return [field.name for field in fields(self)]

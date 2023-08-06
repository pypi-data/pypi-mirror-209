from dataclasses import dataclass, fields
from typing import List

from cerbeyra.src.dto import CerbeyraIndex


@dataclass(kw_only=True)
class HistoryInfo:
    from_date: str
    to_date: str
    index_trend: List[dict]
    anomalies: dict

    def __repr__(self):
        return f"<History {self.from_date} [{','.join(map(lambda el: el['index'], self.index_trend))}] {self.to_date}>"


@dataclass(kw_only=True)
class TechnicalInfo:
    history: HistoryInfo
    index: CerbeyraIndex
    vulnerability_assessment: dict

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items() if k in self.fields]

    @property
    def fields(self) -> list[str]:
        return [field.name for field in fields(self)]

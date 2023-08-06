from dataclasses import dataclass, fields


@dataclass(kw_only=True)
class CerbeyraIndex:
    index: str
    risk_level: str
    explain: dict

    __ci_order = ['A+++', 'A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items() if k in self.fields]

    def __str__(self):
        """
        Defines the string representation for the CerbeyraIndex object.

        :return: the string representation.
        """
        return f"<Index ({self.index}) risk={self.risk_level}>"

    def __eq__(self, other):
        """
        Makes it possible to verify the equality of two CerbeyraIndex object (based on the cerbeyra_index attribute).

        :param other: another CerbeyraIndex object
        :return: a boolean
        """
        return self.index == other.index

    def __gt__(self, other):
        """
        Makes it possible to verify whether a CerbeyraIndex object is greater than another
        (based on the cerbeyra_index attribute).

        :param other: another CerbeyraIndex object
        :return: a boolean
        """
        obj_index = self.__ci_order.index(self.index)
        other_index = self.__ci_order.index(other.index)
        return obj_index < other_index

    @property
    def fields(self) -> list[str]:
        return [field.name for field in fields(self)]

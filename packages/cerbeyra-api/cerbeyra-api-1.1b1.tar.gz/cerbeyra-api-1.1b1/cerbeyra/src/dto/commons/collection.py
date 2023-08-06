from csv import writer
from enum import Enum
from typing import List, Any, Union

from cerbeyra.src.dto.commons.item import Item


class AggregationMethods(Enum):
    COUNT = 'count'


class Collection(list):
    def __init__(self, items: List[Item]):
        super().__init__(items)

    @property
    def length(self):
        return len(self)

    def group_by(self, field: str, aggr: Union[bool, AggregationMethods, None]):
        """
        :param field:
        :param aggr:
        :return: Dict[str, Union[int, Collection]]
        """
        grouped = dict()
        for item in self:
            group_field = str(item.get_field(field))
            if group_field:
                if group_field not in grouped:
                    grouped[group_field] = self.__new__(type(self))
                grouped[group_field].append(item)
        if aggr is not None:
            if aggr is True or aggr == AggregationMethods.COUNT:
                return {k: len(grouped[k]) for k in grouped}
        return grouped

    def filter_by(self, field: str, value: Any):
        """
        :return: Collection
        """
        return type(self)([item for item in self if item.check_field(field, value)])

    def count_by(self, field: str):
        return self.group_by(field, aggr=True)

    def save_csv(self, path: str):
        if '.csv' not in path:
            path += '.csv'
        with open(path, 'w', newline='') as csv_file:
            if len(self) == 0:
                return

            w = writer(csv_file)
            headers = self[0].fields
            w.writerow(headers)

            for item in self:
                line = [item.get_field(field) for field in headers]
                w.writerow(line)

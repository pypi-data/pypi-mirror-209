class VAItem(dict):
    """
    Extends dict to represent a Vulnerability Assessment item.
    Both Network and Web report consist of VAItem.
    """
    def get_field(self, name: str) -> str | None:
        """
        Gets the field value for a specific report's field name. In case the field name is not
        among the available keys, raises a KeyError.

        :param name: the field name to retrieve.
        :return: a report field value.
        """
        try:
            return self[name]
        except KeyError:
            return None

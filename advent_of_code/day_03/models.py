"""
Models for Day 03.
"""


class PowerBank:
    _value: str = ""

    def __init__(self, value: str = "") -> None:
        self._value = value

    @property
    def jotage(self) -> int:
        return self._calc_jotage()

    def _calc_jotage(self) -> int:
        first_char = max(self._value[:-1])
        first_pos = self._value.find(first_char)
        second_char = max(self._value[first_pos + 1 :])
        return int(f"{first_char}{second_char}")

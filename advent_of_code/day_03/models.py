"""
Models for Day 03.
"""


class PowerBank:
    _value: str = ""
    batteries: int = 2

    def __init__(self, value: str = "") -> None:
        self._value = value

    def jotage(self, batteries: int | None = None) -> int:
        if batteries is None:
            batteries = self.batteries
        return self._calc_joltage(batteries=batteries)

    def _calc_joltage(self, batteries: int) -> int:
        joltage: list[str] = []
        position = 0

        # TODO failing to handle the end boundary condition. 12 -11 -1 is -0. 12 - 12 -1 is worse
        for i in range(batteries - 1, -1, -1):
            search_space = self._value[position:-i] if i else self._value[position:]
            char = max(search_space)
            joltage.append(char)
            position += search_space.find(char) + 1
        return int("".join(joltage))

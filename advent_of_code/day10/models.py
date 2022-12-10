from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RegisterValue:
    """
    Class for values before, during, and after a clock cycle.
    """

    before: int = 0
    during: int = 0
    after: int = 0


@dataclass
class CPU:
    """
    Class for the cpu.
    """

    cycles: list[RegisterValue] = field(default_factory=list)

    def noop(self) -> None:
        """
        Move the X register value along for a cycle.
        """
        value = self.cycles[-1].after
        self.cycles.append(RegisterValue(before=value, during=value, after=value))

    def addx(self, value: int) -> None:
        """
        Add the value to the register, after 2 cycles.
        """
        self.noop()
        assert isinstance(value, int)
        register_value = self.cycles[-1].after
        new_value = register_value + value
        self.cycles.append(
            RegisterValue(
                before=register_value,
                during=register_value,
                after=new_value,
            )
        )

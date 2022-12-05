from dataclasses import dataclass, field


@dataclass
class StackOfCrates:
    """
    Class for stacking crates.
    """

    stack: list[str] = field(default_factory=list)

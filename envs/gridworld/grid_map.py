from dataclasses import dataclass, field

@dataclass
class GridMap:
    name: str
    rows: int
    cols: int
    start: tuple[int, int]
    goal: tuple[int, int]
    walls: list[tuple[int, int]] = field(default_factory=list)
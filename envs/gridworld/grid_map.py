from dataclasses import dataclass, field

@dataclass
class GridMap:
    name: str
    rows: int
    cols: int
    start: tuple[int, int]
    goal: tuple[int, int]
    walls: list[tuple[int, int]] = field(default_factory=list)

wall_gap_map = GridMap(
    name="wall_gap_map",
    rows=10,
    cols=10,
    start=(0, 1),
    goal=(9, 8),
    walls=[(4, 0), (4, 1), (4, 2), (4, 3),
        (4, 4), (4, 6), (4, 7), (4, 8), (4, 9),])

maze_map = GridMap(
    name="wall_gap_map",
    rows=10,
    cols=10,
    start=(0, 1),
    goal=(9, 8),
    walls=[(4, 0), (4, 1), (4, 2), (4, 3),
        (4, 4), (4, 6), (4, 7), (4, 8), (4, 9),])

speckle_map = GridMap(
    name="wall_gap_map",
    rows=10,
    cols=10,
    start=(0, 1),
    goal=(9, 8),
    walls=[(4, 0), (4, 1), (4, 2), (4, 3),
        (4, 4), (4, 6), (4, 7), (4, 8), (4, 9),])
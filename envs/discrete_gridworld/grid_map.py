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
    rows=11,
    cols=11,
    start=(0, 0),
    goal=(3, 10),
    walls=[
        (0, 3),(0, 7),
        (1, 1),(1, 2),(1, 3),(1, 5),(1, 7),(1, 9),
        (2, 1),(2, 5),(2, 9),
        (3, 1),(3, 3),(3, 5),(3, 6),(3, 7),(3, 8),(3, 9),
        (4, 3),(4, 7),
        (5, 1),(5, 2),(5, 3),(5, 4),(5, 5),(5, 7),(5, 9),
        (6, 7),(6, 9),(6, 10),
        (7, 0),(7, 1),(7, 3),(7, 5),(7, 6),(7, 7),(7, 9),
        (8, 3),(8, 7),
        (9, 1),(9, 2),(9, 3),(9, 5),(9, 7),(9, 9),
        (10, 5),(10, 9),

        ])

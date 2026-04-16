import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from .grid_map import GridMap

def render_grid_map(grid_map):
    array = []
    for row in range(grid_map.rows):
        r = []
        for col in range(grid_map.cols):
            if (row, col) in grid_map.walls: r.append(1)
            elif (row, col) == grid_map.start: r.append(2)
            elif (row, col) == grid_map.goal: r.append(3)
            else: r.append(0)
        array.append(r)

    cmap = ListedColormap([
        "white", # 0: empty
        "black", # 1: walls
        "red",   # 2: start
        "green",]) # 3: goal
    
    _, ax = plt.subplots()
    ax.imshow(array, cmap=cmap, vmin=0, vmax=3)

    ax.set_xticks(range(grid_map.cols))
    ax.set_yticks(range(grid_map.rows))
    ax.tick_params(which="major", length=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    ax.set_xticks([x - 0.5 for x in range(1, grid_map.cols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, grid_map.rows)], minor=True)

    ax.grid(which="minor", color="gray", linestyle="-", linewidth=1)

    ax.set_aspect("equal")
    ax.set_title(grid_map.name)

    plt.show()

basic_map = GridMap(
    name="wall_gap_map",
    rows=10,
    cols=10,
    start=(0, 1),
    goal=(9, 8),
    walls=[(4, 0), (4, 1), (4, 2), (4, 3),
        (4, 4), (4, 6), (4, 7), (4, 8), (4, 9),])

render_grid_map(basic_map)
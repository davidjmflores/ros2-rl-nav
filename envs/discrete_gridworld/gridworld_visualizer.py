import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
from .grid_map import GridMap, maze_map

FRAMES_PER_SECOND = 4
dt = 1 / FRAMES_PER_SECOND

def generate_grid_array(grid_map):
    array = []
    for row in range(grid_map.rows):
        r = []
        for col in range(grid_map.cols):
            if (row, col) in grid_map.walls: r.append(1)
            #elif (row, col) == grid_map.start: r.append(3)
            elif (row, col) == grid_map.goal: r.append(2)
            else: r.append(0)
        array.append(r)
    
    cmap = ListedColormap([
        "white", # 0: empty
        "black", # 1: walls
        "green",])  # 2: goal
    
    return array, cmap

def init_grid_plot_singleagent(grid_map, start_indicator=False):
    array, cmap = generate_grid_array(grid_map)
    fig, ax = plt.subplots()
    agent_patch = Rectangle([grid_map.start[1] - 0.25, grid_map.start[0] - 0.25], 0.5, 0.5, color="blue")


    ax.imshow(array, cmap=cmap, vmin=0, vmax=2)
    ax.set_xticks(range(grid_map.cols))
    ax.set_yticks(range(grid_map.rows))
    ax.tick_params(which="both", length=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([x - 0.5 for x in range(1, grid_map.cols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, grid_map.rows)], minor=True)
    
    if start_indicator: ax.text(grid_map.start[1] - 0.25, grid_map.start[0] + 0.25, "S", fontsize=18, fontweight="bold")
    ax.add_patch(agent_patch)
    ax.text(grid_map.goal[1] - 0.25, grid_map.goal[0] + 0.25, "G", fontsize=18, fontweight="bold")
    ax.grid(which="minor", color="black", linestyle="-", linewidth=0.5)
    ax.set_aspect("equal")

    episode_text = ax.text(
        0.02, 1.02, "Episode: -",
        transform=ax.transAxes,
        fontsize=12,
        va="bottom")

    step_text = ax.text(
        0.35, 1.02, "Step: -",
        transform=ax.transAxes,
        fontsize=12,
        va="bottom")

    seed_text = ax.text(
        0.60, 1.02, "Seed: -",
        transform=ax.transAxes,
        fontsize=12,
        va="bottom")

    return {
        "fig": fig,
        "ax": ax,
        "agent": agent_patch,
        "episode_text": episode_text,
        "step_text": step_text,
        "seed_text": seed_text,}

# TODO: Implement trajecotry mode; agent position and its past trajectory are actively plotted
def update_grid_frame_singleagent(handles, agent_state, dt, episode=None, step=None, seed=None): # Frame-only mode
    handles["episode_text"].set_text(f"Episode: {episode}")
    handles["step_text"].set_text(f"Step: {step}")
    handles["seed_text"].set_text(f"Seed: {seed}")
    handles["agent"].set_xy((agent_state[1] - 0.25, agent_state[0] - 0.25))
    plt.pause(dt)

def init_grid_plot_multiagent(grid_map, agent_colors, start_indicator=False):
    array, cmap = generate_grid_array(grid_map)
    fig, ax = plt.subplots()

    ax.imshow(array, cmap=cmap, vmin=0, vmax=2)
    ax.set_xticks(range(grid_map.cols))
    ax.set_yticks(range(grid_map.rows))
    ax.tick_params(which="both", length=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([x - 0.5 for x in range(1, grid_map.cols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, grid_map.rows)], minor=True)
    ax.text(grid_map.goal[1] - 0.25, grid_map.goal[0] + 0.25, "G", fontsize=18, fontweight="bold")
    ax.grid(which="minor", color="black", linestyle="-", linewidth=0.5)
    ax.set_aspect("equal")
    if start_indicator: ax.text(grid_map.start[1] - 0.25, grid_map.start[0] + 0.25, "S", fontsize=18, fontweight="bold")
    
    agent_patches = []
    for color in agent_colors:
        agent_patch = Rectangle([grid_map.start[1] - 0.25, grid_map.start[0] - 0.25], 0.5, 0.5, color=color)
        ax.add_patch(agent_patch)
        agent_patches.append(agent_patch)

    step_text = ax.text(
        0.02, 1.02, "Steps: -",
        transform=ax.transAxes,
        fontsize=12,
        va="bottom")

    seed_text = ax.text(
        0.35, 1.02, "Seed: -",
        transform=ax.transAxes,
        fontsize=12,
        va="bottom")

    return {
        "fig": fig,
        "ax": ax,
        "agents": agent_patches,
        "step_text": step_text,
        "seed_text": seed_text,}

# For visualizing multiple independent agents running on same environement
def update_grid_frame_multiagent(handles, agent_states, dt, step=None, seed=None):
    handles["step_text"].set_text(f"Step: {step}")
    handles["seed_text"].set_text(f"Seed: {seed}")

    if len(agent_states) != len(handles["agents"]):
        raise ValueError("agent_states must match number of plotted agents")
    
    for i, agent_state in enumerate(agent_states):
        handles["agents"][i].set_xy((agent_state[1] - 0.25, agent_state[0] - 0.25))

    plt.pause(dt)

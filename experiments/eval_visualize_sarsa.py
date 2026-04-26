import numpy as np

from envs.discrete_gridworld.gridworld import Gridworld
from envs.discrete_gridworld.grid_map import maze_map
from envs.discrete_gridworld.gridworld_visualizer import init_grid_plot, update_grid_frame

from algs.tabular.sarsa import Sarsa
from algs.tabular.policies.policies import EpsilonGreedyPolicy

epsilon = 0.1
alpha = 0.5
gamma = 1.0
seed = 1
rng = np.random.default_rng(seed)
episodes = 20
dt = 0.005


env = Gridworld(maze_map)
policy = EpsilonGreedyPolicy(env, epsilon)
agent = Sarsa(rng, env, policy, epsilon, gamma, alpha)

Q, episode_states = agent.run(episodes)

handles = init_grid_plot(maze_map, start_indicator=False)

ep = 0
for episode in episode_states:
    step = 0
    for state in episode:
        update_grid_frame(handles, state, dt, ep, step, seed)
        step += 1
    ep += 1
    
import numpy as np
import matplotlib.pyplot as plt

from envs.discrete_gridworld.gridworld import Gridworld
from envs.discrete_gridworld.grid_map import maze_map
from envs.discrete_gridworld.gridworld_visualizer import init_grid_plot, update_grid_frame

from algs.tabular.n_step_sarsa import NStepSarsa
from algs.tabular.policies.policies import EpsilonGreedyPolicy

epsilon = 0.1
gamma = 0.99
alpha = 0.5
n = 4
seed = 0
rng = np.random.default_rng(seed)
episodes = 40
dt = 0.005
max_steps = 7420

env = Gridworld(maze_map)
policy = EpsilonGreedyPolicy(env, epsilon)
agent = NStepSarsa(rng, env, policy, epsilon, gamma, alpha, n)

Q, episode_states, episode_cumulatives = agent.run(episodes)

x = np.arange(1, len(episode_cumulatives) + 1)

plt.plot(x, episode_cumulatives, marker = "o", label=f"n-step Sarsa, n={n}")
plt.xlabel("Episodes")
plt.ylabel("Cumulative Reward Per Episode")
plt.grid(True)
plt.legend()
plt.show()

'''
handles = init_grid_plot(maze_map, start_indicator=False)
ep = 0
for episode in episode_states:
    step = 0
    for state in episode:
        update_grid_frame(handles, state, dt, ep, step, seed)
        step += 1
    ep += 1
'''
import numpy as np
import matplotlib.pyplot as plt

from envs.discrete_gridworld.gridworld import Gridworld
from envs.discrete_gridworld.grid_map import maze_map
from envs.discrete_gridworld.gridworld_visualizer import init_grid_plot_multiagent, update_grid_frame_multiagent

from algs.tabular.n_step_sarsa import NStepSarsa
from algs.tabular.expected_sarsa import ExpectedSarsa
from algs.tabular.sarsa import Sarsa
from algs.tabular.policies.policies import EpsilonGreedyPolicy

epsilon = 0.1
gamma = 0.99
alpha = 0.5
n = 4
seed = 4
rng = np.random.default_rng(seed)
episodes = 50
dt = 0.05
max_steps = 7420

env = Gridworld(maze_map)
policy = EpsilonGreedyPolicy(env, epsilon)

nstep_sarsa_agent = NStepSarsa(rng, env, policy, epsilon, gamma, alpha, n)
expected_sarsa_agent = ExpectedSarsa(rng, env, policy, epsilon, gamma, alpha)
sarsa_agent = Sarsa(rng, env, policy, epsilon, gamma, alpha)

Q, nstep_episode_states, nstep_episode_cumulatives = nstep_sarsa_agent.run(episodes)
Q, expected_episode_states, expected_episode_cumulatives = expected_sarsa_agent.run(episodes)
Q, sarsa_episode_states, sarsa_episode_cumulatives = sarsa_agent.run(episodes)

x = np.arange(1, episodes + 1)

plt.plot(x, nstep_episode_cumulatives, marker = "o", label=f"n-step Sarsa, n={n}")
plt.plot(x, expected_episode_cumulatives, marker = "o", label=f"Expected Sarsa")
plt.plot(x, sarsa_episode_cumulatives, marker = "o", label=f"Sarsa")
plt.xlabel("Episodes")
plt.ylabel("Cumulative Reward Per Episode")
plt.grid(True)
plt.legend()
plt.show()

episode_idx = episodes - 1 # which episode you want to visualize

selected_trajectories = [
    nstep_episode_states[episode_idx],
    expected_episode_states[episode_idx],
    sarsa_episode_states[episode_idx],]

handles = init_grid_plot_multiagent(
    maze_map,
    ["blue", "red", "green"],
    start_indicator=True)

max_len = max(len(traj) for traj in selected_trajectories)

for step in range(max_len):
    agent_states = [
        traj[step] if step < len(traj) else traj[-1]
        for traj in selected_trajectories]

    update_grid_frame_multiagent(
        handles,
        agent_states,
        dt,
        step=step,
        seed=seed)

plt.show()
class EpsilonGreedyPolicy:
    def __init__(self, env, epsilon):
        self.env = env
        self.epsilon = epsilon

    def sample(self, rng, s, Q):
        actions = list(self.env.actions(s))
        if not actions: raise ValueError(f"No actions available for state {s}")

        if rng.random() < self.epsilon: return actions[rng.integers(len(actions))]

        q_vals = [Q.get(s, {}).get(a, 0.0) for a in actions]
        max_q = max(q_vals)
        greedy_actions = [a for a, q in zip(actions, q_vals) if q == max_q]
        return greedy_actions[rng.integers(len(greedy_actions))]


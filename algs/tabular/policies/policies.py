class EpsilonGreedyPolicy:
    def __init__(self, env, epsilon):
        self.env = env
        self.epsilon = epsilon
    
    def prob(self, s, a, Q):
        actions = list(self.env.actions(s))
        if not actions: return 0.0

        q_vals = [Q.get(s, {}).get(a_i, 0.0) for a_i in actions]
        max_q = max(q_vals)
        greedy = [a_i for a_i, q in zip(actions, q_vals) if q == max_q]
        prob_base = self.epsilon / len(actions)
        if not greedy: return prob_base

        return ((1.0 - self.epsilon) / len(greedy)) + prob_base if a in greedy else prob_base

    def sample(self, rng, s, Q):
        actions = list(self.env.actions(s))
        if not actions: raise ValueError(f"No actions available in state: {s}")

        if rng.random() < self.epsilon: return actions[rng.integers(len(actions))]

        q_vals = [Q.get(s, {}).get(a, 0.0) for a in actions]
        max_q = max(q_vals)
        greedy_actions = [a for a, q in zip(actions, q_vals) if q == max_q]
        return greedy_actions[rng.integers(len(greedy_actions))]


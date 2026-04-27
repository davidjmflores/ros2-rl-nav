class ExpectedSarsa:
    def __init__(self, rng, env, policy, epsilon, gamma, alpha):
        self.rng = rng
        self.env = env
        self.policy = policy

        if not 0 < epsilon <= 1.0: raise ValueError(f"Invalid parameter value: {epsilon}")
        self.epsilon = epsilon
        if not 0 < gamma <= 1.0: raise ValueError(f"Invalid parameter value: {gamma}")
        self.gamma = gamma
        if not 0 < alpha <= 1.0: raise ValueError(f"Invalid parameter value: {alpha}")
        self.alpha = alpha

        self.Q = {}
    
    def set_Q(self, s, a):
        self.Q.setdefault(s, {})
        self.Q[s].setdefault(a, 0.0)
        return self.Q[s][a]
    
    def expectation(self, s):
        expectation = 0.0
        actions = self.env.actions(s)
        if not actions: raise ValueError(f"No actions for state {s}")

        for a in actions: 
            q_sa = self.set_Q(s, a)
            expectation += self.policy.prob(s, a, self.Q) * q_sa
        
        return expectation
    
    def run(self, episodes):
        episode_states = []
        for ep in range(episodes):
            states = []
            s_t, reset_info = self.env.reset()
            states.append(s_t)

            while True:
                a_t = self.policy.sample(self.rng, s_t, self.Q)
                s_tp1, r_tp1, terminated, truncated, step_info = self.env.step(a_t)
                states.append(s_tp1)
                done = terminated or truncated
                q_sa = self.set_Q(s_t, a_t)

                if done: target = r_tp1
                else:
                    expectation = self.expectation(s_tp1)
                    target = r_tp1 + self.gamma * expectation

                self.Q[s_t][a_t] += self.alpha * (target - q_sa)

                if done:
                    episode_states.append(states)
                    break

                s_t = s_tp1
        
        return self.Q.copy(), episode_states
                
import numpy as np

class NStepSarsa:
    def __init__(self, rng, env, policy, epsilon, gamma, alpha, n):
        self.rng = rng
        self.env = env
        self.policy = policy

        if not 0 < epsilon <= 1.0: raise ValueError(f"Invalid parameter value: epsilon = {epsilon}")
        self.epsilon = epsilon
        if not 0 < gamma <= 1.0: raise ValueError(f"Invalid parameter value: gamma ={gamma}")
        self.gamma = gamma
        if not 0 < alpha <= 1.0: raise ValueError(f"Invalid parameter value: alpha = {alpha}")
        self.alpha = alpha
        if not 0 <= n: raise ValueError(f"Invalid parameter value: n = {n}")
        self.n = int(n)

        self.gamma_pows = [1.0] * (self.n + 1)
        for k in range(1, self.n + 1):
            self.gamma_pows[k] = self.gamma_pows[k - 1] * self.gamma

        self.Q = {}
    
    def set_Q(self, s, a):
        self.Q.setdefault(s, {})
        self.Q[s].setdefault(a, 0.0)
        return self.Q[s][a]
    
    def run(self, episodes):
        episode_states = []
        episode_cumulatives = []

        for ep in range(episodes):
            cumulative = 0.0
            states = []
            t = 0
            INF = float("inf")
            T = INF

            buf_len = self.n + 1
            tau = 0
            S = [None] * buf_len
            A = [None] * buf_len
            R = [0.0] * buf_len

            s_t, reset_info = self.env.reset()
            states.append(s_t)
            a_t = self.policy.sample(self.rng, s_t, self.Q)
            S[t] = s_t
            A[t] = a_t

            while True:
                if t < T:
                    s_tp1, r_tp1, terminated, truncated, step_info = self.env.step(a_t)
                    states.append(s_tp1)
                    S[(t + 1) % buf_len] = s_tp1
                    R[(t + 1) % buf_len] = r_tp1
                    cumulative += r_tp1
                    done = terminated or truncated

                    if done: T  = t + 1
                    else: 
                        a_tp1 = self.policy.sample(self.rng, s_tp1, self.Q)
                        A[(t + 1) % buf_len] = a_tp1
                        a_t = a_tp1
                    s_t = s_tp1
                
                tau = t - self.n + 1
                if tau >= 0:
                    G = 0.0
                    t_end = tau + self.n if T == INF else min(tau + self.n, T)

                    for i in range(tau + 1, t_end + 1):
                        G += self.gamma_pows[i - tau - 1]* R[i % buf_len]
                    if tau + self.n < T:
                        G += self.gamma_pows[self.n] * self.set_Q(S[(tau + self.n) % buf_len], A[(tau + self.n) % buf_len])
                    
                    q_sa = self.set_Q(S[tau % buf_len], A[tau % buf_len])
                    self.Q[S[tau % buf_len]][A[tau % buf_len]] += self.alpha * (G - q_sa)

                if tau == T - 1:
                    episode_states.append(states)
                    episode_cumulatives.append(cumulative)
                    break
                t += 1
        
        return self.Q, episode_states, episode_cumulatives


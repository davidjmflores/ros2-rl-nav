from dataclasses import dataclass, field
@dataclass
class GridMap:
    rows: int = 10
    cols: int = 10
    start: tuple[int, int] = (0, 1)
    goal: tuple[int, int] = (9, 8)
    walls: list[tuple[int, int]] = field(default_factory=list)


class DiscreteGridworld:
    ACTION_TO_DELTA = {
            0: (-1, 0),
            1: ( 1, 0),
            2: ( 0,-1),
            3: ( 0, 1)}
    
    def __init__(self, grid_map):
        self.grid_map = grid_map
        self.current_state = self.grid_map.start

        self._states = [
            (row, col)
            for row in range(self.grid_map.rows)
            for col in range(self.grid_map.cols)
            if (row, col) not in self.grid_map.walls]
    
    def states(self): return self._states
    
    def actions(self, state=None): return tuple(self.ACTION_TO_DELTA.keys())
        
    def reset(self, seed=None):
        self.current_state = self.grid_map.start
        return self.current_state, {}
    
    def step(self, action):
        if action not in self.ACTION_TO_DELTA: raise ValueError(f"Invalid action: {action}")
        action_delta = self.ACTION_TO_DELTA[action]

        next_row = min(self.grid_map.rows - 1, max(0, self.current_state[0] + action_delta[0]))
        next_col = min(self.grid_map.cols - 1, max(0, self.current_state[1] + action_delta[1]))
        next_state = (next_row, next_col)

        if next_state not in self.grid_map.walls: self.current_state = next_state
        
        reward = 0 if self.current_state == self.grid_map.goal else -1
        terminated = (self.current_state == self.grid_map.goal)


        return self.current_state, reward, terminated, False, {}






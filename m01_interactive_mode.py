import random
import sys

#
# 强化学习基本交互模式
# 交互定义：1.state --> action 2.state + action --> next
# 过程: 1.静态奖励 2.随机策略
#

### STEP1 交互定义：状态/动作/奖励/转移
# 3*4 网格 / 目标点 / 障碍物
GRID_ROW = 3;
GRID_COLUMN = 4;
OBJECT_X = 2;
OBJECT_Y = 3;
OBSTACLE_X = 1;
OBSTACLE_Y = 3;

# 初始化状态/特殊状态 
# [(0, 0), (0, 1), (0, 2), (0, 3),
#  (1, 0), (1, 1), (1, 2), (1, 3),
#  (2, 0), (2, 1), (2, 2), (2, 3)]
grid_states = [
    (row, column)
    for row in range(GRID_ROW)
    for column in range(GRID_COLUMN)
]
obstacle_states = [(1,3)];  

# 奖励定义
# [[0, 0, 0, 0],
#  [0, 0, 0, -1],
#  [0, 0, 0, 1]]
grid_rewards = [
    [0 for _ in range(GRID_COLUMN)]
    for _ in range(GRID_ROW)
]
grid_rewards[OBJECT_X][OBJECT_Y] = 1
grid_rewards[OBSTACLE_X][OBSTACLE_Y] = -1

# 动作定义
grid_actions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def grid_states_transition(state, action) -> tuple:
    """状态转移函数，定义游戏规则，遇到边界或者障碍物保持不动

    Args:
        state (tuple): 当前状态
        action (string): 当前动作

    Returns:
        tuple: 下一个状态
    """
    current_state = state;
    next_state = tuple(one + two for one, two
                      in zip(state, grid_actions[action]))
    
    if (next_state in grid_states
        and next_state not in obstacle_states):
        current_state = next_state
    
    return current_state;

### STEP2 无模型/基于策略：随机策略
def grid_random_policy(state) -> tuple:
    """简单的随机策略，返回当前状态下的下一步动作

    Args:
        state (tuple): 当前状态

    Returns:
        tuple: 下一步动作
    """
    return random.choice(list(grid_actions.keys()))


### MAIN
def main() -> int:
    print("hello main")
    current_state = (1, 1);

    for _ in range(5):
        current_grid_action = grid_random_policy(current_state);
        next_state = grid_states_transition(current_state, current_grid_action);
        reward = grid_rewards[next_state[0]][next_state[1]]
        print(f"当前状态:{current_state}, 当前动作:{current_grid_action},\n"
              f"下一个状态:{next_state}, 奖励:{reward}")
        current_state = next_state
    return 0

if __name__ == "__main__":
    sys.exit(main())
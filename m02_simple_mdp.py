import sys
from m01_interactive_mode import *

#
# 简单MDP
# 基于价值: 1.静态奖励 2.价值迭代
#

### STEP1 奖励
grid_rewards = [
    [-0.02 for _ in range(GRID_COLUMN)]
    for _ in range(GRID_ROW)
]
grid_rewards[OBJECT_X][OBJECT_Y] = 1
grid_rewards[OBSTACLE_X][OBSTACLE_Y] = -float('inf')


###STEP2 价值函数迭代
# 迭代次数
ITER_COUNTS = 100
# 折扣因子
GAMMA = 0.9
# 初始化价值函数表
value_function_table = [
    [0 for _ in range(GRID_COLUMN)]
    for _ in range(GRID_ROW)
]
# 迭代函数
def grid_value_iteration(counts):
    """价值迭代函数 更新价值函数表

    Args:
        counts (int): 迭代次数
    """
    for _ in range(counts):
        #一次迭代做遍历循环，只存储最大价值
        for i in range(GRID_ROW):
            for j in range(GRID_COLUMN):
                max_value = -float('inf')
                for action in grid_actions:
                    next_state = grid_states_transition((i, j), action)
                    value = grid_rewards[i][j] + GAMMA * value_function_table[next_state[0]][next_state[1]]
                    max_value = max(value, max_value)
                value_function_table[i][j] = max_value

### MAIN
def main() -> int:
    grid_value_iteration(ITER_COUNTS)
    for row in value_function_table:
        print(row)
    return 0

if __name__ == "__main__":
    sys.exit(main())
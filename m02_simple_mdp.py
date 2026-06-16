import random
import sys
from m01_interactive_mode import *

## 定义奖励
grid_rewards = [
    [-0.02 for _ in range(GRID_COLUMN)]
    for _ in range(GRID_ROW)
]
grid_rewards[OBJECT_X][OBJECT_Y] = 1
grid_rewards[OBSTACLE_X][OBSTACLE_Y] = -float('inf')

print(grid_rewards)

# 折扣因子
GAMMA = 0.9

value_function_table = [
    [0 for _ in range(GRID_COLUMN)]
    for _ in range(GRID_ROW)
]


ITER_COUNTS = 100

        
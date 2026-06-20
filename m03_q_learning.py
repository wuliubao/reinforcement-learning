from m01_interactive_mode import *
from m02_simple_mdp import *

q_table = [
    [0 for _ in range(GRID_ROW * GRID_COLUMN)]
    for _ in range(len(grid_actions))
]

# 回合次数（即迭代次数）
EPISODE_COUNTS = 1000

#ε-greedy策略 
EPSILON_GREEDY = 0.1

START_X = 0
START_Y = 0

def q_learning_trans(episode_counts):
    for _ in episode_counts:
        current = (START_X, START_Y)
        while(current != (OBJECT_X, OBJECT_Y)):
            if random.random() < EPSILON_GREEDY:
                action = random.choice(list(grid_actions.keys()))

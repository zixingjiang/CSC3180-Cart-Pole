import csc3180_cartpole_env
import gymnasium as gym
import numpy as np
import math
import matplotlib.pyplot as plt
    
env = gym.make('csc3180/CartPole_v1', render_mode='human')
n_buckets = (1, 1, 6, 3) 
n_actions = env.action_space.n
state_bounds = list(zip(env.observation_space.low, env.observation_space.high))
state_bounds[1] = [-0.5, 0.5]
state_bounds[3] = [-math.radians(50), math.radians(50)]
q_table = np.zeros(n_buckets + (n_actions,))
print(q_table)
q_table = np.array([[[[[0,0],[0,0],[0,0]],[[49.44993399, 51.30619074],[32.47725767, 49.47642826],[4.97251691, 22.21619079]],[[99.70453993, 99.44634026],[99.71261139, 99.67389341],[99.64673169, 99.7117677]],[[99.71233936,99.65198549],[99.67362476, 99.71274038],[99.46710856, 99.70753277]],[[0,0],[52.6236338,  44.98461976],[51.87116499, 52.88088545]],[[0,0],[0,0],[0,0]]]]])
print(q_table)
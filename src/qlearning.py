'''
cart-pole problem solved by Q-learning
'''
import csc3180_cartpole_env
import gymnasium as gym
import numpy as np
import math

def choose_action(state, q_table, action_space, epsilon):
    if np.random.random_sample() < epsilon: 
        return action_space.sample() 
    else:
        return np.argmax(q_table[state]) 

def get_state(observation, n_buckets, state_bounds):
    try: 
        state = [0] * len(observation[0]) 
        obs = observation[0]
    except: 
        state = [0] * len(observation) 
        obs = observation
    for i, s in enumerate(obs):
        l, u = state_bounds[i][0], state_bounds[i][1] 
        if s <= l:
            state[i] = 0
        elif s >= u:
            state[i] = n_buckets[i] - 1
        else:
            state[i] = int(((s - l) / (u - l)) * n_buckets[i])
    return tuple(state)

if __name__ == '__main__':
    env = gym.make('csc3180/CartPole_v1', render_mode='human')
    n_buckets = (1, 1, 6, 3) 
    n_actions = env.action_space.n
    state_bounds = list(zip(env.observation_space.low, env.observation_space.high))
    state_bounds[1] = [-0.5, 0.5]
    state_bounds[3] = [-math.radians(50), math.radians(50)]
    q_table = np.zeros(n_buckets + (n_actions,))

    get_epsilon = lambda i: max(0.01, min(1, 1.0 - math.log10((i+1)/25))) 
    get_lr = lambda i: max(0.01, min(0.5, 1.0 - math.log10((i+1)/25)))
    gamma = 0.99 

    # Q-learning
    for i_episode in range(200):
        epsilon = get_epsilon(i_episode)
        lr = get_lr(i_episode)

        observation = env.reset() 
        rewards = 0 
        state = get_state(observation, n_buckets, state_bounds) 
        for t in range(500):
            env.render()

            # Agent takes action
            action = choose_action(state, q_table, env.action_space, epsilon) 
            observation, reward, terminated, truncated, info = env.step(action) 
            rewards += reward
            next_state = get_state(observation, n_buckets, state_bounds)

            # Agent learns via Q-learning
            q_next_max = np.amax(q_table[next_state])
            q_table[state + (action,)] += lr * (reward + gamma * q_next_max - q_table[state + (action,)])

            # Transition to next state
            state = next_state

            print("current episode: ", i_episode, "current reward: ", rewards, "game status:", (terminated, truncated))

            if terminated:
                print('Episode {} finished after {} timesteps, total rewards {}'.format(i_episode, t+1, rewards))
                break
            
            if rewards == 475:
                print('Episode {} succeed, total rewards {}'.format(i_episode, t+1, rewards))
                break
         
    print(q_table)

    env.close() 
import gymnasium as gym
# import imageio

# create and initialize a Gym environment
env = gym.make('CartPole-v1', render_mode='human') # <- to record runtine images, set render_mode = "rgb_array"
observation, info = env.reset()

# images = []

# run the RL loop
for i in range(1000):
    # capture runtime images
    # image = env.render()
    # images.append(image)
    
    # Here is the core part of RL loop and gym programming
    # 1. The agent selects an action accoridng to what it may concern, such as observation, reward, ...
    # 2. The environment takes the action of agent and transfroms. After that, it gives the agent a reward and updates the agent's observation
    if i == 0: 
        action = env.action_space.sample()  #<- in this case, we just select ramdon action from the angent's action space
    observation, reward, terminated, truncated, info = env.step(action) # 
    
    if observation[2] < 0:
        action = 0
    else:
        action = 1

    if terminated or truncated:
        observation, info = env.reset()

# save the recordec images as gif 
# imageio.mimsave('animation.gif', images)

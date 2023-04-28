from gymnasium.envs.registration import register

register(
    id='csc3180/CartPole_v1',
    entry_point='csc3180_cartpole_env.envs:CartPoleEnv_CSC3180',
    max_episode_steps=500,
    reward_threshold=475.0,
)
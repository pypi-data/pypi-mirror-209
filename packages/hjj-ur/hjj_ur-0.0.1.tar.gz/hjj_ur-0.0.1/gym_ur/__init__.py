from gym.envs.registration import register

register(
    id='urReach-v0',
    entry_point='gym_ur.envs:urEnv',
    max_episode_steps=50,
)
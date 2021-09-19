import gym
import time
import functools
import numpy as np
from gym_ignition.utils import logger
from BB_gym_Envs import randomizers
from BB_gym_Envs.common.mp_env import make_mp_envs
from BB_gym_Envs.monitor.monitor import TrainingMonitor

# Set verbosity
logger.set_level(gym.logger.ERROR)
# logger.set_level(gym.logger.DEBUG)

# Available tasks
env_id = "Monopod-Gazebo-v1"
NUM_ENVS = 10
NUMBER_TIME_STEPS = 10000
seed = 42
training_monitor = TrainingMonitor(NUM_ENVS, NUMBER_TIME_STEPS)

# def make_env_from_id(env_id: str, **kwargs) -> gym.Env:
#     import gym
#     import BB_gym_Envs
#     return gym.make(env_id, **kwargs)
#
# make_env = functools.partial(make_env_from_id, env_id=env_id)
# env = randomizers.monopod.MonopodEnvRandomizer(
#     env=make_env)
# env.seed(42)

envs = make_mp_envs(env_id, NUM_ENVS, seed, randomizers.monopod.MonopodEnvRandomizer, training_monitor)
envs.reset()
# Enable the rendering
# env.render('human')
current_cumulative_rewards = np.zeros(NUM_ENVS)
epoch = 0
beg_time = time.time()
while epoch < 1000:

    # Execute random actions for each env
    actions = np.stack([envs.action_space_single.sample() for _ in range(NUM_ENVS)])
    observation_arr, reward_arr, done_arr, _ = envs.step(actions)

    if any(done_arr):
        # print(f"Step: {step}, {done_arr} ... their reward: {current_cumulative_rewards[done_arr]}")
        current_cumulative_rewards[done_arr] = 0
        epoch += sum(done_arr)
    current_cumulative_rewards += reward_arr
print('time for 10000 episodes: ' + str(time.time()-beg_time))


envs.close()
time.sleep(5)

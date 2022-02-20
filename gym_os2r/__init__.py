import numpy
from . import tasks
from . import models
from . import randomizers
from . import common
from . import utils

__all__ = ['tasks', 'models', 'randomizers', 'common', 'utils']

from gym.envs.registration import register
from gym_os2r.rewards import BalancingV1, BalancingV3, StandingV1,StandingV2,StandingV3, WalkingV1, HoppingV1, StraightV1, 

max_float = float(numpy.finfo(numpy.float32).max)

register(
    id='Monopod-stand-v1',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'free_hip',
            'reward_class': StandingV3,
            'reset_positions': ['ground']
            })
register(
    id='Monopod-balance-v1',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps= 10000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip',
            # 'task_mode': 'free_hip',
            'reward_class': BalancingV3,
            'reset_positions': ['stand']
            })

register(
    id='Monopod-walk-v1',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'free_hip',
            'reward_class': WalkingV1,
            'reset_positions': ['stand']
            })

register(
    id='Monopod-hop-v1',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip',
            'reward_class': HoppingV1,
            'reset_positions': ['stand']
            })

register(
    id='Monopod-simple-v1',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'simple',
            'reward_class': StraightV1,
            'reset_positions': ['stand']
            })


# register(
#     id='Monopod-v1',
#     entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=100000,
#     kwargs={'task_cls': tasks.monopod.MonopodTask,
#             'agent_rate': 1000,
#             'physics_rate': 1000,
#             'real_time_factor': max_float,
#             })
# register(
#     id='Monopod-fixed_hip-v1',
#     entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=100000,
#     kwargs={'task_cls': tasks.monopod.MonopodTask,
#             'agent_rate': 1000,
#             'physics_rate': 1000,
#             'real_time_factor': max_float,
#             'task_mode': 'fixed_hip'
#             })
#
# register(
#     id='Monopod-fixed_hip_and_boom_yaw-v1',
#     entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=100000,
#     kwargs={'task_cls': tasks.monopod.MonopodTask,
#             'agent_rate': 1000,
#             'physics_rate': 1000,
#             'real_time_factor': max_float,
#             'task_mode': 'fixed_hip_and_boom_yaw'
#             })

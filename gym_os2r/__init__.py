import numpy
from . import tasks
from . import models
from . import randomizers
from . import common
from . import utils

__all__ = ['tasks', 'models', 'randomizers', 'common', 'utils']

from gym.envs.registration import register
from gym_os2r.rewards import *

max_float = float(numpy.finfo(numpy.float32).max)

register(
    id='Monopod-stand-v1',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100_000,
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
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'free_hip',
            'reward_class': BalancingV1,
            'reset_positions': ['stand']
            })
register(
    id='Monopod-balance-v2',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip_simple',
            'reward_class': BalancingV1,
            'reset_positions': ['stand', 'half_stand', 'ground', 'lay', 'float']
            })

register(
    id='Monopod-balance-v3',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=10_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip',
            'reward_class': BalancingV3,
            # 'reset_positions': ['stand', 'half_stand', 'ground', 'lay', 'float']
            'reset_positions': ['float']
            })

register(
    id='Monopod-balance-v4',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=10_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip_torque',
            'reward_class': BalancingV3,
            # 'reset_positions': ['stand', 'half_stand', 'ground', 'lay', 'float']
            'reset_positions': ['float', 'stand', 'half_stand', 'ground']
            })

register(
    id='Monopod-balance-v5',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=10_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip_torque',
            'reward_class': BalancingV5,
            # 'reset_positions': ['stand', 'half_stand', 'ground', 'lay', 'float']
            'reset_positions': ['lay', 'ground']
            })

register(
    id='Monopod-balance-v6',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=10_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip_torque',
            'reward_class': BalancingV6,
            # 'reset_positions': ['stand', 'half_stand', 'ground', 'lay', 'float']
            'reset_positions': ['ground', 'half_stand', 'stand', 'float']
            })

register(
    id='Monopod-balance-v7',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=10_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip_torque',
            'reward_class': BalancingV7,
            # 'reset_positions': ['stand', 'half_stand', 'ground', 'lay', 'float']
            'reset_positions': ['ground', 'half_stand', 'stand', 'float']
            })

register(
    id='Monopod-walk-v1',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100_000,
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
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip',
            'reward_class': HoppingV1,
            'reset_positions': ['stand']
            })

register(
    id='Monopod-hop-v2',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10000,
            'real_time_factor': max_float,
            'task_mode': 'fixed_hip_torque',
            'reward_class': HoppingV2,
            'reset_positions': ['stand']
            })

register(
    id='Monopod-simple-v1',
    entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=100_000,
    kwargs={'task_cls': tasks.monopod.MonopodTask,
            'agent_rate': 1000,
            'physics_rate': 10_000,
            'real_time_factor': max_float,
            'task_mode': 'simple',
            'reward_class': StraightV1,
            'reset_positions': ['stand']
            })


# register(
#     id='Monopod-v1',
#     entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=100000,
#     kwargs={'task_cls': tasks.monopod.MonopodTask,
#             'agent_rate': 1000,
#             'physics_rate': 1000,
#             'real_time_factor': max_float,
#             })
# register(
#     id='Monopod-fixed_hip-v1',
#     entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
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
#     entry_point='gym_os2r.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=100000,
#     kwargs={'task_cls': tasks.monopod.MonopodTask,
#             'agent_rate': 1000,
#             'physics_rate': 1000,
#             'real_time_factor': max_float,
#             'task_mode': 'fixed_hip_and_boom_yaw'
#             })

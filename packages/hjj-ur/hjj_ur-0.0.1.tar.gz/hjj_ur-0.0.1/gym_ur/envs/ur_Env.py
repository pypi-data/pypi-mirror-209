import pybullet as p
import pybullet_data
import os
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from math import sqrt
import random
import time
import math
from utils import distance


class urEnv(gym.Env):
    metadata = {
        'render.modes': ['human'],
        'video,frames_per_second': 50
    }

    def __init__(self, is_render=False, is_good_view=False, reward_type="spare", distance_threshold=0.05, goal_range=0.3):
        self.reward_type = reward_type
        self.distance_threshold = distance_threshold
        self.is_render = is_render
        self.is_good_view = is_good_view
        self.max_episode_steps = 10000

        if self.is_render:
            p.connect(p.GUI)
        else:
            p.connect(p.DIRECT)

        self.x_low_obs = 0.3
        self.x_high_obs = 1.0
        self.y_low_obs = -0.3
        self.y_high_obs = 0.3
        self.z_low_obs = 0
        self.z_high_obs = 0.55

        self.x_low_action = -0.4
        self.x_high_action = 0.4
        self.y_low_action = -0.4
        self.y_high_action = 0.4
        self.z_low_action = -0.6
        self.z_high_action = 0.3

        p.resetDebugVisualizerCamera(cameraDistance=1.5,
                                     cameraYaw=0,
                                     cameraPitch=-40,
                                     cameraTargetPosition=[0.55, -0.35, 0.2])

        self.action_space = spaces.Box(low=np.array(
            [self.x_low_action, self.y_low_action, self.z_low_action]),
            high=np.array([
                self.x_high_action,
                self.y_high_action,
                self.z_high_action
            ]),
            dtype=np.float32)
        self.observation_space = spaces.Dict(
            dict(
                observation = spaces.Box(low=np.array([self.x_low_obs, self.y_low_obs, self.z_low_obs]),
            high=np.array([self.x_high_obs, self.y_high_obs, self.z_high_obs]),
            dtype=np.float32),
                desired_goal = spaces.Box(low=np.array([self.x_low_obs, self.y_low_obs, self.z_low_obs]),
            high=np.array([self.x_high_obs, self.y_high_obs, self.z_high_obs]),
            dtype=np.float32),
                achieved_goal = spaces.Box(low=np.array([self.x_low_obs, self.y_low_obs, self.z_low_obs]),
            high=np.array([self.x_high_obs, self.y_high_obs, self.z_high_obs]),
            dtype=np.float32)
            )
        )

        # self.observation_space = spaces.Box(
        #     low=np.array([self.x_low_obs, self.y_low_obs, self.z_low_obs]),
        #     high=np.array([self.x_high_obs, self.y_high_obs, self.z_high_obs]),
        #     dtype=np.float32)

        self.step_counter = 0

        self.urdf_root_path = pybullet_data.getDataPath()
        # lower limits for null space
        self.lower_limits = [-.967, -2, -2.96, 0.19, -2.96, -2.09, -3.05]
        # upper limits for null space
        self.upper_limits = [.967, 2, 2.96, 2.29, 2.96, 2.09, 3.05]
        # joint ranges for null space
        self.joint_ranges = [5.8, 4, 5.8, 4, 5.8, 4, 6]
        # restposes for null space
        self.rest_poses = [0, 0, 0, 0.5 * math.pi, 0, -math.pi * 0.5 * 0.66, 0]
        # joint damping coefficents
        self.joint_damping = [
            0.00001, 0.00001, 0.00001, 0.00001, 0.00001, 0.00001, 0.00001
        ]

        self.init_joint_positions = [
            0.0,  # Base  (Fixed)
            0.0,  # Joint 1
            -1.5,  # Joint 2
            1.57,  # Joint 3
            -1.57,  # Joint 4
            -1.57,  # Joint 5
            0,  # Joint 6
        ]

        self.orientation = p.getQuaternionFromEuler(
            [0., -math.pi, math.pi / 2.])

        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        dv = 0.05
        dx = action[0] * dv
        dy = action[1] * dv
        dz = action[2] * dv

        self.current_pos = p.getLinkState(self.ur_id, self.num_joints - 1)[4]
        self.new_robot_pos = [
            self.current_pos[0] + dx, self.current_pos[1] + dy,
            self.current_pos[2] + dz
        ]
        self.robot_joint_positions = p.calculateInverseKinematics(
            bodyUniqueId=self.ur_id,
            endEffectorLinkIndex=self.num_joints - 1,
            targetPosition=[
                self.new_robot_pos[0], self.new_robot_pos[1],
                self.new_robot_pos[2]
            ],
            targetOrientation=self.orientation,
            jointDamping=self.joint_damping,
        )
        # 打印旋转角度
        # print(self.robot_joint_positions)
        for i in range(self.num_joints-1):
            p.setJointMotorControl2(self.ur_id, i+1, p.POSITION_CONTROL, self.robot_joint_positions[i])
        p.stepSimulation()

        # 在代码开始部分，如果定义了is_good_view，那么机械臂的动作会变慢，方便观察
        if self.is_good_view:
            time.sleep(0.05)

        self.robot_state = p.getLinkState(self.ur_id, self.num_joints - 1)[4]
        self.object_state = np.array(
            p.getBasePositionAndOrientation(self.object_id)[0]).astype(np.float32)

        square_dx = (self.robot_state[0] - self.object_state[0]) ** 2
        square_dy = (self.robot_state[1] - self.object_state[1]) ** 2
        square_dz = (self.robot_state[2] - self.object_state[2]) ** 2

        # 用机械臂末端和物体的距离作为奖励函数的依据
        self.distance = sqrt(square_dx + square_dy + square_dz)
        # print(self.distance)

        x = self.robot_state[0]
        y = self.robot_state[1]
        z = self.robot_state[2]

        # 如果机械比末端超过了obs的空间，也视为done，而且会给予一定的惩罚
        terminated = bool(x < self.x_low_obs or x > self.x_high_obs
                          or y < self.y_low_obs or y > self.y_high_obs
                          or z < self.z_low_obs or z > self.z_high_obs)
        if terminated:
            reward = -0.1
            self.terminated = True

        # 如果机械臂一直无所事事，在最大步数还不能接触到物体，也需要给一定的惩罚
        # elif self.step_counter > self.max_steps_one_episode:
        #     reward = -0.1
        #     self.terminated = True

        elif self.distance < 0.01:
            reward = self.compute_reward(self, self.robot_state, self.object_state)
            self.terminated = True
        else:
            reward = 0
            self.terminated = False

        info = {'distance:': self.distance}
        # info = self.distance
        self.observation = self.object_state
        return np.array(self.observation).astype(
            np.float32), reward, self.terminated, info

    def compute_reward(self, achieved_goal, desired_goal):
        d = distance(achieved_goal, desired_goal)
        if self.reward_type == "spare":
            return -np.array(d > self.distance_threshold, dtype=np.float32)
        else:
            return -d.astype(np.float32)

    def reset(self):
        self.step_counter = 0

        p.resetSimulation()
        self.done = False
        p.setGravity(0, 0, -10)

        # 这些是周围那些白线，用来观察是否超过了obs的边界
        p.addUserDebugLine(
            lineFromXYZ=[self.x_low_obs, self.y_low_obs, 0],
            lineToXYZ=[self.x_low_obs, self.y_low_obs, self.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.x_low_obs, self.y_high_obs, 0],
            lineToXYZ=[self.x_low_obs, self.y_high_obs, self.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.x_high_obs, self.y_low_obs, 0],
            lineToXYZ=[self.x_high_obs, self.y_low_obs, self.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.x_high_obs, self.y_high_obs, 0],
            lineToXYZ=[self.x_high_obs, self.y_high_obs, self.z_high_obs])

        p.addUserDebugLine(
            lineFromXYZ=[self.x_low_obs, self.y_low_obs, self.z_high_obs],
            lineToXYZ=[self.x_high_obs, self.y_low_obs, self.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.x_low_obs, self.y_high_obs, self.z_high_obs],
            lineToXYZ=[self.x_high_obs, self.y_high_obs, self.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.x_low_obs, self.y_low_obs, self.z_high_obs],
            lineToXYZ=[self.x_low_obs, self.y_high_obs, self.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.x_high_obs, self.y_low_obs, self.z_high_obs],
            lineToXYZ=[self.x_high_obs, self.y_high_obs, self.z_high_obs])

        project_path = os.path.dirname(os.path.abspath(__file__))
        p.loadURDF(os.path.join(self.urdf_root_path, "plane.urdf"),
                   basePosition=[0, 0, -0.65])
        self.ur_id = p.loadURDF(os.path.join(project_path, r'urdf/ur5.urdf'), useFixedBase=True)
        p.loadURDF(os.path.join(self.urdf_root_path, "table/table.urdf"),
                   basePosition=[0.5, 0, -0.65])
        self.object_id = p.loadURDF(os.path.join(self.urdf_root_path,
                                                 "random_urdfs/000/000.urdf"),
                                    basePosition=[
                                        random.uniform(self.x_low_obs,
                                                       self.x_high_obs),
                                        random.uniform(self.y_low_obs,
                                                       self.y_high_obs), 0.01
                                    ])

        self.num_joints = p.getNumJoints(self.ur_id)

        for i in range(self.num_joints):
            p.resetJointState(
                bodyUniqueId=self.ur_id,
                jointIndex=i,
                targetValue=self.init_joint_positions[i],
            )

        self.robot_pos_obs = p.getLinkState(self.ur_id,
                                            self.num_joints - 1)[4]
        # logging.debug("init_pos={}\n".format(p.getLinkState(self.ur_id,self.num_joints-1)))
        p.stepSimulation()
        self.object_pos = p.getBasePositionAndOrientation(self.object_id)[0]
        return np.array(self.object_pos).astype(np.float32)


    def render(self, mode='human'):
        pass

    def close(self):
        p.disconnect()

# if __name__ == '__main__':
#     # 这一部分是做baseline，即让机械臂随机选择动作，看看能够得到的分数
#     env = urEnv(is_render=True, is_good_view=True)
#     print(env)
#     print(env.observation_space.shape)
#     print(env.action_space.shape)
#     obs = env.reset()
#     print(obs)
#     sum_reward = 0
#     for i in range(100):
#         env.reset()
#         for i in range(2000):
#             action = env.action_space.sample()
#             obs, reward, done, info = env.step(action)
#             sum_reward += reward
#             if done:
#                 break
#     print()
#     print(sum_reward)

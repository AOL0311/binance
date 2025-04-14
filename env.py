import gym
import numpy as np
from gym import spaces

class CryptoTradingEnv(gym.Env):
    def __init__(self):
        super(CryptoTradingEnv, self).__init__()
        self.action_space = spaces.Discrete(3)  # 0: buy, 1: sell, 2: hold
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(2,), dtype=np.float32)

        self.current_price = None
        self.sma = None
        self.position = 0  # 1 for long, -1 for short, 0 for no position

    def reset(self):
        self.position = 0
        return np.array([0, 0], dtype=np.float32)

    def step(self, action):
        # 模擬 reward（實際部署時不使用這部分）
        reward = 0
        if self.position == 1:
            reward = self.current_price - self.prev_price
        elif self.position == -1:
            reward = self.prev_price - self.current_price

        # 更新倉位
        if action == 0:
            self.position = 1
        elif action == 1:
            self.position = -1
        else:
            self.position = 0

        obs = np.array([self.current_price, self.current_price - self.sma], dtype=np.float32)
        done = False
        return obs, reward, done, {}

    def render(self, mode='human'):
        print(f"Position: {self.position}")

    def get_state(self, current_price, sma):
        self.prev_price = self.current_price if self.current_price else current_price
        self.current_price = current_price
        self.sma = sma
        return np.array([current_price, current_price - sma], dtype=np.float32)

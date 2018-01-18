# Figure out random distribution

import gym
import random
import numpy as np
import collections
from collections import Counter
from tqdm import *
import matplotlib.pyplot as plt

env = gym.make('CartPole-v0')
env.reset()

scores =[]
howMany = 10000000
steps = 500
count = 0
for _ in tqdm(range(howMany)):
    #count+=1

    #if count% (howMany/100) == 0:
    #    print( str(int(count / howMany * 100)) + "%")

    env.reset()
    score = 0
    for _1 in range(steps):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        score+= reward
        if done:
            break
    scores.append(score)

print(Counter(scores))
plt.bar(list(Counter(scores).keys()), Counter(scores).values(), 1, color='g')
#plt.show()

ordered = collections.OrderedDict(sorted(Counter(scores).items()))
for key,value in ordered.items():
    print(key, value)

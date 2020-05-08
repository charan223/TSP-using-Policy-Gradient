import matplotlib.pyplot as plt
import numpy as np



entropy = open('rewards_heuristic_20.txt', 'r')
neural = open('rewards_entropy_20.txt', 'r')


Lines = entropy.readlines()
entropy_list = [float(line.strip()) for i, line in enumerate(Lines)]

Lines = neural.readlines()
neural_list = [float(line.strip()) for i, line in enumerate(Lines)]


x = np.arange(84)


plt.plot(x, entropy_list, color='blue')
# plt.plot(x, neural_list, color='blue')

plt.xlabel('Iterations/50', fontsize=12)
plt.ylabel('Rewards', fontsize=12)
# plt.suptitle('Rewards for maze navigation task over 50000 training steps ', fontsize=14)

# plt.legend(['Entropy', 'w/o Entropy'], loc='lower right')

plt.show()


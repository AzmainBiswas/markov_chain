import numpy as np
import matplotlib.pyplot as plt

# define number of steps and starting point

NumberOfStape = 1000
start = 0
p = 0.45 # probability of going up.
Prob = [ p, 1 - p ]
Position = [ start ]
Step = [ 1, -1 ]
for i in range(NumberOfStape):
    rr = np.random.random()
    if rr < Prob[0]:
        position = Position[-1] + 1
    else:
        position = Position[-1] -1
    Position.append(position)

# for ploting Random Walk

fig = plt.figure(figsize=(10,6), dpi=125)
plt.plot(Position, linewidth=0.9)
plt.xlabel("Time")
plt.ylabel("State of Random Walk")
plt.title("1D Simple Random Walk for p = 0.45")
plt.grid(True)
plt.show()

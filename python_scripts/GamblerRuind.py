import numpy as np
import matplotlib.pyplot as plt

S_AMOUNT = 50
W_AMOUNT = 140

I_Amount = S_AMOUNT
NumberOfGame = 100000

Amount = [ I_Amount ]
p = 0.45 # probability of winn
Prob = [p,1-p]

t = 0
while NumberOfGame > 0:
    t += 1
    rr = np.random.random()
    if rr < Prob[0]:
        I_Amount += 1
    else:
        I_Amount -= 1 

    Amount.append(I_Amount)

    if I_Amount == 0:
        break
    if I_Amount == W_AMOUNT:
        break
    NumberOfGame -= 1

print(f"Number of game: {t}")
print(f"Total Gain: {I_Amount}")

# Graph Plot,
fig = plt.figure(figsize=(8,5),dpi=200)
plt.plot(Amount, color='red', linewidth=0.6)
plt.xlabel(f"Number of game (start from {S_AMOUNT})")
plt.ylabel(f"State of Gambeler (0-{W_AMOUNT})")
plt.title(f"Gambler's Ruin Problem (p = {p})")
plt.grid(True)
plt.show()

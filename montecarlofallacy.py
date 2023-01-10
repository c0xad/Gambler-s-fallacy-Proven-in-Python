import random

def flip_coin():
  return 'heads' if random.random() < 0.5 else 'tails'

def simulate_coin_flips(n):
  flips = []
  for i in range(n):
    flips.append(flip_coin())
  return flips

def count_heads(flips):
  return sum(1 for flip in flips if flip == 'heads')

# Simulate flipping a coin 1000 times
flips = simulate_coin_flips(1000)

# Count the number of heads
heads = count_heads(flips)

# Calculate the probability of heads
probability = heads / len(flips)

print(f'Number of heads: {heads}')
print(f'Probability of heads: {probability:.2f}')

# Simulate flipping the coin 100 more times
flips = simulate_coin_flips(100)

# Count the number of heads
heads = count_heads(flips)

# Calculate the probability of heads
probability = heads / len(flips)

print(f'Number of heads: {heads}')
print(f'Probability of heads: {probability:.2f}')

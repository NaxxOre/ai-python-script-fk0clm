import random, time

print('Tiny generator')
for _ in range(5):
  print('value:', random.randint(1,999999))
  time.sleep(0.05)

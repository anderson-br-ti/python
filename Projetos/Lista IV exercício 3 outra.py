from random import randint

v1 = [randint(1, 100) for x in range(10)]
v2 = [randint(1, 100) for x in range(10)]
v3 = []
for x in zip(v1, v2):
  v3.extend(list(x))
print('v1:', v1)
print('v2:', v2)
print('v3:', v3)

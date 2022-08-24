t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
# t[0] = 88888
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
v = ([1, 2, 3], [3, 2, 1])
print(v)
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)
x, y, z = t
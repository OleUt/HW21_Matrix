import numpy as np
my = [[4, 2, 0], [1, 3, 2], [-1, 3, 10]]
m = np.array(my)
print(m)

# поміняємо перший та другий рядок місцями
f = m[1]
s = m[0]
t = m[2]
m = np.vstack((f, s, t))
print(m)

# до 2-го рядка додати 1-ший, помножений на -4; до третього рядка додати перший
f = m[0]
s = m[1] + f * (-4)
t = m[2] + f
m = np.vstack((f, s, t))
print(m)

# 2-ий рядок поділити на -2, третій рядок ділимо на 6
f = m[0]
s = m[1] / (-2)
t = m[2] / 6
m = np.vstack((f, s, t))
print(m)

# поміняємо другий та третій рядок місцями
f = m[0]
s = m[2]
t = m[1]
m = np.vstack((f, s, t))
print(m)

# до 3-тього рядка додамо 2-ий, помножений на -5
f = m[0]
s = m[1]
t = m[2] + s * (-5)
m = np.vstack((f, s, t))
print(m)

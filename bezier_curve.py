# Author fuyuan: fuyuan360@qq.com
# Created on 2025/7/16
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


def bezier_curve(points, num=200):
    n = len(points) - 1
    t = np.linspace(0, 1, num)
    curve = np.zeros((num, 2))

    for i in range(n + 1):
        bern = comb(n, i) * (t**i) * ((1 - t) ** (n - i))
        curve += np.outer(bern, points[i])

    return curve


# 设置控制点 (可修改坐标增减点数)
control_points = np.array([[0, 0], [1, 3], [4, 5], [6, 2], [8, 4]])

curve = bezier_curve(control_points)

# 可视化结果
plt.plot(control_points[:, 0], control_points[:, 1], "ro--")
plt.plot(curve[:, 0], curve[:, 1], "b-")
plt.gca().set_aspect("equal")
plt.title(f"{len(control_points)}点贝塞尔曲线")
plt.show()

import numpy as np
from sympy import *
import matplotlib.pyplot as plt

p, la = symbols('x  y')

def NewtonInsert(xk, fxk,degree):
    # 求差商
    n = len(xk)
    dp = np.zeros((n, n))
    for i in range(n):
        dp[i, 0] = fxk[i]
    for i in range(1, n):
        for j in range(i, n):
            dp[j, i] = (dp[j, i-1] - dp[j-1, i-1])/(xk[j] - xk[j - i])
    # 得到的是根据阶数得到的表达式
    s = 0
    for i in range(degree+1):
        la = dp[i, i]
        for j in range(0, i):
            la = la * (p - xk[j])
        s = s + la
    # 返回的是插值得到的牛顿插值多项式
    return s

if __name__ == "__main__":
    # 输入数据，包括函数点和函数值
    xk = [0.40,0.55,0.65,0.80,0.90,1.05]
    fxk = [0.41075,0.57815,0.69675,0.88811,1.02652,1.25386]
    degree=3
    # 牛顿插值法求解并且print
    s = NewtonInsert(xk, fxk, degree)
    print(f"表达式为{s}\n")
    print(f'简化后的表达式为：{expand(s)}\n')
    # 插值点，自选插值点
    x1 = np.linspace(0.2, 1.2, 50)
    x1 = list(x1)
    y1 = []
    for i in x1:
        y1.append(s.subs(p, i))
    print(f"{x1}\n{y1}")
    # 可视化
    plt.scatter(np.array(xk),np.array(fxk),marker='x',color='red')
    plt.plot(x1,y1)
    plt.show()

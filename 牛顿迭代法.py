import sympy as sy
x = sy.symbols('x')
def newton(f,l,o):
    N = [o, o]
    for i in range (1,100):
        N[1]=N[0] -f.subs('x', N[0]) /f.diff().subs('x', N[0])
        N[0] = N[1]
        if abs(abs(N[1] - N[0]) - l)<l*10:
            return N[1]
if __name__=='__main__':
    l = 0.000005
    o=1.5
    f = x ** 3-sy.sin(x) - 1
    ans=newton(f,l,o)
    print(f"在误差为{l}以内求解得到方程在{o}附近的根为:\nx={ans}")
import random
import matplotlib.pyplot as plt

N = ord("P") % 5 + 1
print(f"\n\t Number of variant is {N}")

def check(expression: list, N=5000):
    """
    Функція для перевірки складної умови із
    завдання 1 лабораторної роботи №2.

    Функція нічого не повертає та будує графік області, що задовольняє
    складній умові

    Параметри:
         expression(str): рядок з умовою
            Приклад:
               '-2<=x<=0 and y>0'

         N(int): кількість точок на графіку. Необов'язковий параметр,
                 за замовченням N=5000
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    a = -3
    b = 3
    plt.xlim(a, b)
    plt.ylim(a, b)

    for _ in range(N):
        x = random.random()*(b-a)+a # щоб випадкове число було в інтервалі (a,b)
        y = random.random()*(b-a)+a
        for s in expression[0:]:
            if eval(s):
                plt.plot(x, y, "k.", markersize=1)
    plt.show();
    
check(['-2<=x<=0 and 0<=y<=2 and (y-x)>=2',
       '-2<=x<=0 and 0>=y>=-2 and abs(y+x)>=2',
       '2>=x>=0 and 0>=y>=-2 and abs(y-x)>=2',
       '2>=x>=0 and 0<=y<=2 and abs(y+x)>=2',
       ])




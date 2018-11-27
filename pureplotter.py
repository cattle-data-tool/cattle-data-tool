
u_x = 0;
u_y = 0;

i = 1
t = 1

from data import CsvDataBase
data = CsvDataBase()
data.add_csv("DATA_01_05_Cow_42.csv")

di_x = data.getAccel(42,"acc_x_g")
di_y = data.getAccel(42,"acc_y_g")

n = len

def initial_x(v_x):
    global u_x
    u_x = v_x
    return u_x

def initial_y(v_y):
    global u_y
    u_y = v_y
    return u_y

while i <= n:
    a_x = di_x[i]
    a_y = di_y[i]

    s_x = (u_x*t)+(0.5*(a_x*t))
    s_y = (u_y*t)+(0.5*(a_y*t))

    v_x = u_x+s_x
    v_y = u_y+s_y


    v_x = round(v_x,2)
    v_y = round(v_y,2)
    print(v_x)
    pause = input()
    print(v_x,",",v_y)

    initial_x(v_x)
    initial_y(v_y)

    i += 1

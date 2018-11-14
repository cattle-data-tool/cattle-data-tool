u_x = 0;
u_y = 0;

i = 1
t = 1

di_x = {1:134234324, 2:1322344124, 3:131324234124, 4:12432423421414, 5:123421521252 }
di_y = {1:345345435345, 2:2342343242, 3:2342352332, 4:324235432, 5:4532524353423}

n = 5

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

    v_x = u_x+s_x;
    v_y = u_y+s_y;

    print(v_x,",",v_y)

    initial_x(v_x)
    initial_y(v_y)

    i +=1


u_x = 0;
u_y = 0;

i = 1
t = 1

""" Commented by IcE 14/11/2018 18:01 """


from data import Data
data = Data()
data.add_csv("DATA_01_05_Cow_42.csv")

#uncomment this to use real data for cow 42
di_x = data.getAccel(42,'acc_x_g')
di_y = data.getAccel(42,'acc_y_g')

#Uncomment this to use dummy data
#di_x = {1:134234324, 2:1322344124, 3:131324234124, 4:12432423421414, 5:123421521252 }
#di_y = {1:345345435345, 2:2342343242, 3:2342352332, 4:324235432, 5:4532524353423}

print (di_x)
exit()
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


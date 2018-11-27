i = 0
t = 1

dict = []
u_x = 0
u_y = 0

def initial_x(v_x):
    global u_x
    u_x = v_x
    return u_x

def initial_y(v_y):
    global u_y
    u_y = v_y
    return u_y

def position(v_x, v_y):
    global dict
    
    a = (v_x, v_y)
    dict.append(a)
    
    



def plotter_math(di_x,di_y):
    
    global i 
    n = (len(di_x) - 1)
   

    while i <= n:
        a_x = di_x[i]
        a_y = di_y[i]
        #print(a_x,a_y)

        s_x = (u_x*t)+(0.5*(a_x*t))
        s_y = (u_y*t)+(0.5*(a_y*t))

        v_x = u_x+s_x
        v_y = u_y+s_y

        position(v_x, v_y)

        ##print(v_x,",",v_y)###uncomment this for #printing the values

        initial_x(v_x)
        initial_y(v_y)
        i+=1
    
    return(dict)

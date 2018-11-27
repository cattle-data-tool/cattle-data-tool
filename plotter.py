t = 1

dict = []
u_x = 0
u_y = 0

def initial_x(v_x):
    global u_x
    u_x = v_x


def initial_y(v_y):
    global u_y
    u_y = v_y
  

def position(v_x, v_y):
    global dict
    a = (v_x, v_y)
    #print(a)
    
    dict.append(a)
    
    



def plotter_math(di_x,di_y):
    global u_x
    global u_y
    global t
    i = 0 
    n = (len(di_x) - 1)

   

    while i <= n:
    
        a_x = di_x[i] #current accels from csv file
        a_y = di_y[i]
       
        #print("u_x previous value is ",u_x)
        s_x = (u_x*t)+(0.5*(a_x*t)) # we get displacemnt s 
        #print("s_x calculated value",s_x)
        s_y = (u_y*t)+(0.5*(a_y*t))

        v_x = u_x+s_x 
        v_y = u_y+s_y

        position(v_x, v_y) #stores all calulated cordinates in dict list
        #print("v_x sent to dict is",v_x)
        ##print(v_x,",",v_y)###uncomment this for #printing the values
        #print("-------------------------")
        initial_x(a_x)  #set value as inital to next iter.
        initial_y(a_y)
        i+=1
    
    return(dict)

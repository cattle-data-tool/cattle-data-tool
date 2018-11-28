class Plotter:

    t = 1
    dict = []
    u_x = 0
    u_y = 0

    def __init__(self):
        pass
    
    

    def position(self,v_x, v_y):
        a = (v_x, v_y)
        self.dict.append(a)

    def plotter_math(self,di_x,di_y):

        self.t = 1
        self.dict = []
        self.u_x = 0
        self.u_y = 0
        i = 0 
        t = 1
        n = (len(di_x) - 1)
        while i <= n:
        
            a_x = di_x[i] #current accels from csv file
            a_y = di_y[i]
        
           #print("u_x previous value is ",self.u_x)
            s_x = (self.u_x*t)+(0.5*(a_x*t)) # we get displacemnt s 
            #print("s_x calculated value",s_x)
            s_y = (self.u_y*t)+(0.5*(a_y*t))

            v_x = self.u_x+s_x 
            v_y = self.u_y+s_y

            self.position(v_x, v_y) #stores all calulated cordinates in dict list
            #print("v_x sent to dict is",v_x)
            ##print(v_x,",",v_y)###uncomment this for #printing the values
            #print("-------------------------")
            self.u_x = a_x
            self.u_y = a_y

            i+=1
        
        return(self.dict)







    




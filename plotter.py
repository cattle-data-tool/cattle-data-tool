class Plots:
    u_x = 0;
    u_y = 0;

    i = 1
    t = 1
    step = 0
    dic = {}

    from data import Data
    data = Data()
    data.add_csv("DATA_01_05_Cow_42.csv")

    di_x = data.getAccel(42,'acc_x_g')
    di_y = data.getAccel(42,'acc_y_g')

    #Uncomment this to use dummy data
    #di_x = {1:134234324, 2:1322344124, 3:131324234124, 4:12432423421414, 5:123421521252 }
    #di_y = {1:345345435345, 2:2342343242, 3:2342352332, 4:324235432, 5:4532524353423}


    n = 5

    def initial_x(v_x):
        global u_x
        u_x = v_x
        return u_x

    def initial_y(v_y):
        global u_y
        u_y = v_y
        return u_y

    def position(v_x, v_y):
        global dic
        global step
        a = (v_x, v_y)
        dict[step] = a
        step += 1
        return dict

    while i <= n:
        a_x = di_x[i]
        a_y = di_y[i]

        s_x = (u_x*t)+(0.5*(a_x*t))
        s_y = (u_y*t)+(0.5*(a_y*t))

        v_x = u_x+s_x;
        v_y = u_y+s_y;

        position(v_x, v_y)

        #print(v_x,",",v_y)###uncomment this for printing the values

        initial_x(v_x)
        initial_y(v_y)

        i += 1



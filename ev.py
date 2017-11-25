import turtle
import random
import time

dirs = ['l','r','f','b'] #left, right forward, backward
colors = ['red','orange','yellow','green','blue','purple','black']

def generate_turtles(paths):
    c = 0
    for path in paths:
        t = turtle.Turtle()
        t.shape('turtle')
        if c == len(colors):
            c = 0
        t.color(colors[c])
        c += 1
        
        t.speed(999)
        for direction in path:
            if direction == 'l':
                t.right(-90)
                t.forward(5)
            elif direction == 'r':
                t.right(90)
                t.forward(5)
            elif direction == 'f':
                t.forward(5)
            elif direction == 'b':
                t.forward(-5)

def generate_turtle_paths(n,pl): #n=number of turtles, pl = path length
    l = []
    for _ in range(n):
        p = []
        for _ in range(pl):
            p.append(random.choice(dirs))
        l.append(p)
    return l

def rank_paths(paths):
    rp = [] #rank paths
    for p in paths:
        v = 0
        for direction in p:
            if direction == 'f':
                v += 1
        rp.append(v)
    return rp

def top_x_paths(x,paths):
    best_paths = []
    cp = paths
    for _ in range(x):
        ranks = rank_paths(cp)
        br = max(ranks) #best value
        i_br = ranks.index(br) #index of best value
        print "best path value:", br, cp[i_br]
        best_paths.append(cp[i_br])
        cp.pop(i_br)
    return best_paths

def breed_turtles(x1,x2):
    fx = []
    for i in range(len(x1)):
        if x1[i] == 'f' or x2[i] == 'f':
            fx.append('f')
        else:
            fx.append(random.choice(dirs))
    return fx

            
        

#list_of_turtles = generate_turtles(5)
#list_of_turtles[0].forward(10)
#list_of_turtles[1].forward(20)
num_turtles = 5
top_turtles = 4
num_breed_turtles = 1
path_length = 30
lop = generate_turtle_paths(num_turtles,path_length)
for i in range(20):
    turtle.resetscreen()
    generate_turtles(lop)
    np = top_x_paths(top_turtles,lop)
    new_turtles = generate_turtle_paths(num_turtles-top_turtles-num_breed_turtles,path_length)
    lop = np + new_turtles
    print np[0]
    print np[1]
    lop.append(breed_turtles(np[0],np[1]))
    print i
    print "post done"





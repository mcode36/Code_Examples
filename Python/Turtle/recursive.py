import turtle

t = turtle.Pen()


def move(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    
def shape(d,n):
    if n == 1:
        t.forward(d)
        t.left(60)
        t.forward(d)
        t.right(120)
        t.forward(d)
        t.left(60)
        t.forward(d)
    else:
        n = n - 1
        shape(d,n)
        t.left(60)
        shape(d,n)
        t.right(120)
        shape(d,n)
        t.left(60)
        shape(d,n)
        

y = 200

#n = 1
move(-100,y)
d = 100
shape(d,1)

#n = 2
y = y - 100
move(-100,y)
d = d/3
shape(d,2)

#n = 3
y = y - 100
move(-100,y)
d = d/3
shape(d,3)

# n = 4
y = y - 100
move(-100,y)
d = d/3
shape(d,4)

# n = 5
y = y - 100
move(-100,y)
d = d/3
shape(d,5)


import turtle

# create screen object
sc = turtle.Screen()

# create turtle object
pen = turtle.Turtle()


# method to draw square
def draw():
for i in range(4):
    pen.forward(30)
    pen.left(90)

pen.forward(30)

# Driver Code
if __name__ == "__main__":

    # set screen
    sc.setup(600, 600)

    # set turtle object speed
    pen.speed(100)

    # loops for board
    for i in range(8):

    # not ready to draw
    pen.up()

    # set position for every row
    pen.setpos(0, 30 * i)

    # ready to draw
    pen.down()

    # row
    for j in range(8):

        # conditions for alternative color
        if (i + j) % 2 == 0:
            col = 'black'

        else:
            col = 'white'

        # fill with given color
        pen.fillcolor(col)

        # start filling with colour
        pen.begin_fill()

        # call method
        draw()
        # stop filling
        pen.end_fill()

    # hide the turtle
    pen.hideturtle()

# This code is contributed by Deepanshu Rustagi.



#a=int(input('Введите число: '))
#b=int(input('Введите ещё число :'))
#print('Результат = ', a*b)
#for i in range(1, a+1):
#    for j in range(1, b+1):
#        print( i*j, end='; ')
#    print()


#number = int(input('Введите число: '))
#fac = 1

#while number > 1:
#    fac = fac * number
#    number = number - 1

#print(fac)

 #def is_prime(x):
  #      for i in range(2, x):
  #          if x % i == 0:
  #              return False
   #     return True
#a = int(input('Введите число: '))
#print('Prime(', a, ') is', is_prime(a))

#for i in range(2, a):
 #   if is_prime(i):
  #      print(i)
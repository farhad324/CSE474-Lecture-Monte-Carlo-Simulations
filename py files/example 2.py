import turtle
import random
import matplotlib.pyplot as plt
import math


myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)


myPen.up()
myPen.setposition(-200, -200)
myPen.down()
myPen.fd(400)
myPen.left(90)
myPen.fd(400)

myPen.left(90)
myPen.fd(400)
myPen.left(90)
myPen.fd(400)
myPen.left(90)


myPen.up()
myPen.setposition(0, -200)
myPen.down()
myPen.circle(200)


in_circle = 0
out_circle = 0


pi_values = []


for i in range(5):
    for j in range(1000):

        x = random.randrange(-200, 200)
        y = random.randrange(-200, 200)

        if x ** 2 + y ** 2 > 200 ** 2:
            myPen.color("black")
            myPen.up()
            myPen.goto(x, y)
            myPen.down()
            myPen.dot()
            out_circle = out_circle + 1

        else:
            myPen.color("red")
            myPen.up()
            myPen.goto(x, y)
            myPen.down()
            myPen.dot()
            in_circle = in_circle + 1

        pi = 4.0 * in_circle / (in_circle + out_circle)

        pi_values.append(pi)

        avg_pi_errors = [abs(math.pi - pi) for pi in pi_values]

    print(pi_values[-1])


plt.axhline(y=math.pi, color='g', linestyle='-')
plt.plot(pi_values)
plt.xlabel("Iterations")
plt.ylabel("Value of PI")
plt.show()


plt.axhline(y=0.0, color='g', linestyle='-')
plt.plot(avg_pi_errors)
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()

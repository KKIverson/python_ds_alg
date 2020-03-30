import turtle
# 递归方法绘制谢尔宾斯基三角形

def drawTri(t, points):
    t.down()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.up()


def getMiddle(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


def sierpinski(t, points, degree):
    if degree >= 1:
        t.up()
        t.goto(points[0][0], points[0][1])
        drawTri(t, points)
        left = [
            points[0],
            getMiddle(points[0], points[1]),
            getMiddle(points[0], points[2])]
        sierpinski(t, left, degree - 1)
        middle = [
            getMiddle(points[0], points[1]),
            points[1],
            getMiddle(points[1], points[2])]
        sierpinski(t, middle, degree - 1)
        right = [
            getMiddle(points[0], points[2]),
            getMiddle(points[2], points[1]),
            points[2]]
        sierpinski(t, right, degree - 1)


t = turtle.Turtle()
myScreen = turtle.Screen()
points = [[-200, -100.], [0, 200], [200, -100]]
sierpinski(t, points, 6)
myScreen.exitonclick()

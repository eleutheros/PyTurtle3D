import turtle

turtle.colormode(255)
turtle.tracer(False)

LEVELS = 10
DEGREES = 51
BROWN = 0x60, 0x33, 0x11
GREEN = 0x00, 0xFF, 0x00
dR = (BROWN[0] - GREEN[0]) / LEVELS
dG = (BROWN[1] - GREEN[1]) / LEVELS
dB = (BROWN[2] - GREEN[2]) / LEVELS

def tree(levels, degrees, distance, thickness, scale):
	if levels == 0:
		return
	turtle.width(thickness)
	initial_heading = turtle.heading()
	r, g, b = GREEN[0] + levels*dR, GREEN[1] + levels*dG, GREEN[2] + levels*dB
	turtle.color((r, g, b))
	turtle.forward(distance)
	start = turtle.position()

	turtle.left(degrees)
	tree(levels-1, degrees, scale*distance, scale*thickness, scale)

	turtle.color((r,g,b))
	turtle.up()
	turtle.goto(*start)
	turtle.down()
	turtle.setheading(initial_heading)
	turtle.right(degrees)
	tree(levels-1, degrees, scale*distance, scale*thickness, scale)
	return

if __name__ == "__main__":
	psi = (5**0.5 - 1) / 2
	turtle.left(90)
	turtle.up()
	turtle.goto(0, -100)
	turtle.down()
	tree(LEVELS, DEGREES, 200, 10, psi)
	turtle.mainloop()

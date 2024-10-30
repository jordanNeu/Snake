from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].position())
    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # screen.onkey(key="w", fun=move_forward)
    # screen.onkey(key="s", fun=move_backward)
    # screen.onkey(key="a", fun=turn_left)
    # screen.onkey(key="d", fun=turn_right)
    # screen.onkey(key="c", fun=screen.reset)


    # for segment in segments:
    #     segment.forward(20)
    #     time.sleep(0.1)

# square1 = Turtle(shape = "square")
# square1.color("white")
# square1.pendown()
# square1.goto(0, 0)
#
# square2 = Turtle(shape = "square")
# square2.color("white")
# square2.goto(-20, 0)
#
# square3 = Turtle(shape = "square")
# square3.color("white")
# square3.goto(-40, 0)

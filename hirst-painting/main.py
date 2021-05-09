import turtle as turtle_module
import random
# import colorgram


# colors = colorgram.extract('./img/spot_painting.jpg', 34)

# rgb_colors = []


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()


color_list = [
    (187, 18, 44), (243, 231, 66), (210, 236, 242), 
    (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17),
    (108, 181, 209), (12, 142, 88), (12, 166,214), (210, 152, 96), (187, 41, 61), (241, 231, 2),(23, 39, 76), (77, 174, 94), (36, 44, 112), (215,69, 50), (218, 130, 155), (124, 185, 119),
    (235, 165, 183), (5, 58, 39), (146, 209,220), (8, 95, 55), (4, 86, 111), (162, 29, 27),(234, 171, 164), (162, 212, 176), 
    (87, 22,58), (182, 188, 209), (118, 122, 149), (94, 16, 15)
]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
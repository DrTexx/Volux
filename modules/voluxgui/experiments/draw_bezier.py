from tkinter import Tk, Canvas

root = Tk()

window = Canvas(root, width=800, height=800)
window.pack()


def calc_bezier_points(start_point, end_point):
    if start_point[0] < end_point[0]:
        print("start x behind end x")
        handle1_x = end_point[0] / 2
        handle1_y = start_point[1]
        handle2_x = end_point[0] / 2
        handle2_y = end_point[1]
    elif start_point[0] > end_point[0]:
        print("start x ahead of end x")
        raise NotImplementedError()

    handle1 = [handle1_x, handle1_y]
    handle2 = [handle2_x, handle2_y]

    return [start_point, handle1, handle2, end_point]


def bezier_curve():
    # create empty list for points
    # points = [[0, 0], [250, 0], [250, 500], [500, 500]]
    points = calc_bezier_points([0, 0], [500, 500])

    # loops through 4 times to get 4 control points
    # for i in range(4):
    #     while True:
    #         # user input
    #         p_input = input(f"Enter X,Y Coordinates for point #{str(i)}:")
    #         # splits the string into x and y coordinates
    #         p_components = p_input.split(",")
    #         # checks to see if user hasnt entered two coordinates
    #         if len(p_components) != 2:
    #             print("Missing coordinate please try again.")
    #             p_input = input("Enter starting point X,Y Coordinates:")
    #         # checks to see if the values can not be converted into floats.
    #         try:
    #             x = float(p_components[0])
    #             y = float(p_components[1])
    #         except ValueError:
    #             print("Invalid coordinates", p_components, "please try again.")
    #         # appends the x and y coordinates as a 2 dimensional array.
    #         else:
    #             p.append([float(p_components[0]), float(p_components[1])])
    #             break
    print(points)

    # Start x and y coordinates, when t = 0
    # x_start = points[0][0]
    # y_start = points[0][1]

    # MODIFICATION: TWEAK RESOLUTION OF CURVE
    # lines_rendered = 10  # minimum: 4

    # loops through in intervals of 0.1
    # for i in range(0, lines_rendered, 1):
    #     t = i / (lines_rendered - 1)
    #     x = (
    #         p[0][0] * (1 - t) ** 3
    #         + p[1][0] * 3 * t * (1 - t) ** 2
    #         + p[2][0] * 3 * t ** 2 * (1 - t)
    #         + p[3][0] * t ** 3
    #     )
    #     y = (
    #         p[0][1] * (1 - t) ** 3
    #         + p[1][1] * 3 * t * (1 - t) ** 2
    #         + p[2][1] * 3 * t ** 2 * (1 - t)
    #         + p[3][1] * t ** 3
    #     )

    #     draw_line = window.create_line(x, y, x_start, y_start)
    #     print("draw_line:", draw_line)
    #     # updates initial values
    #     x_start = x
    #     y_start = y

    draw_line = window.create_line(points, smooth=True, width=2)
    print("line drawn:", draw_line)


bezier_curve()
root.mainloop()

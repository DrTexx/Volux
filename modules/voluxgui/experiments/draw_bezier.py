"""Experiments with drawing bezier curves."""

from tkinter import Tk, Canvas, Frame
from typing import Any, NewType, List

Coord = NewType("Coord", List[float])
BezierPoints = NewType("BezierPoints", List[Coord])
NODE_RADIUS = 3
NODE_COLOUR = "red"


class RootCanvas(Canvas):
    """Canvas inside topmost widget."""

    def __init__(self, parent: Any, *args: Any, **kwargs: Any) -> None:
        """See class docstring."""
        super().__init__(parent, *args, **kwargs)


class MainApplication:
    """Topmost Tkinter Widget."""

    def __init__(self, root: Tk) -> None:
        """See class docstring."""
        self.root = root
        self.rootCanvas = RootCanvas(self.root, width=800, height=800)
        self.gen_grid(100, 800, 800)

        # points = [[0, 0], [250, 0], [250, 500], [500, 500]]
        # points = [[100, 100], [250, 100], [250, 400], [400, 400]]

        # points = self.calc_bezier_points(Coord([100, 400]), Coord([400, 100]))
        # print(points)
        # self.draw_bezier_nodes(points)
        # draw_line = self.rootCanvas.create_line(points, smooth=True, width=2)  # type: ignore
        # print("line drawn:", draw_line)

        points = self.calc_bezier_points(Coord([400, 100]), Coord([700, 400]))
        print(points)
        self.draw_bezier_nodes(points)
        draw_line = self.rootCanvas.create_line(points, smooth=True, width=2)  # type: ignore
        print("line drawn:", draw_line)

        points = self.calc_bezier_points(Coord([700, 400]), Coord([400, 700]))
        print(points)
        self.draw_bezier_nodes(points)
        draw_line = self.rootCanvas.create_line(points, smooth=True, width=2)  # type: ignore
        print("line drawn:", draw_line)

        # points = self.calc_bezier_points(Coord([400, 700]), Coord([100, 400]))
        # print(points)
        # self.draw_bezier_nodes(points)
        # draw_line = self.rootCanvas.create_line(points, smooth=True, width=2)  # type: ignore
        # print("line drawn:", draw_line)

        self.rootCanvas.pack()

    def gen_grid(self, step: float, x_max: float, y_max: float) -> None:
        x_now = 0.0
        y_now = 0.0

        while x_now < x_max:
            self.rootCanvas.create_line(x_now, 0, x_now, y_max, tag="john")  # type: ignore
            x_now += step

        while y_now < y_max:
            self.rootCanvas.create_line(0, y_now, x_max, y_now)
            y_now += step

    def draw_node(self, p: Coord) -> None:
        """Draw a node on the canvas."""
        # https://python4kids.brendanscott.com/2012/09/19/quadratic-bezier-curves/
        boundingBox = (
            p[0] - NODE_RADIUS,
            p[1] + NODE_RADIUS,
            p[0] + NODE_RADIUS,
            p[1] - NODE_RADIUS,
        )
        # mixed + and - because y runs from top to bottom not bottom to top
        self.rootCanvas.create_oval(boundingBox, fill=NODE_COLOUR)  # type: ignore

    def draw_bezier_nodes(self, points: BezierPoints) -> None:
        for point in points:
            self.draw_node(point)

    def calc_bezier_points(
        self, start_point: Coord, end_point: Coord
    ) -> BezierPoints:
        """Take a start and end point and generate bezier points between them."""
        x_increases = start_point[0] < end_point[0]
        x_decreases = start_point[0] > end_point[0]
        y_increases = start_point[1] < end_point[1]
        y_decreases = start_point[1] > end_point[1]

        x_start = start_point[0]
        # y_start = start_point[1]

        x_range = abs(end_point[0] - start_point[0])
        # y_range = abs(end_point[1] - start_point[1])

        increase_x_half_range = x_start + x_range / 2
        decrease_x_half_range = x_start - x_range / 2

        if x_increases:

            handle1_x = increase_x_half_range
            handle2_x = increase_x_half_range

            if y_increases:

                handle1_y = start_point[1]
                handle2_y = end_point[1]

            elif y_decreases:

                handle1_y = end_point[1]
                handle2_y = start_point[1]

        elif x_decreases:

            handle1_x = decrease_x_half_range
            handle2_x = decrease_x_half_range

            if y_increases:

                handle1_y = start_point[1]
                handle2_y = end_point[1]

            # elif y_decreases:

            #     handle1_y = end_point[1]
            #     handle1_y = end_point[1]

        # elif start_point[0] > end_point[0]:
        #     print("start x ahead of end x")
        #     handle2_x = (start_point[0] - end_point[0]) + end_point[0] / 2
        #     handle2_y = end_point[1]
        #     handle1_x = (start_point[0] - end_point[0]) + end_point[0] / 2
        #     handle1_y = start_point[1]

        # if start_point[0] < end_point[0]:
        #     print("start y behind end y")

        # elif start_point[0] > end_point[0]:
        #     print("start y ahead of end y")

        handle1 = Coord([handle1_x, handle1_y])
        handle2 = Coord([handle2_x, handle2_y])

        return BezierPoints([start_point, handle1, handle2, end_point])


root = Tk()
app = MainApplication(root)
root.mainloop()

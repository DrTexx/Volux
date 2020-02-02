"""Experiments with drawing bezier curves."""

from tkinter import Tk, Canvas, Frame
from typing import Any, NewType, List

Coord = NewType("Coord", List[float])
BezierPoints = NewType("BezierPoints", List[List[float]])


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

        # points = [[0, 0], [250, 0], [250, 500], [500, 500]]
        points = self.calc_bezier_points(Coord([0, 0]), Coord([500, 500]))
        print(points)
        draw_line = self.rootCanvas.create_line(points, smooth=True, width=2)  # type: ignore
        print("line drawn:", draw_line)

        # points = self.calc_bezier_points(
        #     Coord([1000, 1000]), Coord([500, 500])
        # )
        # print(points)
        # draw_line = self.rootCanvas.create_line(points, smooth=True, width=2)  # type: ignore
        # print("line drawn:", draw_line)

        self.rootCanvas.pack()

    def calc_bezier_points(
        self, start_point: Coord, end_point: Coord
    ) -> BezierPoints:
        """Take a start and end point and generate bezier points between them."""
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

        return BezierPoints([start_point, handle1, handle2, end_point])


root = Tk()
app = MainApplication(root)
root.mainloop()

import math

from PIL import ImageDraw


class MyImageDraw(ImageDraw.ImageDraw):
    def regular_polygon(
        self,
        center_coords,
        sides,
        radius,
        rotation=0,
        fill=None,
        outline=None,
    ):
        x, y = center_coords
        coords = [
            (
                (
                    x
                    + radius
                    * math.cos(2 * math.pi * i / sides - math.pi + rotation)
                ),
                (
                    y
                    + radius
                    * math.sin(2 * math.pi * i / sides - math.pi + rotation)
                ),
            )
            for i in range(sides)
        ]
        self.polygon(coords, fill, outline)

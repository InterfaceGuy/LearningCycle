from manim import *
import numpy as np

class BinaryCode(Scene):
    def construct(self):
        # Configure for square output with transparency
        config.pixel_width = 1080
        config.pixel_height = 1080
        self.camera.background_color = None
        
        # Generate 10x10 random binary digits
        binary_grid = VGroup()
        for i in range(10):
            for j in range(10):
                digit = Text(
                    str(np.random.randint(2)),
                    color=WHITE,
                    font_size=60
                )
                digit.move_to([j-4.5, -i+4.5, 0])  # Position in grid
                binary_grid.add(digit)
        
        self.add(binary_grid)

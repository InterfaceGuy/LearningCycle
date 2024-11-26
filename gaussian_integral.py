from manim import *
import numpy as np

class GaussianIntegral(Scene):
    def construct(self):
        # Configure for square output with transparency
        config.pixel_width = 1080
        config.pixel_height = 1080
        self.camera.background_color = None
        
        # Create the Gaussian function
        def gaussian(x):
            return 2 * np.exp(-x**2 / 2)  # Scaled up by 2 for better visibility
        
        # Create the curve
        curve = ParametricFunction(
            lambda t: np.array([t, gaussian(t), 0]),
            t_range=[-4, 4],
            stroke_width=9,
            color=WHITE
        )
        
        # Create filled area under the curve
        filled_curve = curve.copy()
        filled_curve.add_line_to(np.array([4, 0, 0]))
        filled_curve.add_line_to(np.array([-4, 0, 0]))
        filled_curve.set_fill(WHITE, opacity=0.4)
        filled_curve.set_stroke(width=0)  # Remove the stroke from fill
        
        # Scale and center everything
        curve.scale_to_fit_width(7)
        filled_curve.scale_to_fit_width(7)
        curve.center()
        filled_curve.center()
        
        # Add both to scene
        self.add(filled_curve, curve)

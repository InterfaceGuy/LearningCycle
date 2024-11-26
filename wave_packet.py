from manim import *
import numpy as np

class WavePacket(Scene):
    def construct(self):
        # Configure for square output with transparency
        config.pixel_width = 1080
        config.pixel_height = 1080
        self.camera.background_color = None
        
        # Create the wave packet using a Gaussian envelope multiplied by a carrier wave
        def wave_func(x):
            envelope = np.exp(-x**2 / 2)
            carrier = np.sin(8*x)
            return 2 * envelope * carrier  # Scale y by factor of 2
        
        # Create the parametric function
        wave = ParametricFunction(
            lambda t: np.array([t, wave_func(t), 0]),
            t_range=[-4, 4],
            stroke_width=9,  # Much thicker stroke for scaling
            color=WHITE
        )
        
        # Scale and center the wave
        wave.scale_to_fit_width(7)  # Leave some padding
        wave.center()
        self.add(wave)

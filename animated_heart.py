MIT License

Copyright (c) 2025 IRUTABYOSE Yoramu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
ANIMATED HEART GENERATOR
Creates a smooth, beating heart animation using matplotlib.
Run directly: `python animated_heart.py`
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configure the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')  # Dark background
ax.set_xlim(-17, 17)
ax.set_ylim(-17, 17)
ax.axis('off')  # Hide axes
fig.patch.set_alpha(0.0)  # Transparent figure background

# Heart parametric equation (scalable)
def heart(t: np.ndarray, scale: float = 1.0) -> tuple:
    x = 16 * (np.sin(t) ** 3) * scale
    y = (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)) * scale
    return x, y

# Initialize the heart plot
t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart(t)
heart_line, = ax.plot(x, y, color='red', linewidth=2)
heart_fill = ax.fill(x, y, color='red', alpha=0.6)[0]

# Animation update function
def update(frame):
    # Pulsing effect: 10% size variation
    scale = 1 + 0.1 * np.sin(frame * 0.2)  
    x, y = heart(t, scale)
    
    # Update line and fill
    heart_line.set_data(x, y)
    heart_fill.remove()  # Clear old fill
    new_fill = ax.fill(x, y, color='red', alpha=0.6)
    global heart_fill
    heart_fill = new_fill[0]
    
    # Optional: Color shift (uncomment to enable)
    # r = np.clip(0.8 + 0.2 * np.sin(frame * 0.1), 0, 1)
    # heart_line.set_color((r, 0.2, 0.2))
    
    return heart_line, heart_fill

# Create animation
ani = FuncAnimation(
    fig, update, frames=200, interval=20,
    blit=True, repeat=True
)

plt.title("Beating Heart", color='white', pad=20)
plt.tight_layout()

# Uncomment to save as GIF (requires pillow)
# ani.save('heart_animation.gif', writer='pillow', fps=30, dpi=100)

plt.show()

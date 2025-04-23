# ❤️ Animated Heart Generator

A mesmerizing, mathematically-generated beating heart animation using Python and Matplotlib. Perfect for Valentine's Day, programming tutorials, or just fun visualizations!

## Features

- 🎥 **Smooth animation** with realistic pulsing effect
- 🧮 **Parametric heart equation** for perfect geometric shape
- 🎨 **Customizable** colors, pulse intensity, and animation speed
- 💾 **Exportable** as GIF for sharing
- 📦 **Single-file implementation** - no complex dependencies

## Requirements

- Python 3.6+
- Matplotlib
- NumPy
- Pillow (for GIF export)

## Installation

```bash
# Clone repository
git clone https://github.com/iyoramu/heart-art-generator.git
cd heart-art-generator

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the animation:
```bash
python animated_heart.py
```

Customize the animation by editing these parameters in `animated_heart.py`:
```python
# Change color (RGB values)
heart_line.set_color((1.0, 0.2, 0.2))  # Red

# Adjust pulse intensity (0.1 = 10% size variation)
scale = 1 + 0.1 * np.sin(frame * 0.2)

# Change animation speed (milliseconds between frames)
ani = FuncAnimation(..., interval=20)
```

## Exporting as GIF

Uncomment this line in the script:
```python
ani.save('heart_animation.gif', writer='pillow', fps=30, dpi=100)
```

## How It Works

The animation uses:
1. **Parametric heart equation** to generate perfect heart shapes
2. **Sinusoidal scaling** for natural pulsing effect
3. **Matplotlib's FuncAnimation** for smooth rendering

## License

MIT License - see [LICENSE](LICENSE) file for details

## Contributing

Feel free to:
- Report issues
- Suggest enhancements
- Submit pull requests

# Used to generate color palettes
import colorsys
import random

# Converts an hedadecimal color to RGB
def hexToRgb(hex_color: str) -> tuple[float, ...]:
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def rgbToHex(rgb_color: tuple[float, float, float]) -> str:
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb_color[0] * 255),
        int(rgb_color[1] * 255),
        int(rgb_color[2] * 255)
    )

def generateRandomHexColor() -> str:
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))

def generatePalette() -> list[str]:
    """Generate a palette of five colors using an analogous color scheme."""
    base_color: str = generateRandomHexColor()
    base_rgb: tuple[float, ...] = hexToRgb(base_color)
    base_hsv: tuple[float, float, float] = colorsys.rgb_to_hsv(*base_rgb)
    # Define angles for analogous colors
    angles: list[int] = [-30, -15, 0, 15, 30]
    palette: list[str] = []
    for angle in angles:
        hue: float = (base_hsv[0] + angle / 360) % 1.0
        analog_rgb: tuple[float, float, float] = colorsys.hsv_to_rgb(hue, base_hsv[1], base_hsv[2])
        palette.append(rgbToHex(analog_rgb))
    return palette


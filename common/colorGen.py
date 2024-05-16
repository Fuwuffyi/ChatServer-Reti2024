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

def generatePalette() -> dict[str, str]:
    # Get a random color's hls values
    base_color: str = generateRandomHexColor()
    base_rgb: tuple[float, ...] = hexToRgb(base_color)
    base_hls: tuple[float, float, float] = colorsys.rgb_to_hls(*base_rgb)
    # Define angles for analogous colors
    angles: list[int] = [-30, -15, 0, 15, 30]
    palette: list[str] = []
    for angle in angles:
        hue: float = (base_hls[0] + angle / 360) % 1.0
        # For text color
        lightness = 0.93
        saturation = 0.89
        # For background color
        if angle == -15:
            lightness = 0.04
            saturation = 0.89
        # For primary color
        elif angle == 0:
            lightness = 0.73
            saturation = 0.90
        # For secondary color
        elif angle == 15:
            lightness = 0.34
            saturation = 0.91
        # For accent color
        elif angle == 30:
            lightness = 0.57
            saturation = 0.91
        # Put those colors into rgb, then to hex
        analog_rgb: tuple[float, float, float] = colorsys.hls_to_rgb(hue, lightness, saturation)
        palette.append(rgbToHex(analog_rgb))
    # Return the dict palette 
    return {
        "text": palette[0],
        "background": palette[1],
        "primary": palette[2],
        "secondary": palette[3],
        "accent": palette[4],
    }


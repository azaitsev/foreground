from __future__ import division

__author__ = "Alexander Zaitsev (azaitsev@gmail.com)"
__copyright__ = "Copyright 2019, azaitsev@gmail.com"
__license__ = "MIT"
__version__ = "0.1.2"


def hex_to_rgb(hex_color):
    hex_color_clean = hex_color.lstrip('#').strip()
    return tuple(
        int(hex_color_clean[i:i + 2], 16) for i in range(0, 6, 2)
    )

def get_channel_value(channel):
    """Helper to calculate luminance."""
    channel = channel / 255.0
    if channel <= 0.03928:
        channel = channel / 12.92
    else:
        channel = ((channel + 0.055) / 1.055) ** 2.4
    return channel

def calculate_color_luminance(rgb_tuple):
    """Get color luminance.

    Used formula from w3c guide:
    https://www.w3.org/TR/WCAG20/#relativeluminancedef

    L = 0.2126 * R + 0.7152 * G + 0.0722 * B where R, G and B are defined as:

    if RsRGB <= 0.03928 then R = RsRGB/12.92 else R = ((RsRGB+0.055)/1.055) ^ 2.4
    if GsRGB <= 0.03928 then G = GsRGB/12.92 else G = ((GsRGB+0.055)/1.055) ^ 2.4
    if BsRGB <= 0.03928 then B = BsRGB/12.92 else B = ((BsRGB+0.055)/1.055) ^ 2.4
    """
    r, g, b = rgb_tuple
    r = get_channel_value(r)
    g = get_channel_value(g)
    b = get_channel_value(b)
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance


def get_foreground(background_color, output='hex'):
    """Get foreground font color based on w3c recommendations."""
    hex_white = '#FFFFFF'
    hex_black = '#000000'
    rgb_white = (255, 255, 255)
    rgb_black = (0, 0, 0)

    # convert to rgb if got hex
    if isinstance(background_color, str):
        background_color =  hex_to_rgb(background_color)

    luminance = calculate_color_luminance(background_color)
    if (luminance + 0.05) / (0.0 + 0.05) > (1.0 + 0.05) / (luminance + 0.05):
        return rgb_black if output.lower() == 'rgb' else hex_black
    else:
        return rgb_white if output.lower() == 'rgb' else hex_white

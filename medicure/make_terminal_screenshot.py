import sys
from PIL import Image, ImageDraw, ImageFont

def create_terminal_screenshot(text_file, output_image_path):
    with open(text_file, 'r') as f:
        lines = f.read().split('\n')

    # Basic configuration
    padding = 20
    line_height = 20
    char_width = 10
    
    # Calculate dimensions
    max_line_len = max([len(line) for line in lines] + [80])
    width = (max_line_len * char_width) + (padding * 2)
    height = (len(lines) * line_height) + (padding * 2)

    # MacOS/Linux terminal colors
    bg_color = (30, 30, 30) # Dark gray
    text_color = (200, 200, 200) # Off-white
    header_color = (50, 50, 50)
    
    # Create image
    # Add a bit of space for 'window header' if we want, or just purely terminal
    img = Image.new('RGB', (width, height), color=bg_color)
    d = ImageDraw.Draw(img)

    # Draw text (without true monospace font, we just use default, but it might not perfectly align unless we have a specific font. We'll use default since we are headless)
    y = padding
    for line in lines:
        d.text((padding, y), line, fill=text_color)
        y += line_height

    img.save(output_image_path)

if __name__ == "__main__":
    create_terminal_screenshot(sys.argv[1], sys.argv[2])

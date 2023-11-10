# this will be the IoT map for the house
from PIL import Image, ImageDraw, ImageFont

def create_display_image():
    # Create an image with white background
    image = Image.new('1', (800, 480), 255)  # E-ink display resolution
    draw = ImageDraw.Draw(image)

    # Define font and draw text
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)
    draw.text((10, 10), 'Display 3 content', font=font, fill=0)

    # Return the image object
    return image

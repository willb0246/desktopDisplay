# this will display weather and other outside the house things
# it would be nice to track if Ellen is on the move // headed home
from PIL import Image, ImageDraw, ImageFont

def create_display_image():
    # Create an image with white background
    image = Image.new('1', (800, 480), 255)  # E-ink display resolution
    draw = ImageDraw.Draw(image)

    # Define font and draw text
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)
    draw.text((10, 10), 'Display 4 content', font=font, fill=0)

    # Return the image object
    return image

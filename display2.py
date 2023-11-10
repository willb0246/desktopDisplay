# this will be house energy usage display
# https://www.home-assistant.io/docs/energy/electricity-grid/
import requests
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter import simpledialog

# Replace with your actual Home Assistant URL and the long-lived access token
HOME_ASSISTANT_URL = 'http://your-home-assistant:8123'
LONG_LIVED_ACCESS_TOKEN = 'your_long_lived_access_token'

# Function to get energy usage data from Home Assistant
def get_energy_usage_data():
    headers = {
        'Authorization': f'Bearer {LONG_LIVED_ACCESS_TOKEN}',
        'content-type': 'application/json',
    }

    # This endpoint might change depending on how you've set up energy monitoring in Home Assistant
    response = requests.get(f'{HOME_ASSISTANT_URL}/api/states/sensor.your_energy_sensor', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        # Handle error or no data found
        print("Failed to retrieve data")
        return None

# Function to display the energy usage data
def display_energy_usage(root, label):
    data = get_energy_usage_data()

    if data:
        # Assuming 'state' contains the energy usage value
        energy_usage = data['state']
        # Format the energy usage data as needed, e.g., kWh, current cost, etc.
        # Then update the display
        label.config(text=f'Energy Usage: {energy_usage} kWh')
    else:
        label.config(text='No data available.')

    # Schedule this function to be called again after some time
    # e.g., 60000 milliseconds (1 minute)
    root.after(60000, lambda: display_energy_usage(root, label))

# Set up the tkinter window
root = tk.Tk()
root.title("Home Energy Usage")

# Create a label in the window to display the energy usage
label = tk.Label(root, text="Fetching data...", font=('Arial', 20))
label.pack()

# Initially call your display function; it will schedule itself to be called periodically
display_energy_usage(root, label)

# Start the GUI loop
root.mainloop()

def create_display_image():
    # Create an image with white background
    image = Image.new('1', (800, 480), 255)  # E-ink display resolution
    draw = ImageDraw.Draw(image)

    # Define font and draw text
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)
    draw.text((10, 10), 'Display 1 content', font=font, fill=0)

    # Return the image object
    return image

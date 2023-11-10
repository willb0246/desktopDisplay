import tkinter as tk
from PIL import ImageTk
import display1, display3, display4

# Initialize the display state
display_state = 2


def update_display(display_state):
    displays = [display1.create_display_image, display4.create_display_image,
                display3.create_display_image, display4.create_display_image]

    # Get the image from the corresponding display module
    pil_image = displays[display_state]()

    # Convert to a format Tkinter can use
    tk_image = ImageTk.PhotoImage(pil_image)

    # Update the label with the new image
    display_label.config(image=tk_image)
    display_label.image = tk_image  # Keep a reference!


def on_left_arrow_pressed(event=None):
    global display_state
    display_state = (display_state - 1) % 4  # Go to previous display
    update_display(display_state)

def on_right_arrow_pressed(event=None):
    global display_state
    display_state = (display_state + 1) % 4  # Go to next display
    update_display(display_state)


# Set up the Tkinter window
root = tk.Tk()
root.title("E-Ink Display Simulator")

# Bind the arrow keys to the corresponding functions
root.bind('<Left>', on_left_arrow_pressed)
root.bind('<Right>', on_right_arrow_pressed)

# Create a label that will act as the e-ink display
display_label = tk.Label(root)
display_label.pack()

# Initially update the display
update_display(display_state)

# Start the GUI event loop
root.mainloop()
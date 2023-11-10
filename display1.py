# display1.py
# this will be 10y Treasury today, over the last X weeks, and an up or down arrow?
import tkinter as tk
import yfinance as yf
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

def last_business_day():
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    if today.weekday() >= 5:  # Saturday or Sunday
        offset = today.weekday() - 4  # Friday will be 4 days back
    else:
        offset = 1  # Otherwise, just go back one day for the previous day
    last_trading_date = today - timedelta(days=offset)
    return last_trading_date

def update_mock_display(content):
    label.config(text=content)
    # Update other GUI elements as needed to simulate the e-ink display
    # You can add images, shapes, etc., using tkinter's drawing capabilities.

def fetch_data():
    # Start by checking the last business day
    most_recent_business_day = last_business_day()

    # Define the start and end date for fetching data
    start_date = (most_recent_business_day - timedelta(days=30))
    end_date = most_recent_business_day + timedelta(days=1)
    yesterday = most_recent_business_day

    # Download data for the most recent business day
    data = yf.download("^TNX", start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))

    # Print the date range
    print(f'Fetching data from {start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}. Yesterday is {yesterday.strftime("%Y-%m-%d")}')

    if data.empty:
        # Try going back further if no data is found
        for i in range(2, 10):
            past_date = most_recent_business_day - timedelta(days=i)
            data = yf.download("^TNX", start=past_date.strftime("%Y-%m-%d"),
                               end=(past_date + timedelta(days=30)).strftime("%Y-%m-%d"))
            if not data.empty:
                break  # Break the loop if data is found

    if not data.empty and 'Close' in data.columns:
        one_day_trend_calc = ((data['Close'].iloc[-1] / data['Close'].iloc[-2]) - 1) * 100
        today = data['Close'].iloc[-1]
        yesterday = data['Close'].iloc[-2]
        print(f'the value for today is: {today} and yesterday is: {yesterday}.')# The dates are: today::{}; yesterday::{}')
        data_dict = {'current': data['Close'].iloc[-1], '1_day_trend': one_day_trend_calc, 'last_7': data[-7:-1], 'last_30': data[-30:-1]}
        return data_dict
    else:
        return None  # In case no data is available for the last 10 days

def show():
    # Fetch the yield value
    yield_value = fetch_data()

    # Create text for the display based on the fetched yield value
    if yield_value is not None:
        yield_text = f"10-Year Treasury Yield: {yield_value['current']:.2f}% || 1-day trend: {yield_value['1_day_trend']:.2f}%"
    else:
        yield_text = "10-Year Treasury Yield: No data for today."

    # Update the Tkinter label
    update_mock_display(yield_text)

    # Schedule this function to be called again after 60000 milliseconds (1 minute)
    root.after(60000, show)


# Set up the tkinter window
root = tk.Tk()
root.title("10-Year Treasury Yield")

# Create a label in the window to display the yield
label = tk.Label(root, text="Fetching data...", font=('Arial', 20))
label.pack()

# Initially call your update function; it will schedule itself to be called periodically
root.after(0, show())  # 0 ms delay for the first call

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

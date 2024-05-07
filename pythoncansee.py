import pyautogui
import pytesseract
from PIL import Image
import time

# Configure the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to perform GUI interactions and OCR
def process_line(line):
    # Click on the search bar and type the line
    pyautogui.click(1926, 383)
    time.sleep(.5)
    pyautogui.write(line)
    time.sleep(.5)
    pyautogui.press('tab')
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(.5)
    # Select and edit Hyperfind
    pyautogui.click(1991, 450)  # Select Hyperfind
    time.sleep(.5)
    pyautogui.click(1960, 346)  # Edit Hyperfind
    time.sleep(.5)
    
    # Take a screenshot of the specified area
    image = pyautogui.screenshot(region=(2045, 1100, 3145 - 2045, 1375 - 1100))
    image.save("screenshot.png")  # Save the image for verification
    
    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    
    # Write extracted text to Extracts.txt delimited by |
    
    with open("Extracts.txt", "a") as file:
        file.write(line + " | ")
        file.write(extracted_text.replace("\n", "|") + "\n")
    
    # Print extracted text delimited by tab
    print(extracted_text.replace("\n", "\t"))
    
    # Delete the screenshot
    image.close()  # Close the image file to free up system resources
    pyautogui.moveTo(1960, 346)  # Move to return button (may help avoid misclicks)
    time.sleep(.5)
    pyautogui.click()  # Click return
    time.sleep(.5)
    pyautogui.click(1926, 383)
    time.sleep(.5)
    # Press Ctrl + A to select all text
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(.5)
    # Press Delete to clear the selected text
    pyautogui.press('delete')
    time.sleep(2)  # Wait for 2 seconds

# Read lines from input.txt and process each
with open("input1.txt", "r") as file:
    for line in file:
        process_line(line.strip())


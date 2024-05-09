import pyautogui
import pytesseract
from PIL import Image
import time

# Configure the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to perform GUI interactions and OCR
def process_line(line):
    # Click on the search bar and type the line
    pyautogui.click(1072, 363)
    time.sleep(.5)
    pyautogui.write(line)
    time.sleep(.5)
    pyautogui.press('tab')
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(.5)
    # Select and edit Hyperfind
    pyautogui.click(1120, 434)  # Select Hyperfind
    time.sleep(.5)
    pyautogui.click(1193, 333)  # Edit Hyperfind
    time.sleep(.5)
    
    # Coordinates for the screenshot

    x1, y1 = 1305, 904
    x2, y2 = 1089, 916
    # Take a screenshot of the specified area

    image = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

    
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
    pyautogui.moveTo(1198, 333)  # Move to return button (may help avoid misclicks)
    time.sleep(.5)
    pyautogui.click()  # Click return
    time.sleep(.5)
    pyautogui.click(1072, 363)
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


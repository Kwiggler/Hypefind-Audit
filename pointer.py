import tkinter as tk
from tkinter import ttk, Text
import pyautogui
from pynput import mouse
import threading

class MousePositionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Position Tracker")
        
        self.recent_clicks = []
        self.max_recent_clicks = 10
        
        self.setup_ui()
        
        self.update_position_thread = threading.Thread(target=self.update_position, daemon=True)
        self.update_position_thread.start()
        
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.mouse_listener.start()

    def setup_ui(self):
        self.instructions_label = ttk.Label(self.root, text="Current Mouse Position:", font=("Arial", 12))
        self.instructions_label.pack(pady=(10, 5))
        
        self.position_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.position_label.pack(pady=(5, 10))
        
        # Display screen size
        screen_width, screen_height = pyautogui.size()
        self.screen_size_label = ttk.Label(self.root, text=f"Screen Size: {screen_width}x{screen_height}", font=("Arial", 12))
        self.screen_size_label.pack(pady=(5, 10))
        
        # Textbox for displaying recent clicks
        self.clicks_textbox = Text(self.root, height=5, width=50)
        self.clicks_textbox.pack(pady=(5, 10))
        self.clicks_textbox.configure(font=("Arial", 12))
        
        # Example of setting a background color for the Text widget
        self.clicks_textbox.configure(bg="lightgray")

    def update_position(self):
        while True:
            x, y = pyautogui.position()
            position_text = f"X: {x}, Y: {y}"
            self.position_label.config(text=position_text)
            self.root.after(100, self.root.update_idletasks)

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.recent_clicks.append((x, y))
            self.recent_clicks = self.recent_clicks[-self.max_recent_clicks:]
            
            # Clear the textbox before updating
            self.root.after(0, self.clicks_textbox.delete, 1.0, tk.END)
            
            # Insert each click as a new line with color
            for click in self.recent_clicks:
                click_text = f"{click}\n"
                self.root.after(0, self.clicks_textbox.insert, tk.END, click_text, 'click')
            
            # Set tag configuration for color (optional)
            self.clicks_textbox.tag_configure('click', foreground='blue')

def main():
    root = tk.Tk()
    app = MousePositionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

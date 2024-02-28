import pyautogui
import time
import keyboard

def clear_text_at_cursor():
    # Add a delay to give yourself time to position the mouse cursor
    print("Move your mouse cursor over the text you want to clear...")
    time.sleep(5)  # Adjust the delay time as needed
    
    # Clear text for 1 second
    start_time = time.time()
    while time.time() - start_time < 1:
        position = pyautogui.position()
        
        # Click at the specified coordinates to focus on the text
        pyautogui.click(position)
        time.sleep(0.5)  # Add a short delay to ensure the click is registered
        
        # Select all text and delete it
        pyautogui.hotkey('ctrl', 'a')  # Select all
        pyautogui.press('delete')  # Delete selected text

def input_text_from_file(file_path):
    # Read the content of the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Iterate through each character in the text
    for char in text:
        if char == '\\':
            # If "//" is detected, wait for the user to press Enter
            keyboard.wait('enter')

            # Select all text and delete it
            pyautogui.hotkey('ctrl', 'a')  # Select all
            pyautogui.press('delete')  # Delete selected text

        else:
            # Type the character directly
            pyautogui.press(char)

if __name__ == "__main__":
    # Construct the full file path
    file_path = r"<enter file path>"
    
    while True:
        clear_text_at_cursor()
        
        # Input text from the file
        input_text_from_file(file_path)
        print("Text from file inputted.")

        # Add a short delay before the next iteration
        time.sleep(2)

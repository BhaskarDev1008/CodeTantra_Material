## Automated Text Input and Clearing Script

This Python script provides automation for inputting text from a specified file into an active text editor or application, while also facilitating the clearing of text at the cursor position.

### Features:

- **Clear Text at Cursor:** The script allows users to clear text at the current cursor position by positioning the mouse cursor over the desired text and executing the script.
  
- **Automated Text Input:** Text from a specified file can be automatically inputted into the active text editor or application, character by character. The script pauses when encountering "\" characters in the input file, requiring the user to press Enter first to clear the text then again press Enter to resume inputting text.

### How to Use:

1. **Setup:**
   - Ensure Python and required dependencies (`pyautogui` and `keyboard`) are installed.
   - Clone or download the repository to your local machine.

2. **Position Cursor:**
   - Run the script and follow the prompt to position the mouse cursor over the text you want to clear. The script will wait for 5 seconds for positioning.

3. **Input Text:**
   - Specify the file path containing the text you want to input into the application. 
   - Each "\\" character in the text file indicates a pause where the user needs to press Enter before continuing.

4. **Run Script:**
   - Execute the script, and it will automate the process of clearing text at the cursor position and inputting text from the file.

5. **Adjustments:**
   - Customize the delay times (`time.sleep`) and file paths according to your requirements.

### Example Usage:

```python
python script.py
```

### Dependencies:

- Python 3.x
- `pyautogui`
- `keyboard`

### Notes:

- Ensure the application or text editor is active and in focus when running the script.
- Use with caution, as the script directly interacts with the mouse cursor and keyboard.

### Contributions:

Contributions are welcome! Feel free to open issues for bug reports or feature requests, and submit pull requests to contribute improvements or fixes.

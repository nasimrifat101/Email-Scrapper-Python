# Window Scraper

## Introduction
This repository contains two Python scripts, `a.py` and `window_scrapper.py`, which utilize the `pygetwindow` library to interact with open windows.

## Scripts

### 1. a.py
This script uses `pygetwindow` to get the titles of all open windows. It's the initial step in the workflow to identify the window title for your desired browser tab.

#### Usage
1. Ensure the `pygetwindow` library is installed: `pip install pygetwindow`.
2. Run the script to print the titles of all open windows.

### 2. window_scrapper.py
This script extracts emails from the active browser tab using PyAutoGUI, PyGetWindow, and Pyperclip. It provides a convenient way to save the extracted emails to a text file.

#### Usage
1. After running `a.py` and obtaining window titles, identify the title corresponding to your Google Sheets window.
2. Replace `'Google Sheets'` in `window_scrapper.py` with the actual window title/ browser tab title.
3. Ensure the required libraries are installed: `pip install pygetwindow pyautogui pyperclip`.
4. Test the script in a safe environment before using it on sensitive data.

## Notes
- Both scripts are designed for specific use cases, so make sure to customize them according to your needs.
- Use these scripts responsibly and be cautious when working with sensitive information.

Feel free to reach out if you have any questions or improvements!
```

`a.py` is the initial step in the workflow. Users should run it first to obtain window titles before proceeding to `window_scrapper.py`.
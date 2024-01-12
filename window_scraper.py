import time
import pygetwindow as gw
import pyautogui
import pyperclip
import re

# Function to get emails from the active browser tab
def get_emails_from_browser_tab():
    # Assuming the browser tab is active
    # You may need to adjust these coordinates based on your setup
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy
    time.sleep(1)  # Wait for clipboard to update
    content = pyperclip.paste()  # Get clipboard content using pyperclip

    # Use a regular expression to find email addresses in the content
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = re.findall(email_pattern, content)

    return emails

# Activate the browser tab where your Google Sheets document is opened



# Replace 'Google Sheets' with the title of your browser tab which you got from running a.py script.

window = gw.getWindowsWithTitle('Google Sheets')[0]
window.activate()



# Get emails from the active browser tab
emails = get_emails_from_browser_tab()

# Specify the file path where you want to save the emails
output_file_path = 'extracted_emails.txt'

# Write the emails to the file with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as file:
    for email in emails:
        file.write(email + '\n')

print(f"Emails saved to {output_file_path}")

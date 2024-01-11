import pygetwindow as gw

# Get all open windows
windows = gw.getAllTitles()

# Print the titles for identification
print("Open window titles:")
for window in windows:
    print(window)

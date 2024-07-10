# Tool-for-Thermo-calc
## This repository contains some small scripts I wrote to enhance the efficiency of Thermo-calc. As a beginner in Python, there are many aspects that need improvement. If you find any issues, please let me know directly. Your feedback is greatly appreciated.
## Current Contents

### 1. POP Converter: One-click conversion of specific column-formatted Excel (xlsx) files into POP files.
**Why create this?**
- When organizing experimental data, the primary goal is readability. Writing data directly into POP files can be inconvenient for later reference or modification in case of errors. Organizing data into Excel files (xlsx) is much more convenient for readability.
- However, once the data is organized in Excel, converting hundreds or thousands of data points into POP files becomes an issue. This script handles the conversion with one click.

**Current Features:**
- Only supports experimental data of **solidus and liquidus of binary diagrams**.
- If the specified file does not exist in the folder, it automatically creates a new xlsx file with a specific format. It is recommended to use this feature to create new Excel files.
- The file name needs to start with the element system, such as "Co-Al", followed by any additional text.
- The script can only be run from the command line as I haven't yet learned UI libraries like Tkinter or PyQt.
- After running the script, the user is prompted to input the file name and then to write the info section of the POP file (free text input). The conversion process will then execute, and upon success, it will display "success!".
  ![image](https://github.com/nicetoolman/Tool-for-Thermo-calc/blob/main/popfile%20converter/%E8%BF%90%E8%A1%8C%E7%95%8C%E9%9D%A2.png)

**Future Improvements (no guarantee):**
- Compatibility with more file formats.
- Error reporting indicating which line has an issue.
- A user-friendly UI.

### 2. No second feature yet, cuz I haven't written it. 

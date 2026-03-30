# Simple Digit Recognizer (5x5 Grid)

## Student Details
- Name: Mohit Pratap Singh 
- Registration Number: 25BAI10639
- Branch: B.Tech Computer Science & Engineering (Artificial Intelligence & Machine Learning)
- Year: First Year (2025-2029)

## About the Project
This is a simple Python program that recognizes digits drawn on a 5×5 grid. The user enters values (0s and 1s) to form a digit, and the system compares it with predefined patterns to guess which digit it is.

Currently, the program supports recognition of digits:
0, 1, and 2.

## How It Works
- The program stores templates of digits in a 5×5 format.
- The user inputs their own 5×5 grid.
- The system compares the input with each template.
- It counts how many pixels match.
- The digit with the highest matching score is selected.
- If the match is 80% or more, the digit is recognized.

## Input Instructions
- Enter 5 rows.
- Each row should contain 5 values (only 0 or 1).
- Use spaces between values.

Example Input:  
0 1 1 1 0  
1 0 0 0 1   
1 0 0 0 1  
1 0 0 0 1  
0 1 1 1 0  

## Output
- The program displays your drawn digit using:
  - for 1
  - for 0
- It then prints the recognized digit or a message if it is unsure.

## Features
- Simple and easy logic
- Uses basic Python concepts
- Takes user input interactively
- Shows matching score for each digit

## Limitations
- Only works for digits 0, 1, and 2
- Fixed grid size (5×5)
- Accuracy depends on how closely input matches templates

## Requirements
- Python 3.x

## How to Run
1. Open terminal or command prompt
2. Go to the file location
3. Run:
   python project 2 .py
4. Enter the grid values as instructed

## Future Improvements
- Add support for digits 0–9
- Improve accuracy
- Add GUI
- Allow flexible grid size

## Notes
This project is created to understand basic pattern recognition and simple comparison techniques.

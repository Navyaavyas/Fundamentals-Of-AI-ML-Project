import math

TEMPLATES = {
    '0': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    '1': [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0]
    ],
    '2': [
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]
}

GRID_SIZE = 5

def recognize_digit(input_grid):
    best_match_digit = "Unknown"
    highest_match_score = -1
    
    max_score = GRID_SIZE * GRID_SIZE

    print("\n--- Matching Score Analysis ---")
    
    for digit, template in TEMPLATES.items():
        mismatch_count = 0
        
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if input_grid[r][c] != template[r][c]:
                    mismatch_count += 1
        
        match_score = max_score - mismatch_count
        
        print(f"Template '{digit}': {match_score} / {max_score} pixels matched.")
        
        if match_score > highest_match_score:
            highest_match_score = match_score
            best_match_digit = digit
            
    print("-" * 35)
    
    if highest_match_score / max_score >= 0.8:
        return f"The system recognized this as the digit: {best_match_digit}"
    else:
        return f"Could not confidently recognize the digit. Best match was '{best_match_digit}' with {highest_match_score} matched pixels."

def get_user_input():
    print("\n--- Draw Your Digit (5x5 Grid) ---")
    print("Enter 5 rows of 5 digits (0 for blank, 1 for pixel) separated by spaces.")
    print("Example Row: 0 1 1 1 0")
    
    input_grid = []
    for i in range(GRID_SIZE):
        while True:
            try:
                row_input = input(f"Row {i+1} of {GRID_SIZE}: ").strip().split()
                if len(row_input) != GRID_SIZE:
                    print(f"Error: Must enter exactly {GRID_SIZE} values.")
                    continue
                
                row = [int(p) for p in row_input]
                if not all(p in (0, 1) for p in row):
                    print("Error: Only use 0 (off) and 1 (on).")
                    continue
                
                input_grid.append(row)
                break
            except ValueError:
                print("Error: Invalid input. Please use digits only.")
            except EOFError:
                print("\nInput cancelled.")
                return None
                
    return input_grid

def display_grid(grid):
    print("\n--- Your Drawn Digit ---")
    for row in grid:
        display_row = " ".join(["#" if p == 1 else "." for p in row])
        print(f"  {display_row}")
    print("-" * 26)


if __name__ == "__main__":
    
    while True:
        user_grid = get_user_input()
        
        if user_grid:
            display_grid(user_grid)
            result = recognize_digit(user_grid)
            print(f"\n{result}\n")
        
        again = input("Try another digit? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting Simple Digit Recognizer.")
            break
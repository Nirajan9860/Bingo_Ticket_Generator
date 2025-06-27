import random
import numpy as np


def generate_column_numbers():
    """Generate numbers for each of the 9 columns as per UK Bingo rules."""
    columns = []
    for i in range(9):
        start = i * 10 + 1
        end = start + 9 if i != 8 else 90
        columns.append(list(range(start, end + 1)))
    return columns

def generate_ticket():
    columns = generate_column_numbers()
    ticket = [[None]*9 for _ in range(3)]  # 3 rows x 9 columns

    # For each column, randomly choose 1 to 3 numbers
    col_nums = [random.sample(col, k=random.randint(1, 3)) for col in columns]

    # Ensure total numbers in the ticket is 15
    # Flatten and count how many from each column we’ve picked
    num_counts = [len(c) for c in col_nums]
    total = sum(num_counts)

    # Adjust if total != 15
    while total != 15:
        for i in range(9):
            if total > 15 and len(col_nums[i]) > 1:
                col_nums[i].pop()
                total -= 1
            elif total < 15 and len(col_nums[i]) < 3 and len(columns[i]) > len(col_nums[i]):
                extra = list(set(columns[i]) - set(col_nums[i]))
                if extra:
                    col_nums[i].append(random.choice(extra))
                    total += 1
            if total == 15:
                break

    # Now place numbers into the ticket
    filled = [0, 0, 0]  # How many numbers in each row
    for col_idx, numbers in enumerate(col_nums):
        rows = random.sample(range(3), len(numbers))
        for row, number in zip(rows, numbers):
            ticket[row][col_idx] = number
            filled[row] += 1

    # Fix rows with too few or too many numbers
    for i in range(3):
        while filled[i] < 5:
            col = random.choice([c for c in range(9) if ticket[i][c] is None and any(ticket[r][c] is not None for r in range(3))])
            for r in range(3):
                if ticket[r][col] is not None:
                    ticket[i][col] = ticket[r][col]
                    ticket[r][col] = None
                    filled[i] += 1
                    filled[r] -= 1
                    break
        while filled[i] > 5:
            col = random.choice([c for c in range(9) if ticket[i][c] is not None])
            ticket[i][col] = None
            filled[i] -= 1

    # Sort numbers in each column
    for col in range(9):
        nums = [(ticket[row][col], row) for row in range(3) if ticket[row][col] is not None]
        nums.sort()  # Sort by number (the first element of the tuple)
        for idx, (_, row) in enumerate(nums):
            ticket[row][col] = nums[idx][0]

    return ticket

def print_ticket(ticket):
    for row in ticket:
        print(" | ".join(f"{num:2}" if num is not None else "  " for num in row))




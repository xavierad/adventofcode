from typing import List


INPUT_FILE: str = 'adventofcode.com_2022_day_1_input.txt'

def get_calories_per_elf(file: str) -> List[int]:
    with open(file, 'r') as f:
        input: str = f.read()
    
    calories_per_elf: List[int] = []
    total_calories: int = 0
    for calorie in input.split('\n'):
        if calorie:
            total_calories += int(calorie)
        else:
            calories_per_elf.append(total_calories)
            total_calories = 0

    return calories_per_elf
    
if __name__ == '__main__':
    calories_per_elf: List[int] = get_calories_per_elf(INPUT_FILE)
    print('The highest amount of calories carried:', max(calories_per_elf))

    print('The three highest amount of calories carried:', sum(sorted(calories_per_elf, reverse=True)[:3]))
from enum import Enum
from typing import Dict


INPUT_FILE: str = 'adventofcode.com_2022_day_2_input.txt'



class Shape(Enum):
    # score, defeats
    rock = 1, 'scissors'
    paper = 2, 'rock'
    scissors = 3, 'paper'

    def __new__(cls, score: int, defeats: str):
        obj = object.__new__(cls)
        obj.score = score
        obj.defeats = defeats
        return obj          

    def __gt__(self, opponent):
        return opponent.name == self.defeats


# rock, paper, scissors.
opponent_dict: Dict[str, int] = {'A': Shape.rock, 'B': Shape.paper, 'C': Shape.scissors}
own_dict: Dict[str, int] = {'X': Shape.rock, 'Y': Shape.paper, 'Z': Shape.scissors}


def compute_own_score(file: str) -> int:
    with open(file, 'r') as f:
        input: str = f.readlines()
    
    total_score: int = 0
    for move in input:
        opp, own = move.split()

        total_score += own_dict[own].score 
        if opponent_dict[opp] == own_dict[own]:
            total_score += 3
        elif opponent_dict[opp] < own_dict[own]:
            total_score += 6

    return total_score


if __name__ == '__main__':
    score: int = compute_own_score(INPUT_FILE)

    print('Score:', score)
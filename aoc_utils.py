from pathlib import Path
from typing import List


def get_paths():
    PATHS = {}
    PATHS['puzzle_input'] = Path('puzzle_inputs/')
    assert all(path.exists() for path in PATHS.values())
    return PATHS

def get_inputs(stub:str)-> List[str]:
    PATHS = get_paths()
    file_path = list(PATHS['puzzle_input'].glob(stub))[0]
    with open(file_path, 'r') as file:
        lines = [line.strip()
                 for line in file
                ]
    return lines
    
import sys
import hashlib
from copy import deepcopy

def output(a):
    sys.stdout.write(str(a))

N = 16
S = int(N**(0.5))

def print_field(field):
    if not field:
        output("No solution")
        return
    for i in range(N):
        for j in range(N):
            cell = field[i][j]
            if cell == -1 or isinstance(cell, set):
                output('.')
            else:
                output(format(cell, 'x'))
            if (j + 1) % S == 0 and j < N-1:
                output(' |')

            if j != N-1:
                output(' ')
        output('\n')
        if (i + 1) % S == 0 and i < N-1:
            output("- - - - + - - - - + - - - - + - - - - \n")


def done(state):
    """ Are we done? """

    for row in state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True


def propagate_step(state):
    """ Propagate one step """

    new_units = False

    for i in range(N):
        row = state[i]
        values = set([x for x in row if not isinstance(x, set)])
        for j in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    state[i][j] = state[i][j].pop()
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    for j in range(N):
        column = [state[x][j] for x in range(N)]
        values = set([x for x in column if not isinstance(x, set)])
        for i in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    state[i][j] = state[i][j].pop()
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    for x in range(S):
        for y in range(S):
            values = set()
            for i in range(S*x, S*x+S):
                for j in range(S*y, S*y+S):
                    cell = state[i][j]
                    if not isinstance(cell, set):
                        values.add(cell)
            for i in range(S*x, S*x+S):
                for j in range(S*y, S*y+S):
                    if isinstance(state[i][j], set):
                        state[i][j] -= values
                        if len(state[i][j]) == 1:
                            state[i][j] = state[i][j].pop()
                            new_units = True
                        elif len(state[i][j]) == 0:
                            return False, None

    return True, new_units

def propagate(state):
    """ Propagate until we reach a fixpoint """
    while True:
        solvable, new_unit = propagate_step(state)
        if not solvable:
            return False
        if not new_unit:
            return True


def solve(state):
    """ Solve sudoku """

    solvable = propagate(state)

    if not solvable:
        return None

    if done(state):
        return state

    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if isinstance(cell, set):
                for value in cell:
                    new_state = deepcopy(state)
                    new_state[i][j] = value
                    solved = solve(new_state)
                    if solved is not None:
                        return solved
                return None


field = [
    '3f---689524---ab',
    'b-c6-5-49-d-e3-2',
    '2de-0------7-94c',
    '--4--a----f--0--',

    '----3--86--d----',
    '--d--e56ac7--f--',
    '6--c--27fb--8--1',
    '-23-4-f--9-1-dc-',

    '-b5-9-6--3-e-10-',
    '8--e--b37a--c--5',
    '--9--7e1c65--b--',
    '----5--04--9----',

    '--6--c----9--8--',
    '0cf-2------3-e67',
    '9-12-f-5e-c-3a-d',
    'da---37ebf2---50',
]

# Parse field strings
parsed_field = []
for x, row in enumerate(field):
    parsed_row = []
    for y, char in enumerate(row):
        if char == '-':
            parsed_row.append(set(range(N)))
        else:
            parsed_row.append(int(char, 16))
    parsed_field.append(parsed_row)

solved = solve(parsed_field)
print_field(solved)





output_string = ''
for row in solved:
    for num in row:
        output_string += format(num, 'x')

print(output_string)

hash_object = hashlib.sha256(output_string.upper().encode('UTF-8'))
hex_dig = hash_object.hexdigest()
print('{FLG:' + hex_dig + '}')

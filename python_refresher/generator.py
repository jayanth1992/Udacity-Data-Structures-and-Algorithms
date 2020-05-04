def all_even():
    n = 0
    while True:
        yield n
        n += 2


my_gen = all_even()

# for i in range(5):
#     print(next(my_gen))
#
# a = 3
# b = 4
#
# print(f" Sum : {a + b}")
#
# for i in range(100):
#     print(next(my_gen))

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


# Define a function check_sudoku() here:


def check_sudoku(board):
    n = len(board)

    for row in board:

        elements = get_set(n)

        for i in row:

            if not elements.__contains__(i):
                return False

            elements.remove(i)

    for i in range(len(board)):

        elements = get_set(n)

        for j in board:
            if not elements.__contains__(j[i]):
                return False
            elements.remove(j[i])

    return True


def get_set(n):
    s = set()
    for i in range(n):
        s.add(i + 1)
    return s


print(check_sudoku(incorrect))
# >>> False

# print(check_sudoku(correct))
# >>> True

# print(check_sudoku(incorrect2))
# >>> False

# print(check_sudoku(incorrect3))
# >>> False

# print(check_sudoku(incorrect4))
# >>> False

# print(check_sudoku(incorrect5))
# >>> False

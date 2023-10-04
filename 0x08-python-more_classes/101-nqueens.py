#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """


import sys


class NQueen:
    """ Class for solving the N-Queens problem """
    def __init__(self, n):
        """ Initialize the NQueen object """
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.solutions = []

    def can_place_queen(self, k, i):
        """ Check if a queen can be placed in the (k, i) position """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def solve(self, k):
        """ Recursive method to solve the N-Queens problem """
        for i in range(1, self.n + 1):
            if self.can_place_queen(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = [(r - 1, c - 1) for r, c in enumerate(self.x[1:], start=1)]
                    self.solutions.append(solution)
                else:
                    self.solve(k + 1)

    def find_solutions(self):
        """ Find all solutions to the N-Queens problem """
        self.solve(1)
        return self.solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    queen = NQueen(N)
    res = queen.find_solutions()
    for solution in res:
        print(solution)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
from typing import Callable

MAX_CANDIDATES = 100


def backtrack(construct_candidates: Callable, is_a_solution: Callable, max_soln_sz):
    """
    A backtracking engine - useful for searching a space of solutions in an efficient way.
      Based heavily from this excellent tutorial:
      https://cs.lmu.edu/~ray/notes/backtracking/
    Generalized slightly with inspiration from Skiena's Algorithm Design Manual
    :param construct_candidates:
    :param is_a_solution:
    :param max_soln_sz:
    :return:
    """
    max_soln_sz = min(max_soln_sz, MAX_CANDIDATES)
    solution = [None] * max_soln_sz

    def find_next(ii):
        candidates = construct_candidates(solution_vector=solution, valid_idx=ii)
        for c in candidates:
            solution[ii] = c
            if is_a_solution(solution_vector=solution, valid_idx=ii):
                if ii >= max_soln_sz-1 or find_next(ii + 1):
                    return solution
        return None

    return find_next(0)

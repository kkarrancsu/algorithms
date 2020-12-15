#!/usr/bin/env python
from typing import Callable

# maximum possible size of a solution.
MAX_CANDIDATES = 100


def backtrack(construct_candidates: Callable, is_a_solution: Callable, max_soln_sz):
    """
    A backtracking engine - useful for searching a space of solutions in an efficient way.
      Based heavily on this excellent tutorial:
      https://cs.lmu.edu/~ray/notes/backtracking/
    Generalized slightly with inspiration from Skiena's Algorithm Design Manual
    :param construct_candidates: a callable function which takes 2 keyword arguments as follows:
        construct_candidates(solution_vector=solution, valid_idx=ii):
            solution_vector: a 1-D list/numpy-array of the solution
            valid_idx: the index upto which the solution is valid
        This function constructs the next possible set of candidates, given the current
        partial solution
    :param is_a_solution: a callable function which takes 2 keyword arguments as follows:
        is_a_solution(solution_vector=solution, valid_idx=ii)
            solution_vector: a 1-D list/numpy-array of the solution
            valid_idx: the index upto which the solution is valid
        This function returns a boolean of whether the solution upto the valid_idx is a
        partial or full solution
    :param max_soln_sz: the maximum size of an acceptable solution
    :return: a found solution
    """
    max_soln_sz = min(max_soln_sz, MAX_CANDIDATES)
    solution = [None] * max_soln_sz

    def find_next(ii):
        """
        Finds a compatible solution in the solution vector for index ii
        :param ii: the index for which to find a solution
        """
        candidates = construct_candidates(solution_vector=solution, valid_idx=ii)
        for c in candidates:
            solution[ii] = c
            # if this candidate is a valid solution, then ...
            if is_a_solution(solution_vector=solution, valid_idx=ii):
                # Here, we return solution if the solution has reached the maximum allowable
                # size.  Otherwise, we look for a solution in the next index, and find_next(ii+1)
                # evaluates to True if something other than None is returned.  But since that is a
                # recursive call, we effectively build up our solution, if a valid solution
                # exists, until we reach the maximum solution size.  Otherwise, we return None (L48)
                if ii >= max_soln_sz-1 or find_next(ii + 1):
                    return solution
        return None

    final_solution = find_next(0)
    # remove None from the solution, so that we can allow for shorter than max-solution-size
    #  solutions
    final_solution = [x for x in final_solution if x is not None]
    return final_solution

#!/usr/bin/env python
from typing import Callable, Union
import math
import copy

# maximum possible size of a solution.
MAX_CANDIDATES = 100


def goodness_min(cur_best, new_metric):
    """
    Determins if the new_metric is less than the current best, and if so,
    returns True.  Otherwise, returns False
    :param cur_best: the current best metric
    :param new_metric: the metric of the new solution
    """
    if new_metric < cur_best:
        return True
    else:
        return False


def goodness_max(cur_best, new_metric):
    """
    Determins if the new_metric is greater than the current best, and if so,
    returns True.  Otherwise, returns False
    :param cur_best: the current best metric
    :param new_metric: the metric of the new solution
    """
    if new_metric > cur_best:
        return True
    else:
        return False


def backtrack_bnb(construct_candidates: Callable,
                  is_a_partial_solution: Callable,
                  is_a_full_solution: Callable,
                  goodness_fn: Callable,
                  max_soln_sz,
                  max_solutions: int = 100,
                  goodness_fn_comparator: Union[Callable, str] = goodness_min,
                  best_metric_start=math.inf):
    """
    A backtracking engine with branch-and-bound - useful for searching a space of solutions
    in an efficient way, and eliminating solutions based on a goodness metric.
    Based heavily on this excellent tutorial:
      https://cs.lmu.edu/~ray/notes/backtracking/
    :param construct_candidates: a callable function which takes 2 keyword arguments as follows:
        construct_candidates(solution_vector=solution, valid_idx=ii):
            solution_vector: a 1-D list/numpy-array of the solution
            valid_idx: the index upto which the solution is valid
        This function constructs the next possible set of candidates, given the current
        partial solution
    :param is_a_partial_solution: a callable function which takes 2 keyword arguments as follows:
        is_a_partial_solution(solution_vector=solution, valid_idx=ii)
            solution_vector: a 1-D list/numpy-array of the solution
            valid_idx: the index upto which the solution is valid
        This function returns a boolean of whether the solution upto the valid_idx is a
        partial solution
    :param is_a_full_solution: a callable function which takes 2 keyword arguments as follows:
        is_a_full_solution(solution_vector=solution, valid_idx=ii)
            solution_vector: a 1-D list/numpy-array of the solution
            valid_idx: the index upto which the solution is valid
        This function returns a boolean of whether the solution upto the valid_idx is a
        full solution
    :param goodness_fn: a callable function which takes 2 keyword arguments as follows:
        goodness_fn(solution_vector=solution, valid_idx=ii)
            solution_vector: a 1-D list/numpy-array of the solution
            valid_idx: the index upto which the solution is valid
        This function computes a metric on how "good" the solution is.
    :param max_soln_sz: The maximum size of a solution
    :param max_solutions: The maximum number of solutions to search before declaring
        the current best as optimal
    :param goodness_fn_comparator: A callable which takes 2 inputs as follows:
        goodness_fn_comparator(cur_best, new_metric)
            cur_best - the value of the current best solution, according to a metric returned by goodness_fn
            new_metric - the value of the goodness_fn on the current solution being evaluated
        Returns True if new_metric is *strictly* better than cur_best, otherwise False.  This is used
            to determine if we continue down a certain branch, or move to the next branch
        This can also be a string 'min' or 'max', if it is desired to either minimize or maximize
        the goodness metric
    :param best_metric_start: the initial value of the best metric. Automatically set if
        goodness_fn_comparator is either 'min' or 'max'.  Otherwise, this value will influence
        which solution is selected as the best
    :return: the best solution amongst the searched solutions, with best being measured by
        goodness_fn
    """
    max_soln_sz = min(max_soln_sz, MAX_CANDIDATES)
    solution = [None] * max_soln_sz

    # setup the comparison functions, and the current best metric to start the search
    if isinstance(goodness_fn_comparator, str):
        if goodness_fn_comparator == 'min':
            goodness_fn_comparator = goodness_min
            best_metric = math.inf
        elif goodness_fn_comparator == 'max':
            goodness_fn_comparator = goodness_max
            best_metric = -math.inf
        else:
            raise ValueError("Unrecognized goodness_fn_comparator")
    else:
        best_metric = best_metric_start

    best_soln = []
    num_soln_found = 0

    def find_next(ii):
        """
        Finds a compatible solution in the solution vector for index ii
        :param ii: the index for which to find a solution
        """
        nonlocal best_soln
        nonlocal best_metric
        nonlocal num_soln_found

        candidates = construct_candidates(solution_vector=solution, valid_idx=ii)
        for c in candidates:
            solution[ii] = c
            cur_soln_goodness = goodness_fn(solution_vector=solution, valid_idx=ii)
            # determine if the currently proposed solution has a goodness metric "better" than
            # the current, otherwise move onto the next candidate
            continue_search = goodness_fn_comparator(best_metric, cur_soln_goodness)
            if is_a_partial_solution(solution_vector=solution, valid_idx=ii) and continue_search:
                # if the current candidate is a partial solution, then ...
                if (is_a_full_solution(solution_vector=solution, valid_idx=ii)) or \
                   (ii >= max_soln_sz - 1) or \
                   (find_next(ii + 1)):
                    # if the current solution is a full solution, or if we have reached the maximum
                    # solution size, update our notion of the best solution w/ the goodness_fn provided.
                    # Alternatively, we recursively call to see if we can add onto the solution first
                    cur_soln_goodness = goodness_fn(solution_vector=solution, valid_idx=ii)
                    is_best_soln = goodness_fn_comparator(best_metric, cur_soln_goodness)
                    if is_best_soln:
                        best_soln = copy.copy(solution[0:ii+1])
                        best_metric = cur_soln_goodness

                    num_soln_found += 1
                    if num_soln_found < max_solutions:
                        # move back one level in the tree and continue the search
                        find_next(ii)
                    else:
                        break

        return None

    find_next(0)

    return best_soln

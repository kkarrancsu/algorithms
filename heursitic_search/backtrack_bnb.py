#!/usr/bin/env python
from typing import Callable, Union
import math
import copy

MAX_CANDIDATES = 100


def goodness_min(cur_best, new_metric):
    if new_metric < cur_best:
        return True
    else:
        return False


def goodness_max(cur_best, new_metric):
    if new_metric > cur_best:
        return True
    else:
        return False


def backtrack_bnb(construct_candidates: Callable,
                  is_a_solution: Callable,
                  goodness_fn: Callable,
                  max_soln_sz,
                  max_solutions: int = 100,
                  goodness_fn_comparator: Union[Callable, str] = goodness_min):
    max_soln_sz = min(max_soln_sz, MAX_CANDIDATES)
    solution = [None] * max_soln_sz

    if isinstance(goodness_fn_comparator, str):
        if goodness_fn_comparator == 'min':
            goodness_fn_comparator = goodness_min
        elif goodness_fn_comparator == 'max':
            goodness_fn_comparator = goodness_max
        else:
            raise ValueError("Unrecognized goodness_fn_comparator")

    best_soln = []
    best_metric = math.inf
    num_soln_found = 0

    def find_next(ii):
        nonlocal best_soln
        nonlocal best_metric
        nonlocal num_soln_found

        candidates = construct_candidates(solution_vector=solution, valid_idx=ii)
        # print('candidates', candidates)
        for c in candidates:
            solution[ii] = c
            cur_soln_goodness = goodness_fn(solution_vector=solution, valid_idx=ii)
            continue_search = goodness_fn_comparator(best_metric, cur_soln_goodness)
            print(best_soln, best_metric, ":", solution[0:ii+1], cur_soln_goodness, continue_search)
            if is_a_solution(solution_vector=solution, valid_idx=ii) and continue_search:
                if ii >= max_soln_sz - 1 or find_next(ii + 1):
                    cur_soln_goodness = goodness_fn(solution_vector=solution, valid_idx=ii)
                    is_best_soln = goodness_fn_comparator(best_metric, cur_soln_goodness)
                    print(ii, solution, best_metric, cur_soln_goodness, is_best_soln)
                    if is_best_soln:
                        best_soln = copy.copy(solution)
                        best_metric = cur_soln_goodness
                        print(">> best_soln", best_soln, "best_metric", best_metric)

                    num_soln_found += 1
                    if num_soln_found < max_solutions:
                        # move back one level in the tree and continue the search
                        find_next(ii)
                    else:
                        break

        return None

    find_next(0)

    return best_soln

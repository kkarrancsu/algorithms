#!/usr/bin/env python

import backtrack


def solve_coinchange_backtrack(change_needed, coins):
    max_soln_sz = 10

    def construct_change_candidates(solution_vector=None, valid_idx=0):
        # assume that we have an infinite amount of coins of each kind,
        # so our candidates here are the entire set of coins
        return coins

    def is_a_coinchange_solution(solution_vector=None, valid_idx=0):
        current_soln = solution_vector[0:valid_idx + 1]
        current_change_made = sum(current_soln)
        remainder = change_needed - current_change_made
        if len(current_soln) < max_soln_sz:
            # check if a partial solution is valid.  Here, we haven't filled in
            # all the slots, so any time we have a remainder of >= 0, we are still
            # valid
            if remainder >= 0:
                return True
            else:
                return False
        else:
            # this is a full solution b/c all the slots are filled.  Here, a solution
            # is only valid if it sums to 0
            if remainder == 0:
                return True
            else:
                return False

    a_soln = backtrack.backtrack(construct_change_candidates, is_a_coinchange_solution, max_soln_sz)
    print(a_soln)


def setup_sample_problem():
    change_needed = 28
    coins = [1, 5, 10]
    return change_needed, coins


if __name__ == '__main__':
    change_needed, coins = setup_sample_problem()
    solve_coinchange_backtrack(change_needed, coins)
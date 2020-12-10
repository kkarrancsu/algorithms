#!/usr/bin/env python

import numpy as np
import backtrack

"""
Solves a Traveling Salesman problem (TSP) using heursitic_search,
where the graph is represented as an adjacency matrix.

Note that b/c we are using backtracking to solve the TSP problem,
it will *not* be an optimal solution, just a solution which satisfies
the constraints.  To find the optimal solution, refer to
the tsp_bnb.py which uses backtracking with branch & bound to solve the
TSP problem.
"""


def solve_tsp_backtrack(tsp_problem):
    soln_sz = len(tsp_problem) + 1  # make it a roundtrip

    # TODO: should we prune from the candidates constructed ones that would be invalid?
    #  the consequences of that are (as it seems to me):
    #   1 - is_a_tsp_solution() is effectively outdated.  we can simply return True every time
    #   2 - this also means that the order in which candidate_solutions are returned will
    #       matter
    def construct_tsp_candidates(solution_vector=None, valid_idx=0):
        # a valid candidate is the next valid move we can take, from our current
        # location.
        current_city = solution_vector[valid_idx]
        if (valid_idx == 0 and current_city is None) or (valid_idx == soln_sz - 1):
            return [0]  # start & end on the same city-A

        valid_next_cities = []
        for ii in range(len(tsp_problem)):  # len(tsp_problem) gets us the # of cities
            if ii not in solution_vector[0:valid_idx]:
                valid_next_cities.append(ii)

        return valid_next_cities

    def is_a_tsp_solution(solution_vector=None, valid_idx=0):
        # in the context of TSP, a solution is one in which we don't visit
        # the same city twice.  Hence, in our solution vector, we simply
        # see if all the elements are unique.  If so, this means that it we
        # have not revisited and thus, we have a partial solution
        if valid_idx < soln_sz - 1:
            solution_vector_valid = solution_vector[0:valid_idx + 1]
            solution_set = set(solution_vector_valid)  # casting as a set removes redundant elements
            # easy to understand this code, but probably
            # inefficient

            if len(solution_vector_valid) == len(solution_set):
                return True
            else:
                return False
        else:
            # here, we only deem it a solution if the path is complete
            # meaning that we started at 0 and ended at 0.
            # we don't need to check the middle againk b/c that should have
            # been taken care of with the if block above
            if solution_vector[0] == 0 and solution_vector[-1] == 0:
                return True
            else:
                return False

    a_soln = backtrack.backtrack(construct_tsp_candidates, is_a_tsp_solution, soln_sz)
    print(a_soln)


def setup_sample_tsp_problem():
    tsp_problem = np.empty((6, 6))
    tsp_problem[0, 0] = 0  # A --> A
    tsp_problem[0, 1] = 11  # A --> B
    tsp_problem[0, 2] = 13  # A --> C
    tsp_problem[0, 3] = 33  # A --> D
    tsp_problem[0, 4] = 5   # A --> E
    tsp_problem[0, 5] = 17  # A --> F

    tsp_problem[1, 0] = 11  # B --> A
    tsp_problem[1, 1] = 0  # B --> B
    tsp_problem[1, 2] = 9  # B --> C
    tsp_problem[1, 3] = 8  # B --> D
    tsp_problem[1, 4] = 7  # B --> E
    tsp_problem[1, 5] = 21  # B --> F

    tsp_problem[2, 0] = 13 # C --> A
    tsp_problem[2, 1] = 9  # C --> B
    tsp_problem[2, 2] = 0  # C --> C
    tsp_problem[2, 3] = 3  # C --> D
    tsp_problem[2, 4] = 9  # C --> E
    tsp_problem[2, 5] = 8  # C --> F

    tsp_problem[3, 0] = 33  # D --> A
    tsp_problem[3, 1] = 8  # D --> B
    tsp_problem[3, 2] = 3  # D --> C
    tsp_problem[3, 3] = 0  # D --> D
    tsp_problem[3, 4] = 19  # D --> E
    tsp_problem[3, 5] = 29  # D --> F

    tsp_problem[4, 0] = 5  # E --> A
    tsp_problem[4, 1] = 7  # E --> B
    tsp_problem[4, 2] = 9  # E --> C
    tsp_problem[4, 3] = 19  # E --> D
    tsp_problem[4, 4] = 0  # E --> E
    tsp_problem[4, 5] = 16  # E --> F

    tsp_problem[5, 0] = 17  # F --> A
    tsp_problem[5, 1] = 21  # F --> B
    tsp_problem[5, 2] = 8  # F --> C
    tsp_problem[5, 3] = 29  # F --> D
    tsp_problem[5, 4] = 16  # F --> E
    tsp_problem[5, 5] = 0  # F --> F

    return tsp_problem


if __name__ == '__main__':
    # define a sample graph that needs to be traversed
    tsp_problem = setup_sample_tsp_problem()
    solve_tsp_backtrack(tsp_problem)

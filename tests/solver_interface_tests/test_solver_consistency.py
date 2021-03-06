from src.ppopt.solver_interface.gurobi_solver_interface import *
from src.ppopt.solver_interface.cvxopt_interface import *
from src.ppopt.solver_interface.quad_prog_interface import *
import random

import numpy


def test_lp_consistency():
    # test 100 random LPs
    num_lp = 100

    for i in range(num_lp):

        dim = numpy.random.randint(3, 20)
        num_constraints = 3 * dim

        A = numpy.random.random((num_constraints, dim))
        b = numpy.random.random((num_constraints, 1))
        c = numpy.random.random((dim))
        num_equals = numpy.random.randint(0, dim // 2)
        equality_constraints = random.sample(range(num_constraints), num_equals)

        glpk_sol = solve_lp_cvxopt(c, A, b, equality_constraints)
        gurobi_sol = solve_lp_gurobi(c, A, b, equality_constraints)

        if glpk_sol != gurobi_sol:
            print(glpk_sol)
            print(gurobi_sol)
            assert False


def test_qp_consistancy():

    num_qp = 100

    for i in range(num_qp):
        dim = numpy.random.randint(3, 20)
        num_constraints = 3 * dim

        A = numpy.random.random((num_constraints, dim))
        b = numpy.random.random((num_constraints, 1))
        c = numpy.random.random((dim))
        Q = numpy.random.random((dim, dim))
        Q = Q.T @ Q
        num_equals = numpy.random.randint(0, dim // 2)
        # equality_constraints = random.sample(range(num_constraints), num_equals)
        equality_constraints = []
        quadprog_sol = solve_qp_quadprog(Q, c, A, b, equality_constraints)
        gurobi_sol = solve_qp_gurobi(Q, c, A, b, equality_constraints)

        if quadprog_sol != gurobi_sol:
            # print(A)
            # print(b)
            # print(c)
            # print(Q)
            print(equality_constraints)
            print(quadprog_sol)
            print(gurobi_sol)
            assert False

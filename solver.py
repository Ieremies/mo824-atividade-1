import gurobipy as gp
from gurobipy import GRB

model = gp.Model('Atividade 1')

# Variables declaration
x = [ [ [ model.addVar(0.0, GBR.INFINITY, 0.0, GRB.INT, f"x[{i}][{j}][{k}])")
            for i in range(L) ]
        for j in range(F) ]
        for k in range(P) ]
y = [ [ [ model.addVar(0.0, GBR.INFINITY, 0.0, GRB.INT, f"x[{i}][{j}][{k}])")
            for i in range(J) ]
        for j in range(F) ]
        for k in range(P) ]
model.update()

# Objective function
expr = GRBLinExpr()
for p in range(P):
    for f in range(F):
        # x_{p,f,l} terms
        for l in range(L):
            expr.addTerm(C_p[p][f][l], x[p][f][l])
        # y_{p,f,j} terms
        for j in range(J):
            expr.addTerm(C_t[p][f][j], x[p][f][j])
model.setObjective(expr, GRB.MAXIMIZE)

# Restrictions
## TODO Demmand constrains
## TODO Produced equals transported constrains
## TODO Material availability constrains
## TODO Capacity constrains

model.optimize()

# TODO Print result

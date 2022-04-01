from random import randint as rand

class Gerador ( object ):

    def gen (self, J):
        # J is the number of client
        F = rand ( J, 2*J ) # number of factories
        L = rand ( 5, 10 ) # number of machines in each factory
        M = rand ( 5, 10 ) # number of feedsotcks
        P = rand ( 5, 10 ) # number of products
        D =   [ [  rand( 10, 20 ) for p in range(P) ] for j in range(J) ] # demmand matrix
        r = [ [ [  rand(  1, 5 )  for l in range(L) ] for m in range(P) ] for p in range(M) ] # amount used to produce each product
        R =   [ [  rand(800,1000) for f in range(F) ] for m in range(M) ] # amount of feedstock avilable in each factory
        C =   [ [  rand( 80,100)  for f in range(F) ] for l in range(L) ] # capacity of production of each machine
        C_p = [ [ [ rand(10,100)  for f in range(F) ] for l in range(L) ] for p in range(P) ] # cost of production
        C_t = [ [ [ rand(10,20 )  for j in range(J) ] for f in range(F) ] for p in range(P) ] # cost of transport

        return (J, F, L, M, P, D, r, R, C, C_p, C_t)

from random import randint as rand

class Gerador ( object ):

    def gen (self, J):
        F = rand ( J, 2*J )
        L = rand ( 5, 10 )
        M = rand ( 5, 10 )
        P = rand ( 5, 10 )
        D =   [ [ rand(10,20 ) for i in range(P) ] for i in range(J) ]
        r = [ [ [ rand( 1, 5 ) for i in range(L) ] for i in range(P) ] for i in range(M) ]
        R =   [ [ rand(80,100) for i in range(F) ] for i in range(M) ]
        C =   [ [ rand(80,100) for i in range(F) ] for i in range(L) ]
        C_p = [ [ [ rand(10,100) for i in range(F) ] for i in range(L) ] for i in range(P) ]
        C_t = [ [ [ rand(10,20 ) for i in range(J) ] for i in range(F) ] for i in range(P) ]

        return (J, F, L, M, P, D, r, R, C, C_p, C_t)

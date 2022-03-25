from random import randint as rand

class Gerador ( object ):

    def gen (self, j):
        f = rand ( j, 2*j )
        l = rand ( 5, 10 )
        m = rand ( 5, 10 )
        p = rand ( 5, 10 )
        d =   [ [ rand(10,20 ) for i in range(p) ] for i in range(j) ]
        r = [ [ [ rand( 1, 5 ) for i in range(l) ] for i in range(p) ] for i in range(m) ]
        R =   [ [ rand(80,100) for i in range(f) ] for i in range(m) ]
        C =   [ [ rand(80,100) for i in range(f) ] for i in range(l) ]
        P = [ [ [ rand(10,100) for i in range(f) ] for i in range(l) ] for i in range(p) ]
        t = [ [ [ rand(10,20 ) for i in range(j) ] for i in range(f) ] for i in range(p) ]

        return (j, f, l, m, p, d, r, R, C, P, t)

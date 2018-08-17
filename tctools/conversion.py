# -*- coding: utf-8 -*-

import numpy as np
from periodictable import elements
from scipy.linalg import solve


class System(object):
    def __init__(self, majorelement, x={}, w={}):
        self.x = x
        self.w = w

        self.major = majorelement
        self.M = None

        try:
            self.Mi = {self.major: elements.symbol(self.major).mass}
            self.Mi.update({el: elements.symbol(el).mass for el in x.keys()})
            self.Mi.update({el: elements.symbol(el).mass for el in w.keys()})
        except:
            raise

    def solve(self):
        if set(self.x.keys()) != set(self.w.keys()):
            A = np.ndarray((2, 2))
            B = np.ndarray(2)

            A[0, 0] = sum([w/self.Mi[el] for el, w in self.w.items()])
            A[0, 1] = 1.
            A[1, 0] = sum([w for el, w in self.w.items()]) - 1.
            A[1, 1] = self.Mi[self.major]

            B[0] = 1. - sum([x for el, x in self.x.items()])
            B[1] = -sum([x*self.Mi[el] for el, x in self.x.items()])

            try:
                X = solve(A, B)
            except:
                print('Cannot solve system')
                raise
            else:
                self.M = X[0]
                self.x[self.major] = X[1]
                
                x = {el: w*self.M/self.Mi[el] for el, w in self.w.items()}
                w = {el: x*self.Mi[el]/self.M for el, x in self.x.items()}

                self.x.update(x)
                self.w.update(w)


if __name__ == '__main__':
    x = dict(Mn=1e-1, Si=1e-1)
    w = dict(C=.5e-2, Cr=1e-1)
    
    print(x)
    print(w)
    
    alloy = System('Fe', x, w)
    alloy.solve()
    
    print(alloy.x)
    print(alloy.w)

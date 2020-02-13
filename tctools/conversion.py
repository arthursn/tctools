# -*- coding: utf-8 -*-

import numpy as np
from periodictable import elements
from scipy.linalg import solve


class System(object):
    def __init__(self, majorelement, x=None, w=None):
        if x is None:
            self.x = dict()
        else:
            self.x = x

        if w is None:
            self.w = dict()
        else:
            self.w = w

        self.major = majorelement  # element that's accounted by balance
        self.M = None  # average molar mass of the alloy

        # If major element passed in either x or w, then remove from respective dictionaries
        if self.major in self.x:
            print('Major element composition should not be provided and will be ignored.')
            self.x.pop(self.major)

        if self.major in self.w:
            print('Major element composition should not be provided and will be ignored.')
            self.w.pop(self.major)

        # Load molar masses of alloy elements
        try:
            self.Mi = {self.major: elements.symbol(self.major).mass}
            self.Mi.update({el: elements.symbol(el).mass for el in self.x.keys()})
            self.Mi.update({el: elements.symbol(el).mass for el in self.w.keys()})
        except:
            raise

    def solve_numerically(self):
        """
        Numerically solve system of equations for converting between mass
        and atomic composition bases.
        """
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

    def solve(self):
        """
        Solve system of equations for converting between mass and atomic
        composition bases.
        """
        if set(self.x.keys()) != set(self.w.keys()):
            num = self.Mi[self.major] - sum([(self.Mi[self.major] - self.Mi[el])*x for el, x in self.x.items()])
            den = 1 + sum([(self.Mi[self.major]/self.Mi[el] - 1.)*w for el, w in self.w.items()])
            self.M = num/den
            self.x[self.major] = 1. - sum([x for el, x in self.x.items()]) - \
                sum([w/self.Mi[el] for el, w in self.w.items()])*self.M

            x = {el: w*self.M/self.Mi[el] for el, w in self.w.items()}
            w = {el: x*self.Mi[el]/self.M for el, x in self.x.items()}

            self.x.update(x)
            self.w.update(w)


if __name__ == '__main__':
    x = dict(Mn=1e-1, Si=1e-1)
    w = dict(C=.5e-2, Cr=1e-1, Fe=.8)

    print('Input parameters:')
    print('at. fraction:', x)
    print('wt. fraction:', w, '\n')

    alloy = System('Fe', x, w)

    alloy.solve_numerically()
    print('Compositions solved numerically:')
    print('at. fraction:', alloy.x)
    print('wt. fraction:', alloy.w, '\n')

    alloy.solve()
    print('Compositions solved analytically:')
    print('at. fraction:', alloy.x)
    print('wt. fraction:', alloy.w)

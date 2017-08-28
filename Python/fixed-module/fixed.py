# -*- coding: utf-8 -*-
__author__ = 'OldChen'

import myhdl
from myhdl import intbv
from math import modf


# パラメータ	値の型	説明
# W	int(正の値)	全体のビット幅(ワード長)
# I	int	整数部のビット幅、正負の値が指定できる
# Q	sc_q_mode	量子化モード(省略可)
# O	sc_o_mode	オーバーフローモード(省略可)
# N	int	オーバーフロー用ビット数(省略可、Oのためのオプション)
class Signal_fixed(intbv):
    def __init__(self, w, i, q='SC_TRN', o='SC_WRAP', n=0, val=None):
        self.W = w
        self.I = i
        self.Q = q
        self.O = o
        self.N = n
        self.overflow_flag = 0
        min = - (2 ** (self.W-1))
        max = (2 ** (self.W-1)) - 1

        fixed_val = self.calc_fixed_val(val)
        intbv.__init__(self, min=min, max=max, val=fixed_val)

    def calc_fixed_val(self, c):
        val = c * (2.0 ** (self.W - self.I))
        (frac_part, int_part) = modf(val)

        #量子化
        if self.Q=='SC_TRN':
            if c < 0.0:
                val-=-1.0
        elif self.Q=='SC_RND':
            if frac_part >= 0.5:
                val += 1.0
            elif frac_part<-0.5:
                val += 1.0
        elif self.Q=='SC_TRN_ZERO':
            None
        elif self.Q==SC_RND_INF:
            if(frac_part >= 0.5):
                val += 1.0
            elif(frac_part<=-0.5):
                val -=1.0
        elif self.Q=='SC_RND_CONV':
            if (frac_part > 0.5) or  (frac_part == 0.5 and fmod(int_part, 2.0) ):
                val+=1.0
            elif (frac_part < -0.5) or (frac_part == -0.5 and fmod(int_part, 2.0)):
                val-=1.0
        elif self.Q=='SC_RND_ZERO':
            if frac_part > 0.5:
                val += 1.0
            elif frac_part < -0.5:
                val -= 1.0
        elif self.Q=='SC_RND_MIN_INF':
            if frac_part > 0.5:
                val += 1.0
            elif frac_part <= -0.5:
                val -= 1.0
        else:
            raise ValueError

        return int(val)

    def fixed_add(self, y):
        fx = self.float()
        fy = y.float()
        W = max(self.W, y.W) + 1
        I = max(self.I, y.I) + 1
        return Signal_fixed(W, I, self.Q, self.O, self.N, val=fx+fy)

    def fixed_sub(self, y):
        return self.fixed_add(-y)

    def fixed_sadd(self, y):
        fx = self.float()
        fy = y.float()
        return Signal_fixed(self.W, self.I, self.Q, self.O, self.N, val=fx+fy)

    def fixed_ssub(self, y):
        return self.fixed_sadd(-y)


    def fixed_mul(self, y):
        fx = self.float()
        fy = y.float()
        W = self.W+y.W
        I = self.I+y.I
        return Signal_fixed(W, I, self.Q, self.O, self.N, val=fx*fy)

    def fixed_div(self, y):
        W = self.W+y.W
        I = self.I+y.I
        return Signal_fixed(W, I, self.Q, self.O, self.N, val=fx/fy)

    def float(self):
        val = int(self)
        return val / (2.0 ** (self.W - self.I))


x = Signal_fixed(w=5, i=3, q='SC_TRN', o='SC_WRAP', n=0, val=0.6 )
print x.float()
print bin(x)

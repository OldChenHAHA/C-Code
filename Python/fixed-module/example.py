__author__ = 'OldChen'

from src.myhdl_fixed import Signal_fixed

val = Signal_fixed(w=9, i=5, q='SC_RND', o='SC_SAT', val=10.25)
print(len(val))
print("val = %s" % bin(val))
print("val = %f" % val.float())

val2 = Signal_fixed(w=9, i=5, q='SC_RND', o='SC_SAT', val=2.5)

print("val1 + val2 = %f" % val.fixed_add(val2))

val3 = val.fixed_add(val2)
print("val3 = %s" % bin(val3))
print("val3 = %f" % val3.float())

val4 = val.fixed_mul(val2)
print("val4 = %s" % bin(val4))
print("val4 = %f" % val4.float())

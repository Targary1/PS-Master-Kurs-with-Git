import math as mt
import numpy as np
import scipy as sp
import random as rd
import Modul10calc

test1 = sp.integrate.quad(lambda x, a, b: a * x + b, 0, 1, args=(1, 0))

# Nützliche Funktionen: random, uniform, randint, choice, choices, sample, shuffle with respective weights
lottery = ["Susi", "Dieter", "Hans", "Daniela", "Carsten"]
rd.shuffle(lottery)
print(lottery)
winner = rd.sample(lottery, k=3)
print(winner)

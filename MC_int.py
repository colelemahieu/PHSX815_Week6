# import packages
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import Random class
from Random import Random

# instantiate Random class with seed
random=Random(5555)

# define function to integrate over
def func(x):
    return math.sqrt(x)

# define our limits of integration
a=0
b=10

# true integral value over this region
true_value = 21.08185107

# return random x on our interval of integration
def Sample():
    return a + (b-a)*random.rand()

# define number of points to use with MC
points = 10000

# do MC integral
mc_int = 0
vol = 317
for i in range(0,points):
    x = Sample()
    y = func(x)
    if x < y:
        mc_int = mc_int + (vol*y)/points

print("The MC integration value for %i points is %.8f" %(points, mc_int))
print("The true value is %.8f " %(true_value))

# a list of sample points and corresponding MC integral value
# (obtained from running this macro with different values for "points"
sample = [10, 100, 1000, 10000]
MC_values = [72.1904053389, 27.8569284517, 23.6765305727, 21.185146386]

# lists of sample points and corresponding values from Trapezoid Integration
# and Gaussian Quadrature (obtained from running integration.py in the Week5 Repository
trap_sample = [3, 5, 7, 9]
trap_values = [19.08603404, 20.34239606, 20.67113893, 20.81190497]
gaus_sample = [3, 5, 7, 9]
gaus_values = [21.43006693, 21.13741625, 21.05747974, 21.00343325]

# make a nice plot
plt.figure()
plt.plot(sample, MC_values, color="forestgreen", label="MC Integral")
plt.plot(trap_sample, trap_values, color="firebrick", label="Trapezoid Integral")
plt.plot(gaus_sample, gaus_values, color="steelblue", label="Gaus Quad Integral")
plt.axhline(true_value, 0, 1000, color="k", label="True Integral")
plt.title("Comparison of Various Integration Methods", fontweight="bold")
plt.xlabel("Number of Sample Points Used in Integration")
plt.ylabel("Integration Value")
plt.legend()
#plt.xlim([0,12.5])
#plt.ylim([18,24])

plt.show()

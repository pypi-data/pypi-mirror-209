"""Tests for converter.py."""
# %% Imports
# Third Party Imports
from matplotlib import pyplot as plt
from numpy import arange, array, cos, sin

# econoplots Imports
from econoplots.converter import convert2Econo

# %% Make data
x = arange(-4.9, 6, 0.2)
y = array([1.5 * sin(x), cos(x)]).T

fig, ax = plt.subplots()
ax.plot(x, y, color="red")
ax.set_xlabel("-X label here")
ax.set_ylabel("Y label here")

# %% Test converter function
ax_new = convert2Econo(ax)
# %% done
plt.show()
print("done")

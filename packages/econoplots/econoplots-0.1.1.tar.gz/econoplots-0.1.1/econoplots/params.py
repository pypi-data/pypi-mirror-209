"""Set global parameters of matplotlib."""
# %% Imports
from __future__ import annotations

# Standard Library Imports
import json

# Third Party Imports
import matplotlib as mpl
from cycler import cycler

# %% Load color map
with open("econoplots/color_map.json") as json_file:
    color_map = json.load(json_file)


# %% Set Params
def setRCParams():
    mpl.rcParams["font.sans-serif"] = [
        "CMU Bright",
    ]
    mpl.rcParams["font.family"] = "sans-serif"
    mpl.rcParams.update(
        {
            "font.size": 14,
            "font.weight": "bold",
        }
    )
    mpl.rcParams["lines.linestyle"] = "-"
    mpl.rcParams["lines.linewidth"] = 3
    mpl.rcParams["axes.prop_cycle"] = cycler(color=color_map["line_chart"])
    mpl.rcParams["figure.facecolor"] = "w"
    mpl.rcParams["axes.facecolor"] = "w"
    mpl.rcParams["xtick.major.size"] = 6
    mpl.rcParams["xtick.minor.size"] = 3

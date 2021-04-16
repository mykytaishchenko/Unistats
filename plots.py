"""
plots.py

Module for visualizations.
"""

from typing import Dict

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot


def get_teacher_plot(data: Dict[str, int]) -> str:
    """Return a string containing HTML code.
    The returned HTML code is displayed in the browser as a bar chart.
    """
    trace = go.Bar(x=list(data.keys()), y=list(data.values()))
    fig = go.Figure(data=[trace])
    return plot(fig, output_type="div", include_plotlyjs="cdn")


if __name__ == "__main__":
    div = get_teacher_plot({"Лояльність": 2.432,
                    "Компетентність": 3.5351,
                    "Рівень професійно-педагогічної підготовки": 5.123442,
                    })
    with open("test_plots.html", 'w') as f:
        f.write(div)

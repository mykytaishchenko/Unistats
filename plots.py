"""
plots.py

Module for visualizations.
"""

from typing import Dict

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib
import matplotlib.cm as cm
import pandas as pd
import numpy as np


def get_teacher_vertical_plot(data: Dict[str, int]) -> str:
    """Return a string containing HTML code.
    The returned HTML code is displayed in the browser as a bar chart.
    """
    x, y = [], []
    for key, value in data.items():
        y.append(value)
        x.append(key)
    trace = go.Bar(y=y, x=x, text=y, texttemplate="<b style='font-size: 150%;'>%{text:.2f}</b>",
                  textposition='inside', hoverinfo = 'skip', orientation="v", marker_color='#535ba0')
    fig = go.Figure(data=[trace])
    fig.update_layout(
        xaxis = dict(
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=10,
            tickfont=dict(
                family='Arial',
                size=20,
                color='black',
            ),
        ),
        yaxis = dict(            
            tickfont=dict(
                family='Arial',
                size=20,
                color='black',
            ),
            
            showgrid=True,
            zeroline=True,
            showline=True,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=10,
            gridcolor='black',
            title_font=dict(
                size=20,
                color="black"
            )
        ),
        plot_bgcolor='rgba(0,0,0,0)',
    )
    
    return plot(fig, output_type="div", include_plotlyjs="cdn", show_link=False, config={
        'displayModeBar': False
    })

def get_teacher_horizontal_plot(data: Dict[str, int]) -> str:
    """Return a string containing HTML code.
    The returned HTML code is displayed in the browser as a bar chart.
    """
    x, y = [], []
    for key, value in data.items():
        x.append(value)
        y.append(key)
    trace = go.Bar(y=y, x=x, text=y, texttemplate="<b style='font-size: 150%;'>%{text}</b>",
                  textposition='inside', hovertemplate = '%{x:.2f}/5.00<extra></extra>', orientation="h", marker_color='#535ba0',
                  )
    fig = go.Figure(data=[trace])
    fig.update_layout(xaxis= dict(
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=10,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=20,
            color='black',
        ),),
        yaxis = dict(visible=False),  
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_range=[0,5],
        hoverlabel=dict(
            font_size=20,
            font_family="Arial"
        ),
        #hovermode="x unified"
    )
    
    return plot(fig, output_type="div", include_plotlyjs="cdn", show_link=False, config={
        'displayModeBar': False
    })



def get_teacher_polar_plot(data: Dict[str, int]) -> str:
    """Return a string containing HTML code.
    The returned HTML code is displayed in the browser as a polar chart.
    """
    r = list(data.values())
    r.append(r[0])
    theta = list(data.keys())
    theta.append(theta[0])
    trace = go.Scatterpolar(
        r = r,
        theta = theta,
        mode = 'lines',
        name = '',
        fill="toself",
        fillcolor="black",
        line=dict(color="green", width=5),
        opacity=0.7
    )
    layout = go.Layout(

    )
    fig = go.Figure(data=[trace], layout=layout)

    return plot(fig, output_type="div", include_plotlyjs="cdn", show_link=False, config={
        'displayModeBar': False
    })


def get_all_universities_statistics(df: pd.DataFrame) -> str:
    """Return HTML code, that represents a chart showing statistics on all universities.

    Parameters
    ----------
    df : DataFrame
        each row represents a university and each column represents a characteristic.
    """
    norm = matplotlib.colors.Normalize(vmin=0, vmax=5, clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=cm.RdYlGn)
    def val_to_color(val):
        rgba = mapper.to_rgba(val)
        res = "#"
        for i in range(3):
            color = round(rgba[i] * 255)
            color = f"{hex(color)[2:]:0>2}".upper()
            res += color
        return res

    fig = go.Figure()
    for char in df.columns:

        color = list(map(val_to_color, df[char]))

        trace = go.Bar(x=df.index, y=df[char], name=char,
                    hovertemplate='%{fullData.name}: %{y:.2f}<extra><span style="color: green"></span></extra>',
                    marker=dict(color=color), text=char, textposition = 'inside',
                    customdata=(df[char]/df.shape[0], df[char]),
                    textangle=90
        )
        fig.add_trace(trace)
        
        
    fig.update_layout(
    #     title='Статистика по всіх університетах',
        xaxis_title="Університети",
        yaxis_title="Загальна оцінка",
        legend_title="Характеристики",
        hoverlabel=dict(
            bgcolor="white",
            font_size=20,
            font_family="Arial"),
        yaxis=dict(
            showgrid=True,
            zeroline=True,
            showline=True,
            showticklabels=True,
            linecolor='black',
            gridcolor='black',
            tickfont = dict(
                size=20,
                color="black"
            ),
            title_font=dict(
                size=20,
                color="black"
            )
        ),
        xaxis=dict(
            tickfont=dict(size=20),
            title_font=dict(
                size=20,
                color="black"
            )
        ),
        yaxis_range=[0,5],
    #     legend_font=dict(size=20),
    #     legend_title_font=dict(size=20),
    #     title_font=dict(size=20, color="black")
    )


    button1 = dict(method= 'update',
                label='group',
                args=[
                        {'textangle': 90,}, #dict for fig.data[0] updates
                    {"barmode": 'group'} #update layout attribute   
                    ])

    button2 = dict(method= 'update',
                label='stack',
                args=[
                    {'textangle': 0, },
                    {"barmode": 'stack'} #update layout attribute    
            ])

    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons= [button1, button2]
                )
        ],
        plot_bgcolor='rgba(0,0,0,0)', 
        showlegend=False
    )

    fig.update_layout(barmode="group")
    return plot(fig, output_type="div", include_plotlyjs="cdn", show_link=False, config={
        'displayModeBar': False
    })



if __name__ == "__main__":
    if True:
        div = get_teacher_horizontal_plot({"Лояльність": 2.432,
                    "Компетентність": 3.5351,
                    "Рівень професійно-педагогічної підготовки": 5.0,
                    })
    else:
        df = pd.DataFrame(5*np.random.rand(3, 4), columns=['Пунктуальність', 'Об\'єктивність оцінювання', 'Ввічливість викладача', 'Володіння матеріалом'],
                    index=['Uni1', 'Uni2', 'Uni3'])
        div = get_all_universities_statistics(df)

    with open("test_plots.html", 'w') as f:
        f.write(div)

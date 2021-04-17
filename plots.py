"""
plots.py

Module for visualizations.
"""

from typing import Dict, List
import random

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib
import matplotlib.cm as cm
import pandas as pd
import numpy as np

from models import Response


def generate_vertical_plot(data: Dict[str, int]) -> str:
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

def generate_horizontal_plot(data: Dict[str, int]) -> str:
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

def generate_polar_plot(data: Dict[str, int]) -> str:
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

def get_teacher_plot(responses: List[Response], plot_type: str):
    """Return a plot given responses.

    plot_type : str
        should be one of "vertical", "horizontal", "polar"
    """
    assert len(responses) >= 1, "Length of responses should be greater than 0"
    average = {char: 0 for char in responses[0].characteristics.keys()}
    for response in responses:
        for char in response.characteristics:
            average[char] += response.characteristics[char]

    for char in average:
        average[char] /= len(responses)

    if plot_type == "vertical":
        return generate_vertical_plot(average)
    elif plot_type == "horizontal":
        return generate_horizontal_plot(average)
    elif plot_type == "polar":
        return generate_polar_plot(average)
    else:
        raise ValueError(f'Invalid argument for plot_type: \"{plot_type}\". Should be either\
 "vertical", "horizontal" or "polar"')


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

def get_universities_comparison(df : pd.DataFrame) -> str:
    """Return HTML code, that represents a chart showing comperison of universities.
    User can select which two universities to compare by using dropdown menu.

    Parameters
    ----------
    df : DataFrame
        each row represents a university and each column represents a characteristic.
    """
    d = {'x': [], 'y': [], 'group': []}
    for i in df.index:
        d['group'].extend([i]*df.shape[1])
        d['x'].extend(list(df.columns))
        d['y'].extend(list(df.loc[i]))
    df1 = pd.DataFrame(data=d)

    # split df1 by groups and organize them in a dict
    groups = df1['group'].unique().tolist()
    dfs={}
    for g in groups:
        dfs[str(g)]=df1[df1['group']==g]



    # one trace for each column per dataframe
    fig=go.Figure()

    # set up the first trace
    fig.add_trace(go.Bar(x=dfs[df.index[0]]['x'], customdata=[df.index[0]]*df.shape[1], text = df.index[0],
                                y=dfs[df.index[0]]['y'], texttemplate="%{customdata}", textposition = 'outside',
                                visible=True, hovertemplate="%{y:.2f}<extra></extra>", name=df.index[0])
                )
    # set up the second trace
    fig.add_trace(go.Bar(x=dfs[df.index[1]]['x'], customdata=[df.index[1]]*df.shape[1], text = df.index[1],
                                y=dfs[df.index[1]]['y'], texttemplate="%{customdata}", textposition = 'outside',
                                hovertemplate="%{y:.2f}<extra></extra>", name=df.index[1])
                )

    buttons1=[]

    # button with one option for each dataframe
    for df1 in dfs.keys():
        #print(b, df)
        buttons1.append(dict(method='restyle',
                            label=df1,
                            visible=True,
                            args=[{'y':[dfs[str(df1)]['y'].values],
                                'customdata':([df1]*df.shape[1],),
                                'name': df1}, [0]],
                            )
                    )

    # another button with one option for each dataframe
    buttons2=[]
    for df1 in dfs.keys():
        buttons2.append(dict(method='restyle',
                            label=df1,
                            visible=True,
                            args=[{'y':[dfs[str(df1)]['y'].values],
                                'customdata':([df1]*df.shape[1],),
                                    'name': df1}, [1]],
                            ),
                    )

    updatemenu=[dict(), dict()]

    updatemenu[0]['buttons']=buttons1
    updatemenu[0]['direction']='down'
    updatemenu[0]['showactive']=True
    updatemenu[0]['y']=0.75
    updatemenu[0]['active']=0

    updatemenu[1]['buttons']=buttons2
    updatemenu[1]['y']=0.3
    updatemenu[1]['active']=1

    # add dropdown menus to the figure
    fig.update_layout(showlegend=False, updatemenus=updatemenu,
            yaxis_range=[0,5])

    # add notations to the dropdown menus
    fig.update_layout(
        annotations=[
            go.layout.Annotation(text="<b>Перший<br>університет</b>",
                                x=-0.15, xref="paper",
                                y=0.9, yref="paper",
                                align="center", showarrow=False),
            go.layout.Annotation(text="<b>Другий<br>університет</b>",
                                x=-0.15, xref="paper", y=0.4,
                                yref="paper", showarrow=False),
                    ],

        yaxis=dict(
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
        showlegend=True
    #     plot_bgcolor='rgba(0,0,0,0)',
    )

    return plot(fig, output_type="div", include_plotlyjs="cdn", show_link=False, config={
            'displayModeBar': False
        })


def get_universities_table(data: Dict[str, int]) -> str:
    style = """<style>
    .styled-table {
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 1.5em;
        font-family: sans-serif;
        min-width: 400px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }

    .styled-table thead tr {
        background-color: #535ba0;
        color: #ffffff;
        text-align: left;
    }

    .styled-table th,
    .styled-table td {
        padding: 12px 15px;
    }

    .styled-table tbody tr {
        border-bottom: 1px solid #dddddd;
    }

    .styled-table tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }

    .styled-table tbody tr:last-of-type {
        border-bottom: 2px solid #535ba0;
    }

    .styled-table tbody tr.active-row {
        font-weight: bold;
        color: #009879;
    }
    </style>
    """

    thead = """
    <thead>
        <tr>
            <th>Університет</th>
            <th>Рейтинг</th>
        </tr>
    </thead>
    """
    tbody = "<tbody>"
    for char, mark in data.items():
        tbody += f"""<tr>
            <td>{char}</td>
            <td>{mark:.2f}</td>
        </tr>"""
    tbody += "</tbody>"

    return style + '<table class="styled-table">' + thead + tbody + "</table>"


if __name__ == "__main__":
    if False:
        # test generate_horizontal_plot
        div = generate_horizontal_plot({"Лояльність": 2.432,
                    "Компетентність": 3.5351,
                    "Рівень професійно-педагогічної підготовки": 5.0,
                    })
    elif False:
        # test get_all_universities_statistics
        df = pd.DataFrame(5*np.random.rand(3, 4), columns=['Пунктуальність', 'Об\'єктивність оцінювання', 'Ввічливість викладача', 'Володіння матеріалом'],
                    index=['Uni1', 'Uni2', 'Uni3'])
        div = get_all_universities_statistics(df)
    elif False:
        # test get_teacher_plot
        responses = []
        for i in range(10):
            chars = ['general', 'sufficiency', 'relevance', 'loyalty', 'politeness', 'material', 'punctuality', 'objectivity', 'adaptation', 'complexity']
            evaluation = {char: random.randint(1, 6) for char in chars}
            responses.append(Response(2, random.randint(1, 10**6), evaluation))
        div = get_teacher_plot(responses, 'polar')
    elif False:
        # test get_universities_comparison
        df = pd.DataFrame(5*np.random.rand(3, 4), columns=['Пунктуальність', 'Об\'єктивність оцінювання', 'Ввічливість викладача', 'Володіння матеріалом'],
                  index=['Uni1', 'Uni2', 'Uni3'])
        div = get_universities_comparison(df)
    elif True:
        universities = ["UCU", "DSA", "National University of Ivan Franko", "НАУКМА"]
        aver_evaluations = {uni: random.random()*5 for uni in universities}
        div = get_universities_table(aver_evaluations)

    with open("test_plots.html", 'w') as f:
        f.write(div)

    import database
    print(database.DBConnection().get_responses_by_position_id('pos-16185-0WJIl5-99238')) # why it doesn't work?

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:25:39 2020

@author: siirias
"""
#Rahoituskausi:1.2.2021-30.11.2024

import plotly.express as px
import pandas as pd
output_folder = "D:\\Data\\figures\\"
out_file_name = "ExtremeSea_Gantt.png"
wp_desc = {
        'WP1':'WP1: Calculation/determination of extremes',
        'WP2':'WP2: Impacts on ecosystem',
        'WP3':'WP3: Impact on society ',
        'WP4':'WP4: New policies and methods',
        'WP5':'WP5: Comprehensive interdiciplinary advice'}
the_scale=0.7   # with this can kind of set the text size. 
                # Larger number=smaller text
plot_w = 1500*the_scale
plot_h = 700*the_scale
df = pd.DataFrame([
    dict(Task="T1.1", Start='2021-02-01', Finish='2022-06-30', WP = wp_desc['WP1']),
    dict(Task="T1.2", Start='2021-06-01', Finish='2023-06-01', WP = wp_desc['WP1']),
    dict(Task="T1.3", Start='2021-06-01', Finish='2023-06-01', WP = wp_desc['WP1']),
    dict(Task="T1.4", Start='2021-06-01', Finish='2023-06-01', WP = wp_desc['WP1']),
    dict(Task="T1.5", Start='2022-01-01', Finish='2024-01-30', WP = wp_desc['WP1']),
    dict(Task="T2.1", Start='2021-02-01', Finish='2023-06-30', WP = wp_desc['WP2']),
    dict(Task="T2.2", Start='2021-06-01', Finish='2024-01-01', WP = wp_desc['WP2']),
    dict(Task="T2.3", Start='2022-01-01', Finish='2024-06-30', WP = wp_desc['WP2']),
    dict(Task="T2.4", Start='2022-06-01', Finish='2024-11-30', WP = wp_desc['WP2']),
    dict(Task="T3.1", Start='2021-02-01', Finish='2023-06-30', WP = wp_desc['WP3']),
    dict(Task="T3.2", Start='2021-06-30', Finish='2024-01-30', WP = wp_desc['WP3']),
    dict(Task="T3.3", Start='2021-03-01', Finish='2023-12-30', WP = wp_desc['WP3']),
    dict(Task="T3.4", Start='2022-06-01', Finish='2024-11-30', WP = wp_desc['WP3']),
    dict(Task="T3.5", Start='2021-08-01', Finish='2024-06-30', WP = wp_desc['WP3']),
    dict(Task="T4.1", Start='2021-02-01', Finish='2023-11-30', WP = wp_desc['WP4']),
    dict(Task="T4.2", Start='2021-07-01', Finish='2024-06-01', WP = wp_desc['WP4']),
    dict(Task="T4.3", Start='2021-12-29', Finish='2024-11-30', WP = wp_desc['WP4']),
    dict(Task="T5", Start='2021-02-01', Finish='2024-11-30', WP = wp_desc['WP5']),
])
meet_color = 'rgba(0.0,0.0,0.0,0.7)' # color for the vertical lines
my_colormap = ['rgb(70,70,160)',    # colors for the workpackages
               'rgb(100,150,200)',
               'rgb(150,200,150)',
               'rgb(150,180,255)',
               'rgb(180,180,255)']
meetings =[
        dict(Time='2021-02-01', Color = meet_color),
        dict(Time='2022-06-30', Color = meet_color),
        dict(Time='2023-06-01', Color = meet_color),
        dict(Time='2024-01-30', Color = meet_color),
        dict(Time='2024-11-30', Color = meet_color),
        ]

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color = 'WP',\
                  height = plot_h, width = plot_w, \
                  color_discrete_sequence=my_colormap)
fig.update_yaxes(autorange="reversed",tickson="boundaries", showgrid=True) # otherwise tasks are listed from the bottom up
fig.update_xaxes(dtick='M3',tickangle=45) # otherwise tasks are listed from the bottom up

for meet in meetings:   # add the vertical lines for meeting times etc.
    fig.add_shape(
                type="line",
                xref="x",
                yref="paper",
                x0=meet['Time'],
                y0=0,
                x1=meet['Time'],
                y1=1.0,
                line=dict(
                    color=meet['Color'],
                    width=3,
                ),
            )
fig.write_image(output_folder + out_file_name,scale=1.0/the_scale)
fig
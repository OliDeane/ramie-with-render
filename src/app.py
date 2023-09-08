# package imports
from dash import html, Dash, dcc, Input, Output, callback, State, no_update, dash_table, ctx, callback_context, Patch, ALL
import dash_bootstrap_components as dbc
from swiplserver import PrologMQI, PrologThread
import pandas as pd
import plotly.express as px
import json
import re
import os
import glob

# with open('test.json') as meta_data:

# with PrologMQI() as mqi:
#     with mqi.create_thread() as main_prolog_thread:
        
app = Dash(__name__)
server = app.server

download_button = html.Button(id="download_button",children=["Download Filtered CSV"], style={"marginTop": 20})
# download_component = dcc.Download()

app.layout = html.Div(
    [
        html.H2("RAIMEE Data Download PySwipl", style={"marginBottom": 20}),
        download_button,
        html.Div(id="output", children = [])
    ]
)

@app.callback(
    Output("output", "children"),
    Input("download_button", "n_clicks"),
)
def download_data(n_clicks):
    # dff = pd.DataFrame(data)
    if not n_clicks:
        return no_update
        # Load in a test file
    selected_data = json.load(meta_data)

    selected_data = selected_data[str(3)]['title']
    # main_prolog_thread.query(f"A=4.")
    return html.Div([html.P(str(selected_data)+str(3))])

app.run_server(debug=True)

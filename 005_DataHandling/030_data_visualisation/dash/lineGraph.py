#%%
import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

#%% Data Prep
# source: https://www.kaggle.com/datasets/medharawat/google-stock-price?resource=download&select=Google_Stock_Price_Train.csv
df = pd.read_csv("Google_Stock_Price_Train.csv")

#%% Visualisation
fig = px.line(df, x="Date", y="Open", title="Google Stock")
fig
#%%
app = dash.Dash(__name__)
app.title = "Google Stock"

app.layout = html.Div(
    id="app-container",
    children=[
        html.H1("Google Stock"),
        html.P("[USD]"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
# %%

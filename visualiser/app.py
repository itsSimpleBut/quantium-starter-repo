from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash()
df = pd.read_csv("../data/cleandata.csv")
fig = px.line(df, x="Date", y="Sales", color="Region")

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales"),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    app.run(debug=True)

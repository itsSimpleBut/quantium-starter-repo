from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/cleandata.csv")
app = Dash()
displaySettingsText = '''
## Display Settings  
Use these to filter the data by their  
regions!
'''

app.layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            "Pink Morsel Sales",
            id="title",
            style={"textAlign": "center", "color": "#4A80F0"}),
        dcc.Graph(id="visualiser")
    ],style={"flex": 1,"backgroundColor": "#746980"}),

    html.Div(children=[
        dcc.Markdown(id="markdown", children=displaySettingsText),
        html.Label("Filter by Region"),
        dcc.RadioItems([str(i) for i in df['Region'].unique()],'north',id='regionInput'),
    ],style={
        "display":"flex",
        "alignItems":"center",
        "justifyContent":"center",
        "flexDirection":"column",
        "flex":1,
        "backgroundColor":"#4D4555",
        "color":"#A5A836",
        "padding":"12vh",
        "border":"1px solid #A5A836"
    }),
],style={"width":"100%","display":"flex","flexDirection":"row","backgroundColor":"black"})

@callback(
    Output("visualiser", "figure"),
    Input("regionInput", "value"))
def update_graph(selected_region):
    filtered_df = df[df['Region'] == selected_region]
    fig = px.line(filtered_df, x="Date", y="Sales")
    fig.update_layout(
        transition_duration=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=600
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)

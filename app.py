import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from components.sidebar import sidebar

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

server = app.server

app.layout = html.Div([
         dcc.Location(id="url", pathname="/02_usaid"),
         sidebar(),
         html.Div(className="page-content"),
         dash.page_container,
     ],
 )


if __name__ == '__main__':
    app.run(debug=True, dev_tools_hot_reload=True)
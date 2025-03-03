import dash_bootstrap_components as dbc
from dash import html


def sidebar():
    sidebar_layout = dbc.Col(
        [
            dbc.Row(
                [html.Img(src="assets/usa_flag.png", style={"height": "60px"})],
                justify="center",
                className="sidebar-logo",
            ),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("USAID Terminations", href="/02_usaid", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            html.Div(
                [
                    html.Span("Created by "),
                    html.A(
                        "Emily Steed",
                        href="https://github.com/emilysteed",
                        target="_blank",
                    ),
                    html.Br(),
                    html.Span("Data Source "),
                    html.A(
                        "USAID Terminations Tracker",
                        href="https://docs.google.com/spreadsheets/d/1Q-WLZkl-q39mCl6GwItuRQxhg6Ote_OOqvp8mcYV3fI/edit?gid=0#gid=0",
                        target="_blank",
                    ),
                ],
                className="subtitle-sidebar",
                style={"position": "absolute", "bottom": "10px", "width": "100%"},
            ),
        ],
        className="sidebar",
    )
    return sidebar_layout

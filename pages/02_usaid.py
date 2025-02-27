import dash
import dash_bootstrap_components as dbc
from dash import callback, dcc, html, Output, Input 
from data.get_usaid_term_data import get_usaid_term_data
from components.usaid_term_map_usa import usaid_term_map_usa
from components.usaid_term_graph_state import usaid_term_graph_state

df = get_usaid_term_data()

# Create state dropdown options 
valid_states = df["state_abbrev"].dropna().unique()
state_dropdown_options = [{"label": state, "value": state} for state in valid_states]
state_dropdown_options.insert(0, {"label": "All States", "value": "All"})  

#Create prime dropdown options
valid_primes = df["Prime"].dropna().unique()
prime_dropdown_options = [{"label": prime, "value": prime} for prime in valid_primes]
prime_dropdown_options.insert(0, {"label": "All Primes", "value": "All"})


dash.register_page(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    path="/02_usaid",
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H2(
                                    "USAID Terminations", 
                                    className="title-card-large"
                                ),
                            ]
                        ),
                        className="title-card-container",
                    ),
                    width=12, 
                ),
            ],
        ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H3(
                                    "Select State",
                                    className="subtitle-small",
                                ),
                                dcc.Dropdown(
                                    id="state-dropdown",
                                    options=state_dropdown_options,
                                    value="All",
                                    clearable=True,
                                    multi=True,
                                    placeholder="Select here",
                                    className="custom-dropdown",
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                html.H3(
                                    "Select Prime",
                                    className="subtitle-small",
                                ),
                                dcc.Dropdown(
                                    id="prime-dropdown",
                                    options=prime_dropdown_options,
                                    value="All",
                                    clearable=True,
                                    multi=True,
                                    placeholder="Select here",
                                    className="custom-dropdown",
                                ),
                            ],
                            width=4,
                        ),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    id="map-usa",
                                    config={"displayModeBar": False},
                                    className="chart-card",
                                    style={"height": "337px"},
                                ),
                                type="circle",
                                color="#B41240",
                            ),
                            width=6,
                        ),
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    id="chart-state",
                                    config={"displayModeBar": False},
                                    className="chart-card",
                                    style={"height": "337px"},
                                ),
                                type="circle",
                                color="#B41240",
                            ),
                            width=6,
                        ),
                    ],
                ),
                html.Br(),
    ],
    fluid=True,
    className="page-content",  
)

# Callback to update the prime-dropdown options based on selected state
@callback(
    Output('prime-dropdown', 'options'),
    Input('state-dropdown', 'value'),
    Input('prime-dropdown', 'value')
)
def update_prime_dropdown(select_state, select_prime):
    if not select_state or "All" in select_state:
        return prime_dropdown_options
    else:
        filtered_df = df[df['state_abbrev'].isin(select_state)]
        valid_primes = filtered_df['Prime'].fillna("NA").unique()
        
        return [{"label": prime, "value": prime} for prime in valid_primes]

# Callback to update the state-dropdown options based on selected prime
@callback(
    Output('state-dropdown', 'options'),
    Input('prime-dropdown', 'value'),
    Input('state-dropdown', 'value')
)
def update_state_dropdown(select_prime, select_state):
    if isinstance(select_prime, str):
        select_prime = [select_prime]

    if not select_prime or "All" in select_prime:
        return state_dropdown_options
    else:
        filtered_df = df[df['Prime'].astype(str).isin(select_prime)]
        valid_states = filtered_df['state_abbrev'].unique()
        
        return [{"label": state, "value": state} for state in valid_states]

# Callback to update both map and chart based on the selections in both dropdowns
@callback(
    [
        Output("map-usa", "figure"),
        Output("chart-state", "figure")
    ],
    [
        Input("state-dropdown", "value"),
        Input("prime-dropdown", "value")
    ],
)
def update_values(select_state, select_prime):
    df = get_usaid_term_data().dropna(subset=["state_abbrev"])
    filtered_df = df.copy()

    # Filter by selected states (handle multi-selection)
    if select_state and "All" not in select_state:
        filtered_df = filtered_df[filtered_df['state_abbrev'].isin(select_state)]

    # Filter by selected primes (handle multi-selection)
    if select_prime and "All" not in select_prime:
        filtered_df = filtered_df[filtered_df['Prime'].isin(select_prime)]

    # Call the functions to generate the figures
    map_figure = usaid_term_map_usa(filtered_df)
    chart_figure = usaid_term_graph_state(filtered_df)

    return [map_figure, chart_figure]










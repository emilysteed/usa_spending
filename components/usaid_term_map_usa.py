import plotly.express as px
import pandas as pd


def usaid_term_map_usa(usaid_term_data):

    fig = px.choropleth(
        usaid_term_data,
        color="state_term_count",
        color_continuous_scale="bluered",
        hover_name="Prime State",
        hover_data={
            "state_term_count": True,
            "state_oblg_funds": True,
            "state_abbrev": False,
        },
        labels={
            "state_term_count": "Number of Terminated Awards",
            "state_oblg_funds": "Obligated Funds",
        },
        locations="state_abbrev",
        locationmode="USA-states",
        scope="usa",
        title="Terminations by State",
    )
    fig.update_layout(coloraxis_showscale=False, margin=dict(l=15, r=15, t=60, b=15))
    return fig

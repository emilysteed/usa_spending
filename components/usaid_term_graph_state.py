import plotly.express as px
import pandas as pd


def usaid_term_graph_state(usaid_term_data):
    usaid_term_data = usaid_term_data[["state_abbrev", "Prime", "Obligation"]]

    fig = px.bar(
        usaid_term_data,
        x="state_abbrev",
        y="Obligation",
        color="Prime",
        title="Obligated Funds for Terminations",
        barmode="stack",
    )

    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Value of Obligated Funds",
        xaxis_tickangle=-45,
        showlegend=False,
        margin=dict(l=15, r=15, t=60, b=15),
    )
    fig.update_yaxes(visible=False)

    return fig

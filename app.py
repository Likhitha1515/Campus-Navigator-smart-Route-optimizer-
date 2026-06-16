import streamlit as st

import networkx as nx

import matplotlib.pyplot as plt

from graph_data import campus

from algorithms import dijkstra


st.set_page_config(
    page_title="Campus Navigator",
    layout="wide"
)

st.title("Campus Navigator & Smart Route Optimizer")


locations = list(campus.keys())


start = st.selectbox(
    "Select Starting Point",
    locations
)

destination = st.selectbox(
    "Select Destination",
    locations
)


blocked = st.selectbox(
    "Road Block Simulation",
    ["None"] + locations
)


temp_graph = {
    node: neighbors.copy()
    for node, neighbors in campus.items()
}


if blocked != "None":

    for node in temp_graph:

        temp_graph[node].pop(
            blocked,
            None
        )

    temp_graph.pop(
        blocked,
        None
    )


if st.button("Find Route"):

    path, distance = dijkstra(
        temp_graph,
        start,
        destination
    )

    if not path:

        st.error("No route available")

    else:

        st.success(
            " ➜ ".join(path)
        )

        st.write(
            f"Distance : {distance} meters"
        )

        G = nx.Graph()

        for node in temp_graph:

            for neighbor, weight in temp_graph[node].items():

                G.add_edge(
                    node,
                    neighbor,
                    weight=weight
                )

        pos = nx.spring_layout(
            G,
            seed=42
        )

        fig, ax = plt.subplots(
            figsize=(9,6)
        )

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=2500,
            font_size=9,
            ax=ax
        )

        route_edges = []

        for i in range(
            len(path)-1
        ):

            route_edges.append(
                (
                    path[i],
                    path[i+1]
                )
            )

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=route_edges,
            width=4,
            ax=ax
        )

        st.pyplot(fig)
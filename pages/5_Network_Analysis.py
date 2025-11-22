"""
Network Analysis - Friendship Network Visualization
Lab 6.1 - Network Visualization and Analysis Assignment
"""

import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import pandas as pd
from networkx.algorithms import community

st.title("🕸️ Network Analysis: College Friendship Network")
st.markdown("""
This page analyzes a friendship network among 10 college students using graph theory 
and network analysis techniques. We explore connections, influence, and community structures.
""")
st.markdown("---")

# Create the network graph
@st.cache_data
def create_friendship_network():
    """Create the friendship network graph"""
    G = nx.Graph()
    
    # Add nodes
    nodes = ["Alice", "Bob", "Charlie", "Diana", "Eve", 
             "Frank", "Grace", "Hannah", "Ian", "Jack"]
    G.add_nodes_from(nodes)
    
    # Add edges (friendships)
    edges = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "Charlie"),
        ("Charlie", "Diana"),
        ("Diana", "Eve"),
        ("Bob", "Diana"),
        ("Frank", "Eve"),
        ("Eve", "Ian"),
        ("Diana", "Ian"),
        ("Ian", "Grace"),
        ("Grace", "Hannah"),
        ("Hannah", "Jack"),
        ("Grace", "Jack"),
        ("Charlie", "Frank"),
        ("Alice", "Eve"),
        ("Bob", "Jack")
    ]
    G.add_edges_from(edges)
    
    return G

G = create_friendship_network()

# Calculate network metrics
def calculate_metrics(G):
    """Calculate various network metrics"""
    metrics = {}
    
    # Degree centrality
    degree_cent = nx.degree_centrality(G)
    metrics['degree'] = degree_cent
    
    # Betweenness centrality
    betweenness_cent = nx.betweenness_centrality(G)
    metrics['betweenness'] = betweenness_cent
    
    # Closeness centrality
    closeness_cent = nx.closeness_centrality(G)
    metrics['closeness'] = closeness_cent
    
    # Find most influential (highest betweenness)
    most_influential = max(betweenness_cent.items(), key=lambda x: x[1])[0]
    metrics['most_influential'] = most_influential
    
    # Community detection
    communities = community.greedy_modularity_communities(G)
    metrics['communities'] = communities
    
    return metrics

metrics = calculate_metrics(G)

# Network Overview
st.header("📊 Network Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Nodes", G.number_of_nodes())
    
with col2:
    st.metric("Total Edges", G.number_of_edges())
    
with col3:
    avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
    st.metric("Avg Connections", f"{avg_degree:.1f}")
    
with col4:
    density = nx.density(G)
    st.metric("Network Density", f"{density:.2f}")

st.markdown("---")

# Task 1: Visualize the Network
st.header("1. 🔍 Network Visualization")

st.markdown("""
This interactive network graph shows the friendship connections among 10 college students. 
Each node represents a person, and edges represent friendships between them.
""")

# Create interactive network visualization using Plotly
def create_network_viz(G, metrics, highlight_influential=True):
    """Create interactive network visualization with Plotly"""
    
    # Use spring layout for positioning
    pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)
    
    # Create edge traces
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines',
        name='Friendships'
    )
    
    # Create node traces with colors based on influence
    node_x = []
    node_y = []
    node_text = []
    node_colors = []
    node_sizes = []
    
    most_influential = metrics['most_influential']
    
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        
        # Get metrics for hover text
        degree = G.degree(node)
        betweenness = metrics['betweenness'][node]
        closeness = metrics['closeness'][node]
        
        node_text.append(
            f"<b>{node}</b><br>"
            f"Connections: {degree}<br>"
            f"Betweenness: {betweenness:.3f}<br>"
            f"Closeness: {closeness:.3f}"
        )
        
        # Color the most influential person differently
        if highlight_influential and node == most_influential:
            node_colors.append('#FF4B4B')  # Red for most influential
            node_sizes.append(30)
        else:
            node_colors.append('#1f77b4')  # Blue for others
            node_sizes.append(20)
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[node for node in G.nodes()],
        textposition="top center",
        hovertext=node_text,
        hoverinfo='text',
        marker=dict(
            size=node_sizes,
            color=node_colors,
            line=dict(width=2, color='white')
        ),
        name='Students'
    )
    
    # Create figure
    fig = go.Figure(data=[edge_trace, node_trace])
    
    fig.update_layout(
        title=dict(
            text="Friendship Network - Most Influential Person Highlighted in Red",
            font=dict(size=16)
        ),
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=600,
        plot_bgcolor='white'
    )
    
    return fig

fig = create_network_viz(G, metrics)
st.plotly_chart(fig, use_container_width=True)

with st.expander("📖 How to Read This Network Graph"):
    st.markdown("""
    - **Nodes (circles)**: Represent individual students
    - **Edges (lines)**: Represent friendships between students
    - **Node Size**: Larger nodes indicate the most influential person
    - **Red Color**: Highlights the most influential person (highest betweenness centrality)
    - **Blue Color**: Regular network members
    - **Hover**: Move your mouse over nodes to see detailed metrics
    """)

st.markdown("---")

# Task 2: Degree Analysis
st.header("2. 📈 Degree Analysis: Most Connected Students")

st.markdown("""
**Degree centrality** measures how many direct connections (friendships) each person has. 
A higher degree means more friends in the network.
""")

# Calculate degrees
degrees = dict(G.degree())
degree_df = pd.DataFrame([
    {'Student': node, 'Connections': degree, 'Degree Centrality': metrics['degree'][node]}
    for node, degree in degrees.items()
]).sort_values('Connections', ascending=False).reset_index(drop=True)

# Display top 3
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🏆 Top 3 Most Connected")
    for idx, row in degree_df.head(3).iterrows():
        medal = "🥇" if idx == 0 else "🥈" if idx == 1 else "🥉"
        st.metric(
            f"{medal} {row['Student']}", 
            f"{row['Connections']} friends",
            delta=f"Centrality: {row['Degree Centrality']:.3f}"
        )

with col2:
    # Bar chart of connections
    import plotly.express as px
    fig_degree = px.bar(
        degree_df, 
        x='Student', 
        y='Connections',
        title="Number of Friendships per Student",
        color='Connections',
        color_continuous_scale='Blues'
    )
    fig_degree.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig_degree, use_container_width=True)

# Full table
with st.expander("📊 View Full Degree Analysis Table"):
    st.dataframe(degree_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Task 3: Centrality Measures
st.header("3. 🎯 Centrality Measures: Who's Most Important?")

st.markdown("""
**Centrality metrics** help identify the most important people in the network:
- **Betweenness Centrality**: Measures how often a person acts as a bridge between others
- **Closeness Centrality**: Measures how close a person is to everyone else in the network
- **Degree Centrality**: Measures how many direct connections a person has
""")

# Create centrality dataframe
centrality_df = pd.DataFrame({
    'Student': list(G.nodes()),
    'Degree': [metrics['degree'][node] for node in G.nodes()],
    'Betweenness': [metrics['betweenness'][node] for node in G.nodes()],
    'Closeness': [metrics['closeness'][node] for node in G.nodes()]
})

# Normalize for visualization (0-1 scale already, but multiply by 100 for readability)
centrality_df_display = centrality_df.copy()
centrality_df_display['Degree'] = centrality_df_display['Degree'] * 100
centrality_df_display['Betweenness'] = centrality_df_display['Betweenness'] * 100
centrality_df_display['Closeness'] = centrality_df_display['Closeness'] * 100

# Multi-metric visualization
fig_centrality = go.Figure()

fig_centrality.add_trace(go.Bar(
    name='Degree',
    x=centrality_df_display['Student'],
    y=centrality_df_display['Degree'],
    marker_color='#1f77b4'
))

fig_centrality.add_trace(go.Bar(
    name='Betweenness',
    x=centrality_df_display['Student'],
    y=centrality_df_display['Betweenness'],
    marker_color='#ff7f0e'
))

fig_centrality.add_trace(go.Bar(
    name='Closeness',
    x=centrality_df_display['Student'],
    y=centrality_df_display['Closeness'],
    marker_color='#2ca02c'
))

fig_centrality.update_layout(
    title="Centrality Measures Comparison (Scaled 0-100)",
    xaxis_title="Student",
    yaxis_title="Centrality Score",
    barmode='group',
    height=500
)

st.plotly_chart(fig_centrality, use_container_width=True)

# Show detailed table
with st.expander("📊 View Full Centrality Measures Table"):
    st.dataframe(centrality_df.sort_values('Betweenness', ascending=False), 
                 use_container_width=True, hide_index=True)

st.markdown("---")

# Task 4: Community Detection
st.header("4. 👥 Community Detection: Friend Groups")

st.markdown("""
Using the **Greedy Modularity** algorithm, we identify natural friend groups or clusters 
within the network. People in the same community are more densely connected to each other 
than to people in other communities.
""")

# Display communities
communities = metrics['communities']
num_communities = len(communities)

st.subheader(f"Found {num_communities} Distinct Friend Groups")

# Create community dataframe
community_data = []
for idx, comm in enumerate(communities, 1):
    members = sorted(list(comm))
    community_data.append({
        'Group': f"Community {idx}",
        'Size': len(members),
        'Members': ", ".join(members)
    })

community_df = pd.DataFrame(community_data)

# Display communities
for idx, row in community_df.iterrows():
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.metric(row['Group'], f"{row['Size']} members")
        with col2:
            st.write("")
        with col3:
            st.write(f"**Members:** {row['Members']}")

# Visualize communities with colors
st.subheader("Network Colored by Communities")

def create_community_viz(G, communities):
    """Create network visualization with community colors"""
    
    pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)
    
    # Create edge traces
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines'
    )
    
    # Color palette for communities
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    # Create node color mapping
    node_colors_map = {}
    for idx, comm in enumerate(communities):
        for node in comm:
            node_colors_map[node] = colors[idx % len(colors)]
    
    # Create node traces
    node_x = []
    node_y = []
    node_text = []
    node_colors = []
    
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        
        # Find which community this node belongs to
        comm_num = None
        for idx, comm in enumerate(communities, 1):
            if node in comm:
                comm_num = idx
                break
        
        node_text.append(f"<b>{node}</b><br>Community {comm_num}")
        node_colors.append(node_colors_map[node])
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[node for node in G.nodes()],
        textposition="top center",
        hovertext=node_text,
        hoverinfo='text',
        marker=dict(
            size=25,
            color=node_colors,
            line=dict(width=2, color='white')
        )
    )
    
    fig = go.Figure(data=[edge_trace, node_trace])
    
    fig.update_layout(
        title="Friendship Network - Colored by Community",
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=600,
        plot_bgcolor='white'
    )
    
    return fig

fig_communities = create_community_viz(G, communities)
st.plotly_chart(fig_communities, use_container_width=True)

st.markdown("---")

# Task 5: Influence Analysis
st.header("5. 💫 Influence: Information Spreaders")

st.markdown("""
The **most influential person** for spreading information is identified using betweenness centrality. 
This person acts as a bridge between different parts of the network and can efficiently spread 
information to many people.
""")

most_influential = metrics['most_influential']
influence_score = metrics['betweenness'][most_influential]
connections = G.degree(most_influential)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏆 Most Influential", most_influential)

with col2:
    st.metric("Betweenness Score", f"{influence_score:.3f}")

with col3:
    st.metric("Direct Connections", connections)

st.markdown(f"""
### Why is {most_influential} the most influential?

{most_influential} has the highest **betweenness centrality** score of {influence_score:.3f}, meaning:

1. **Bridge Position**: {most_influential} connects different groups in the network
2. **Information Flow**: Many shortest paths between other students pass through {most_influential}
3. **Strategic Location**: {most_influential} is positioned to control or facilitate information spread
4. **Reach**: {most_influential} can efficiently reach all {connections} direct friends and beyond

If you wanted to spread information quickly through this network, starting with {most_influential} 
would be the most effective strategy.
""")

# Show path examples
st.subheader(f"Example: Shortest Paths Through {most_influential}")

# Find some paths that go through the most influential person
sample_paths = []
nodes_list = list(G.nodes())
for i, source in enumerate(nodes_list[:3]):
    for target in nodes_list[i+3:i+4]:
        if source != target and source != most_influential and target != most_influential:
            try:
                path = nx.shortest_path(G, source, target)
                if most_influential in path:
                    sample_paths.append(f"{' → '.join(path)}")
            except:
                continue

if sample_paths:
    st.markdown("These paths demonstrate how information flows through the network:")
    for path in sample_paths[:3]:
        st.markdown(f"- `{path}`")

st.markdown("---")


# Data Ethics Note
st.info("""
**📌 Ethics Note:** This network represents hypothetical friendship data among college students. 
In real-world applications, social network data must be handled with care:
- Respect privacy and obtain informed consent
- Consider the implications of influence metrics on individuals
- Be mindful that network position doesn't define personal worth
- Avoid using network analysis for manipulation or exclusion
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem 0;'>
    <p><em>"In graph theory, every connection tells a story."</em></p>
</div>
""", unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging
# Set page configuration
st.set_page_config(page_title="India Data Visualization", layout='wide')

# Load data
df = pd.read_csv('india.csv')
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")
logging.info("logging")

# Main header
st.title("Look into India")

# Sidebar title and state selection
st.sidebar.title('India Data Visualization')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')
selected_state = st.sidebar.selectbox('Select a State', list_of_states)

# Primary and secondary parameter selection
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]), key='primary')
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]), key='secondary')

# Filters for threshold values
primary_threshold = st.sidebar.slider(f'Set minimum {primary}', min_value=float(df[primary].min()), max_value=float(df[primary].max()), value=float(df[primary].min()), key='primary_threshold')
secondary_threshold = st.sidebar.slider(f'Set minimum {secondary}', min_value=float(df[secondary].min()), max_value=float(df[secondary].max()), value=float(df[secondary].min()), key='secondary_threshold')

# Filter button
filter_data = st.sidebar.button('Filter Data', key='filter_data')

# Summary statistics
st.sidebar.markdown("## Summary Statistics")
st.sidebar.write(df.describe())

# Main application
if filter_data:
    # Filter data based on thresholds
    filtered_df = df[(df[primary] >= primary_threshold) & (df[secondary] >= secondary_threshold)]

    st.text('Size represents the primary parameter')
    st.text('Color represents the secondary parameter')

    if selected_state == 'Overall India':
        # Plot for India
        fig = px.scatter_mapbox(
            filtered_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4, size_max=35,
            mapbox_style="carto-positron", width=1200, height=700, hover_name='District'
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        #selected state
        state_df = filtered_df[filtered_df['State'] == selected_state]
        fig = px.scatter_mapbox(
            state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6, size_max=35,
            mapbox_style="carto-positron", width=1200, height=700, hover_name='District'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Additional insights
    st.markdown("## Additional Insights")

    # Bar chart for population distribution
    fig_bar = px.bar(
        filtered_df, x='District', y='Population', color='State',
        title='Population Distribution', labels={'Population': 'Population', 'District': 'District'}
    )
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.markdown("### Select filters and click 'Filter Data' to see the visualizations.")

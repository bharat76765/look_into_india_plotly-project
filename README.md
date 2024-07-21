# look_into_india_plotly-project
This Streamlit application provides an interactive visualization of various socio-economic parameters for different states and districts in India. The application allows users to explore data on population, literacy rates, internet usage, and more, using an intuitive and interactive interface.
![Screenshot 2024-07-18 122539](https://github.com/user-attachments/assets/cac9e951-b2dc-4adf-ae51-bafe002e6e0f)
![Screenshot 2024-07-18 122554](https://github.com/user-attachments/assets/2a829f0e-065a-41bc-9e01-77f93463f35c)

## Features

- **State and District Selection:** Choose any state or the entire country for analysis.
- **Primary and Secondary Parameters:** Select primary and secondary parameters to visualize on the map.
- **Threshold Filters:** Apply threshold filters to focus on specific ranges of data.
- **Summary Statistics:** View summary statistics of the dataset in the sidebar.
- **Interactive Maps:** Visualize data on scatter maps with size and color representing the selected parameters.
- **Additional Insights:** Bar charts for population distribution and more.

## Usage

1. **Select a State:** Use the sidebar to choose a specific state or "Overall India" for nationwide data.
2. **Select Parameters:** Choose the primary and secondary parameters you want to visualize.
3. **Set Thresholds:** Adjust the sliders to set minimum values for the primary and secondary parameters.
4. **Filter Data:** Click the "Filter Data" button to apply the filters and generate the visualizations.
5. **Explore Visualizations:** Interact with the scatter maps and bar charts to gain insights.

## Dataset

The application uses a dataset containing various socio-economic parameters for districts in India, including:

- State
- District
- Latitude
- Longitude
- District Code
- Population
- Households with Internet
- Sex Ratio
- Literacy Rate

## Example Usage

1. **State Selection:** Select "Overall India" to see data for the entire country.
2. **Primary Parameter:** Choose "Population" as the primary parameter.
3. **Secondary Parameter:** Choose "Literacy Rate" as the secondary parameter.
4. **Set Thresholds:** Adjust the sliders to filter data based on minimum population and literacy rate.
5. **Filter Data:** Click "Filter Data" to update the visualizations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Streamlit for providing the framework for this interactive application.
- Plotly for the visualization tools.
- The creators and maintainers of the dataset used in this application.

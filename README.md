# 🚀 NASA Exoplanet Data Pipeline and Dashboard

This project builds a complete data pipeline and interactive dashboard using the NASA Exoplanet Archive data. It is designed to showcase end-to-end data science skills, from data ingestion and cleaning to dashboard deployment, offering insights into exoplanet discoveries and their properties.

---

## Features

- Ingest live exoplanet data from NASA Exoplanet Archive.
- Clean and preprocess key planetary and stellar properties.
- Save the cleaned dataset for easy reuse in future analyses.
- Build an interactive **Streamlit** dashboard to visualize the data:
  - Filter by discovery method, confirmation status, radius, temperature, and more.
  - Visualize data using various plots: scatter, bar, histogram, bubble, pie, and heatmap.

---

## Project Structure

This project follows a structured pipeline for ingesting, cleaning, and visualizing exoplanet data.

```bash
├── dashboard_app.py          # Streamlit dashboard app to visualize the data
├── 1_data_ingestion.py       # Script to download the raw exoplanet data
├── 2_data_cleaning.py        # Script to clean and preprocess the raw data
├── raw_exoplanet_data.csv    # Raw data from NASA Exoplanet Archive
├── cleaned_exoplanet_data.csv # Cleaned and preprocessed data
├── requirements.txt          # Python dependencies for the project
└── README.md                 # Project documentation (this file)

---

## 🚀 Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/nasa-exoplanet-dashboard.git
cd nasa-exoplanet-dashboard

### 2. Create a Virtual Environment

It's a good practice to use a virtual environment to manage project dependencies. You can create one using:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use venv\Scripts\activate

### 3. Install Dependencies

Install all required libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt

### 4. Run the Project

Now you're ready to run the different components of the project:

#### Data Ingestion

To download the raw exoplanet data from the NASA Exoplanet Archive, run:

```bash
python data_ingestion.py
This will download the latest exoplanet data into a `.csv` file called `raw_exoplanet_data.csv`.

#### Data Cleaning

Next, clean and preprocess the raw data. Run the following:

```bash
python data_cleaning.py

This will clean the raw data and save the cleaned version as `cleaned_exoplanet_data.csv` for future analysis.

#### Streamlit Dashboard

Finally, you can run the interactive Streamlit dashboard to visualize the data:

```bash
streamlit run dashboard_app.py

The dashboard will open in your browser, where you can filter the data by various parameters (discovery method, confirmation status, radius, temperature, etc.) and view different visualizations (scatter plots, bar charts, histograms, etc.).

---

## Project Details

### 1. Data Ingestion (data_ingestion.py)

This script fetches the raw exoplanet data from the NASA Exoplanet Archive API or FTP. The data is saved as a `.csv` file (`raw_exoplanet_data.csv`) for further processing.

### 2. Data Cleaning (data_cleaning.py)

This script performs several cleaning steps, including:

- Removing rows with missing or erroneous data.
- Converting columns to the correct data types (e.g., numerical, categorical).
- Adding new features or calculations (e.g., exoplanet density, distance to Earth).

The cleaned data is saved as `cleaned_exoplanet_data.csv`.

### 3. Streamlit Dashboard (dashboard_app.py)

This file runs the Streamlit application, allowing users to interact with the cleaned data. The dashboard offers:

- **Interactive Filters**: Explore specific subsets of the data.
- **Visualizations**: Includes scatter plots, bar charts, histograms, pie charts, and more.
- **Real-time Updates**: Visualizations update as users adjust the filters.

---

## Requirements

The following Python packages are required for this project:

- **Streamlit**: For building the interactive web dashboard.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib**: For static plots and visualizations.
- **Seaborn**: For advanced visualizations and plot styling.

You can install the required packages using:

```bash
pip install -r requirements.txt

---

## Acknowledgments

- **NASA Exoplanet Archive**: For providing the raw data of exoplanet discoveries.
- **Streamlit**: For enabling rapid dashboard development.
- **Pandas, NumPy, Matplotlib, and Seaborn**: For data analysis and visualization tools.

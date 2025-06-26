import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("cleaned_exoplanet_data.csv")

st.set_page_config(page_title="NASA Exoplanet Dashboard", layout="wide")

st.title("🪐 NASA Exoplanet Explorer Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filter Exoplanets")

# Discovery Method Filter
methods = st.sidebar.multiselect("Discovery Method", options=sorted(df['disc_method'].dropna().unique()), default=df['disc_method'].dropna().unique())

# Planet Status Filter
status_map = {0: 'Candidate', 1: 'Confirmed'}
status_options = st.sidebar.multiselect("Planet Status", options=[0, 1], format_func=lambda x: status_map[x], default=[0, 1])

# Sliders for numerical filters
radius_range = st.sidebar.slider("Planet Radius (scaled)", float(df.pl_radius_rearth.min()), float(df.pl_radius_rearth.max()), (float(df.pl_radius_rearth.min()), float(df.pl_radius_rearth.max())))
orbper_range = st.sidebar.slider("Orbital Period (scaled)", float(df.pl_orbper.min()), float(df.pl_orbper.max()), (float(df.pl_orbper.min()), float(df.pl_orbper.max())))
temp_range = st.sidebar.slider("Equilibrium Temperature (K)", float(df.pl_eqt.min()), float(df.pl_eqt.max()), (float(df.pl_eqt.min()), float(df.pl_eqt.max())))
mass_range = st.sidebar.slider("Star Mass (Solar Masses)", float(df.st_mass.min()), float(df.st_mass.max()), (float(df.st_mass.min()), float(df.st_mass.max())))
age_range = st.sidebar.slider("Star Age (Gyr)", float(df.st_age.min()), float(df.st_age.max()), (float(df.st_age.min()), float(df.st_age.max())))

# Filter Data
filtered_df = df[
    (df['disc_method'].isin(methods)) &
    (df['Confirmed'].isin(status_options)) &
    (df['pl_radius_rearth'].between(*radius_range)) &
    (df['pl_orbper'].between(*orbper_range)) &
    (df['pl_eqt'].between(*temp_range)) &
    (df['st_mass'].between(*mass_range)) &
    (df['st_age'].between(*age_range))
]

# Summary Metrics
st.subheader("📊 Key Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Planets", filtered_df.shape[0])
col2.metric("Avg Radius", f"{filtered_df['pl_radius_rearth'].mean():.2f}")
col3.metric("Avg Temperature", f"{filtered_df['pl_eqt'].mean():.1f} K")
col4.metric("Discovery Range", f"{filtered_df['disc_year'].min()} - {filtered_df['disc_year'].max()}")

st.divider()

# Layout for Charts
st.header("📈 Data Visualizations")

# Scatter: Orbital Period vs Radius
st.subheader("Scatter: Orbital Period vs Planet Radius")
fig1 = px.scatter(
    filtered_df, x="pl_orbper", y="pl_radius_rearth",
    color="disc_method", hover_name="pl_name",
    labels={"pl_orbper": "Orbital Period", "pl_radius_rearth": "Planet Radius"},
    title="Orbital Period vs Planet Radius by Discovery Method"
)
st.plotly_chart(fig1, use_container_width=True)

# Bar Plot: Discoveries per Year
st.subheader("Bar Chart: Discoveries per Year")
fig2 = px.histogram(
    filtered_df, x="disc_year",
    title="Number of Planets Discovered per Year",
    nbins=30, color="disc_method"
)
st.plotly_chart(fig2, use_container_width=True)

# Histogram: Planet Radius
st.subheader("Histogram: Planet Radius Distribution")
fig3 = px.histogram(
    filtered_df, x="pl_radius_rearth",
    title="Distribution of Planet Radii"
)
st.plotly_chart(fig3, use_container_width=True)

# Histogram: Planet Temperature
st.subheader("Histogram: Equilibrium Temperature")
fig4 = px.histogram(
    filtered_df, x="pl_eqt",
    title="Exoplanet Temperature Distribution (K)"
)
st.plotly_chart(fig4, use_container_width=True)

# Bubble Chart: Period vs Temperature vs Radius
st.subheader("Bubble Chart: Period vs Temp vs Radius")
fig5 = px.scatter(
    filtered_df, x="pl_orbper", y="pl_eqt", size="pl_radius_rearth",
    color="disc_method", hover_name="pl_name",
    labels={"pl_orbper": "Orbital Period", "pl_eqt": "Temperature"},
    title="Orbital Period vs Temperature (Size = Radius)"
)
st.plotly_chart(fig5, use_container_width=True)

# Scatter: Star Mass vs Radius
st.subheader("Star Mass vs Planet Radius")
fig6 = px.scatter(
    filtered_df, x="st_mass", y="pl_radius_rearth", color="disc_method",
    title="Star Mass vs Planet Radius"
)
st.plotly_chart(fig6, use_container_width=True)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
corr = filtered_df[['pl_orbper', 'pl_radius_rearth', 'pl_eqt', 'st_mass', 'st_teff', 'st_rad', 'st_age']].corr()
fig7, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig7)

# Pie Chart: Discovery Methods
st.subheader("Pie Chart: Discovery Method Distribution")
method_counts = filtered_df['disc_method'].value_counts()
fig8 = px.pie(
    names=method_counts.index,
    values=method_counts.values,
    title="Discovery Method Distribution"
)
st.plotly_chart(fig8, use_container_width=True)

# Box Plot: Radius by Method
st.subheader("Box Plot: Planet Radius by Discovery Method")
fig9 = px.box(filtered_df, x="disc_method", y="pl_radius_rearth", title="Planet Radius by Discovery Method")
st.plotly_chart(fig9, use_container_width=True)

# Summary Table
st.subheader("🧾 Filtered Data Preview")
st.dataframe(filtered_df.head(20), use_container_width=True)
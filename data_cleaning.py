import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv("raw_exoplanet_data.csv")

# Select relevant columns for analysis
columns = [
    'pl_name', 'pl_orbper', 'pl_radj', 'disc_method', 'disc_year',
    'pl_orbeccen', 'pl_eqt', 'pl_controv_flag',
    'st_mass', 'st_teff', 'st_rad', 'st_lum', 'st_age'
]

df = df[columns]

# Rename for clarity
df.rename(columns={
    'pl_controv_flag': 'Confirmed',
    'pl_radj': 'pl_radius_rjup'  # keep Jupiter radius temporarily
}, inplace=True)

# Handle missing data
# Drop rows with essential nulls (e.g., planet name, radius)
df = df.dropna(subset=['pl_name', 'pl_radius_rjup', 'pl_orbper'])

# Fill numerical NaNs with column medians
num_cols = ['pl_orbeccen', 'pl_eqt', 'st_mass', 'st_teff', 'st_rad', 'st_lum', 'st_age']
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill categorical NaNs
df['disc_method'] = df['disc_method'].fillna('Unknown')
df['Confirmed'] = df['Confirmed'].fillna(0).astype(int)

# Fix types
df['disc_year'] = df['disc_year'].astype(int)
df['pl_orbper'] = pd.to_numeric(df['pl_orbper'], errors='coerce')
df['pl_radius_rjup'] = pd.to_numeric(df['pl_radius_rjup'], errors='coerce')

# Convert radius from Jupiter radii to Earth radii
df['pl_radius_rearth'] = df['pl_radius_rjup'] * 11.21

# Remove extreme outliers
df = df[df['pl_orbper'] < 1e4]
df = df[df['pl_radius_rearth'] < 100] # Jupiter ~11, so 100 Earth radii is a very generous cap

# Drop the original Jupiter radius column
df.drop(columns=['pl_radius_rjup'], inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

print("Data cleaned.")

# Save cleaned data
df.to_csv("cleaned_exoplanet_data.csv", index=False)
print("Cleaned data saved as cleaned_exoplanet_data.csv")
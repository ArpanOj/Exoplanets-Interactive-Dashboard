import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv("raw_exoplanet_data.csv")

# Select relevant columns for analysis
columns = [
    'pl_name', 'pl_orbper', 'pl_radius', 'pl_discmethod', 'pl_discyear',
    'pl_orbeccen', 'pl_eqt', 'pl_controvflag',
    'st_mass', 'st_teff', 'st_rad', 'st_lum', 'st_age'
]

df = df[columns]

# Rename for clarity
df.rename(columns={'pl_controvflag': 'Confirmed'}, inplace=True)

# Handle missing data
# Drop rows with essential nulls (e.g., planet name, radius)
df = df.dropna(subset=['pl_name', 'pl_radius', 'pl_orbper'])

# Fill numerical NaNs with column medians
num_cols = ['pl_orbeccen', 'pl_eqt', 'st_mass', 'st_teff', 'st_rad', 'st_lum', 'st_age']
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill categorical NaNs
df['pl_discmethod'] = df['pl_discmethod'].fillna('Unknown')
df['Confirmed'] = df['Confirmed'].fillna(0).astype(int)

# Fix types
df['pl_discyear'] = df['pl_discyear'].astype(int)
df['pl_orbper'] = pd.to_numeric(df['pl_orbper'], errors='coerce')
df['pl_radius'] = pd.to_numeric(df['pl_radius'], errors='coerce')

# Remove extreme outliers
df = df[df['pl_orbper'] < 1e4]
df = df[df['pl_radius'] < 50]

# Reset index
df.reset_index(drop=True, inplace=True)

print("Data cleaned.")

# Save cleaned data
df.to_csv("cleaned_exoplanet_data.csv", index=False)
print("Cleaned data saved as cleaned_exoplanet_data.csv")
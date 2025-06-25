import pandas as pd

# URL to download the confirmed planets table (you can switch to other tables as needed)
url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+pscomppars&format=csv"

# Read and save the raw data
df = pd.read_csv(url)
df.to_csv("raw_exoplanet_data.csv", index=False)

print("Data downloaded and saved as raw_exoplanet_data.csv")
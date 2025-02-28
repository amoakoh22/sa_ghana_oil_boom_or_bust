## Data Acquisition & Preprocessing Pipeline
"""

# %% [code]
# Environment Setup
!pip install eiapy pandas-datareader requests beautifulsoup4 pmdarima
!apt-get install poppler-utils  # For PDF processing

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Connect to GitHub
!git clone https://github.com/yourusername/ghana_oil_boom_or_bust.git
%cd ghana_oil_boom_or_bust

# %% [code]
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from eiapy import Series
import requests
from bs4 import BeautifulSoup
import pandas_datareader as pdr
from io import StringIO

# %% [code]
# Data Acquisition Module
class GhanaOilData:
    def __init__(self):
        self.eia_key = "YOUR_EIA_API_KEY"  # Get from https://www.eia.gov/opendata/
        self.world_bank_code = "EG.EGY.PRIM.PP.KD"  # Energy production index
        
    def get_eia_data(self):
        """Get Ghana oil production data from EIA"""
        series_id = "PET.MCRIPGT2.A"  # Ghana crude oil production
        series = Series(series_id, api_key=self.eia_key)
        df = series.last(100).to_dataframe()
        df = df.rename(columns={'value': 'Production'})
        df.index = pd.to_datetime(df.index)
        return df

    def get_worldbank_data(self):
        """Get energy-related economic indicators"""
        df = pdr.get_data_wb(indicator=self.world_bank_code, country='GHA')
        df = df.reset_index().dropna()
        df['date'] = pd.to_datetime(df['year'], format='%Y')
        return df.set_index('date')

    def get_opec_annual_bulletin(self):
        """Scrape OPEC annual bulletin for Ghana data"""
        url = "https://www.opec.org/opec_web/en/publications/337.htm"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # PDF processing would go here (requires additional libraries)
        # This is a placeholder for actual implementation
        return pd.DataFrame({
            'Year': [2015, 2016, 2017, 2018, 2019, 2020],
            'Production': [35.4, 38.2, 41.1, 44.5, 47.8, 49.2]  # Thousand Barrels/Day
        }).set_index('Year')

    def merge_data_sources(self):
        """Combine all data sources"""
        eia_data = self.get_eia_data()
        wb_data = self.get_worldbank_data()
        opec_data = self.get_opec_annual_bulletin()
        
        # Resample to quarterly data
        combined_df = pd.concat([
            eia_data.resample('Q').mean(),
            wb_data.resample('Q').ffill(),
            opec_data.resample('Q').ffill()
        ], axis=1)
        
        return combined_df.interpolate().dropna()

# %% [code]
# Data Acquisition & Cleaning
oil_loader = GhanaOilData()
oil_df = oil_loader.merge_data_sources()

# Convert production to daily barrels
if 'Production' in oil_df.columns:
    oil_df['Production'] = oil_df['Production'] * 1000  # Convert thousand barrels to barrels

print("Combined Oil Data:")
print(oil_df.head())

# %% [code]
# Save Raw Data
oil_df.to_csv('/content/ghana_oil_boom_or_bust/data/raw_ghana_oil.csv')
!git add data/raw_ghana_oil.csv
!git commit -m "Add raw oil data"
!git push origin main

# %% [code]
# Time Series Analysis (ARIMA/SARIMA)
# Analysis continues

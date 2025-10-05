import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- Step 1: Load both datasets ---
seattle = pd.read_csv('seattle_rain.csv', parse_dates=['DATE'])
nola = pd.read_csv('neworleans_rain.csv', parse_dates=['DATE'])

# --- Step 2: Clean and align ---
seattle = seattle.sort_values('DATE')
nola = nola.sort_values('DATE')

seattle = seattle.set_index('DATE')
nola = nola.set_index('DATE')

# Keep only precipitation column
seattle_prcp = seattle['PRCP']
nola_prcp = nola['PRCP']

# --- Step 3: Create comparable summaries ---
# Monthly totals
sea_monthly = seattle_prcp.resample('ME').sum()
nola_monthly = nola_prcp.resample('ME').sum()

# Monthly mean daily rainfall
sea_monthly_mean = seattle_prcp.resample('ME').mean()
nola_monthly_mean = nola_prcp.resample('ME').mean()

# Wet days per month (>0)
sea_wetdays = (seattle_prcp > 0).resample('ME').sum()
nola_wetdays = (nola_prcp > 0).resample('ME').sum()

# --- Step 4: Plots ---
plt.rcParams.update({'figure.dpi':150})
out_files = []

# 1. Daily precipitation comparison (smoothed)
fig = plt.figure(figsize=(10,3))
plt.plot(seattle_prcp.rolling(30).mean(), label='Seattle (30-day avg)')
plt.plot(nola_prcp.rolling(30).mean(), label='New Orleans (30-day avg)')
plt.title('Daily Precipitation: Seattle vs New Orleans (30-day moving average)')
plt.xlabel('Date'); plt.ylabel('Precipitation')
plt.legend()
plt.tight_layout()
fig.savefig('fig1_daily_precip_comparison.png', bbox_inches='tight')
plt.close(fig)
out_files.append('fig1_daily_precip_comparison.png')

# 2. Monthly total precipitation
fig = plt.figure(figsize=(10,3))
plt.plot(sea_monthly, label='Seattle')
plt.plot(nola_monthly, label='New Orleans')
plt.title('Monthly Total Precipitation (2018–2022)')
plt.xlabel('Month'); plt.ylabel('Total Precipitation')
plt.legend()
plt.tight_layout()
fig.savefig('fig2_monthly_total_comparison.png', bbox_inches='tight')
plt.close(fig)
out_files.append('fig2_monthly_total_comparison.png')

# 3. Distribution of daily rainfall (histogram)
fig = plt.figure(figsize=(6,3))
plt.hist(seattle_prcp.dropna(), bins=30, alpha=0.6, label='Seattle')
plt.hist(nola_prcp.dropna(), bins=30, alpha=0.6, label='New Orleans')
plt.yscale('log')
plt.title('Distribution of Daily Rainfall (log scale)')
plt.xlabel('Daily Precipitation'); plt.ylabel('Days (log scale)')
plt.legend()
plt.tight_layout()
fig.savefig('fig3_hist_comparison.png', bbox_inches='tight')
plt.close(fig)
out_files.append('fig3_hist_comparison.png')

# 4. Monthly wet days comparison
fig = plt.figure(figsize=(10,3))
plt.plot(sea_wetdays, label='Seattle')
plt.plot(nola_wetdays, label='New Orleans')
plt.title('Monthly Wet-Day Count (days with >0 precipitation)')
plt.xlabel('Month'); plt.ylabel('Wet Days per Month')
plt.legend()
plt.tight_layout()
fig.savefig('fig4_wetdays_comparison.png', bbox_inches='tight')
plt.close(fig)
out_files.append('fig4_wetdays_comparison.png')

# --- Step 5: Print some summary stats for your report ---
print("\n--- Summary Statistics ---")
print("Seattle mean daily precipitation:", round(seattle_prcp.mean(), 3))
print("New Orleans mean daily precipitation:", round(nola_prcp.mean(), 3))
print("Seattle avg wet days/month:", round(sea_wetdays.mean(), 1))
print("New Orleans avg wet days/month:", round(nola_wetdays.mean(), 1))
print("Seattle date range:", seattle.index.min().date(), "to", seattle.index.max().date())
print("New Orleans date range:", nola.index.min().date(), "to", nola.index.max().date())
print("\nSaved figures:", out_files)

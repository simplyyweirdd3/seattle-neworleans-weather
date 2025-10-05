# Seattle vs New Orleans: A Comparison of Rainfall Patterns (2018–2022)

## Project Overview
This project compares rainfall patterns in Seattle, WA, and New Orleans, LA, using daily precipitation data from 2018 to 2022.  
The goal is to describe how often it rains, how rainfall amounts differ between the two cities, and what seasonal patterns appear in each.  
Using simple statistical summaries and visualizations, the analysis highlights differences between Seattle’s frequent light rain and New Orleans’s heavier but less frequent rainfall.

## Data
The datasets used are daily precipitation records from weather stations located in:
- **Seattle, WA**
- **New Orleans, LA**

The data covers **January 1, 2018 – December 31, 2022** and contains daily precipitation values (PRCP) and related weather attributes.

> **Source:** [NOAA National Centers for Environmental Information (NCEI)](https://www.ncei.noaa.gov/)

Data files included:
- `Data/seattle_rain.csv`
- `Data/neworleans_rain.csv`

## Analysis
The main analyses were performed in:
- `Code/Weather_data.ipynb`

### Key Steps
1. Load and clean the daily precipitation data for both cities.
2. Compute 30-day moving averages for daily rainfall.
3. Aggregate monthly totals and count wet days per month.
4. Visualise comparisons between Seattle and New Orleans using four figures.

### Software and Libraries Used
- pandas  
- matplotlib  
- numpy  

(See `requirements.txt` for the complete list of dependencies.)

## Results
The results show clear contrasts between the two climates:
- **Seattle:** More rainy days but lighter rainfall amounts.  
- **New Orleans:** Fewer rainy days but heavier downpours, especially in late summer.

Figures generated and stored in the `Results` folder:
- `fig1_daily_precip_comparison.png`
- `fig2_monthly_total_comparison.png`
- `fig3_hist_comparison.png`
- `fig4_wetdays_comparison.png`

For a full written summary and interpretation, refer to:
- `Docs/Ruman Sidhu - Communicating the Result.pdf`

## Author
**Ruman Sidhu**  
Seattle University  

## License
This project is shared under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments
Data sourced from NOAA.  
Developed for the **DATA 5100: Communicate Weather** project at Seattle University.

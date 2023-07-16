import pandas as pd
import numpy as np
import datetime as dt

# Set the number of rows
num_rows = 100

# Generate random data for the KPIs
equipment_ids = np.random.randint(1, 11, num_rows)
product_ids = np.random.randint(1, 6, num_rows)
order_dates = pd.date_range(start='2022-01-01', periods=num_rows)
quantities = np.random.randint(10, 100, num_rows)
scrap_quantities = np.random.randint(0, 10, num_rows)
start_times = pd.to_datetime(pd.Series(np.random.randint(1, 24, num_rows)).astype(str) + ':00', format='%H:%M').dt.time
end_times = pd.to_datetime(pd.Series(np.random.randint(1, 24, num_rows)).astype(str) + ':00', format='%H:%M').dt.time

# Calculate the KPIs based on the generated data
oee = np.random.uniform(0.6, 0.9, num_rows)
production_yield = (quantities - scrap_quantities) / quantities
scrap_rate = scrap_quantities / quantities
cycle_time = pd.to_timedelta(np.abs(pd.to_datetime(end_times) - pd.to_datetime(start_times))).astype('timedelta') / 60

# Create the DataFrame
data = pd.DataFrame({
    'EquipmentID': equipment_ids,
    'ProductID': product_ids,
    'OrderDate': order_dates,
    'Quantity': quantities,
    'ScrapQuantity': scrap_quantities,
    'StartTime': start_times,
    'EndTime': end_times,
    'OEE': oee,
    'ProductionYield': production_yield,
    'ScrapRate': scrap_rate,
    'CycleTime': cycle_time
})

# Display the sample data
print(data)

data.to_csv('data/production_data')
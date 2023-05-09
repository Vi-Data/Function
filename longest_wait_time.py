import pandas as pd
import matplotlib.pyplot as plt

def read_file(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
    return df

def get_longest_wait_times_per_day(df):
    daily_max_wait_time = df.groupby('date')['wait_time'].max().reset_index()
    daily_max_wait_time_with_time = daily_max_wait_time.merge(df, on=['date', 'wait_time'], how='left')
    return daily_max_wait_time_with_time

def plot_longest_wait_times(daily_max_wait_time_with_time):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(daily_max_wait_time_with_time['date'], daily_max_wait_time_with_time['wait_time'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Longest Wait Time in Seconds')
    ax.set_title('Longest Wait Time per Day')
    plt.show()

# Read data from a CSV file
data_file_path = 'path/to/your/csv_file.csv'
df = read_file(data_file_path)

# Get the longest wait times for each day
daily_max_wait_time_with_time = get_longest_wait_times_per_day(df)

# Plot the longest wait times
plot_longest_wait_times(daily_max_wait_time_with_time)
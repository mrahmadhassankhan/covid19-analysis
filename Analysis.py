import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np


path = 'https://raw.githubusercontent.com/mrahmadhassankhan/covid19-analysis/main/Processed%20Data%20File/Final_File.csv'

df = pd.read_csv(path)

# Calculations with outliers

# Calculate affected people in rural and urban areas
df["Affected_Rural"] = df["cases"] * (df["Rural"] / df["Total"])
df["Affected_Urban"] = df["cases"] * (df["Urban"] / df["Total"])

total_affected_rural = df["Affected_Rural"].sum()
total_affected_urban = df["Affected_Urban"].sum()

print("Total affected in rural areas:", total_affected_rural)
print("Total affected in urban areas:", total_affected_urban)


median_rural = statistics.median(df["Affected_Rural"])
median_urban = statistics.median(df["Affected_Urban"])

mean_rural = statistics.mean(df["Affected_Rural"])
mean_urban = statistics.mean(df["Affected_Urban"])

mode_rural = statistics.mode(df["Affected_Rural"])
mode_urban = statistics.mode(df["Affected_Urban"])

range_rural = np.ptp(df["Affected_Rural"])  # Range
range_urban = np.ptp(df["Affected_Urban"])

variance_rural = np.var(df["Affected_Rural"])  # Variance
variance_urban = np.var(df["Affected_Urban"])

std_dev_rural = np.std(df["Affected_Rural"])  # Standard Deviation
std_dev_urban = np.std(df["Affected_Urban"])

iqr_rural = np.percentile(df["Affected_Rural"], 75) - np.percentile(df["Affected_Rural"], 25)  # Interquartile Range
iqr_urban = np.percentile(df["Affected_Urban"], 75) - np.percentile(df["Affected_Urban"], 25)

skewness_rural = df["Affected_Rural"].skew()
skewness_urban = df["Affected_Urban"].skew()

print("Median (Rural):", median_rural)
print("Median (Urban):", median_urban)
print("Mean (Rural):", mean_rural)
print("Mean (Urban):", mean_urban)
print("Mode (Rural):", mode_rural)
print("Mode (Urban):", mode_urban)
print("Range (Rural):", range_rural)
print("Range (Urban):", range_urban)
print("Variance (Rural):", variance_rural)
print("Variance (Urban):", variance_urban)
print("Standard Deviation (Rural):", std_dev_rural)
print("Standard Deviation (Urban):", std_dev_urban)
print("Interquartile Range (Rural):", iqr_rural)
print("Interquartile Range (Urban):", iqr_urban)
print("Skewness (Rural):", skewness_rural)
print("Skewness (Urban):", skewness_urban)




# After Removing Outliers

filtered_data_rural = df[df["Affected_Rural"] < 20000000]
filtered_data_urban = df[df["Affected_Urban"] < 9999999]

print("\n\nAfter Removing Outliers")

# Recalculate total affected people after removing outliers
total_affected_rural_filtered = filtered_data_rural["Affected_Rural"].sum()
total_affected_urban_filtered = filtered_data_urban["Affected_Urban"].sum()

print("Total affected in rural areas (filtered):", total_affected_rural_filtered)
print("Total affected in urban areas (filtered):", total_affected_urban_filtered)

median_rural = statistics.median(filtered_data_rural["Affected_Rural"])
median_urban = statistics.median(filtered_data_urban["Affected_Urban"])

mean_rural = statistics.mean(filtered_data_rural["Affected_Rural"])
mean_urban = statistics.mean(filtered_data_urban["Affected_Urban"])

mode_rural = statistics.mode(filtered_data_rural["Affected_Rural"])
mode_urban = statistics.mode(filtered_data_urban["Affected_Urban"])

range_rural = np.ptp(filtered_data_rural["Affected_Rural"])  # Range
range_urban = np.ptp(filtered_data_urban["Affected_Urban"])

variance_rural = np.var(filtered_data_rural["Affected_Rural"])  # Variance
variance_urban = np.var(filtered_data_urban["Affected_Urban"])

std_dev_rural = np.std(filtered_data_rural["Affected_Rural"])  # Standard Deviation
std_dev_urban = np.std(filtered_data_urban["Affected_Urban"])

iqr_rural = np.percentile(filtered_data_rural["Affected_Rural"], 75) - np.percentile(filtered_data_rural["Affected_Rural"], 25)  # Interquartile Range
iqr_urban = np.percentile(filtered_data_urban["Affected_Urban"], 75) - np.percentile(filtered_data_urban["Affected_Urban"], 25)

skewness_rural = filtered_data_rural["Affected_Rural"].skew()
skewness_urban = filtered_data_urban["Affected_Urban"].skew()

print("Median (Rural):", median_rural)
print("Median (Urban):", median_urban)
print("Mean (Rural):", mean_rural)
print("Mean (Urban):", mean_urban)
print("Mode (Rural):", mode_rural)
print("Mode (Urban):", mode_urban)
print("Range (Rural):", range_rural)
print("Range (Urban):", range_urban)
print("Variance (Rural):", variance_rural)
print("Variance (Urban):", variance_urban)
print("Standard Deviation (Rural):", std_dev_rural)
print("Standard Deviation (Urban):", std_dev_urban)
print("Interquartile Range (Rural):", iqr_rural)
print("Interquartile Range (Urban):", iqr_urban)
print("Skewness (Rural):", skewness_rural)
print("Skewness (Urban):", skewness_urban)

# Create a box plot for Rural
data_to_plot = [df["Affected_Rural"]]
labels = ['Rural']
plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=labels)
plt.xlabel("Area")
plt.ylabel("Affected People")
plt.title("Affected People in Rural(With Outliers)")
plt.show()


# After Removing the outliers
data_to_plot = [filtered_data_rural["Affected_Rural"]]
plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=['Rural'])
plt.xlabel("Area")
plt.ylabel("Affected People")
plt.title("Affected People in Rural (Filtered)")
plt.show()


# Create a box plot for urban 
data_to_plot = [df["Affected_Urban"]]
labels = ['Urban']
plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=labels)
plt.xlabel("Area")
plt.ylabel("Affected People")
plt.title("Affected People in Urban(With Outliers)")
plt.show()


#Removed Outliers
data_to_plot = [filtered_data_urban["Affected_Urban"]]
plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=['Urban'])
plt.xlabel("Area")
plt.ylabel("Affected People")
plt.title("Affected People in Urban (Filtered)")
plt.show()

# Below Plots are without outliers filtered data 

# Bar Plot
labels = ['Rural', 'Urban']
values = [filtered_data_rural["Affected_Rural"].sum(), filtered_data_urban["Affected_Urban"].sum()]
plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'orange'])
plt.xlabel("Area")
plt.ylabel("Total Affected People")
plt.title("Total Affected People in Rural and Urban Areas")
plt.show()

#Histogram for Rural
plt.figure(figsize=(8, 6))
plt.hist(filtered_data_rural["Affected_Rural"], bins=5, color='blue', edgecolor='black')
plt.xlabel("Affected People")
plt.ylabel("Frequency")
plt.title("Histogram of Affected People in Rural")
plt.show()

#Histogram for urban
plt.hist(filtered_data_urban["Affected_Urban"], bins=5, color='orange', edgecolor='black')
plt.xlabel("Affected People")
plt.ylabel("Frequency")
plt.title("Histogram of Affected People in Urban")
plt.show()



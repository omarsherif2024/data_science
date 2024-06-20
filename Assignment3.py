import pandas as pd

# Load the dataset
file_path = '/content/iris.xls'
iris_data = pd.read_excel(file_path)
# Display the columns in the dataset
iris_data.columns.tolist()
iris_data.head()

#Output
SL	SW	PL	PW	Classification
0	5.1	3.5	1.4	0.2	Iris-setosa
1	4.9	3.0	1.4	0.2	Iris-setosa
2	4.7	3.2	1.3	0.2	Iris-setosa
3	4.6	3.1	1.5	0.2	Iris-setosa
4	5.0	3.6	1.4	0.2	Iris-setosa


import pandas as pd
# Load the dataset
file_path = '/content/iris.xls'
iris_data= pd.read_excel(file_path)
#mean
iris_data.describe()


#Output
SL	SW	PL	PW
count	150.000000	150.000000	150.000000	150.000000
mean	5.843333	3.054000	3.758667	1.198667
std	0.828066	0.433594	1.764420	0.763161
min	4.300000	2.000000	1.000000	0.100000
25%	5.100000	2.800000	1.600000	0.300000
50%	5.800000	3.000000	4.350000	1.300000
75%	6.400000	3.300000	5.100000	1.800000
max	7.900000	4.400000	6.900000	2.500000


import pandas as pd
# Load the dataset
file_path = '/content/iris.xls'
iris_data= pd.read_excel(file_path)
#null value present in the dataset
null_values = iris_data.isnull().sum()
null_values

#Output
SL                0
SW                0
PL                0
PW                0
Classification    0
dtype: int64

#Visualization 1
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.scatter(iris_data['SL'], iris_data['SW'], c='blue')
plt.title('Scatter plot of SL vs SW')
plt.xlabel('SL')
plt.ylabel('SW')
plt.grid(True)
plt.show()

#Output
https://github.com/omarsherif2024/data_science/blob/main/Scatter_plot.png


#Visualization 2
plt.figure(figsize=(6, 4))
iris_data['SL'].plot(kind='box')
plt.title('Box plot of SL')
plt.ylabel('SL')
plt.grid(True)
plt.show()

#Outputhttps://github.com/omarsherif2024/data_science/blob/main/box_PL.png


#Visualization 3
plt.figure(figsize=(6, 4))
iris_data['PL'].plot(kind='hist', bins=5, alpha=0.7, color='green')
plt.title('Histogram of PL')
plt.xlabel('PL')
plt.grid(True)
plt.show()

#Outputhttps://github.com/omarsherif2024/data_science/blob/main/histogram_Plot.png

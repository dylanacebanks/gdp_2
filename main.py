import numpy as np
import matplotlib.pyplot as plt

uk_gdp_data = np.genfromtxt('data/united-kingdom-gdp-gross-domestic-product.csv', delimiter=',', skip_header=29, usecols=(1))
us_gdp_data = np.genfromtxt('data/united-states-gdp-gross-domestic-product.csv', delimiter=',', skip_header=29, usecols=(1))
ger_gdp_data = np.genfromtxt('data/germany-gdp-gross-domestic-product.csv', delimiter=',', skip_header=19, usecols=(1))

# print(uk_gdp_data)


sample_number = len(uk_gdp_data)
# print(sample_number)
array_dimensions = (sample_number, 3)
gdp_data = np.zeros(array_dimensions)
# print(gdp_data.shape)

gdp_data[:, 0] = uk_gdp_data
gdp_data[:, 1] = us_gdp_data
gdp_data[:, 2] = ger_gdp_data
# gdp_data = np.insert(gdp_data, 1, uk_gdp_data , axis=1)
print(gdp_data)

#gdp_data = np.add(gdp_data, us_gdp_data, ger_gdp_dat)

years = np.arange(1971, 2021, 1)

plt.figure(1)

plt.plot(years, gdp_data[:, 0], color='red', label='U.K.')
#plt.plot(years, gdp_data[:, 1], color='green', label='U.S.')
plt.plot(years, gdp_data[:, 2], color='blue', label='Germany')
plt.legend(title='Countries')
plt.title('GDP by country')
plt.xlabel('Years')
plt.ylabel('USD (Billions)')

plt.show()

uk_gdp_per_capita_data = np.genfromtxt('data/united-kingdom-gdp-gross-domestic-product.csv', delimiter=',', skip_header=29, usecols=(2))
us_gdp_per_capita_data = np.genfromtxt('data/united-states-gdp-gross-domestic-product.csv', delimiter=',', skip_header=29, usecols=(2))
ger_gdp_per_capita_data = np.genfromtxt('data/germany-gdp-gross-domestic-product.csv', delimiter=',', skip_header=19, usecols=(2))

# print(uk_gdp_data)
sample_number = len(uk_gdp_data)
# print(sample_number)
array_dimensions = (sample_number, 3)
gdp_data = np.zeros(array_dimensions)
# print(gdp_data.shape)

gdp_data[:, 0] = uk_gdp_per_capita_data
gdp_data[:, 1] = us_gdp_per_capita_data
gdp_data[:, 2] = ger_gdp_per_capita_data
# gdp_data = np.insert(gdp_data, 1, uk_gdp_data , axis=1)
print(gdp_data)

#gdp_data = np.add(gdp_data, us_gdp_data, ger_gdp_dat)


plt.figure(2)

plt.plot(years, gdp_data[:, 0], color='red', label='U.K.')
#plt.plot(years, gdp_data[:, 1], color='green', label='U.S.')
plt.plot(years, gdp_data[:, 2], color='blue', label='Germany')
plt.legend(title='Countries')
plt.title('GDP per capita by country')
plt.xlabel('Years')
plt.ylabel('USD (Billions)')

plt.show()

import matplotlib.pyplot as plt
from numpy import corrcoef
import numpy as np
from scipy.stats import linregress

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,2018]
real_gdp_hungary = [7900, 8240, 8660, 9040, 9490, 9910, 10330, 10370, 10500, 9810, 9900, 10110, 10010, 10230, 10690, 11130, 11410, 11930, 12560]
unemployment_rate_hungary = [6.3, 5.6, 5.6, 5.8,  6.1, 7.2, 7.5, 7.4, 7.8, 10, 11.2, 11, 11, 10.2, 7.7, 6.8,  5.1, 4.2, 3.7]

plt.style.use('ggplot')

plt.xlabel('Unemployment rate')
plt.ylabel('Real GDP per capita')
plt.title('Correlation between unemployment rate  & real GDP per capita')

plt.scatter(unemployment_rate_hungary, real_gdp_hungary)
correlation_coefficient = corrcoef(unemployment_rate_hungary, real_gdp_hungary)[1, 0]

mean_real_gdp_hun = np.mean(real_gdp_hungary)

linear_regression = linregress(unemployment_rate_hungary, real_gdp_hungary)

print(correlation_coefficient)
print(linear_regression)
print(mean_real_gdp_hun)

plt.show()

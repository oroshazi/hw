import matplotlib.pyplot as plt

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,2018]
real_gdp_hungary = [7900, 8240, 8660, 9040, 9490, 9910, 10330, 10370, 10500, 9810, 9900, 10110, 10010, 10230, 10690, 11130, 11410, 11930, 12560]
plt.plot(year, real_gdp_hungary, color='g')

plt.xticks(year, rotation=75)


plt.xlabel('Year')
plt.ylabel('GDP per capita ')
plt.title('Real GDP per capita in EUR - Hungary (2000 - 2018)')

plt.show()

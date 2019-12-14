import matplotlib.pyplot as plt

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,2018]
unemployment_rate_hungary  = [6.3, 5.6, 5.6, 5.8,  6.1, 7.2, 7.5, 7.4, 7.8, 10, 11.2, 11, 11, 10.2, 7.7, 6.8,  5.1, 4.2, 3.7]
plt.plot(year, unemployment_rate_hungary, color='g')

plt.xticks(year, rotation=75)


plt.xlabel('Year')
plt.ylabel('Unemployment rate')
plt.title('Unemployment rate - Hungary (2000 - 2018)')

plt.show()

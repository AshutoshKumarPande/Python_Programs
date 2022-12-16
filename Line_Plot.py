import matplotlib.pyplot as plt

year=[2001,2002,2003,2004,2005,2006,2007,2008,2009]
unemply=[9,8,5,2,7,3,1,6,4]

plt.plot(year,unemply,marker='o',linestyle=':')
plt.xlabel("year")
plt.ylabel("Unemployment rate")
plt.title("Year vs unemployment rate")
plt.show()

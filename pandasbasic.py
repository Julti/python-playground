import pandas as pd
pd.plotting.register_matplotlib_converters()
import seaborn as sns
import matplotlib.pyplot as plt
fileroute = "./covid19.csv"
data=pd.read_csv(fileroute)
print(data.describe())
#plt.figure(figsize=(16,6))
#sns.regplot(x='Date',y='Cum',data=data,fit_reg=False)
#plt.show()
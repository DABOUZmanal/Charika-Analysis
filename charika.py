# declare the libraries
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

# Create a sample dataset
days=np.arange(1,11)
sales=np.random.randint(50,150,size=10)
cost=np.random.randint(30,100,size=10)
income=sales-cost

# Create a DataFrame
data={
    'Days': days,
    'Sales': sales,
    'Cost': cost,
    'Income': income
}
# Create a DataFrame
df=pd.DataFrame(data)
plt.figure(figsize=(10,6))
plt.plot(df['Days'], df['Sales'], marker='o',linestyle='-', label='Sales',color='blue')
plt.plot(df['Days'], df['Cost'], marker='s',linestyle='--', label='Cost',color='red')
plt.plot(df['Days'], df['Income'], marker='^',linestyle='-.', label='Income',color='green')
# analyse the data
plt.title('Company Analysis')
plt.xlabel('Days')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid()
plt.show()    
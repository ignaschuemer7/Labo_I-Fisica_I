import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('pr1.mplstyle')

df = pd.read_csv('leaves.csv')

print(df)


df['weight_error'] = df['weigth']

print(df)

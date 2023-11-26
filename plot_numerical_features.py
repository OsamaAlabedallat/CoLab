def plotNumData(dataFrame):
  import numpy as np
  import matplotlib.pyplot as plt
  
  # Sample data creation
  np.random.seed(0)
  
  # Plotting Histogram with KDE and Boxplot for each numerical feature
  fig, axes = plt.subplots(len(dataFrame.columns), 2, figsize=(12, 5 * len(dataFrame.columns)))
  
  for i, col in enumerate(dataFrame.columns):
      # Histogram with KDE
      dataFrame[col].plot(kind='hist', density=True, ax=axes[i, 0], bins=20, alpha=0.5, color='blue')
      dataFrame[col].plot(kind='kde', ax=axes[i, 0], color='red')
      axes[i, 0].set_title(f'{col} - Histogram with KDE')
  
      # Boxplot
      dataFrame.boxplot(column=col, ax=axes[i, 1])
      axes[i, 1].set_title(f'{col} - Boxplot')
  
  plt.tight_layout()
  plt.show()
  

def heatPlot(dataFrame):
  import seaborn as sns
  corr = dataFrame.corr()  
  # Plot heatmap
  plt.figure(figsize=(10, 8))
  sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
  plt.title('Heatmap of Numerical Features')
  plt.show()
  

def scatterFeaturs(dataFram):
  n_features = dataFram.shape[1] - 1  # excluding the first column
  fig, axs = plt.subplots(n_features, figsize=(10, n_features * 5))
  
  for i, feature in enumerate(dataFram.columns[:-1]):  # excluding the first column
      axs[i].scatter(dataFram[feature], dataFram['price'])
      axs[i].set_xlabel(feature)
      axs[i].set_ylabel('Price')
      axs[i].set_title(f'Scatter plot of {feature} vs Price')
  
  plt.tight_layout()
  plt.show()

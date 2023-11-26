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

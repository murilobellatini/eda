from scipy.stats import ttest_ind
import numpy as np


def compare2groups(arr1, arr2, sample_size=150, alpha=0.05):
  """
  Compara se dois grupos de dados tem origem da mesma distribuição.
  Método: Pearson-value (p-value)
  """
  arr1_sampled = np.random.choice(arr1, sample_size)
  arr2_sampled = np.random.choice(arr2, sample_size)
  stat, p = ttest_ind(arr1_sampled, arr2_sampled)
  
  print(f't-statistic: {stat}\np-value: {p}')

  if p > alpha:
    print('Same Distribution (null hypothesis not rejected)')
  else:
    print('Different Distribution (null hypothesis rejected)')

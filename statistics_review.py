"""Module containing basic statistics."""
import numpy as np

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print("mean:", np.mean(data))                               # 23.0
print("median:", np.median(data))                           # 22.0
print("50th percentile (median):", np.percentile(data, 50)) # 22.0
print("25th percentile:", np.percentile(data, 25))          # 18.0
print("75th percentile:", np.percentile(data, 75))          # 29.0
print("standard deviation:", np.std(data))                  # 6.342099196813483
print("variance:", np.var(data))                            # 40.22222222222222

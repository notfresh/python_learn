import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc("font",family='Adobe Heiti Std')

frame = pd.DataFrame(np.arange(20).reshape(4,5)) # 4行5列
frame2 = frame.copy()
len = len(frame[0])
frame2.columns=[0,1,2,3,4]

for i in range(1,len):
    for j in range(5):
        frame2[j][i] = frame2[j][i] + frame2[j][i-1]

print(frame)
print(frame2)





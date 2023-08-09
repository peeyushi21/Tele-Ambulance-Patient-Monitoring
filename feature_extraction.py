import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import neurokit2 as nk
import wfdb
from pathlib import Path
import scipy.io.wavfile
import scipy.signal
#import pyecg
#from pyecg import ECGRecord



#path = Path("""C:/Users/Peeyushi/Desktop/ICG/sgpgi/nurokt/database/congestive-heart-failure-rr-interval-database-1.0.0/chf201""")
#fileToOpen = datadir/"practice.txt"


#path = "C:/Users/Peeyushi/Desktop/ICG/sgpgi/nurokt/database/congestive-heart-failure-rr-interval-database-1.0.0/chf201" 

#record = ECGRecord.from_ishine(path)
record=wfdb.rdrecord(r"C:\\Users\\Peeyushi\Desktop\sgpgi\\nurokt\database\\mit-bih-arrhythmia-database-1.0.0\\mit-bih-arrhythmia-database-1.0.0\\102",channels=[1])
#time = record.time
#signal = record.get_lead(1)
#print(signal.1)


signal=record.p_signal
#plt.plot(signal)
#plt.show()
k=len(signal)
new_signal=[0]*k
for i in range(k):
  new_signal[i]=signal[i][0]


x=[0]*k
for i in range(k):
  x[i]=i


b, a = scipy.signal.butter(3, 0.06)
filtered = scipy.signal.filtfilt(b,a,new_signal)
'''
plt.plot(filtered)
plt.title('102')
plt.show()

final_data=nk.ecg_process(filtered, sampling_rate=500, method='neurokit')
df=final_data[0]





from scipy.fft import dct, idct
y = dct(filtered, norm='ortho')
window = np.zeros(10000)
window[:10000] = 1
yr = idct(y*window, norm='ortho')
#sum(abs(x-yr)**2) / sum(abs(x)**2)

#plt.plot(x,yr,x, filtered)
#plt.plot(x, yr)
window = np.zeros(10000)
window[:15] = 1
yr = idct(y*window, norm='ortho')
#sum(abs(filtered-yr)**2) / sum(abs(filtered)**2)

#plt.plot(x, yr)
#plt.legend(['x', '$x_{20}$', '$x_{15}$'])

#plt.show()







from scipy.fft import dct
y = dct(filtered, norm='ortho')
#plt.plot(x,y,x,filtered)
#plt.show()

p=df['ECG_P_Peaks']
q=df['ECG_Q_Peaks']
r=df['ECG_R_Peaks']
s=df['ECG_S_Peaks']
t=df['ECG_T_Peaks']


count_p=0
for i in range(k):
  if p[i]==1:
    count_p=count_p+1

x_p=[0]*count_p
z_p=[0]*count_p
t_p=[0]*count_p
var=0

for i in range(k):
  if p[i]==1:
    x_p[var]=i
    z_p[var]=filtered[i]
    t_p[var]=record.get_elapsed_time(i)
    var=var+1


count_q=0
for i in range(k):
  if q[i]==1:
    count_q=count_q+1

x_q=[0]*count_q
z_q=[0]*count_q
t_q=[0]*count_q
var=0

for i in range(k):
  if q[i]==1:
    x_q[var]=i
    z_q[var]=filtered[i]
    t_q[var]=record.get_elapsed_time(i)
    var=var+1


count_r=0
for i in range(k):
  if r[i]==1:
    count_r=count_r+1

x_r=[0]*count_r
z_r=[0]*count_r
t_r=[0]*count_r
var=0

for i in range(k):
  if r[i]==1:
    x_r[var]=i
    z_r[var]=filtered[i]
    t_r[var]=record.get_elapsed_time(i)
    var=var+1


count_s=0
for i in range(k):
  if s[i]==1:
    count_s=count_s+1

x_s=[0]*count_s
z_s=[0]*count_s
t_s=[0]*count_s
var=0

for i in range(k):
  if s[i]==1:
    x_s[var]=i
    z_s[var]=filtered[i]
    t_s[var]=record.get_elapsed_time(i)
    var=var+1


count_t=0
for i in range(k):
  if t[i]==1:
    count_t=count_t+1

x_t=[0]*count_t
z_t=[0]*count_t
t_t=[0]*count_t
var=0

for i in range(k):
  if t[i]==1:
    x_t[var]=i
    z_t[var]=filtered[i]
    t_t[var]=record.get_elapsed_time(i)
    var=var+1
'''

widths = np.arange(1, 31)
cwtmatr = scipy.signal.cwt(filtered, scipy.signal.ricker, widths)

plt.plot(x,cwtmatr[29],x,filtered)
plt.show()
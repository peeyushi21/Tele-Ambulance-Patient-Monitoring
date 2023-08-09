import pywt as pywt
import wfdb as wfdb
import matplotlib.pyplot as plt
import scipy
import numpy as np
import sklearn as sk
import pandas as pd

record = wfdb.rdrecord(r"C:\Users\Peeyushi\Documents\MATLAB\database\mitbih\107",channels=[1]) 

signal=record.p_signal
#plt.plot(signal)
#plt.show()
k=len(signal)
new_signal=[0]*k
for i in range(k):
  new_signal[i]=signal[i][0]

b,a=scipy.signal.butter(3,0.06)
filtered = scipy.signal.filtfilt(b,a,new_signal)
#plt.plot(filtered)
#plt.show()




'''
#custom wavelet
dec_lo=[0.415089569387100,0.523558719560028,0.181437465474450,-0.145055968585562]
dec_hi=[0.145055968585562,0.181437465474450,-0.523558719560028,0.415089569387100]
rec_lo=[-0.290111937171124,0.362874930948901,1.04711743912006,0.830179138774201]
rec_hi=[0.830179138774201,-1.04711743912006,0.362874930948901,0.290111937171124]

dec_lo=[0.327315023462437,0.544377790846505	,0.270717030315986,-0.104521500473480,-0.0952621880747085,0.0573310543015937]
dec_hi=[-0.0573310543015937,-0.0952621880747085,0.104521500473480,0.270717030315986,-0.544377790846505,0.327315023462437]
rec_lo=[0.114662108603187,-0.190524376149417,-0.209043000946961,0.541434060631972,1.08875558169301,0.654630046924874]
rec_hi=[0.654630046924874,-1.08875558169301,0.541434060631972,0.209043000946961,-0.190524376149417,-0.114662108603187]

dec_lo=[0.243513106701266,0.569266880986490,0.320177213996611,-0.0965091624767850,-0.0636901597100752,0.0272421205024935]
dec_hi=[-0.0272421205024935,-0.0636901597100752,0.0965091624767850,0.320177213996611,-0.569266880986490,0.243513106701266]
rec_lo=[0.0544842410049869,-0.127380319420150,-0.193018324953570,0.640354427993223,1.13853376197298,0.487026213402532]
rec_hi=[0.487026213402532,-1.13853376197298,0.640354427993223,0.193018324953570,-0.127380319420150,-0.0544842410049869]

dec_lo=[0.18556516,0.68232366,0.68232366,0.18556516]
dec_hi=[-0.18556516,0.68232366,-0.68232366,0.18556516]
rec_lo=[0.18556516,0.68232366,0.68232366,0.18556516]
rec_hi=[-0.18556516,0.68232366,-0.68232366,0.18556516]

dec_lo=[0.243513106701266,0.569266880986490,0.320177213996611,-0.0965091624767850,-0.0636901597100752,0.0272421205024935]
dec_hi=[-0.0272421205024935,-0.0636901597100752,0.0965091624767850,0.320177213996611,-0.569266880986490,0.243513106701266]
rec_lo=[0.0544842410049869,-0.127380319420150,-0.193018324953570,0.640354427993223,1.13853376197298,0.487026213402532]
rec_hi=[0.487026213402532,-1.13853376197298,0.640354427993223,0.193018324953570,-0.127380319420150,-0.0544842410049869]
'''


dec_lo=[0.01415185,0.37682154,0.37682154,0.01415185]
dec_hi=[0.01415185, 0.37682154,0.37682154,0.01415185]
rec_lo=[0.01415185,0.37682154,0.37682154,0.01415185]
rec_hi=[0.01415185,0.37682154,0.37682154,0.01415185]
wavelet = pywt.Wavelet('db1')
filter_bank = [dec_lo, dec_hi, rec_lo, rec_hi]
myWavelet = pywt.Wavelet(name="myWavelet", filter_bank=filter_bank)

coeffs=pywt.wavedec(filtered, 'db1')

c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20=coeffs


#making all the values of c20,c19,c18=0
#c18_list=[0]*325002
#c18_test=np.asarray(c18_list)
c20_list=[0]*325000
c20_test=np.asarray(c20_list)
c19_list=[0]*162500
c19_test=np.asarray(c19_list)
c18_list=[0]*81250
c18_test=np.asarray(c18_list)
c17_list=[0]*40625
c17_test=np.asarray(c17_list)
c16_list=[0]*20313
c16_test=np.asarray(c16_list)

#applying hresholding to the rest of the arrays
c20_new=pywt.threshold(c20, 1, mode='soft', substitute=0)
c19_new=pywt.threshold(c19, 0.5, mode='soft', substitute=0)
c18_new=pywt.threshold(c18, 0.00075, mode='soft', substitute=0)
c17_new=pywt.threshold(c17, 1, mode='soft', substitute=0)
c16_new=pywt.threshold(c16, 0.5, mode='soft', substitute=0)
c15_new=pywt.threshold(c15, 0.25, mode='soft', substitute=0)
c14_new=pywt.threshold(c14, 0.2, mode='soft', substitute=0)
c13_new=pywt.threshold(c13, 0.5, mode='soft', substitute=0)
c12_new=pywt.threshold(c12, 3, mode='soft', substitute=0)
c11_new=pywt.threshold(c11, 5, mode='soft', substitute=0)
c10_new=pywt.threshold(c10, 10, mode='soft', substitute=0)
c9_new=pywt.threshold(c9, 0.00075, mode='soft', substitute=0)
c8_new=pywt.threshold(c8, 0.00075, mode='soft', substitute=0)
c7_new=pywt.threshold(c7, 0.00075, mode='soft', substitute=0)
c6_new=pywt.threshold(c6, 0.00075, mode='soft', substitute=0)
c5_new=pywt.threshold(c5, 0.00075, mode='soft', substitute=0)
c4_new=pywt.threshold(c4, 0.00075, mode='soft', substitute=0)
new_coeffs=c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13_new,c14_new,c15_new,c16_test,c17_test,c18_test,c19_test,c20_test


rec=pywt.waverec(new_coeffs,'db1')
filtered_rec = scipy.signal.filtfilt(b,a,rec)

y = pd.Series(filtered_rec)
x = pd.Series(filtered)
correlation = y.corr(x)
print(correlation)

'''
print(len(c20))
print(len(c19))
print(len(c18))
print(len(c17))
'''
plt.plot(filtered)
plt.plot(filtered_rec)
plt.show()

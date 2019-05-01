import os
import tempfile
import numpy as np; np.set_printoptions(threshold='nan')
import digital_rf as drf
import matplotlib.pyplot as plt
import scipy.signal as ss
import timeit

# Read in data
dro=drf.DigitalRFReader('Dropbox (MIT)/data/crabneb_sixjuly_updated/')
start,end=dro.get_bounds('ch0')
bins=500                # number of bins
n=round(670056.0/bins)  # Number of samples for 1 bin, used period of 33.50285
m=3600 # amount of times for the for loop to run it
#-------------------------
# Loading in data in desired amount
data=[]
sum_d=[]
for i in range(m): # m*n = 218181600
    da=dro.read_vector(start+i*n,n,'ch0')
    data.append(da)
    # Now sum data
    sum_d0=sum(data[i])
    sum_d.append(sum_d0) # this is a list of the sum data
marray=np.asarray(sum_d)
#---------------------------------
# Plotting all of the bins together
sli=[]
for j in range(m/bins):
    sl=marray[0+j*bins:bins+j*bins]
    sli.append(sl)
    #print sl
    plt.plot(sl)
    #plt.plot(sli)
    # I have to add the respective bins to each other: 1st bin of first array + 1t bin of 2nd array + etc
plt.xlabel('# of bins')
#plt.savefig('bins.pdf')
#---------------------------------------------
# Folding Process
sl_arr=np.asarray(sli)
plt_sl=[]
for i in range(sl_arr.shape[1]): #sl_arr.shape[1]
    for j in range(sl_arr.shape[0]): #327
        sum_fold=np.sum(sl_arr[:,i])
    plt_sl.append(sum_fold)
# Now plt_sl has 11 bins with each bin representing the sum of all of it.
er=np.asarray(plt_sl)#print er
#plt.plot(er)

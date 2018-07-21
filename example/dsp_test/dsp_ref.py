from __future__ import print_function
import math
import numpy
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy.fftpack import fft,ifft,dct 
import matplotlib.pyplot as plt
import time



N=64
#sin cos 
print("sin(0.1)=%f"% math.sin(0.1))
print("cos(2.0)=%f"% math.cos(2.0))
#------------------------------------------------
# FIR.
#------------------------------------------------
x=[1.1016856340840009,1.3819116564898124,1.2902960763808005,1.0566626343732346,
    0.9442254510513154,0.9579868821695956,1.046306253339488,1.2410366852938386,
    1.4436282176750759,1.3874515506551908,1.0378805602935988,0.7756155443385301,
    0.9178050511383941,1.2537702552749763,1.3426204627941956,1.117610065929717,
    0.8800604905211858,0.8012517778630224,0.7821389128510301,0.7711632039505969,
    0.8501510692896972,0.951564312477108,0.8436661347816815,0.5268377902750552,
    0.33441324855963317,0.4608704807237677,0.660838911589431,0.6315802275119023,
    0.4503064294285132,0.3690546542314113,0.3830365542353578,0.32286699253190193,
    0.23477111445056748,0.30990336758188164,0.4885556520187167,0.49487230610275945,
    0.29017088466245566,0.15479252877059746,0.24169920785325388,0.3670607943691402,
    0.36701157780354643,0.3520189111198753,0.42271529556318366,0.4225052367712395,
    0.23092439222513883,0.06926710273608785,0.1994021343386783,0.4723172130423151,
    0.5111771910438687,0.2622959422441363,0.03179207010391415,0.00435686084990973,
    0.060746245121383116,0.09208186182560787,0.14769880330463428,0.18278609616995745,
    0.004175541124054452,-0.36016119316009115,-0.5430364808518742,-0.33032288155563755,
    -0.031070289589745434,-0.0789812885502211,-0.444599870929681,-0.7399276026332652]

taps=[-0.00028361,-0.00075393,-0.00109268,-0.0006769,0.00102914,0.00391172,\
  0.00678037,0.0074884,0.00382395,-0.00503141,-0.0171363,-0.02737452,\
 -0.02859017,-0.01418401,0.01873238,0.0670341,0.12139937,0.16869521,\
  0.19622892,0.19622892,0.16869521,0.12139937,0.0670341,0.01873238,\
 -0.01418401,-0.02859017,-0.0273745,-0.0171363,-0.00503141,0.00382395,\
  0.0074884,0.00678037,0.00391172,0.00102914,-0.0006769,-0.00109268,\
 -0.00075393,-0.00028361]

# Use lfilter to filter x with the FIR filter.

filtered_x = lfilter(taps, 1.0, x)
print("FIR Result:",filtered_x,end="\r\n**************\r\n")

#------------------------------------------------
# FFT
#------------------------------------------------
ffted_x=numpy.fft.rfft(x)
print("RFFT Length:",len(ffted_x))
print("FFT Result:",ffted_x,end="\r\n**************\r\n")
print("Complex Magnitude Module:",numpy.abs(ffted_x),end="\r\n***************\r\n")
#------------------------------------------------
# IFFT
#------------------------------------------------
iffted_x=numpy.fft.irfft(ffted_x)
print("IFFT Result:",iffted_x,end="\r\n**************\r\n")
#------------------------------------------------
# DCT2 and DCT4
#------------------------------------------------
dcted_x=dct(x)
print("DCT2 Result:",dcted_x,end="\r\n**************\r\n")
#caculate dct4 from dct2 
#y4(k)=y2(k)-y4(k-1)
#y4(-1)=y4(0)
dct4ed_x=[None]*64
dct4ed_x[0]=dcted_x[0]/2
for i in range(1,N):
    dct4ed_x[i]=dcted_x[i]-dct4ed_x[i-1]
print("DCT4 Result:",dct4ed_x,end="\r\n**************\r\n")
#------------------------------------------------
# Martix
#------------------------------------------------
m= numpy.matrix('1 2; 3 4')
print("Source Martix:",m,end="\r\n**************\r\n")
print("Inverse Martix:",m.getI(),end="\r\n**************\r\n")
print("Transpose Martix:",m.T,end="\r\n**************\r\n")
# noinspection PyUnresolvedReferences
import numpy as np
import matplotlib.pyplot as plt

## Functions
def Mod(Numbersymbols,modulation):
    if modulation=="BPSK":
        n=Numbersymbols
        x=np.divide(np.random.randint(0, 2, n)*2-1,np.sqrt(2))
    elif modulation=="QPSK":
        n=Numbersymbols*2
        x_aux = np.divide(np.random.randint(0, 2, n)*2-1, np.sqrt(2))
        x=x_aux[0:int(x_aux.size/2)]+1j*x_aux[int(x_aux.size/2):]
    elif modulation=="16-QAM":
        n=Numbersymbols*2
        x_aux = np.divide(np.random.randint(1, 5, n)*2-5, np.sqrt(10))
        x = x_aux[0:int(x_aux.size / 2)] + 1j * x_aux[int(x_aux.size / 2):]
    elif modulation=="64-QAM":
        n = Numbersymbols * 2
        x_aux = np.divide(np.random.randint(1, 9, n)*2-9, np.sqrt(42))
        x = x_aux[0:int(x_aux.size / 2)] + 1j * x_aux[int(x_aux.size / 2):]
    return x

def SubMap(x,submap,IFFTlen,FFTlen):
    Q = IFFTlen // FFTlen
    if submap=="Interleaved":
        y = np.zeros(IFFTlen, dtype=complex)
        y[0::Q] = x
    return y

def Upsam(x,os):
    y = np.zeros(len(x)*os, dtype=complex)
    y[0::os] = x
    return y

def RaisedC(ts,Nos,alpha,Trunc):
    Ts = 1
    Nos = os
    T = 1
    t1 = np.arange(-Trunc * Ts, -Ts / Nos + Ts / Nos, Ts / Nos)
    t2 = np.arange(Ts / Nos, Trunc * Ts + Ts / Nos, Ts / Nos)
    t = np.hstack((t1, 0, t2))
    v = np.empty(len(t))
    for i in range(0, len(t)):
        if np.abs(np.abs(alpha * t[i] / T) - 0.5) > 1e-5:
            v[i] = np.sinc(t[i] / T) * np.cos(np.pi * alpha * t[i] / T) / (1 - np.power((2 * alpha * t[i] / T), 2))
        else:
            v[i] = np.sinc(t[i] / T) * np.pi * np.sin(np.pi * alpha * t[i] / T) / (8 * alpha * t[i] / T)
    return v

## Parameters
#Modulation
mod="QPSK"
#Number of bits
nbits=100
#Length of FFT
FFTlen=100
#Subcarrier-mapping
submapC="Interleaved"
#Length of IFFT
IFFTlen=300
#Length of CP
CP=20
#Up-sampling
os=4
#Roll-off factor
alpha=0.22
#Truncation
Trunc=8
#Filter
filter=np.array(RaisedC(1,os,alpha,Trunc))

## System
#Modulation
x=Mod(nbits,mod)
#FFT
FFT_x=np.fft.fft(x,FFTlen)
#Subcarrier-Mapping
FFT_inter=SubMap(FFT_x,submapC,IFFTlen,FFTlen)
#IFFT
IFFT_x=np.fft.ifft(FFT_inter,IFFTlen)
#CPIFFTlen
IFFT_cp=y = np.zeros(IFFTlen+CP, dtype=complex)
IFFT_cp[0:CP]=IFFT_x[-CP:]
IFFT_cp[CP:]=IFFT_x
#Pulse shaping
#Up-sampling
IFFT_up=Upsam(IFFT_cp,os)
#Conv









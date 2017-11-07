# noinspection PyUnresolvedReferences
import numpy as np

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

##System
#Modulation
x=Mod(nbits,mod)
#FFT
FFT_x=np.fft.fft(x,FFTlen)
#Subcarrier-Mapping
FFT_inter=SubMap(FFT_x,submapC,IFFTlen,FFTlen)
#IFFT
IFFT_x=np.fft.ifft(FFT_inter,IFFTlen)
#CP
IFFT_cp=y = np.zeros(IFFTlen+CP, dtype=complex)
IFFT_cp[0:CP]=IFFT_x[-CP:]
IFFT_cp[CP:]=IFFT_x
# Pulse shaping
# Up-sampling
ye











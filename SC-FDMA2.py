import numpy as np

## Parameters
#Modulation
mod="BPSK"
#Length of FFT
FFTlen=10
#Number of bits
nbits=FFTlen
#Subcarrier-mapping
submapC="Interleaved"
#SNRdb
SNRdb=np.arange(0,20,1)
#Length of IFFT
IFFTlen=30
#Q
Q=IFFTlen//FFTlen

## Canal
#Channels based on 3GPP TS 25.104.
IFFTlen=30
ch='vehA'
if ch=='pedA':
    pedAchannel=np.array([1,10**(-9.7/20),10**(-22.8/20)])
    channel=pedAchannel/np.sqrt(np.sum(pedAchannel**2))
elif ch=='vehA':
    vehAchannel=np.array([1 ,0 ,10**(-1/20), 0, 10**(-9/20), 10**(-10/20), 0, 0, 0, 10**(-15/20), 0, 0, 0, 10**(-20/20)])
    channel=vehAchannel/np.sqrt(np.sum(vehAchannel**2))
elif ch=='AWGN':
    channel=1
Hchannel = np.fft.fft(channel,IFFTlen)


## FDE
#Find the channel response for the interleaved subcarriers.
Heff=Hchannel[0::Q]
#Perform channel equalization in the frequency domain.
if equalizer=='ZERO':
    r_eq=r_dFFT/Heff
elif equalizer == 'MMSE':
    C=np.conj(Heff)/(np.conj(Heff)*Heff+10**(-SNRdb/10))
    r_eq=r_dFFT*C

# noinspection PyUnresolvedReferences
import numpy as np

## Functions

def Mod(Numbersymbols,modulation):
    if modulation=="BPSK":
        n=Numbersymbols
    elif modulation=="QPSK":
        n=Numbersymbols*2
    elif modulation=="16-QAM":
        n=Numbersymbols*4
    x = np.random.randint(0, 2, n)
    return x

## Parameters
mod="16-QAM"
nsym=100
print(Mod(nsym,mod))




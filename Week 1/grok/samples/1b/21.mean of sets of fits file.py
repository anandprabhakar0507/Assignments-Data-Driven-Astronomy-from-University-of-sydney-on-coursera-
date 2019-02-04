from astropy.io import fits
import numpy as np

def mean_fits(files):
  n = len(files)
  if n > 0:
    
    hdulist = fits.open(files[0])
    data = hdulist[0].data
    hdulist.close()
    
    for i in range(1, n):
      hdulist = fits.open(files[i])
      data += hdulist[0].data
      hdulist.close()
    
    mean = data / n
    return mean
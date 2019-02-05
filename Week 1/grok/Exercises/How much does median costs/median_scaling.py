import time, numpy as np
from astropy.io import fits
# Write your function median_FITS here:
def median_fits(x):
  start = time.time()  #it will start the timer
  #now lets read all the FITS files and store in list
  FITS_list = []
  for filename in x:
    a = fits.open(filename)
    FITS_list.append(a[0].data)
    a.close()
  #now stack image arrays in 3d array for median calculation
  FITS_stack = np.dstack(FITS_list)  
  median = np.median(FITS_stack, axis=2) 
 
  #now calculating memory consumed by data
  memory = FITS_stack.nbytes  
  #or we can also try
  #memory = 200 * 200 * len(x) * FITS_stack.itemsize
  #convert memory in kb
  memory /= 1024 
  stop = time.time() - start    #stops timer i.e start=time.time so net = 0
  return median, stop, memory
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
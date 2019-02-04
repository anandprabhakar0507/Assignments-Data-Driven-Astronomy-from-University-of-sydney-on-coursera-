# Write your load_fits function here.
from astropy.io import fits
import numpy as np

def load_fits(y):
  a = fits.open(y)
  data = a[0].data

  max_arg = np.argmax(data)  
  max_pos = np.unravel_index(max_arg, data.shape)
  
  return max_pos

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  x = fits.open('image1.fits')
  data = x[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.xlabel('x-pix. (RA)')
  plt.ylabel('y-pix. (Dec)')
  plt.colorbar()
  plt.show()

 

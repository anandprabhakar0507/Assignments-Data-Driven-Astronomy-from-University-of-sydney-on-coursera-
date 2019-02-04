from astropy.io import fits
import matplotlib.pyplot as plt

x = fits.open('image0.fits')
data = x[0].data

# Plot the 2D array
plt.imshow(data, cmap=plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()
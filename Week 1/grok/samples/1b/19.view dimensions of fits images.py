from astropy.io import fits

a = fits.open('image0.fits')
image = a[0].data

print(image.shape)
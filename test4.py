import math
import numpy
import matplotlib.pyplot
import scipy
import skimage

#img = numpy.load('dat/hxdf_acs_wfc_f850lp_small.npy')
img0 = numpy.load('dat/hxdf_acs_wfc_f850lp.npy')

# Some image information
print("Size: ", img0.shape)

# Fraction of image to speed up the program
img1 = img0[4000:5000,4000:5000]

img_fraction = img1.shape[0]/img0.shape[0]

print("Image fraction: ", img_fraction)

print("Mean: ", numpy.mean(img1))
print("Highest: ", numpy.amax(img1))
print("Lowest: ", numpy.amin(img1))

threshold = 0

# Filter image
# Count number of distinct local maxima 
# What is an objective threshold?
img2 = scipy.ndimage.gaussian_filter(img1, sigma = 4)
print("Filtering complete")
peaks = skimage.feature.peak_local_max(img2, threshold_abs = threshold)
print("Peak finding complete")

# Number of galaxies in image
galaxies_in_image_fraction = len(peaks)
print("Number of galaxies in image fraction: ", galaxies_in_image_fraction)

print("1/img_fraction =", 1/img_fraction)
# Number of galaxies in the full image
galaxies_in_full_image = galaxies_in_image_fraction / img_fraction
print("Number of galaxies in full image: ", galaxies_in_full_image)

# The image has the angle of a grain of sand at arm's length
# Assume a grain of sand is 1mm and an arm is 1m

print("fraction_of_sky =", 4 * 3.1415 / 10**(-6))

# Number of galaxies in the spherical sky
galaxies_in_sky = galaxies_in_full_image * 4 * 3.1415 / 10**(-6)

# How much of the sky is obscured by other galaxies?

print("Calculating fraction obscured...")
obscured = 0
for h in range(0, img1.shape[0]):
    for w in range(0, img1.shape[1]):
        if img1[h, w] > threshold:
            obscured = obscured + 1
fraction_obscured = obscured / (img1.shape[0]*img1.shape[1])
print("Fraction obscured: ", fraction_obscured)

# Image is filtered in near-infrared; highly redshifted/distant/weak galaxies are lost
# Galaxies obscured or melded by the Gaussian filter are lost
galaxies_in_total = galaxies_in_sky

print("Number of galaxies in total: ", galaxies_in_total)

# Show filtered image
matplotlib.pyplot.figure()
for h, w in peaks:
    matplotlib.pyplot.gcf().gca().add_artist(matplotlib.pyplot.Circle((w,h), 5, color = 'Blue', fill=False))
matplotlib.pyplot.imshow(img2.clip(-0.0002,0.0002), origin='lower', interpolation='nearest', cmap='afmhot')
matplotlib.pyplot.show()

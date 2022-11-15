# Trying to estimate the number of galaxies in the universe from the Hubble deep field view F850LP filter image
#
# 

import math
import numpy
import matplotlib.pyplot
import scipy
import skimage

img1 = numpy.load('dat/hxdf_acs_wfc_f850lp.npy')

# The threshold for cutting off peaks
threshold = 0.0001

# Filter image to try to reduce noise
img2 = scipy.ndimage.gaussian_filter(img1, sigma = 4)

# Count number of distinct local maxima above a certain threshold
peaks = skimage.feature.peak_local_max(img2, threshold_abs = threshold)

# Number of galaxies in image
galaxies_in_image = len(peaks)
print("Number of galaxies in image: ", galaxies_in_image)


# The image has the angle of a grain of sand at arm's length
# Assume a grain of sand is 1mm and an arm is 1m
# Number of galaxies in the full spherical sky
galaxies_in_total = galaxies_in_image * 4 * 3.1415 * 10**6

# Image is filtered in near-infrared; highly redshifted/distant/weak galaxies
# are lost in the noise

print("Number of galaxies in the universe: ", galaxies_in_total)

# Show filtered image and detected galaxies
#matplotlib.pyplot.figure()
#for h, w in peaks:
#    matplotlib.pyplot.gcf().gca().add_artist(matplotlib.pyplot.Circle((w,h), 5, color = 'Blue', fill=False))
#matplotlib.pyplot.imshow(img2.clip(-0.001,0.001), origin='lower', interpolation='nearest', cmap='afmhot')
#matplotlib.pyplot.show()
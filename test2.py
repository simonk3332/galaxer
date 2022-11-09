import math
import numpy
import matplotlib.pyplot
import scipy
import skimage



#img = numpy.load('dat/hxdf_acs_wfc_f850lp_small.npy')
img = numpy.load('dat/hxdf_acs_wfc_f850lp.npy')[4000:4500, 4000:4500]

print("Mean: ", numpy.mean(img))
print("Highest: ", numpy.amax(img))
print("Lowest: ", numpy.amin(img))
# Try to remove noise
#threshold = 0.00006
threshold = 0.00006
#threshold = 0.000000001
# What is an objective threshold?
img2 = scipy.ndimage.gaussian_filter(img, sigma = 4)
# Count number of distinct local maxima 
peaks = skimage.feature.peak_local_max(img2, threshold_abs = threshold, indices = True)
print("Count: ", len(peaks))
matplotlib.pyplot.figure()
for h, w in peaks:
    matplotlib.pyplot.gcf().gca().add_artist(matplotlib.pyplot.Circle((w,h), 15, color = 'Blue', fill=False))
matplotlib.pyplot.imshow(img2, origin='lower', interpolation='nearest', cmap='afmhot')
matplotlib.pyplot.show()
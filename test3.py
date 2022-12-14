import math
import numpy
import matplotlib.pyplot
import scipy
import skimage

#count = len(skimage.feature.peak_local_max(filtered_image))
#img = skimage.color.rgb2gray(skimage.data.hubble_deep_field()[0:500,0:500])
img = numpy.load('dat/hxdf_acs_wfc_f850lp.npy')[4000:4500, 4000:4500]
print("Mean: ", numpy.mean(img))
print("Highest: ", numpy.amax(img))
print("Lowest: ", numpy.amin(img))
img = img - numpy.amin(img)
print("Mean: ", numpy.mean(img))
print("Highest: ", numpy.amax(img))
print("Lowest: ", numpy.amin(img))
blobs = skimage.feature.blob_log(img, max_sigma=30, num_sigma=10, threshold=.00032)
print(" Count: ", len(blobs))

matplotlib.pyplot.figure()
for h, w, r in blobs:
    matplotlib.pyplot.gcf().gca().add_artist(matplotlib.pyplot.Circle((w,h), 15, fill=False))
matplotlib.pyplot.imshow(img, origin='lower', interpolation='nearest', cmap='afmhot')
matplotlib.pyplot.show()

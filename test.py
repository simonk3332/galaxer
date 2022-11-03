import math
import numpy
import matplotlib.pyplot
import scipy

def plot_image(img):
    matplotlib.pyplot.figure()
    matplotlib.pyplot.imshow(img, origin='lower', interpolation='nearest', cmap='afmhot')
    matplotlib.pyplot.show()

# Find a nearby local maximum in a grayscale image by recursively going uphill
def find_local_peak(image, h, w):
    if h < image.shape[0] - 1:
        if image[h, w] < image[h+1, w]:
            return find_local_peak(image, h+1, w)
    if h > 0:
        if image[h, w] < image[h-1, w]:
            return find_local_peak(image, h-1, w)
    if w < image.shape[1] - 1:
        if image[h, w] < image[h, w+1]:
            return find_local_peak(image, h, w+1)
    if w > 0:
        if image[h, w] < image[h, w-1]:
            return find_local_peak(image, h, w-1)
    return (h, w)

# Load image
raw_image = numpy.load('hxdf_acs_wfc_f850lp_small.npy')
# Try to remove noise
mean = numpy.mean(raw_image)
variance = numpy.var(raw_image)
print("Mean: ", mean, " Variance: ", variance)
threshold = 0.00006
#threshold = mean + x*math.sqrt(variance) ?
# What is an objective threshold?
image = scipy.ndimage.gaussian_filter(raw_image, 4)
for h in range(0, image.shape[0]):
    for w in range(0, image.shape[1]):
        if image[h, w] < threshold:
            image[h, w] = 0
# Count number of distinct local maxima 
peaks = []
for h in range(0, image.shape[0]):
    for w in range(0, image.shape[1]):
        if image[h, w] >= threshold:
            peak = find_local_peak(image, h, w)
            if not (peak in peaks):
                peaks += [peak]
count = len(peaks)
print("Count: ", count)
# Display image
plot_image(image)


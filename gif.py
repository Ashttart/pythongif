import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['gif1.png', 'gif2.png']
images = []

first_img = Image.open(filenames[0])
standard_size = first_img.size 

for filename in filenames:
    # Resize
    img = Image.open(filename)
    # Make image match
    img = img.resize(standard_size)
    # Convert to numpy array and append
    images.append(np.array(img))

# Should have same size now
iio.imwrite('bop.gif', images, duration=500, loop=0)
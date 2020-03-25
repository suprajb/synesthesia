from PIL import Image, ImageOps
import math, wave, argparse

def sinewave(frequency, amplitude, samples, rate):
    """generate a sinewave
    
    generate a sinewave with properties as specfied by arguments

    Returns:
        A list of size 'samples' that contains the values of the sine wave

    """
    wave = []
    for i in range(samples):
        x = math.sin(2 * math.pi * frequency * (i / float(rate))) * float(amplitude)
        wave.append(x)
    return wave

def synethesise(inp_image, out_wave, min_freq, max_freq, rate, scale):
    
    #open in grayscale
    image = Image.open(inp_image).convert('L')
    
    img_width = image.[0]
    img_height = image.[1]

    output = wave.open(out_wave, 'w')
    output.setparams((1, 2, rate, 0, 'NONE', 'not compressed'))
    wave = []

    block_size = (max_freq - min_freq) / img_height
    samples_per_pixel = rate//scale
    data = array.array('h')

    for i in range(img_width):
        for j in range(img_height):
            yinv = img_width - y - 1     
            amplitude = img.getpixel((x,y))
            data = genwave(yinv * block_size + min_freq, amplitude, samples_per_pixel, rate)
            for k in range(samples_per_pixel):
                for l in data:
                    wave[i + x * samples_per_pixel] += l[k]


    
    
    



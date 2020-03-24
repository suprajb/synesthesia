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

    interval_size = (max_freq - min_freq) / img_height
    
    




from PIL import Image, ImageOps
import math, wave


def createwave(frequency, amplitude, samples):
    wave = []
    for i in range(samples):
        x = math.sin(2 * math.pi * frequency * (i / float(rate))) * float(amplitude)
        wave.append(x)
    return wave

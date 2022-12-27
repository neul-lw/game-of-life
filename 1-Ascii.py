from PIL import Image
from pprint import pprint as pp 
import os
"""
If image is png you should just get RGB values not the length of it
"""

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255
                                     
df_dir = "Desktop/CS-P/Python/Advance-Beginners/images/trip.jpg"
#img_dir = input("Please enter your image's absolute directory: ")

def img_color_matrix(img=df_dir):
    img = im.resize((300, 300))
    pixels = list(img.getdata()) 
    """
    To clarify 
        list = []
        for i in range(0, len(pixels), width):
            list += pixels[0:600]
    """
    pixels = [pixels[i: i+width] for i in range(0, len(pixels), width)]
    return pixels


def get_intensity_matrix(pixels_matrix, mode="average"):
    intensity_matrix = []
    for row in pixels_matrix:
        intensity_row = []
        for p in row:
            if mode == "average":
                intensity = (p[0] +  p[1] +  p[2]) / 3 
            elif mode == "lightness":
                intensity = max(p[0], p[1], p[2]) + min(p[0], p[1], p[2]) / 2
            elif mode == "luminosity":
                intensity = 0.21 * p[0] + 0.72 *  p[1] + 0.07 * p[2]
            else:
                raise Exception(f"Unrecognized mod {mode}")

            intensity_row.append(intensity)
        intensity_matrix.append(intensity_row)
    return intensity_matrix


def brightness_ascii(ascii_intensity_matrix):
    ascii_intensity = []
    for row in ascii_intensity_matrix:
        ascii_row = []
        for value in row:
            ascii_row.append(ASCII_CHARS[int(value/MAX_PIXEL_VALUE * len(ASCII_CHARS) + 1)])
        ascii_intensity.append(ascii_row)
    return ascii_intensity 




if __name__ == "__main__":

    if os.path.isfile(df_dir):
        im = Image.open(df_dir)
        width, height = im.size
        #print(f"Image size: {width} x {height}")
        pixels = img_color_matrix()
        get_intensity_matrix(pixels, mode="luminosity")
        bg = get_intensity_matrix(pixels, mode="luminosity")
        for row in brightness_ascii(bg):
            for p in row:
                print(p, end="")
        
    else:
        print("File doesn't exists!")


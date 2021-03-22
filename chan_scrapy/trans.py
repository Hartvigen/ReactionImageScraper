#Check for transparency in image
#TODO: check edges of images for transparency rather than simply checking for a transparency layer

def has_transparency(img):
    if img.mode == "P":
        print("Iamge is P")
        transparent = img.info.get("transparency", -1)

        for index in img.getcolors():
            if index == transparent:
                print(index)
                return True


    elif img.mode == "RGBA":
        print("Image is RGBA")
        extrema = img.getextrema()

        px = img.load()
        print(px[1,1])
        if extrema[3][0] < 180:
            print(extrema)
            return True
    else:
        print("Image is " + img.mode)
    return False
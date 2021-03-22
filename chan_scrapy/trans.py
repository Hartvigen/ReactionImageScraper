#Check for transparency in image
#TODO: check edges of images for transparency rather than simply checking for a transparency layer

def has_transparency(img):
    if img.mode == "RGBA":

        print("Image is RGBA")
        width = img.size[0]
        height = img.size[1]
        px = img.load()


        transCountH = 0
        transCountW = 0

        for i in range(width):
            if px[i, 0][3] < 180:
                transCountW += 1
            if px[i, height - 1][3] < 180:
                transCountW += 1
        
        for i in range(height):
            if px[0, i][3] < 180:
                transCountH += 1
            if px[width - 1, i][3] < 180:
                transCountH += 1

        if(transCountH > 10 and transCountW > 10):
            return True


        #Old method using extremas for entire picture, was discarded due to edge case erros
        #extrema = img.getextrema()
        #if extrema[3][0] < 180:
        #    print(extrema)
        #    return True


    elif img.mode == "P":
        print("Image is P")
        transparent = img.info.get("transparency", -1)

        for index in img.getcolors():
            if index == transparent:
                print(index)
                return True

    else:
        print("Image is " + img.mode)
    return False
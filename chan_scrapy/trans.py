#Check for transparency in image

def has_transparency(img):
    if img.mode == "RGBA":

        print("Image is RGBA")
        width = img.size[0]
        height = img.size[1]
        px = img.load()


        transCountH = 0
        transCountW = 0

        #We check the edges of the image for transparent pixels. Which, if present, in turn indicates 
        #something akin to a reaction image. this method is used as previously images with just a single
        #transparent pixel, or a transparent part focused on the middle was included 
        #in the kept results
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


    #Old method using extremas for entire picture, this was discarded due to edge case erros however may still be used
    #if we want any trasnparent image
        #extrema = img.getextrema()
        #if extrema[3][0] < 180:
        #    print(extrema)
        #    return True

    #No idea how these images work, they pop up every now and then and this case catches 90% of valid cases
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
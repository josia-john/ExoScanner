# This file contains the function "generateField()" which will, given a target
# coordinate, radius, and image, return the small field around the target
# coordinate. The fields size is determined by radius. This is used when
# calculating the brightness of one star, as it would not make sense to look at
# the whole image when calculating the brightness of just one star.

import ExoScanner.config


def generateField(rgb, targetX, targetY):
    radius = ExoScanner.config.config["boxSize"]
    field = []
    for i in range(round(targetY-radius), round(targetY+radius)):
        field.append([])
        for j in range(round(targetX-radius), round(targetX+radius)):
            [x, y]=[j, i]
            x=int(round(x))
            y=int(round(y))
            try:
                field[-1].append(rgb[y][x] ** 1)
            except IndexError as error:
                print(error)
                print("star is probably not fully contained by all images!")
                field[-1].append(0 ** 1)

    return field

import pprint

"""
    m is 2 dimensions array as matrix
    return highest count of adjustcent value (biggest area)
"""
def FindCountElementOfBiggestArea(m):
    a = [] # already lookup index array, for efficiency

    dx = len(m[0]) # dimension x
    dy = len(m) # dimension y

    count = {} # keep tracking for current adjustcent count
    biggest_count = [0] # value for returning result as maximum adjustcent

    # recusive needed, use inner function
    def GetMatchAdjustcentValue(y, x, val, root=False):
        if (y, x) not in a:
            current_val = m[y][x]

            if val == current_val:
                if count.has_key(val):
                    count[val] += 1
                else:
                    count[val] = 1
                a.append((y, x))

                if x < dx - 1: # right
                    GetMatchAdjustcentValue(y, x + 1, val)
                if x > 0: # left
                    GetMatchAdjustcentValue(y, x - 1, val)
                if y < dy - 1: # top
                    GetMatchAdjustcentValue(y + 1, x, val)
                if y > 0: # bottom
                    GetMatchAdjustcentValue(y - 1, x, val)

                if root:
                    # update result if found higher counter
                    if count[val] > biggest_count[0]: biggest_count[0] = count[val]
                    # reset counter after get all adjustcent matched value
                    del count[val]

    for iy in xrange(dy):
        for ix in xrange(dx):
            GetMatchAdjustcentValue(iy, ix, m[iy][ix], True)

    return biggest_count[0]


if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 2, 2],
        [1, 1, 7, 2, 2],
        [2, 2, 7, 2, 1],
        [2, 1, 7, 4, 4],
        [2, 7, 7, 4, 4],
        [4, 6, 6, 0, 4],
        [4, 4, 6, 4, 4],
        [4, 4, 6, 4, 4],
    ]

    biggest_count =  FindCountElementOfBiggestArea(matrix)

    print """Biggest Area of

{0}

is {1}
    """.format(pprint.pformat(matrix), biggest_count)

    input('press any key to exit')

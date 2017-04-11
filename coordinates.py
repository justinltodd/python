#!/Users/Justin/anaconda/bin/python
'''
Build Dictionary with coordinates
'''
coord_dict = {}
while True:
    coord = raw_input("Please enter a coordinate-word pair in the format (x, y, word): ")
    # If no entry break/exit
    if not coord:
        break
    #Split x,y, word
    x, y, word = coord.split(", ")
    #print x, y, word
    coord_dict[x, y] = word
    print coord_dict

while True:
        locate = raw_input("Please enter a coordinate to look up: ")
        # If no entry break/exit
        if locate == "q":
            break
        coord_location = tuple(locate.split(", "))
        print coord_location
        if coord_location not in coord_dict:
            print 'Coordinate not found'
            continue
        print coord_dict[coord_location]

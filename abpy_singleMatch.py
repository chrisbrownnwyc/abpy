import re
import sys

from abpy import Filter

if __name__ == '__main__':
    f = Filter(file(sys.argv[1]))
    print 'start matching'
    # read urls from file into a list and strips new lines
    lines = (line.rstrip('\n') for line in open(sys.argv[2]))
    #check each url fom list if it matches a filter rule
    hitlist = []
    for line in lines:
        hitlist.extend( f.match(line) )

    # write hits to file
    outputfile  = open(sys.argv[3], 'w')
    for item in hitlist:
        outputfile.write("%s\n" % unicode(item))
    print 'finished successful'

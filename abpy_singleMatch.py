from __future__ import absolute_import
import sys

from .abpy import Filter

if __name__ == '__main__':
    fh = open(sys.argv[1], 'r')
    f = Filter(fh)
    print('start matching')
    # read urls from file into a list and strips new lines
    lines = (line.rstrip('\n') for line in open(sys.argv[2]))

    # check each url fom list if it matches a filter rule
    hitlist = []
    for line in lines:
        hitlist.extend( f.match(line) )

    # write hits to file
    outputfile  = open(sys.argv[3], 'w')
    for item in hitlist:
        outputfile.write("%s\n" % str(item))
    print('finished successful')

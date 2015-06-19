import re
import sys

from abpy import Filter as BaseFilter
from abpy import RE_TOK


class Filter(BaseFilter):
    def __init__(self, f):
        super( Filter,self ).__init__(f)
        self.hitlist = []

    def match(self, url, elementtype=None):
        matched = False
        tokens = RE_TOK.split(url)
        for tok in tokens:
            if len(tok) > 2 and not matched:
                if tok in self.index:
                    for rule in self.index[tok]:
                        if rule.match(url, elementtype=elementtype):


                            # for debug - appends matched rule
                            # hit = url + " " + unicode(rule)
                            # hitlist.append(hit)

                            # we matched a rule with the url and dont need to check the url any further
                            self.hitlist.append(url)
                            matched = True


if __name__ == '__main__':
    f = Filter(file(sys.argv[1]))
    print 'start matching'
    # read urls from file into a list and strips new lines
    lines = (line.rstrip('\n') for line in open(sys.argv[2]))
    #check each url fom list if it matches a filter rule
    for line in lines:
        f.match(line)

    # write hits to file
    outputfile  = open(sys.argv[3], 'w')
    for item in f.hitlist:
        outputfile.write("%s\n" % item)
    print 'finished successful'

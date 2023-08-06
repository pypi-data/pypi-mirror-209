import sys
import os

ap = os.path.abspath(os.path.dirname(os.path.dirname('./../krutils')))
print (ap)

sys.path.append(ap)

from krutils import logger
l = logger(__file__)
print (l)
l.debug('[%%]', 123)


from krutils import utils

kl = utils.logger(__file__)
kl.debug('[%%]', 'xxxxx')


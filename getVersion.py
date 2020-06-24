import os
import sys
from xml.dom import minidom

if (os.path.isfile(sys.argv[1])):
  print minidom.parse(sys.argv[1]).getElementsByTagName('widget')[0].getAttribute('version')

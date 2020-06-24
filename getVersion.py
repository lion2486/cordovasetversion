import os
import sys
from xml.dom import minidom

def getVersion(filename):
	if (os.path.isfile(filename)):
		return minidom.parse(filename).getElementsByTagName('widget')[0].getAttribute('version')
	else:
		print '*****ERROR: config.xml file not exists'
		sys.exit(1)
  
if __name__ == "__main__":
	# execute only if run as a script
	print getVersion(sys.argv[1])

from datetime import datetime
import platform

#Creating log file and his name
file = '%s_%s' % (datetime.now().strftime('%d.%m.%Y_%H.%M.%S'), 'log.txt')

#Creating header of log (inside of file)
open(file, 'w').write("Tested on: " + platform.platform() + "\n")

#'%d.%m.%Y_%H.%M.%S'
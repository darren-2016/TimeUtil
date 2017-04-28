################################################################################
# Python Time Converter
# D J Draper, April 2017
# 
# Time Conversion Utility

import time
import sys


################################################################################
# Function:    LocalTime
# Description: Display the current time (local).
# Parameters:  None
# Returns:     None
#
def LocalTime():
    print "Current Time (Local): " + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())

################################################################################
# Function:    GMTime
# Description: Display the current time (GMT).
# Parameters:  None
# Returns:     None
#
def GMTime():
    print "Current Time (GMT): " + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

################################################################################
# Function:    ConvertTime
# Description: Convert the time value to local time and date.
# Parameters:  timeval
# Returns:     None
#
def ConvertTime(timeval):
    print "Timer value: " + str(timeval)
    print time.ctime(timeval)


################################################################################
# Function:    main
# Description: Main program function.
# Returns:     None
#
def main(argv):
    print "Time Converter"
    if len(sys.argv) > 1:
            ConvertTime(float(argv[0]))
    else:
        LocalTime()


################################################################################
# Main entry point
#
if __name__ == "__main__":
    main(sys.argv[1:])



<<<<<<< HEAD
# Read Digital RF file
# Author: W. Engelke, AB4EJ, University of Alabama

import matplotlib.pyplot as plt
import numpy as np
import digital_rf as drf
from datetime import datetime
import datetime
from datetime import timezone
import math
import os, tempfile
import maidenhead as mh 
import sys, getopt, os


# Get supplied argument(s)
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
dataDir = ''

# Options - these are valid options
options = "hf:"
 
# Long options
long_options = ["Help", "theDate", "file"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("-d YYYY-MM-DD -f filewname")

        elif currentArgument in ("-f", "--file"):
            print ("the file:",currentValue)
            dataDir = currentValue

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

if dataDir == '':
    print("Enter DRF dataset to be processed (full path):")
    dataDir = input()

plt.style.use('_mpl-gallery-nogrid')
maidenheadGrid = 'EN91' # this is just a default
# plot
fig, ax = plt.subplots()

metadata_dir = dataDir + '\\ch0\\metadata'

print("Looking for metadata at:" + metadata_dir)

do = drf.DigitalRFReader(dataDir)
s, e = do.get_bounds('ch0')

#print("Data avail. starting ", datetime.datetime.fromtimestamp(s/10))
#print("   thru ", datetime.datetime.fromtimestamp(e/10))

#print("Plot spectrum for what date?  (YYYY-MM-DD)")
#t =input()
t = dataDir[-16:] # + "T00:00"
print("request date:" + t)
requestTime = datetime.datetime.strptime(t, '%Y-%m-%dT%H-%M')
# these are based on unix time * 10 (for 10 samples/sec)
timestamp = requestTime.replace(tzinfo=timezone.utc).timestamp() * 10

s = int(timestamp)
print("time stamp ",s)


freqList = [0]
theLatitude = 0
theLongitude = 0

# get Metadata, if it exists
try:
    dmr = drf.DigitalMetadataReader(metadata_dir)
    print("metadata init okay")
  #  start_idx = int(np.uint64(stime * dmr.get_samples_per_second()))
   # start_idx = int(np.uint64(s)) # test
    first_sample, last_sample = dmr.get_bounds()
    print("metadata bounds are %i to %i" % (first_sample, last_sample))
    from datetime import datetime # refresh this
    print("This is ",datetime.utcfromtimestamp(first_sample/10).strftime('%Y-%m-%d %H:%M:%S'),
          "to", datetime.utcfromtimestamp(last_sample/10).strftime('%Y-%m-%d %H:%M:%S'),"UTC")

    start_idx = int(np.uint64(first_sample))
    print('computed start_idx = ',start_idx)

    fields = dmr.get_fields()
    print("Available fields are <%s>" % (str(fields)))

    #print("first read - just get one column ")
    data_dict = dmr.read(start_idx, start_idx + 2, "center_frequencies")
    for key in data_dict.keys():
      #  print((key, data_dict[key]))
        freqList = data_dict[key]
        print("freq = ",freqList[0])

    data_dict = dmr.read(start_idx, start_idx + 2, "lat")
    for key in data_dict.keys():
     #   print((key, data_dict[key]))
        theLatitude = data_dict[key]
        print("Latitude: ",theLatitude)
        
    data_dict = dmr.read(start_idx, start_idx + 2, "long")
    for key in data_dict.keys():
      #  print((key, data_dict[key]))
        theLongitude = data_dict[key]
        print("Longitude: ",theLongitude)

   #  maidenheadGrid = to_grid(theLatitude, theLongitude)
    maidenheadGrid = mh.to_maiden(theLatitude, theLongitude, 3)
    
    
except IOError:
    print("IO Error; metadata not found at " + metadata_dir)


gain = 1.5
hr1 = np.arange(1024, dtype='f')
#print("numpy array type = ",type(hr1[0]))
zeros = np.zeros(1024, dtype='f')

print('Read data... this may take a few minutes...')
offset = 0
# Get data from DRF dataset and build the 2D Q array
for i in range(1439): # 1439 gives 1440 bins
    try:
        data = do.read_vector(s + offset, 1024, 'ch0')
        # At this point, the variable 'data' contains 1024 complex 32-bit float values
        # from the DRF dataset, starting at Unix time = s + offset
      #  z=input() # debugging stop

    except IOError: # tried to read DRF data but did not find requsted time slice
      #  print("data gap at ", s + offset)
        if (offset == 0):
            Q = np.array([zeros])
        else:
            Q = np.append(Q, [zeros], axis = 0) # 

    # in narrow case, there are 10 samples/sec, so 600 samples = 1 minute
    offset = offset + 600  #  note overlap of the 1024 bins
    # if you want no overlap, set the above to offset = offset + 1024
    if (i % 100 == 0): # progress indicator, marching dots
        print(".",end='') # this works the same as when DRF used to store data
 

 
>>>>>>> 98c286e50c0187328681fbac885d853e2ba2f566

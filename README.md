# DRF_processing
Programs for working with Grape1 Digital RF datasets.

DRF_reader.py reads a 24-hour Digital RF spectrum dataset; it processes through 1440 minutes. 
For each minute, the system fills the array named 'data' with 600 32-bit float complex
values (I/Q).

plotspectrum_V4a.py reads ina DRF dataset and plots it as a spectrogram - in this case, a
waterfall plot showing 24 hours and Doppler excursions of the carrier signal being tracked.
Input:
-f   name of top-level directory (must be the directory above the ch0 level)
-p   path to an output directory where the plot will be saved.

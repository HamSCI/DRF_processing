# DRF_processing
<<<<<<< HEAD
Programs for working with Digital RF datasets
=======
Programs for working with Grape1 Digital RF datasets.

DRF_reader.py reads a 24-hour Digital RF spectrum dataset; it processes through 1440 minutes. 
For each minute, the system fills the array named 'data' with 600 32-bit float complex
values (I/Q).

plotspectrum_V4a.py reads ina DRF dataset and plots it as a spectrogram - in this case, a
waterfall plot showing 24 hours and Doppler excursions of the carrier signal being tracked.
Input:

-f       name of top-level directory (must be the directory above the ch0 level)

-p       path to an output directory where the plot will be saved.

Example:
python3 plotspectrum_V4a.py -f C:\\temp\\OBS2023-11-01T00-00 -p C:\\temp\\myplotfile.png

The escape sequences "\\" are mandatory for Python.

Refer to docs/An Introduction to Digital RF.pdf to understand DRF dataset structure.
>>>>>>> a74af6662fcd65e59e12ba4fe01594cd659e6a0a

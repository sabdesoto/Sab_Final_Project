
Project created by Sabrina DeSoto 10-27-2015.
Computation in the Physical Science

PROJECT SEARCH FOR SPACE TREASURE
10 MINUTE PLAN

INTRODUCTION
The purpose of this project is to create a code that can analyze any
microwave amplification by stimulated emission of radiation (MASER) data and 
return coordinates in the sky for where the MASER is located. This work can 
be divided into two major sections. The first part is to take the raw data 
collected and confirm a detection was made. The second part is to take that 
detection data and to use it to establish the celestial location of the MASER.
Both python and astronomical image processing system (AIPS) coding helped to
achieve these outcomes.
When the data is received it must be processed and written into tables for 
analysis (write about data processing). From the processed large data set the
first step is to confirm a detection was made. A MASER detection is defined by
a sudden large increase in the amplification (which is…) data. Phase diagrams
are used to visualize this increased amplification, which appears as a spike 
when amplification is plotted against the channel. This spike is arguable a 
more obvious way of identifying there was detection rather than reading 
through the data, which is why these diagrams are included in this project. 
Additionally, these diagrams include a second frame witch plots the 
corresponding phases through out the observing period. Knowing the phase the 
detection was made in is the real key to establishing the coordinates. Since 
the data comes in chunks of 30minute observation periods the phases of each of
the detections must be deciphered from the large data set into a smaller set 
of just detection data. The purpose of collecting multiple phase data for each
detection is to be able to compare them from each period helping to confirm a 
more accurate phase of the detection. Think of the phase data as circles of a 
Venn- diagram, overlapping more and more circles creates distinct point where 
they all meet, which in this case would be the precise phase the MASER was 
detected in. Statistical analysis was also used for reassurance of these phase
comparisons. (explain stats). 
Finally once a detection is confirmed in a phase, steps towards establishing a
set of coordinates for the MASER can start. (Physics steps…). 

METHOD
The script begins with creating an imports library containing all necessary 
coding aides. Data is then imported using the open command and a loop to print
it line by line. Next another loop is run to resample the data, separating out
only the observation amplitudes and phases for each 30minute period. Together 
this resampled data composes a data table that is used to create each periods 
phase diagram. This portion of the code first creates a single diagram made by
matplotlib’s subplot function so that the phase data and amplitude data are 
plotted one on top of the other, sharing the same x-axis, the channel count. 
The lower amplitude plot is a continuous line plot in blue while the upper 
phase section is a scatter plot with green x points. This plot method is then 
repeated for each 30minute period by referencing all the resampled data and 
setting subplots = true. The phase points corresponding to the amplitude spike
are also pulled from the resampled data using a function called def 
detection_phases. This function uses an if statement to loop through the 
resampled amplitude data, separating the amplitude greater than (_), 
indicating a detection. The loop returns the phase point, which corresponded to
the greater amplitudes.  Additionally, a second loop is coded in the function 
allowing only the desired detection points to be printed. Another data table is
then created with the first row identifying each 30minute observation period 
and the columns being the detection phases found in the previous step. A 
regular expression captured only the time record portion of the headings from 
the large data set to be column separators at the top of the table. To create 
the columns data from the detection_phases function was called and separated 
out by comas inside double squared brackets [[_]]. (add stats and physics part/
include completed flow chart)

KEY VARIABLES AND FUNCTIONS
pd = pandas library
plt = matplotlib.pyplot library (for plotting)
re = re library (for regular expressions)
readings= large processed data set
re_ampl = amplitude data separated by 30minute observation periods
re_phase = phase data separated by 30mintue observation periods
resampled = resampled data set of re_ampl and re_phase 
subplot 1 = plot of phase vs. channel (top of phase diagram)
subplot 2 = plot of amplitude vs. channel (bottom of phase diagram)
def detection_phases = function for finding phase pts for greater amplitudes





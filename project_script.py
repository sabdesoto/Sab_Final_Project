#11/16/2015 Sabrina DeSoto
#Computational Physics Final Project Script 1


#Define main function that will...

def main():
	#Set up. Import Libraries
	import pandas as pd 
	import matplotlib.pyplot as plt
	import sys
	
	#Step0. Define arguments
	script_name = sys.argv[0]
	
	#Step1. Define variables
	
	#length of data collected directly from antena array
	length_of_file = 12624
	#empty list, called table, holds each chunk of data separated by observation time
	table = []
	
	#Step2. load data separating each chunk of observation time
	load_data('/Users/sabrinadesoto/Documents/Sab_Final_Project/Data/sabrina.dat')
	
	#Step3. plot phase diagrams for each chunk of observation time
	make_phase_diagrams(table)
	
	#Step4. get signal amplitudes from data
	#signal_amplitude(data, column) 
	
	#Step5. get average signal phase and phase location 
	#signal_phase(table)
	
	#Step6. assign variable to output of signal_phase function
	#phase_results = signal_phase(table)
	
	#GET FRINGE PLOTS
	
#Define functions in main function
def load_data(filepath):
	'''load_data function loads the data by separating each chunk of data for a different observation time into a list called table. Input: file path to project data from antena array. Output: number of times loop ran, aka the number of observation periods'''
	
	import pandas as pd
	table= []
	
	#1. assign variables
	#length of data collected directly from antena array
	length_of_file = 12624
	#skipped rows is equal to the number of rows at the bottom of the antena data to skip
	skipped_footer = length_of_file
	#header row is equal to the row that contains the header for the first chunk of data
	header_row = 10
	#observation periods is a count variable that says how many times while loop ran
	#thus how many chunks of data there are separated by observation times
	observation_periods = 0
	
	#2. create while loop that runs through antena data
	while skipped_footer > 0:
		#shift the skipped footer down the length of the data
		skipped_footer -= 526
		#dataframe is the dataframe that contains the separated data
		dataframe = pd.read_table(filepath, sep='\s+', header=header_row, skipfooter=skipped_footer, engine='python')
		#appends the dataframe to the list
		table.append(dataframe)
		#Renamed Ampl(JY) to avoide syntax errors
		dataframe.columns=['Channel', 'IF', 'Polar', 'Frequency', 'Velocity', 'Amplitude', 'Phase']
		#converted Ampl from str(because of E) to float 
		dataframe['Amplitude']=dataframe[1:]['Amplitude'].astype(float)
		#converted Ampl from str(because of E) to float 
		header_row += 523
		#count each time list is ran through
		observation_periods+=1
		
	#checks how many times the while list ran and data chunks separated 
	print(observation_periods)
	
def make_phase_diagrams(table):
	'''make_phase_diagrams makes all the phase diagrams for every observation period. Input: table, defined above. Output: phase diagrams saved to file.'''
	
	#1. make for loop to go through each data chunk in the list, table
	for chunk in table:
		
		#2. Plot frequency vs. phase/ampl. for all times
        #use multi-pannel plots stacked on eachother since they share the same x-axis
        
        #make plots reasonable size
        plt.figure(figsize=(10,4))
        
        #3. top subplot is for phase data
        plt.subplot(2,1,1)
        #specify plot type and values
        plt.scatter(chunk.Frequency, chunk.Phase)
        #add y label
        plt.ylabel('Phase')
        #add title for both plots since they're stacked
        plt.title('Phase Diagram')
        
        #4. bottom subplot is for amplitude data 
        plt.subplot(2,1,2)
        #specify plot type and values
        plt.plot(chunk.Frequency, chunk.Amplitude)
        #add y label
        plt.ylabel('Amplitude')
        #add x label for both plots since they're stacked
        plt.xlabel('Frequency(MHz)')
        
        #5. save same phase diagram
        plt.savefig('/Users/sabrinadesoto/Documents/Sab_Final_Project/Data/Phase_Diagrams.pdf')
        plt.show()
        
main()
        
        
        
		 
	
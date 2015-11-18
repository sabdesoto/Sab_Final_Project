#11/16/2015 Sabrina DeSoto
#Computational Physics Final Project Script 1


#Define main function that will...

#Step0. Set up. Import Libraries
import pandas as pd 
import matplotlib.pyplot as plt
import sys
	
#Step1. Define arguments 
#enter filename for antena_data for first function
input_data_file = sys.argv[1]

#prefix to save all separated antena_data files
#data_chunk_name= sys.argv[2]
#prefix for saving all phase diagrams
#prefix= sys.argv[3]

#output_name for saving average signal phase data for all observation periods
output_name = sys.argv[2]

#Step2. Define variables	
#length of data collected directly from antena array
length_of_file = 12624
#empty list, called table, holds each chunk of data separated by observation time
table = []
#empty list to hold signal amplitudes
signal_ampl_list= []

def main():
	
	#Step3. load data separating each chunk of observation time
	load_data(input_data_file)
	
	#Step4. plot phase diagrams for each chunk of observation time
	make_phase_diagrams(table) 
	
	#Step5. get average signal phase and phase location 
	signal_phase(table)
	
#Define functions in main function
def load_data(input_data_file):
	'''load_data function loads the data by separating each chunk of data for a different observation time into a list called table. Input: file path to project data from antena array. Output: number of times loop ran, aka the number of observation periods'''
	
	#1. assign variables
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
		dataframe = pd.read_table(input_data_file , sep='\s+', header=header_row, skipfooter=skipped_footer, engine='python')
		#appends the dataframe to the list
		table.append(dataframe)
		#Renamed Ampl(JY) to avoide syntax errors
		dataframe.columns=['Channel', 'IF', 'Polar', 'Frequency', 'Velocity', 'Amplitude', 'Phase']
		#converted Ampl from str(because of E) to float 
		dataframe['Amplitude']=dataframe[1:]['Amplitude'].astype(float)
		#save sorted dataframe to cvs file wherever argv2 specifies
		dataframe.to_csv('Data/Analyzed_data/obv_period' + str(observation_periods) + 'data.csv', sep=',')
		#converted Ampl from str(because of E) to float 
		header_row += 523
		#count each time list is ran through
		observation_periods+=1
	
	assert observation_periods == 24, 'Loop should run 24 times, for 12hrs of observation time, divided into 30minute observation periods'
		
	#checks how many times the while list ran and data chunks separated 
	print('Number of observation periods in data:', observation_periods)
	return()
	
def make_phase_diagrams(table):
	'''make_phase_diagrams makes all the phase diagrams for every observation period. Input: table, defined above. Output: phase diagrams saved to file.'''
	
	#set count variable
	count=0
	
	#1. make for loop to go through each data chunk in the list, table
	for chunk in table:
		count+=1
		#2. Plot frequency vs. phase/ampl. for all times
        #use multi-pannel plots stacked on eachother since they share the same x-axis
        
        #make plots reasonable size
		plt.figure(figsize=(10,5))
        
        #3. top subplot is for phase data
		plt.subplot(2,1,1)
        #specify plot type and values
		plt.scatter(chunk.Frequency, chunk.Phase)
        #add y label
		plt.ylabel('Phase')
        #add title for both plots since they're stacked
		plt.title('Phase_Diagram_for_Observation_period_'+ str(count))
        
        #4. bottom subplot is for amplitude data 
		plt.subplot(2,1,2)
		#specify plot type and values
		plt.plot(chunk.Frequency, chunk.Amplitude)
        #add y label
		plt.ylabel('Amplitude')
        #add x label for both plots since they're stacked
		plt.xlabel('Frequency(MHz)')
        
        #5. save phase diagram separately using count variable 
		plt.savefig('Results/Plot_obv_period'+ str(count) +'.pdf')
		plt.close()

	assert count == 24, 'Loop should run 24 times, for 12hrs of observation time, divided into 30minute observation periods'

def signal_amplitude(data, column):
	'''Function that reads through amplitudes and returns amplitudes > constant threshold Input:dataframe, datafram.column output:list of amplitudes > threshold'''
	#signal is defined as pts over a threshold value
	#define threshold value (here I just assigned one but should be done by stats or something)
	threshold_ampl=0.010
    
	for values in column: 
		if values >= threshold_ampl:
			#put values into list
			signal_ampl_list.append(values)
	return(signal_ampl_list)
    	
def signal_phase(table):
	#create open lists for data
	#SA stores Signal Amplitude(SA) (Ampl>threshold) 
	SA = []
	#SD stores signal data (SD) (lines from table that correspond to a signal ampl)
	SD =[]
	#ASP stores average signal phase (ASP)  
	ASP =[]
	#add count variable to test function accuracy
	counts=0
    
	   
	for chunk in table:
    
		#1.)
		#run function on all data to get signal amplitudes
		signal_amplitude(chunk, chunk.Amplitude)
		#assign signal amplitudes to list SA
		x = signal_amplitude(chunk, chunk.Amplitude)
		sig_ampl=pd.DataFrame({'Amplitude':x})
		SA.append(sig_ampl)
    
		#2.)
		#merge all data with signal amps data (from step above) to get rows for detection ampl only
		signal_data= pd.merge(chunk, sig_ampl, on='Amplitude')
		SD.append(signal_data)
    
		#3.)
		#Average phase values
		Ave_phase=signal_data['Phase'].mean()
		#send values to a list
		ASP.append(Ave_phase)
		#save list of average phase value for each observation period to a dataframe
		ave_sig_phase=pd.DataFrame({'ave_phase':ASP}) 
		#make sure values are floats
		ave_sig_phase['ave_phase']=ave_sig_phase['ave_phase'].astype(float)
		#add phase location column to dataframe
		ave_sig_phase['Phase_location']=ave_sig_phase/360

		counts+=1
	#test function
	assert counts == 24, 'Loop should run 24 times, for 12hrs of observation time, divided into 30minute observation periods'
	
	#save dataframe as projects final output
	ave_sig_phase.to_csv('Results/Product_' + output_name + '.csv', sep=',')
	return()

     
main()
        
        
        
		 
	
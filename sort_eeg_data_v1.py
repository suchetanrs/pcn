import pandas as pd
import numpy as np
import csv
import time
import os


class SortEEGData():

    def __init__(self):
        #Edit if needed
        self.subject_info="04_Joh"
        self.required_cols=['Timestamp','EEG.Counter','EEG.AF3','EEG.F7','EEG.F3','EEG.FC5','EEG.T7','EEG.P7','EEG.O1','EEG.O2','EEG.P8','EEG.T8','EEG.FC6','EEG.F4','EEG.F8','EEG.AF4','EEG.RawCq']
        self.data_file_name="title_removed_Psychopy_04_Joh_2023-02-02T143022.383966_EPOCPLUS_157583_2023.02.02T14.30.22+05.30.md.mc.pm.fe.bp.csv"
        #Edit ended

        self.currwdir=os.getcwd()
        print("Current working directory: "+str(self.currwdir))
        self.data_folder=f"{self.currwdir}/Data/"
        self.file_path_data_file=f"{self.currwdir}/Data/{self.data_file_name}"

        self.df_marker_np=0
        self.df_eeg_data_np=0

        self.df_segregated_data=[[]]
        self.observation_no=0
        self.sort_start_time=time.time()


    def make_useful_epochs(self):
        df = pd.read_csv(self.file_path_data_file, usecols=self.required_cols)
        df.to_csv(f'{self.data_folder}/useful_channels_{self.subject_info}_.csv')

        return
    

    def segregate_marker_vals(self):
        file_path_marker=f"{self.data_folder}Psychopy_04_Joh_2023-02-02T143022.383966_EPOCPLUS_157583_2023.02.02T14.30.22+05.30_intervalMarker.csv"
        df_marker = pd.read_csv(file_path_marker)
        self.df_marker_np=df_marker.to_numpy()
        file_path_eeg_data=f'{self.data_folder}/useful_channels_{self.subject_info}_.csv'
        df_eeg_data=pd.read_csv(file_path_eeg_data)
        self.df_eeg_data_np=df_eeg_data.to_numpy()

        return
    

    def marker_segregated_data(self):
        timestart=0
        timeend=0
        for item in self.df_marker_np:
            if(item[3]==11):
                timestart=item[5]
            if(item[3]==22):
                timeend=item[5]
            if(timestart>0 and timeend>0):
                self.csv_segregated_write(timestart,timeend)
                timestart=0
                timeend=0
        file = open(f'{self.subject_info}_segregated_eeg_data.csv', 'w+', newline ='')
        with file:
            write = csv.writer(file)
            write.writerows(self.df_segregated_data)
        self.result_show()
        

    
    def csv_segregated_write(self,timestart,timeend):
        self.observation_no+=1
        print("Current observation number: "+str(self.observation_no))
        for item in self.df_eeg_data_np:
            if(item[1]>=timestart and item[1]<=timeend):
                self.df_segregated_data.append(item.tolist())
        self.df_segregated_data.append(['***Observation completed***',self.observation_no])

        return
    
    def result_show(self):
        self.sort_end_time=time.time()
        print("*********************************************************************")
        print("\n \n")
        print(f"Sorting completed of {self.subject_info}")
        print("Generated files:")
        print(f"{self.subject_info}_segregated_eeg_data.csv")
        print("")
        print("Time taken: "+str(self.sort_end_time-self.sort_start_time)+" secs!")
        print("Total number of observations: "+str(self.observation_no))
        
        return


    def main(self):
        self.make_useful_epochs()
        self.segregate_marker_vals()
        self.marker_segregated_data()

if __name__=="__main__":
    SortEEGData().main()
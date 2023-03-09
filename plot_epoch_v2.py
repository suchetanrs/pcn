import matplotlib.pyplot as plt
import pandas as pd
import csv
import os

class PlotGraph():
    def __init__(self):
        #Edit if needed
        self.sorted_csv_name="04_Joh_segregated_eeg_data.csv"
        self.required_channels=['type','marker_value','marker_id','Timestamp','EEG.AF3','EEG.F7','EEG.F3','EEG.FC5','EEG.T7','EEG.P7','EEG.O1','EEG.O2','EEG.P8','EEG.T8','EEG.FC6','EEG.F4','EEG.F8','EEG.AF4']
        self.NO_OTHER_CHANNELS=4
        self.TIMESTAMP_INDEX=3
        self.BASELINE=4200
        #Edit ended

        self.currwdir=os.getcwd()
        print("Current working directory: "+str(self.currwdir))
        self.file_path_data_file=f"{self.currwdir}/{self.sorted_csv_name}"
        self.df=0
        self.df_np=[]
        self.display_types=[]
        self.marker_id_types=[]
        self.signals=[]
        self.input_display=0
        self.input_markerid=0
        self.av_vals_arr=[]
        self.timestamps_arr=[]
        self.start_timestamp_flag=True
        self.start_timestamp=0

    def read_sorted_csv(self):
        self.df = pd.read_csv(self.file_path_data_file)
        self.df_np=self.df.to_numpy()
    
    def get_user_input_data(self):
        for item in self.df_np:
            if(item[0] in self.display_types)==False:
                self.display_types.append(item[0])
            if(item[2] in self.marker_id_types)==False:
                if (float('-inf') < float(item[2]) < float('inf')):
                    self.marker_id_types.append(item[2])
        
        print("You can choose from the following image combinations")
        for item in range(0,len(self.display_types)):
            print(str(item)+str(".")+str(self.display_types[item]))
        print("")
        self.input_display=int(input("Enter your choice: "))
        self.input_display_str=self.display_types[self.input_display]
        print("")
        print("")

        print("You can choose from the following marker IDs")
        for item in range(0,len(self.marker_id_types)):
            print(str(item)+str(". ")+str(self.marker_id_types[item]))
        print("")
        self.input_markerid=int(input("Enter your choice: "))
        self.input_markerid_str=self.marker_id_types[self.input_markerid]


        self.average_signals()
    
    def average_signals(self):
        df = pd.read_csv(self.file_path_data_file, usecols=self.required_channels)
        df_np=df.to_numpy()
        for item in df_np:
            sum=0
            av_val=0
            if(item[0]==self.input_display_str and item[2]==self.input_markerid_str):
                if(self.start_timestamp_flag==True):
                    self.start_timestamp=item[self.TIMESTAMP_INDEX]
                    self.start_timestamp_flag=False
                for x in range(self.NO_OTHER_CHANNELS,len(item)):
                    sum=sum+item[x]
                av_val=sum/(len(item)-self.NO_OTHER_CHANNELS)
                self.av_vals_arr.append(av_val)
                self.timestamps_arr.append((item[self.TIMESTAMP_INDEX]-self.start_timestamp))
    
    def plot_graph(self):
        plt.clf()
        for i in range(0,len(self.av_vals_arr)):
            self.av_vals_arr[i]=self.av_vals_arr[i]-self.BASELINE
        plt.plot(self.timestamps_arr,self.av_vals_arr)
        plt.grid()
        plt.pause(2)
            
    
    def main(self):
        self.read_sorted_csv()
        self.get_user_input_data()
        self.plot_graph()

        self.__init__()
        self.main()


if __name__=="__main__":
    PlotGraph().main()
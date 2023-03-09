import pandas as pd
import numpy as np
import csv
import utils
import os
import matplotlib.pyplot as plt

class BasicAnalysis():
    def __init__(self):
        self.currwdir=os.getcwd()
        self.required_cols=['Timestamp','EEG.O1','EEG.O2']
        # self.required_cols=['EEG.O1']
        self.data_file_name="test_mamaearth_chico.csv"
        self.file_path_data_file=f"{self.currwdir}/{self.data_file_name}"
        self.df_1 = pd.read_csv(self.file_path_data_file, usecols=self.required_cols)

        self.currwdir=os.getcwd()
        self.required_cols=['Timestamp','EEG.O1','EEG.O2']
        # self.required_cols=['EEG.O1']
        self.data_file_name="test_chicco_mamearth.csv"
        self.file_path_data_file=f"{self.currwdir}/{self.data_file_name}"
        self.df_2 = pd.read_csv(self.file_path_data_file, usecols=self.required_cols)

    def dc_offset(self,df_pass):
        self.df_np=df_pass.to_numpy()
        self.signal_1_o1=[]
        self.signal_1_o2=[]
        self.time_data=[]
        for item in self.df_np:
            self.signal_1_o1.append(item[1])
            self.signal_1_o2.append(item[2])
            self.time_data.append(item[0])
        self.signal_1_o1=utils.butter_highpass_filter(self.signal_1_o1,0.16,250)
        self.signal_1_o2=utils.butter_highpass_filter(self.signal_1_o2,0.16,250)
        # plt.subplot(2,1,1)
        # plt.plot(self.signal_1_o1)
        # plt.subplot(2,1,2)
        # plt.plot(self.signal_1_o2)
        # plt.show()
        print(len(self.signal_1_o2))
        return (self.signal_1_o1-self.signal_1_o2)

    
    def PCN(self):
        pass

    def time_fix(self,time_data):
        init_time=time_data[0]
        for item in range(0,len(time_data)):
            time_data[item]=time_data[item]-init_time
        return time_data


    def main(self):
        temp1=self.dc_offset(self.df_1)
        temp2=self.dc_offset(self.df_2)
        temp2_sorted=[]
        time_sorted=self.time_fix(self.time_data)
        for item in range(0,len(temp2)):
            temp2_sorted.append(temp2[item])
            if(item==1760):
                break
        print(len(temp2_sorted))

        # print(temp1)
        plt.plot(time_sorted,(-(temp1-temp2_sorted)/2))
        plt.show()
        


if __name__=="__main__":
    BasicAnalysis().main()
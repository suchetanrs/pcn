*****sort_eeg_data.py*****

For running sort_eeg_data.py ensure the following:

1. Remove the "title" line (first line) of the csv file and save the csv file seperately. This line is different from the column names.

2. Place the sort_eeg_data.py in an empty folder.
3. Make a "Data" folder inside that folder.
4. Place the EEG data file with the title removed and interval file inside the "Data" folder.
5. Make sure the first three variables in __init__ function of sort_eeg_data.py are correct.
6. Run the sort_eeg_data.py file using Python3.


Version history and changes:
V2:
1. Headers added to the segregated files.
2. The required columns from identity marker file are to be edited in __init__ of sort_eeg_data.py
3. The marker file's name is now available for changes in __init__.

V3:
1. Header files column alignment fixed
2. The number of observations required can be set in the __init__ function.


*****plot_epoch.py*****

VFor running plot_epoch.py ensure the following:
1. self.sorted_csv_name, self.required_channels. Don't edit the first four.
2. The program runs in a loop, takes 2 to 3 seconds to plot and then you can enter your choices again.

V2:
1. The value of baseline can be set in self.BASELINE in the __init__ function.
2. This value is subtracted sequentially and plotted
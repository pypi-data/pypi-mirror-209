# Dataloader for reading real time sensor data from DHMS server
# Author: Daijie Bao 
# Date: 2023-04-13
# Belongs to: DHMS AI Team 

# Import necessary libraries 
from read_util.read import read_local_file
import pandas as pd 
import os

# Create a function to read aiff data into pandas data frame 
def convert_aiff_to_df(data_source: str, sensor_name: str)-> pd.DataFrame:
    """
    Convert aiff vibration sensor data source to pandas dataframe
    :param data_source: path to data source on local computer 
    :param sensor_name: collect point which user want to name it 
    :return data_frame: a pandas DataFrame which contains converted data from aiff
    """
    src  = read_local_file(data_source)
    data = src.data
    data_frame = pd.DataFrame(data, columns=[sensor_name])
    return data_frame

# Creata a function to read aiff data and save it as csv file on local machine 
def save_aiff_as_csv(data_source: str, data_save: str, sensor_name: str) -> None:
    """
    Read aiff file from DHMS server and save it as csv file
    :param data_source: the path of aiff file
    :param data_save: the path of csv file
    :param sensor_name: the name of vibration sensor
    :return: None
    """
    for filename in os.listdir(data_source):
        print('Current Working on File: ', filename)
        file_path = os.path.join(data_source, filename)
        src = read_local_file(file_path)
        data = src.data
        df = pd.DataFrame(data, columns=[sensor_name])
        df.to_csv(os.path.join(data_save, filename + '.csv'), index=False)
    print('All Files have been saved as csv file')

# Create a function to read aiff data into pandas data frame and also add time index
def convert_aiff_to_df_include_time(data_source: str, data_name: str)-> pd.DataFrame:
    """
    Convert aiff vibration sensor data source to pandas dataframe
    :param data_source: path to data source on local computer 
    :param data_name: collect point which user want to name it 
    :return data_frame: a pandas DataFrame which contains converted data from aiff
    """
    src  = read_local_file(data_source)
    start_time = src.time 
    time_interval = src.delta
    freq_microsec = time_interval * 1000000
    freq_string = f"{freq_microsec}U"
    num_points = src.length
    data = src.data
    date_index = pd.date_range(start_time, periods=num_points, freq=freq_string)
    data_frame= pd.DataFrame(index=date_index)
    data_frame[data_name] = data
    return data_frame

# Creata a function to read aiff data and save it as csv file on local machine and also add time index
def save_aiff_as_csv_include_time(data_source: str, data_save: str, data_name: str) -> None:
    """
    Read aiff file from DHMS server and save it as csv file
    :param data_source: the path of aiff file
    :param data_save: the path of csv file
    :param data_name: the name of vibration sensor
    :return: None
    """
    for filename in os.listdir(data_source):
        print('Current Working on File: ', filename)
        file_path = os.path.join(data_source, filename)
        src = read_local_file(file_path)
        start_time = src.time
        time_interval = src.delta
        freq_microsec = time_interval * 1000000
        freq_string = f"{freq_microsec}U"
        num_points = src.length
        data = src.data
        date_index = pd.date_range(start_time, periods=num_points, freq=freq_string)
        df = pd.DataFrame(index=date_index)
        df[data_name] = data
        df.to_csv(os.path.join(data_save, filename + '.csv'), index=True, index_label='time')
    print('All Files have been saved as csv file')
    
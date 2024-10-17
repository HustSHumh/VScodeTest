import os 
import numpy as np
import pandas as pd 
import torch
from cfg import cfg4washing





class DataWashing():

    def __init__(self) -> None:
        pass

    def norm_feature(self, feature_ls):
        '''
        归一化
        '''
        pass

    def ctnorm_feature(self, feature_ls):
        '''
        还原
        '''
        pass


_cfg = cfg4washing()
df_base_data = pd.read_csv('D:\python root\project root\\test\data\A榜-训练集_海上风电预测_基本信息.csv',
                       encoding='gbk')

df_base_data = df_base_data.rename(
    columns={
        '站点名称' : 'name',
        '站点编号' : 'id',
        '地区' : 'position',
        '装机容量(MW)' : 'capacity'
    }
)

df_value_data = pd.read_csv('D:\python root\project root\\test\data\A榜-训练集_海上风电预测_气象变量及实际功率数据.csv',
                            encoding='gbk')

num_feature = _cfg.num_feature

df_value_data = df_value_data.rename(columns=
                                     {
                                         '站点编号' : 'id',
                                         '时间' : 'time',
                                         '气压(Pa）': 'Pa',
                                         '相对湿度（%）' : 'humi',
                                         '云量' : 'cloud',
                                         '10米风速（10m/s）' : '10fs',
                                         '10米风向（°)' : '10fx',
                                         '温度（K）' : 'temp',
                                         '辐照强度（J/m2）' : 'radi',
                                         '降水（m）' : 'js',
                                         '100m风速（100m/s）' : '100fs',
                                         '100m风向（°)' : '100fx',
                                         '出力(MW)' : 'power'
                                     })
df_value_data = df_value_data.loc[df_value_data['power'] != '<NULL>', :]
# print(df_value_data.shape)
df_value_data['power'] = pd.to_numeric(df_value_data['power'])
df_value_data['time'] = pd.to_datetime(df_value_data['time'])
df_value_data['10fs3'] = df_value_data['10fs'] ** 3
df_value_data['100fs3'] = df_value_data['100fs'] ** 3
df_value_data['10fx'] = df_value_data['10fx'] * np.pi / 360
df_value_data['100fx'] = df_value_data['100fx'] * np.pi / 360
df_value_data['10fx_sin'] = np.sin(df_value_data['10fx'])
df_value_data['10fx_cos'] = np.cos(df_value_data['10fx'])
df_value_data['100fx_sin'] = np.sin(df_value_data['100fx'])
df_value_data['100fx_sin'] = np.cos(df_value_data['100fx'])

dict_station_value = {}
dict_station_norm = {}
dict_station_value_max = {}
dict_station_value_min = {}
dict_station_value_mean = {}


# 按站点进行归一化
for i in range(1, 6):
    station_id = 'f{}'.format(i)
    # 容量归一化
    station_capacity = df_base_data.loc[df_base_data['id'] == station_id, 'capacity']
    station_value = df_value_data.loc[df_value_data['id'] == station_id, :].copy()
    dict_station_value = station_value
    df_value_data.loc[df_value_data['id'] == station_id, 'power'] = station_value['power'] / station_capacity
    # 其他归一化
    df_value_max = station_value[num_feature].max(axis=0)
    df_value_min = station_value[num_feature].min(axis=0)
    dict_station_value_max[station_id] = df_value_max
    dict_station_value_min[station_id] = df_value_min
    df_station_norm = (station_value[num_feature] - df_value_min) / (df_value_max - df_value_min) * \
                       (_cfg.norm_uplimit - _cfg.norm_downlimit) + _cfg.norm_downlimit
    

    # dict_station_norm[station_id] = df_station_norm

# print(_cfg.get_cfg())
print(df_station_norm.head())
df_value_data_f2 = df_value_data.loc[df_value_data['id'] == 'f2']



print(df_value_data_f2['10fx'].max())







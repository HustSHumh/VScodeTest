import numpy as np
import pandas as pd 
import torch
import os 


f2_capacity = pd.read_csv('D:\python root\project root\\test\data\A榜-测试集_海上风电预测_基本信息.csv', 
                          encoding='gbk').loc[1, '装机容量(MW)']





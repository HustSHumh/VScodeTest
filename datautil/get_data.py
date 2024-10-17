import pandas as pd
import os 

data_work_path = 'D:\python root\project root\\test'


def get_train_data():
    data_dir_path = os.path.join(data_work_path, 'data')
    df_train = pd.read_csv(os.path.join(data_dir_path, 'A榜-训练集_海上风电预测_气象变量及实际功率数据.csv'), encoding='gbk')
    return df_train

def get_test_data():
    data_dir_path = os.path.join(data_work_path, 'data')
    df_test = pd.read_csv(os.path.join(data_dir_path, 'A榜-测试集_海上风电预测_气象变量数据.csv'), encoding='gbk')
    return df_test

def get_train_add_data():
    data_dir_path = os.path.join(data_work_path, 'data')
    df_train_add_data = pd.read_csv(os.path.join(data_dir_path, 'A榜-训练集_海上风电预测_基本信息.csv'), encoding='gbk')
    return df_train_add_data

def get_test_add_data():
    data_dir_path = os.path.join(data_work_path, 'data')
    df_test_add_data = pd.read_csv(os.path.join(data_dir_path, 'A榜-测试集_海上风电预测_基本信息.csv'), encoding='gbk')
    return df_test_add_data

if __name__ == '__main__':
    df = get_train_data()
    print(df.head())
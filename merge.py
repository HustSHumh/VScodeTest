import pandas as pd
import numpy as np
import os

ans_dir_path = 'ans'
cqq_dir_path = os.path.join(ans_dir_path, 'ans_cqq')
qhx_dir_path = os.path.join(ans_dir_path, 'ans_qhx')

cqq_file_path = os.path.join(cqq_dir_path, 'lgb_base_0.04826.csv')
qhx_file_path = os.path.join(qhx_dir_path, 'A_submit_example_t8_UTF-8.csv')


df_cqq_data = pd.read_csv(cqq_file_path, encoding='utf-8')
print(df_cqq_data.head())



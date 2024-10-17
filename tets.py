import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
# import torch

def sort1(ls):
    leng = len(ls)
    for i in range(len(ls)):
        max_it = ls[0]
        max_idx = 0
        for j in range(len(ls) - i):
            if ls[j] > max_it:
                max_it = ls[j]
                max_idx = j
        temp_it = ls[len(ls) - i - 1]
        ls[max_idx] = temp_it
        ls[len(ls) - i - 1] = max_it
    return ls

ls1 = [1, 3, 5, 2, 2, 3, 4, 5, 6, 11,10,23, 60 ]
print(sort1(ls1))

        


# def norm(x):
#     mu = x.mean()
#     sigma = x.std()
#     return (x-mu) / sigma


# df_loc1 = pd.DataFrame()
# df_loc1['jd'] = 100 * np.random.random(100)
# df_loc1['wd'] = 20 * np.random.random(100)

# print(df_loc1['jd'].apply(lambda x: round(x, 3)))

# df_loc2 = pd.DataFrame()
# df_loc2['jd'] = 100 * np.random.random(100)
# df_loc2['wd'] = 20 * np.random.random(100)

# def get_oid_centers(dict_oid, k=5):
#     dic_oid_center_jd = {}
#     dic_oid_center_wd = {}
#     for oid, values in dict_oid.items():
#         data_ = norm(values[['jd', 'wd', 'capacity']])
#         model = KMeans(n_clusters=k, n_init=10)
#         model.fit(data_)
#         label_pred = model.labels_
#         values['label'] = label_pred
#         dic_oid_center_jd[oid] = []
#         dic_oid_center_wd[oid] = []
#         # TODO check the KMeans results
#         for i in range(k):
#             label_station = values.loc[values['label'] == i, :]
#             dic_oid_center_jd[oid].append((label_station['jd'] * label_station['capacity']).sum() / label_station['capacity'].sum())
#             dic_oid_center_wd[oid].append((label_station['wd'] * label_station['capacity']).sum() / label_station['capacity'].sum())
#     return dic_oid_center_jd, dic_oid_center_wd
        

# # dic_oid_center_jd, dic_oid_center_wd = get_oid_centers(dict_oid=dict_oid)
# # oid_pred_ls = []
# # for oid, df_oid in df_power.groupby('oid'):
# #     df_center_points = pd.DataFrame()
# #     df_center_points['jd'] = dic_oid_center_jd[oid]
# #     df_center_points['wd'] = dic_oid_center_wd[oid]
# #     df_jiutian_ = sumilate_curve3(df_center_points, df_jiutian_data, 'jiutian')
# #   TODO feature engineering
    




# estimator = KMeans(n_clusters=5, n_init=10)
# estimator.fit(df_loc1)#聚类
# label_pred = estimator.labels_ #获取聚类标签
# centroids = estimator.cluster_centers_ #获取聚类中心
# inertia = estimator.inertia_ # 获取聚类准则的总和


# # print(norm(df_loc2[['jd', 'wd']]))
# # print(df_loc2[['jd', 'wd']].std())



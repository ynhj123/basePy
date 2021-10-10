import numpy as np
import pandas as pd
import scipy

if __name__ == '__main__':
    # Pearson系数的取值范围为[-1,1]，
    # 当值为负时，为负相关，当值为正时，为正相关，绝对值越大，则正/负相关的程度越大。
    # 若数据无重复值，且两个变量完全单调相关时，spearman相关系数为+1或-1。
    # 当两个变量独立时相关系统为0，但反之不成立
    aa = np.array([2, 3, 9, 6, 8])
    bb = np.array([5, 6, 3, 7, 9])
    cc = np.array([aa, bb])
    print(cc)

    cc_mean = np.mean(cc, axis=0)  # axis=0,表示按列求均值 ——— 即第一维
    cc_std = np.std(cc, axis=0)
    cc_zscore = (cc - cc_mean) / cc_std  # 标准化

    cc_zscore_corr = np.corrcoef(cc_zscore)  # 相关系数矩阵
    print(cc_zscore_corr)

    cc_pd = pd.DataFrame(cc_zscore.T, columns=['c1', 'c2'])
    cc_corr = cc_pd.corr(method='pearson')  # 相关系数矩阵
    print(cc_corr['c1'])  # 某个因子与其他因子的相关系数
    print(cc_pd.c1.cov(cc_pd.c2))  # 协方差
    print(cc_pd.c1.corr(cc_pd.c2))  # 两个因子的相关系数
    y_cov = cc_pd.cov()  # 协方差矩阵
    x = [2, 3, 9, 6, 8]
    y = [5, 6, 3, 7, 9]

    df = pd.DataFrame({'x': x, 'y': y})
    # print(df.x.corr(df.y))
    # print(df.x.corr(df.y, method='spearman'))
    # print(df.x.corr(df.y, method='kendall'))
    # print(df.corr())
    # print(df.corr('spearman'))
    # print(df.corr('kendall'))
    print(scipy.stats.pearsonr(x, y))
    print(scipy.stats.spearmanr(x, y))
    print(scipy.stats.kendalltau(x, y))
    # 总结 相关性绝对值越大 显著性越小 越相关

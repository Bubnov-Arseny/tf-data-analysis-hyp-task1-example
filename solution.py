import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 700385968 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = proportions_ztest([y_success, x_success], [y_cnt, x_cnt], alternative = 'larger')
    if (pval < 0.09):
      ans = True
    else:
      ans = False
    return ans

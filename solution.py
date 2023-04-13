import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 845786312 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return ks_2samp(x, y, alternative="two-sided").pvalue < 0.02 # Ваш ответ, True или False

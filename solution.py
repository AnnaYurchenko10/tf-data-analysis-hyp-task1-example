import pandas as pd
import numpy as np
from scipy import stats

chat_id = 762047857 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Рассчитываем доли успешных продаж
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    # Рассчитываем стандартную ошибку разности
    se = np.sqrt(p1*(1-p1)/x_cnt + p2*(1-p2)/y_cnt)
    
    # Рассчитываем Z-статистику
    z = (p1 - p2) / se
    
    # Определяем критическое значение Z для уровня значимости 0.05
    # Двусторонная критическая область
    critical_value = stats.norm.ppf(0.975) 
               
    # Сравниваем Z-статистику с критическим значением
    return z > critical_value

"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def optimal_predict(number: int = 1) -> int:
    """ Угадываем число с минимизацией числа попыток 
        посредством многократного разделения зоны поиска пополам и
        сравнением полученного среднего числа с загаданным. 
        По итогам сравнения меняем минимальное или максимальное число
        на расчитанное серединное зоны и запускаем новый цикл,
        в котором ищем очередную середину зоны и сравниваем
        с загаданным числом

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min_number, max_number = 1, 101 # задаем стартовый диапазон чисел для проверки вхождения
    mid_number = 0 # заведомо задаем проверяемое число вне диапазона, чтобы начать цикл
    
    # цикл сравнивает середину проверяемого диапазона с искомым числом     
    while mid_number != number:
        count += 1
        mid_number = round((max_number+min_number) / 2) # находим середину проверяемого диапазона        
        if number > mid_number:
            min_number = mid_number # задаем новую нижнюю границу диапазона
        elif number < mid_number:
            max_number = mid_number # задаем новую верхнюю границу диапазона           
    return count


def score_game(optimal_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(optimal_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(optimal_predict)
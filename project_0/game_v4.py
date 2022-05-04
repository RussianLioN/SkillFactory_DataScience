"""Игра угадай число
Компьютер сам загадывает число и сам угадывает число
"""

import numpy as np


def game_core_v2(number: int = 1) -> int:
    """
    Угадываем число с корректировкой диапазона поиска.
    Сравниваем угадываемое число (очередную попытку)
    с загаданным и корректируем диапазон поиска
    по результатам сравнения

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min_limits = 0 # Стартовый диапазон поиска - граница минимума
    count = 1   # стартовый счетчик. Равен 1, так как первый поиск 
                # делается до запуска цикла
    max_limits = 101 # Стартовый дипазон поиска - граница максимума
    predict = np.random.randint(min_limits, max_limits) 
    
    while number != predict:
        count += 1
        if number > predict:
            min_limits = predict            

        elif number < predict:
            max_limits = predict
            
        predict = np.random.randint(min_limits, max_limits)

    return count
    
def score_game(game_core_v2) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v2 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали списоконлайн переводчик чисел

    for number in random_array:
        count_ls.append(game_core_v2(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

    
if __name__ == "__main__":
    # RUN    
    score_game(game_core_v2)
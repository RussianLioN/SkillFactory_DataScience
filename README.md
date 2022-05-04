# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](#описание-проекта)  
[2. Какой кейс решаем?](#какой-кейс-решаем)  
[3. Краткая информация о данных](#краткая-информация-о-данных)  
[4. Этапы работы над проектом](#этапы-работы-над-проектом)  
[5. Результат](#результаты)    
[6. Выводы](#выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

⤒ [к оглавлению](#оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Для работы кода используются модули:

    game_v2.py
    game_v3.py
    game_v4.py
а также основной файл ноутбука:

    game.ipynb
в котором производится вызов всех модулей(файлов) проекта и выводится результат со средним количеством попыток угадываний для каждого метода
  
⤒ [к оглавлению](#оглавление)


### Этапы работы над проектом  
1. Создан стартовый учебный модуль 

        game_v2.py
    в котором создан алгоритм случайного угадывания
2. Создан модуль 

        game_v3.py
    оптимальным количеством попыток угадать загаданное число
3. Создан модуль

        game_v4.py
    в котором реализован метод угадывания числа с коррекцией диапазона. 
4. Оформлен файл ноутбука

        game.ipynb
    в котором импотрируются необходимые модули и вызываются функции из импортированных модулей

⤒ [к оглавлению](#оглавление)


### Результаты:  
По итогам тестирования лучший алгоритм по поиску загаданного числа является алгоритм, использованный в модуле 

        game_v3.py
В котором используется проверка среднего числа искомого диапазон

⤒ [к оглавлению](#оглавление)


### Выводы:  
Использование алгоритма деления диапазона пополам и проверки вычисленного среднего числа с загаданным числом дает самый лучший результат по количеству попыток "угадывания" числа. Фактически используется не угадывание, а расчет этого числа, путем отбрасывания сразу половины числового порядка. 

⤒ [к оглавлению](#оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
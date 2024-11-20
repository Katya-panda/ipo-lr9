class RectCorrectError(Exception):
    # определяем пользовательское исключение для некорректных прямоугольников
    pass
def isCorrectRect(rect):
    # проверяем, что список содержит ровно два элемента (кортежа)
    if len(rect) != 2:
        return False
    # извлекаем координаты из переданных кортежей
    (x1, y1), (x2, y2) = rect
    # проверяем, что координаты левого нижнего угла меньше координат верхнего правого угла
    return x1 < x2 and y1 < y2
def intersectionAreaRect(rect1, rect2):
    # проверяем корректность первого прямоугольника
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    # проверяем корректность второго прямоугольника
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")
    # извлекаем координаты углов прямоугольников
    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2
    # вычисляем координаты пересечения
    x_left = max(x1_min, x2_min)  # левая граница пересечения
    y_bottom = max(y1_min, y2_min)  # нижняя граница пересечения
    x_right = min(x1_max, x2_max)  # правая граница пересечения
    y_top = min(y1_max, y2_max)  # верхняя граница пересечения
    # вычисляем ширину и высоту области пересечения
    width = x_right - x_left
    height = y_top - y_bottom
    # если прямоугольники не пересекаются, ширина или высота будут отрицательными или нулевыми
    if width < 0 or height < 0:
        return 0
    # вычисляем площадь пересечения
    return width * height
def intersectionAreaMultiRect(rects):
    # проверяем корректность каждого прямоугольника в списке
    for i, rect in enumerate(rects):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"{i + 1}й прямоугольник некоректный")
    # начинаем с площади первого прямоугольника
    total_area = 0
    # перебираем все пары прямоугольников
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            # вычисляем площадь пересечения для текущей пары прямоугольников
            intersection_area = intersectionAreaRect(rects[i], rects[j])
            total_area += intersection_area
    return total_area
# примеры использования
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
try:
    result = intersectionAreaMultiRect(rectangles)
    print(f"Уникальная площадь пересечения: {result}")  
except RectCorrectError as e:
    print(e)
# пример с некорректным прямоугольником
incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]  # некорректный прямоугольник
]
try:
    intersectionAreaMultiRect(incorrect_rectangles)  # ожидается ошибка
except RectCorrectError as e:
    print(e)
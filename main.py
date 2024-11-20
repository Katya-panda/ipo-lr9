from collision.functions import (
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect,
    RectCorrectError
)
def main():
    # пример использования функции isCorrectRect
    print("Пример использования функции isCorrectRect")
    print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  # выводит True
    print(isCorrectRect([(-7, 9), (3, 6)]))       # выводит False
    # пример использования функции isCollisionRect
    print("\nПример использования функции isCollisionRect")
    try:
        print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))  # выводит True
        print(isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))              # выводит False
        print(isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))             # ожидается ошибка
    except RectCorrectError as e:
        print(e)
    # пример использования функции intersectionAreaRect
    print("\nПример использования функции intersectionAreaRect")
    try:
        print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))  # выводит: Положительное число
        print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))      # выводит: 0
        print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))     # ожидается ошибка
    except RectCorrectError as e:
        print(e)
    # пример использования функции intersectionAreaMultiRect
    print("\nПример использования функции intersectionAreaMultiRect")
    rectangles = [
        [(-3, 1), (9, 10)],
        [(-7, 0), (13, 12)],
        [(0, 0), (5, 5)],
        [(2, 2), (7, 7)]
    ]
    try:
        result = intersectionAreaMultiRect(rectangles)
        print(f"Уникальная площадь пересечения: {result}")  # ожидаемый результат: Площадь пересечения прямоугольников
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
if __name__ == "__main__":
    main()
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Пример использования:
if __name__ == "__main__":
    # Ввод данных от пользователя
    nums = list(map(int, input("Введите элементы массива через пробел: ").split()))
    target = int(input("Введите целевое значение: "))

    # Поиск индекса целевого значения
    result = binary_search(nums, target)

    # Вывод результата
    if result != -1:
        print(f"Индекс целевого значения {target}: {result}")
    else:
        print(f"Целевое значение {target} не найдено в массиве.")

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

def sort_array(nums):
    return sorted(nums)

def validate_input(nums, target):
    if not (1 <= len(nums) <= 10**4):
        raise ValueError("Длина массива должна быть в диапазоне от 1 до 10^4.")
    if any(not (-10 <= num <= 10**4) for num in nums):
        raise ValueError("Элементы массива должны быть в диапазоне от -10 до 10^4.")
    if not (-10 <= target <= 10**4):
        raise ValueError("Целевое значение должно быть в диапазоне от -10 до 10^4.")
    if len(nums) != len(set(nums)):
        raise ValueError("Все элементы массива должны быть уникальными.")

# Пример использования:
if __name__ == "__main__":
    # Ввод данных от пользователя
    nums = list(map(int, input("Введите элементы массива через пробел: ").split()))
    target = int(input("Введите целевое значение: "))

    # Проверка ограничений
    validate_input(nums, target)

    # Сортировка массива (хотя массив уже должен быть отсортирован)
    nums = sort_array(nums)
    print(f"Отсортированный массив: {nums}")

    # Поиск индекса целевого значения
    result = binary_search(nums, target)

    # Вывод результата
    if result != -1:
        print(f"Индекс целевого значения {target}: {result}")
    else:
        print(f"Целевое значение {target} не найдено в массиве.")
        print("-1")

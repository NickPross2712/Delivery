def min_platforms(weights: list[int], limit: int) -> int:
    weights.sort()

    left: int = 0
    right: int = len(weights) - 1
    platforms: int = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms


if __name__ == '__main__':
    input_weights: str = input('Вес отдельных роботов: ')
    weights: list[int] = [int(weight) for weight in input_weights.split()]
    limit: int = int(input('Предельная грузоподъемность платформы: '))
    result: int = min_platforms(weights, limit)
    print('Необходимое количество платформ:', result)

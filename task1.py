"""Напишите программу, которая выводит n первых элементов последовательности 122333444455555…
(число повторяется столько раз, чему оно равно)."""

def first_elements(n: int) -> list:

    result = []
    num = 1
    count = 0

    while count < n:
        for _ in range(num):
            if count >= n:
                break
            result.append(num)
            count += 1
        num += 1

    return result

assert first_elements(10) == [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], "неверный результат"
assert first_elements(1) == [1], "неверный результат"
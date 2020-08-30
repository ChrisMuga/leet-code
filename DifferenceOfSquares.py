def solution(N):
    """
        Given a number,
        compute difference
        between the sum of the squares
        of all natural numbers up to and including the number,
        and the square of the sum of the same numbers.
    """
    total = 0
    sum_of_squares = 0
    for x in range(N + 1):
        sum_of_squares += x ** 2
        total += x
    return sum_of_squares - (total ** 2)


values = [1, 4, 56, 78, 99, 78, 44, 33, 1000, -1000]
for value in values:
    print(solution(value))

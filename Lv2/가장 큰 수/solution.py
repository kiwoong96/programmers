def solution(numbers):
    answer = ''
    # numbers = [0,0,0,0,0]
    new_numbers = [[] for _ in range(len(numbers))]
    for i in range(len(numbers)):
        new_numbers[i] = [int((str(numbers[i]) * 4)[:4]), i]

    new_numbers.sort(reverse=True)
    for data in new_numbers:
        answer += str(numbers[data[1]])

    # print(new_numbers)
    return str(int(answer))

def list_of_multiples(num, length):
    result = []
    for i in range(length):
        current_result = num * (i + 1)
        result.append(current_result)

    print(result)

list_of_multiples(7,5)
list_of_multiples(12,10)
list_of_multiples(17,6)
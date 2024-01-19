#Дан одномерный массив целых чисел. Напишите скрипт нахождения суммы максимальной по длине возрастающей последовательности за один проход по массиву.

def max_increasing_sequence(arr):
    current_len = 1
    max_len = 1 
    start_index = 0 
    max_start_index = 0  

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start_index = start_index
            start_index = i
            current_len = 1

    max_sequence = arr[max_start_index:max_start_index + max_len]  #максимальная по длине возрастающая последовательность

    return max_sequence

def sum_of_sequence(seq):
    return sum(seq)

arr = [1, 5, 3, 4, 5, 6, 7, 4, 7, 10, 90, 20, 2, 40, 42]
max_seq = max_increasing_sequence(arr)
sum_of_max_seq = sum_of_sequence(max_seq)
print("Максимальная по длине возрастающая последовательность:", max_seq)
print("Сумма этой последовательности:", sum_of_max_seq)
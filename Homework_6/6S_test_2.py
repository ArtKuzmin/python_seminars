#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
#  список повторяемых и убрать дубликаты из заданной последовательности.

num_sequence = [1, 2, 3, 5, 1, 5, 3, 10]
duplicate_seq = []
[duplicate_seq.append(x) for x in num_sequence if num_sequence.count(x) > 1]
unique_seq = []
[unique_seq.append(x) for x in num_sequence if num_sequence.count(x) == 1]
print(unique_seq)
print(list(set(duplicate_seq)))
print(list(set(num_sequence)))





#Вопрос 1
is_even = lambda num: num % 2 == 0
print(is_even(2))
print(is_even(3))

#Вопрос 2
import array
import time

class bitBuf: # использование битовых операций
    def __init__(self, size):
        self.buffer = [0] * (size // 32 + 1)
        self.mask = (1 << 32) - 1
        self.head = 0
        self.tail = 0
        self.size = size

    def enqueue(self, item):
        index = self.tail // 32
        shift = self.tail % 32
        self.buffer[index] |= (item & self.mask) << shift
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        index = self.head // 32
        shift = self.head % 32
        item = (self.buffer[index] >> shift) & self.mask
        self.head = (self.head + 1) % self.size
        return item

class arrBuf: # использование массива
    def __init__(self, size, typecode='i'):
        self.buffer = array.array(typecode, [0] * size)
        self.head = 0
        self.tail = 0
        self.size = size

    def enqueue(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        return item

# Тестирование битовых операций
buffer_size = 1000000
buffer = bitBuf(buffer_size)

start_time = time.time()
for i in range(buffer_size):
    buffer.enqueue(i)
    buffer.dequeue()
end_time = time.time()

print("Время выполнения (битовые):", end_time - start_time)

# Тестирование исп массива array
buffer_size2 = 1000000
buffer2 = arrBuf(buffer_size2)

start_time = time.time()
for i in range(buffer_size2):
    buffer2.enqueue(i)
    buffer2.dequeue()
end_time = time.time()

print("Время выполнения (массив):", end_time - start_time)

#Вопрос 3
import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        rndel = arr[0]
        less = [x for x in arr[1:] if x <= rndel]
        greater = [x for x in arr[1:] if x > rndel]
        return quicksort(less) + [rndel] + quicksort(greater)

my_list = [random.randint(0, 1000) for _ in range(10000)]
print("Начальный массив: ", my_list)
start_time = time.time()
sorted_list = quicksort(my_list)
end_time = time.time()

print("Время сортировки:", end_time - start_time)
print("Отсортированный массив", sorted_list)
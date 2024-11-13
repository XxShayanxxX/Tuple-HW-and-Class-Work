tuple1 = (2, 3, 4)
tuple2 = (5, 6, 7)


result = tuple(tuple1[i] * tuple2[i] for i in range(len(tuple1)))

print(result)

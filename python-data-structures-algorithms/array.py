import numpy as np

arr = [32, "python", 44]
print([x for x in arr])


names: list[str] = ["alisson", "oliveira", 33]
print([x for x in names])


typed_array = np.array([10, 2, 3, 4], dtype=np.int32)
print(typed_array)
samp_array = [2,4,6,-8]
samp_value = 5


middle_idx = int(len(samp_array) / 2)
print(middle_idx)


def insert_shift_array(a, v, index):
    return a[:index] + [v] + a[index:]

final = insert_shift_array(samp_array, samp_value, middle_idx)
print(final)



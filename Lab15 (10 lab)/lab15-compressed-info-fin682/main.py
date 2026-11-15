#lab15-compressed-info-fin682
import numpy as np

def encode_data(arr1, arr2):
    diff = np.array(arr1) - np.array(arr2)

    encoding = []
    count = 1

    for i in range(1, len(diff)):
        if diff[i] == diff[i - 1]:
            count += 1
        else:
            encoding.append((int(diff[i - 1]), count))
            count = 1

    encoding.append((int(diff[-1]), count))

    return encoding

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

out_enc = encode_data(arr1, arr2)

print('Sender sent:')
print(' First input: ', end='')

for v in arr1: 
    print(v, end=' ')
print()

print(f' Encode data: {out_enc}')

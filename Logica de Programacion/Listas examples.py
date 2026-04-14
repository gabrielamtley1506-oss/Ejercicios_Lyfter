nums = [3, 7, 7, 1, 9]

print(nums[0])          # primer elemento
print(nums[-1])         # último elemento

nums.append(5)          # agrega al final
print(nums)

ultimo = nums.pop()     # saca y devuelve el último
print("saco:", ultimo, "queda:", nums)

print(nums[1:4])        # slice (del index 1 al 3)
print(nums.count(7))    # cuántas veces aparece 7

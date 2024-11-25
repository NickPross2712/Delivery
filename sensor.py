def operations(generation):
    if generation == 0 or generation == 1:
        return 1
    else:
        return operations(generation - 1) + operations(generation - 2)

generation_number = int(input())

print(operations(generation_number))

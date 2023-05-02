# Direction reduction


def dirReduc(arr):
    result = ['default']
    while len(arr) != 0:
        end = result[len(result) - 1]
        coming = arr[0]
        flag = 0

        if end == "NORTH" and coming == "SOUTH":
            flag = 1
        elif end == "SOUTH" and coming == "NORTH":
            flag = 1
        elif end == "WEST" and coming == "EAST":
            flag = 1
        elif end == "EAST" and coming == "WEST":
            flag = 1

        if flag == 1:
            result = result[:-1]
            arr = arr[1:]
        else:
            result.append(arr[0])
            arr = arr[1:]

    return result[1:]

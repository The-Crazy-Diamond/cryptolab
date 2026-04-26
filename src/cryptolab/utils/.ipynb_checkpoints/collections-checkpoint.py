def toggle_number(arr, n):
    if n in arr:
        arr.remove(n)
    else:
        arr.append(n)
    return arr
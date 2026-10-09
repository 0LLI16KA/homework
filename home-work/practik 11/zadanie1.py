for n in range(1, 13):
    for k in range(1, 13):
        for m in range(1, 13):
            if  n * 28 + k * 30 + m * 31 == 365:
                print(f"n = {n} | k = {k} | m = {m}")

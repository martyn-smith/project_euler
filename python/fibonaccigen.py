def fibonacci():
    f = []
    if len(f) == 0:
        f.append(1)
    elif len(f) == 1:
        f.append(1)
    else:
        f.append(f[:-1] + f[:-2])
    yield f
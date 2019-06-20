
def is_sorted(t):
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True


def selection_t(t):
    return t


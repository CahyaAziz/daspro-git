# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

def fibonacci(n):
    sequence = [0, 1]
    if n == 1:
        return [0]
    elif n == 2:
        return sequence
    
    for i in range(n-2):
        next = sequence[i] + sequence[i+1]
        sequence.append(next)
 
    return sequence

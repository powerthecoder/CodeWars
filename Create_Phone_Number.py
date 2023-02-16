def create_phone_number(n):
    number = "("
    x = 0
    for i in n:
        x += 1
        if x == 4:
            number += ") "
        if x == 7:
            number += "-"
        number += str(i)
    return number
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
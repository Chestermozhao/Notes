def sum_of_string(s1, s2):
    length_1 = len(s1)
    length_2 = len(s2)

    pointer_1 = length_1
    pointer_2 = length_2

    sum_string = []
    carry = 0

    while all([pointer_1 >= 0, pointer_2 >= 0]):
        d1 = 0
        d2 = 0
        if pointer_1 > 0:
            d1 = int(s1[pointer_1-1])
        if pointer_2 > 0:
            d2 = int(s2[pointer_2-1])
        _sum = d1 + d2 + carry
        if _sum >= 10:
            carry = _sum / 10
            _sum = _sum % 10
        else:
            carry = 0
        pointer_1 -= 1
        pointer_2 -= 1

        sum_string.insert(0, str(_sum))
    return "".join(sum_string)

def string_to_int(s1):
    tens = 1
    num = 0
    for i in range(len(s1)):
        breakpoint()
        num += s1[len(s1)-1-i] - "0" * tens
        tens *= 10
    return num


print(sum_of_string("10", "5"))
#res = string_to_int("15")
#print(res)

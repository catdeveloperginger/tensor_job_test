def check_str_in(str_main, str_check, count_simbol):
    s = 0
    i = 0
    while i < len(str_check):
        if str_check[i] in str_main:
            s += 1
        i +=1
    if s  >= count_simbol:
        return True
    else:
        return False



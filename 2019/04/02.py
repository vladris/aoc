def meets_criteria(pwd):
    found_run, c, run = False, pwd[0], 1
    for digit in pwd[1:]:
        if digit < c:
            return False
        elif digit == c:
            run += 1
        else:
            if run == 2:
                found_run = True
            c, run = digit, 1
    return run == 2 or found_run

print(len(list(filter(meets_criteria, map(str, range(272091, 815432))))))
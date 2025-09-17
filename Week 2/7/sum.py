def sum_range(begin, end, step=1):
    sum = 0
    # end는 +1이 되어야 할 것 같지만 일단 교재에 나온 대로 작성
    for n in range(begin, end, step):
        sum += n
    return sum

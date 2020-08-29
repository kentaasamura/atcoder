# 累積和
def cumsum(xs):
    result = [xs[0]]
    for x in xs[1:]:
        result.append(result[-1] + x)
    return result

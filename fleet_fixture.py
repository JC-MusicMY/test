def clamp(value, lower, upper):
    if lower > upper:
        raise ValueError("lower must not be greater than upper")
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value

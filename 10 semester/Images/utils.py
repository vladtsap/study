def normalize_pixel(value: [float, int]) -> int:
    if value > 255:
        return 255
    elif value < 0:
        return 0
    else:
        return int(value)

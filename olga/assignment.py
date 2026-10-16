def classify(value):
    if value < 98:
        return "Below range"
    elif value <= 102:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    if count == 0:
        return 0.0
    average_result= total / count 
    return average_result


def main():
    total = 0
    t_below_r = 0
    t_in_r = 0
    t_above_r = 0

    num_tiles = int(input("Enter the number of tiles: "))

    for i in range(num_tiles):
        width = int(input("Enter the tile width: "))

        category = classify(width)
        print(category)

        total += width

        if category == "Below range":
            t_below_r += 1
        elif category == "In range":
            t_in_r += 1
        elif category == "Above range":
            t_above_r += 1

    average_width = calculate_average(total, num_tiles)

    print(f"Total width: {total} mm")
    print(f"Average width: {average_width} mm")
    print(f"Below range: {t_below_r}")
    print(f"In range: {t_in_r}")
    print(f"Above range: {t_above_r}")



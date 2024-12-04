def is_increasing(level):
    return all(level[i] < level[i + 1] for i in range(len(level) - 1))


def is_decreasing(level):
    return all(level[i] > level[i + 1] for i in range(len(level) - 1))


def safe_with_removal_of_one(level):
    for idx in range(len(level)):
        removed = level.pop(idx)
        if safe(level):
            return True
        level.insert(idx, removed)

    return False


def safe(level: list) -> bool:
    """
    return true if level is safe i.e. always increasing by min 1 or max 3 or always decreasing by the same limits
    """
    min_difference = 1
    max_difference = 3
    is_increasing_safely = all(
        (level[i] < level[i + 1])
        and (min_difference <= (level[i + 1] - level[i]) <= max_difference)
        for i in range(len(level) - 1)
    )
    is_decreasing_safely = all(
        (level[i] > level[i + 1])
        and (min_difference <= (level[i] - level[i + 1]) <= max_difference)
        for i in range(len(level) - 1)
    )

    return any([is_increasing_safely, is_decreasing_safely])


def main():
    safe_levels = 0
    safe_with_dampener = 0
    unsafe_levels = []
    with open("src/day02/input_1.txt") as file:
        for line in file:
            level = [int(num) for num in line.strip().split(" ")]
            if safe(level):
                safe_levels += 1
                safe_with_dampener += 1
            elif safe_with_removal_of_one(level):
                safe_with_dampener += 1
            else:
                unsafe_levels.append(line)

    print(f"Number of safe levels = {safe_levels}")
    print(f"Number of safe levels with dampener = {safe_with_dampener}")


if __name__ == "__main__":
    main()

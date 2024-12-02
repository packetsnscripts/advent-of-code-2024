def is_increasing(level):
    return all(level[i] < level[i + 1] for i in range(len(level) - 1))


def is_decreasing(level):
    return all(level[i] > level[i + 1] for i in range(len(level) - 1))

    # def unsafe_transitions_within_limit(level,trend)->int:
    #     min_difference = 1
    #     max_difference = 3
    #     limit = 1
    #     unsafe_transitions = 0
    #     if trend == "increasing":
    #         for i in range(len(level)-1):
    #             if not (min_difference <= (level[i+1]-level[i]) <= max_difference):
    #                 unsafe_transitions +=1

    #     elif trend == "decreasing":
    #         for i in range(len(level)-1):
    #             if not (min_difference <= (level[i]-level[i+1]) <= max_difference):
    #                 unsafe_transitions +=1

    # return unsafe_transitions <= limit


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


# def safe2(level:list)-> bool:
#     """
#     return true if level is safe for part2 i.e. always increasing by min 1 or max 3 or always decreasing by the same limits
#     Additionally if removing one number from the level keeps is safe as per safe()
#     """
#     return (is_increasing(level) and unsafe_transitions_within_limit(level, trend="increasing")) or (is_decreasing(level) and unsafe_transitions_within_limit(level,trend="decreasing"))


def main():
    safe_levels = 0
    # safe_with_dampener = 0
    with open("src/day02/input_1.txt") as file:
        for line in file:
            level = line.split(" ")
            level = [int(num) for num in level]
            if safe(level):
                safe_levels += 1
            # if safe2(level):
            #     safe_with_dampener += 1

    print(f"Number of safe levels = {safe_levels}")
    # print(f"Number of safe levels with dampener = {safe_with_dampener}")


if __name__ == "__main__":
    main()

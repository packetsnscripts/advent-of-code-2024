def sum_of_diffs(list1: list, list2: list) -> int:
    """
    Takes 2 lists of ints and returns the sum of the difference between ith element.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")

    list1.sort()
    list2.sort()
    return sum(abs(a - b) for a, b in zip(list1, list2))


def occurences(list) -> dict:
    num_of_occurences = {}
    for num in list:
        if num in num_of_occurences:
            num_of_occurences[num] += 1
        else:
            num_of_occurences[num] = 1

    return num_of_occurences


def similarity_score(list1: list, list2: list):
    """
    similarity score by adding up each number in the left list after multiplying
    it by the number of times that number appears in the right list
    """
    list2_occurences = occurences(list2)
    return sum(num * list2_occurences.get(num, 0) for num in list1)


def main():
    list1 = []
    list2 = []
    with open("src/day01/input_1.txt", "r") as file:
        for line in file:
            num1, num2 = line.split("   ")
            list1.append(int(num1))
            list2.append(int(num2))

    print(f"Sum of differences in input = {sum_of_diffs(list1,list2)}")
    print(f"Similarity score of lists = {similarity_score(list1,list2)}")


if __name__ == "__main__":
    main()

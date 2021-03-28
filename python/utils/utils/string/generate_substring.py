from typing import List


def generate_substring(string: str) -> List[str]:
    substrings: List[str] = []

    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])

    print(substrings)

    return substrings

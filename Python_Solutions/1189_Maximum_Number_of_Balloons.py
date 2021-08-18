import collections


class Solution:
    """
    My Solution: Unoptimized O(N) Solution

    IDEA: Get the character counts of all the letters in the string.
    Then, have a dict that stores the required letter counts to create
    BALLOON. Continue to count until one of those letters turns negative,
    which means we run out.

    # Time Complexity: O(N), where n = len(text)
    # Space Complexity: O(N), where n = number of unique characters
    """

    def maxNumberOfBalloons(self, text: str) -> int:
        # Get the counts of each character in the string
        counts = collections.defaultdict(int)
        for c in text:
            counts[c] += 1

        # Count the number of "balloon" that exists in dict
        BALLOON_COUNTS = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1
        }

        num = 0
        continueCounting = True
        # Continue to subtract the letter counts of BALLOON
        # until we run out of usuable letters
        while continueCounting:
            for k in BALLOON_COUNTS.keys():
                counts[k] -= BALLOON_COUNTS[k]
                if counts[k] < 0:
                    continueCounting = False
                    return num
            num += 1

    """
    Optimized O(N) Solution

    IDEA: We only care about the letters "b", "a", "l", "o", "n".

    Define *potential*, which is the number of times BALLOON can
    be produced. As an example, given that b = 5 and a = 4, we know the max
    potential would be 4, since for the 5th balloon, there would be no "a".
    Thus, the max potential is the minimum potential across all the
    dependent characters.

    Since BALLOON uses two "l"s and two "o"s, the potential for those 
    is count/2.
    
    # Time Complexity: O(N), where n = len(text)
    # Space Complexity: O(1), since we have a finite dictionary
    """

    def maxNumberOfBalloons(self, text: str) -> int:
        # Get the counts of the necessary characters in the string
        b_count = a_count = l_count = o_count = n_count = 0
        for c in text:
            if c == "b":
                b_count += 1
            elif c == "a":
                a_count += 1
            elif c == "l":
                l_count += 1
            elif c == "o":
                o_count += 1
            elif c == "n":
                n_count += 1

        # Divide multiple letters
        l_count //= 2
        o_count //= 2

        return min(b_count, a_count, l_count, o_count, n_count)

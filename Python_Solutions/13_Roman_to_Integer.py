class Solution:
    def romanToInt(self, s: str) -> int:
        """
        My Solution: O(n) Solution

        IDEA: Check for doubles, since there are special cases.
        If it doesn't exist in doubles, then evaluate the first
        character. Continue until no more

        # Time Complexity: O(n), where n = number characters in string
        # Space Complexity: O(1)
        """

        doubles = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        singles = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        i = _sum = 0
        n = len(s)
        while i < n:
            # Check for double groupings
            c = s[i:i+2]
            if c in doubles:
                _sum += doubles[c]
                i += 2
            else:
                # Evaluate as single
                c = s[i]
                _sum += singles[c]
                i += 1
        return _sum

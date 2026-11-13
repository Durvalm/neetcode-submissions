class Solution:
    def findContestMatch(self, n: int) -> str:
        """
        n teams ranked 1 to n (weakest)
        n is a power of 2

        return a string describing the complete tournament bracket

        : pair the first rank with last, and there on


        n = 4
        "((1,4),(2,3))"
        """

        teams = [str(i) for i in range(1, n + 1)]

        while len(teams) > 1:
            new_teams = []
            left = 0
            right = len(teams) - 1

            while left < right:
                match = f"({teams[left]},{teams[right]})"
                new_teams.append(match)

                left += 1
                right -= 1

            teams = new_teams

        return teams[0]


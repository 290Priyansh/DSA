class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        count = 0

        for j in range(cols):              # iterate column by column
            for i in range(rows - 1):      # check adjacent rows
                if strs[i][j] > strs[i + 1][j]:
                    count += 1             # delete this column
                    break                  # move to next column

        return count

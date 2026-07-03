class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict (set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                box = (r//3, c//3)
                if (
                num in rows[r]
                or num in cols[c]
                or num in boxes[box]
                ):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        return True

        
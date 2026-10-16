class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordlist = list(word)
        row = len(board)
        col = len(board[0])

        def existHelper(r, c, index):
            if board[r][c] != wordlist[index]:
                return False

            if index == len(wordlist) - 1:
                return True
            
            if board[r][c] != wordlist[index]:
                return False
            temp = board[r][c]
            board[r][c] = '#'

            directions = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]

            for d in directions:
                if(0 <= d[0] and d[0] < row and 0 <= d[1] and d[1] < col and existHelper(d[0], d[1], index + 1)):              
                    board[r][c] = temp
                    return True
            board[r][c] = temp
            return False

        for r in range(row):
            for c in range(col):
                if(existHelper(r, c, 0)):
                    return True
        return False

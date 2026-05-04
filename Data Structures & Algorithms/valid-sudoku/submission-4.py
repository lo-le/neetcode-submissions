class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        #check rows contains duplicate
        for i in range(9) : 
            for j in range(9) : 
                current = board[i][j]
                print(current)
                if current == "." : 
                    continue
                
                #check if in row
                if current in board[i][j+1:] : 
                    return False
                #check if in prev columns
                for x in range(i) : 
                    print(board[x][j])
                    if board[x][j] == current : 
                        return False
                #add to boxes
                boxref = (3 * (i // 3)) + j // 3
                print("ref:", boxref)
                #check if in boxes
                if current in boxes[boxref] : 
                    return False
                boxes[boxref].append(current)
        print(boxes)
        return True
        
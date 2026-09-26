class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            HashSet<Character> foundInRowI = new HashSet<>();
            HashSet<Character> foundInColI = new HashSet<>();
            HashSet<Character> foundInBoxI = new HashSet<>();
            /*
            0 1 2
            3 4 5
            6 7 8
            */
            //box[i] == boxes[(int)(i/3)][i%3]
            //.    0.     1.     2. 
            //0  (1,1), (1,4), (1,7)
            //1  (4,1), (4,4), (5,7)
            //2  (7,1), (7,4), (7,7)
            //center = (3*(int)(i/3)+1, 3*(i%3)+1) = [x, y]
            //(r-1,c-1)   (r-1,c) (r-1,c+1)        0 1 2
            //(r,c-1)     (r,c)   (r,c+1)    <--   3 4 5
            //(r+1,c-1)   (r+1,c) (r+1,c+1)        6 7 8
            //box j: (3*(int)(i/3)+(int)j/3, 3*(i%3)+j%3)
            for (int j = 0; j < 9; j++) {
                char rowVal = board[i][j];
                char colVal = board[j][i];
                char boxVal = board[3*(int)(i/3)+(int)j/3][3*(i%3)+j%3];
                if (foundInRowI.contains(rowVal) || foundInColI.contains(colVal) || foundInBoxI.contains(boxVal)) {
                    return false;
                }
                if (rowVal != '.') {
                    foundInRowI.add(rowVal);
                }
                if (colVal != '.') {
                    foundInColI.add(colVal);
                }
                if (boxVal != '.') {
                    foundInBoxI.add(boxVal);
                }
            }
        }
        return true;
    }
}

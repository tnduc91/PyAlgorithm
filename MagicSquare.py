#https://leetcode.com/problems/magic-squares-in-grid/solution/

def numMagicSquaresInside1(grid) -> int:
    
        row, col = len(grid), len(grid[0])

        def magic (a,b,c,d,e,f,g,h,i):
            
            if (sorted([a,b,c,d,e,f,g,h,i]) != list(range(1,10))):
                return False;

            return a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15

        ans = 0

        for r in range(0, row -2, 1):
            for c in range(0, row -2, 1):
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2], grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2], grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1

        return ans

input = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
output = numMagicSquaresInside1(input)
print(output)
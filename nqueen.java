import java.util.Scanner;

public class nqueen {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of Queens: ");
        int n = sc.nextInt();

        int[][] board = new int[n][n]; // chessboard initialized with 0s

        if (solve(board, 0, n)) {
            printBoard(board, n);
        } else {
            System.out.println("No solution exists for " + n + " queens.");
        }

        sc.close();
    }

    // Try to place queens column by column
    public static boolean solve(int[][] board, int col, int n) {
        if (col >= n) return true; // all queens placed

        for (int row = 0; row < n; row++) {
            if (isSafe(board, row, col, n)) {
                board[row][col] = 1; // place queen

                if (solve(board, col + 1, n)) return true; // move to next column

                board[row][col] = 0; // backtrack if not safe
            }
        }
        return false;
    }

    // Check if placing queen at (row, col) is safe
    public static boolean isSafe(int[][] board, int row, int col, int n) {
        // Check left side of row
        for (int i = 0; i < col; i++) {
            if (board[row][i] == 1) return false;
        }

        // Check upper-left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) return false;
        }

        // Check lower-left diagonal
        for (int i = row, j = col; i < n && j >= 0; i++, j--) {
            if (board[i][j] == 1) return false;
        }

        return true;
    }

    // Print the board with queens
    public static void printBoard(int[][] board, int n) {
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                System.out.print(board[row][col] == 1 ? " Q " : " _ ");
            }
            System.out.println();
        }
    }
}

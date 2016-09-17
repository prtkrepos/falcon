#include <iostream>
#include <cstdio>
#include <random>
#include <vector>
#include <utility>

using namespace std;

const int N = 5;


// Checks if the move is valid or not
bool isValidMove(int grid[N][N], int hx, int hy, char move)
{
    if(move == 'L')
    {
        if(hy == 0 or grid[hx][hy-1] == 1) return false;
        else return true;
    }
    else if(move == 'R')
    {
        if(hy == N-1 or grid[hx][hy+1] == 1) return false;
        else return true;
    }
    else if(move == 'U')
    {
        if(hx == 0 or grid[hx-1][hy] == 1) return false;
        else return true;
    }
    else if(move == 'D')
    {
        if(hx == N-1 or grid[hx+1][hy] == 1) return false;
        else return true;
    }
    else
        return false;
}



// Making move
void makeMove(int grid[N][N], int& hx, int& hy, char move)
{
    if(move == 'L') hy--;
    else if(move == 'R') hy++;
    else if(move == 'U') hx--;
    else hx++;
    grid[hx][hy] = 1;
}


// Get score
int getScore(int grid[N][N])
{
    int score = 0;
    for(int i = 0;i < N;++i)
        for(int j = 0;j < N;++j)
            if(grid[i][j] == 1) score++;
    return score;
}


// Checks if the game is terminated
bool isGameTerminated(int grid[N][N])
{
    for(int i = 0;i < N;++i)
        for(int j = 0;j < N;++j)
            if(grid[i][j] != 1) return false;
    return true;
}

int main(int argc, char* argv[])
{
    if(argc == 2 or argc == 3) freopen(argv[1], "r", stdin);
    if(argc == 3) freopen(argv[2], "w", stdout);

    int grid[N][N], hx, hy, score;
    char move;

    // Previous State
    for(int i = 0;i < N;++i)
        for(int j = 0;j < N;++j)
            cin >> grid[N][N];

    // Head of the snake
    if(!(cin >> hx >> hy))
    {
        cout << "INVALID" << endl;
        return 0;
    }

    // Player Move
    if(!(cin >> move))
    {
        cout << "INVALID" << endl;
        return 0;
    }

    // Check for Valid Move
    if(!isValidMove(grid, hx, hy, move))
    {
        cout << "INVALID" << endl;
        return 0;
    }

    // Making Move
    makeMove(grid, hx, hy, move);

    cout << "VALID" << endl;

    for(int i = 0;i < N;++i)
    {
        for(int j = 0;j < N;++j)
        {
            cout << grid[i][j];
            if(j < N-1) cout << ' ';
        }
        cout << endl;
    }

    cout << x << ' ' << y << endl;

    cout << "CHECKER OUTPUT" << endl;

    // Calculate score
    score = getScore(grid);

    // Check if game is terminated
    if(isGameTerminated(grid))
        cout << "END " << score << endl;
    else
        cout << "INBETWEEN " << score << endl;
    return 0;
}

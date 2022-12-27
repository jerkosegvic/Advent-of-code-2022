#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

const int N = 710;

int mod1, mod2, mod3;
char grid[N][N];
bool visited[N][N][N];

int dx[5] = {0, 0, 0, 1, -1};
int dy[5] = {0, 1, -1, 0, 0};

struct Node {
  int x, y, t;
};

bool is_valid(int x, int y, int t) {
  if (x == -1 && y == 0) return true;
  if (x == mod2 && y == mod1 - 1) return true;
  if (x < 0 || x >= mod2 || y < 0 || y >= mod1) return false;
  if (t % mod1 == 0 || t % mod2 == 0) return false;
  if (visited[x][y][t % mod3]) return false;
  return true;
}

int main() {
  string ulaz;
  getline(cin, ulaz);
  mod1 = ulaz.size() - 2;
  mod2 = mod3 = 0;

  while (getline(cin, ulaz)) {
    if (ulaz[0] == '#') break;
    mod2++;
    for (int i = 0; i < ulaz.size(); i++) {
      grid[mod2 - 1][i] = ulaz[i];
      if (ulaz[i] == '>') mod1 = min(mod1, i);
      else if (ulaz[i] == '<') mod1 = max(mod1, i);
      else if (ulaz[i] == 'v') mod2 = max(mod2, i);
      else if (ulaz[i] == '^') mod2 = min(mod2, i);
    }
  }

  mod2 -= 2;
  mod3 = 700;

  queue<Node> q;
  q.push({-1, 0, 0});

  while (!q.empty()) {
    Node curr = q.front();
    q.pop();

    if (curr.x == mod2 && curr.y == mod1 - 1) {
      cout << curr.t << endl;
      break;
    }

    for (int i = 0; i < 5; i++) {
      int nx = curr.x + dx[i];
      int ny = curr.y + dy[i];
      int nt = curr.t + 1;
      if (is_valid(nx, ny, nt)) {
        visited[nx][ny][nt % mod3] = true;
        q.push({nx, ny, nt});
      }
    }
  }

  return 0;
}

#include <iostream>
#include <vector>
using namespace std;

class Cow {
public:
    int cow;
    vector<int> preferences;

    Cow(int cow, const vector<int>& preferences) {
        this->cow = cow;
        // Copy preferences until cow's number is found
        for(auto& pref : preferences) {
            this->preferences.push_back(pref);
            if(pref == cow) break;
        }
    }
};

int main() {
    int n;
    cin >> n;

    vector<Cow> cows;
    for(int cow = 1; cow <= n; ++cow) {
        vector<int> preferences(n);
        for(int& pref : preferences) {
            cin >> pref;
        }
        cows.push_back(Cow(cow, preferences));
    }

    vector<vector<int>> G(n + 1);
    for(auto& cow : cows) {
        G[cow.cow] = cow.preferences;
    }

    vector<vector<bool>> isPath(n + 1, vector<bool>(n + 1, false));
    for(int i = 1; i <= n; ++i) {
        for(int j : G[i]) {
            isPath[i][j] = true;
        }
    }

    // Compute transitive closure using Floyd-Warshall algorithm
    for(int k = 1; k <= n; ++k) {
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= n; ++j) {
                if(isPath[i][k] && isPath[k][j]) {
                    isPath[i][j] = true;
                }
            }
        }
    }

    vector<int> answer(n + 1, 0);
    for(auto& cow : cows) {
        int c = cow.cow;
        for(int p : cow.preferences) {
            if(isPath[p][c]) { // This cycle exists: c->p->...->c
                answer[c] = p; // Cow c can hope for the gift p.
                break;
            }
        }
    }

    for(int i = 1; i <= n; ++i) {
        cout << answer[i] << endl;
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm> // for std::max

int main() {
    int t, c;
    std::cin >> t >> c;
    std::vector<int> targets(t);
    for (int i = 0; i < t; ++i) std::cin >> targets[i];
    std::string instructions;
    std::cin >> instructions;

    int hit = 0, current_pos = 0;
    std::vector<bool> target_line(2 * c + 1, false);
    std::vector<int> hits(2 * c + 1, 0);
    for (int target : targets) {
        target_line[target + c] = true; // Offset to handle negative indices
    }

    for (char move : instructions) {
        if (move == 'R') current_pos++;
        else if (move == 'L') current_pos--;
        else if (move == 'F' && target_line[current_pos + c]) { // Offset for negative index handling
            if (hits[current_pos + c] == 0) hit++;
            hits[current_pos + c]++;
        }
    }
    int answer = hit, final_position = current_pos;

    std::vector<char> moves = {'F', 'R', 'L'};
    for (int old_offset : {-1, 0, 1}) {
        char old_move = moves[1 + old_offset]; // Offset for 0-based indexing
        for (int new_offset : {-1, 0, 1}) {
            char new_move = moves[1 + new_offset]; // Offset for 0-based indexing
            if (old_move != new_move) {
                int offset = new_offset - old_offset;

                hit = 0;
                int suffix_pos = final_position + offset + c; // Offset for negative index handling
                std::fill(hits.begin(), hits.end(), 0);
                for (int i = c - 1; i >= 0; --i) {
                    char move = instructions[i];
                    if (move == 'R') suffix_pos--;
                    else if (move == 'L') suffix_pos++;
                    else if (move == 'F' && target_line[suffix_pos]) {
                        if (hits[suffix_pos] == 0) hit++;
                        hits[suffix_pos]++;
                    }
                }

                int prefix_pos = c; // Offset for negative index handling
                for (int i = 0; i < c; ++i) {
                    char move = instructions[i];
                    if (move == 'R') suffix_pos++;
                    else if (move == 'L') suffix_pos--;
                    else if (move == 'F' && target_line[suffix_pos]) {
                        hits[suffix_pos]--;
                        if (hits[suffix_pos] == 0) hit--;
                    }

                    if (move == old_move) {
                        if (new_move == 'F' && target_line[prefix_pos]) {
                            if (hits[prefix_pos] == 0) hit++;
                            hits[prefix_pos]++;
                        }
                        answer = std::max(answer, hit);
                        if (new_move == 'F' && target_line[prefix_pos]) {
                            hits[prefix_pos]--;
                            if (hits[prefix_pos] == 0) hit--;
                        }
                    }

                    if (move == 'R') prefix_pos++;
                    else if (move == 'L') prefix_pos--;
                    else if (move == 'F' && target_line[prefix_pos]) {
                        if (hits[prefix_pos] == 0) hit++;
                        hits[prefix_pos]++;
                    }
                }
            }
        }
    }
    std::cout << answer << std::endl;

    return 0;
}

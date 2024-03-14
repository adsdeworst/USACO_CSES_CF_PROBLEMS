#include <iostream>
#include <vector>
#include <algorithm> // for std::find and std::distance

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> list_a(k), list_b(k);
    for (int i = 0; i < k; ++i) std::cin >> list_a[i];
    for (int i = 0; i < k; ++i) std::cin >> list_b[i];

    std::vector<bool> included(n + 1, false);
    int not_inc = 0;

    for (int i = 0; i < k; ++i) {
        included[list_a[i]] = true;
        included[list_b[i]] = true;
    }

    for (int i = 1; i <= n; ++i) {
        if (!included[i]) not_inc++;
    }

    std::vector<int> offset;
    for (int i = 0; i < k; ++i) {
        auto it = std::find(list_b.begin(), list_b.end(), list_a[i]);
        if (it != list_b.end()) {
            int index = std::distance(list_b.begin(), it);
            if (index - i < 0) offset.push_back(index - i + k);
            else offset.push_back(index - i);
        }
    }

    int length = offset.size();
    std::vector<int> offset_counts;
    int count = 0;
    if (length != 0) {
        for (int i = 0; i < length - 1; ++i) {
            if (offset[i] == offset[i + 1]) count++;
            else {
                count++;
                offset_counts.push_back(count);
                count = 0;
            }
        }
        count++;
        offset_counts.push_back(count);
    }
    int answer = length == 0 ? 0 : not_inc + *std::max_element(offset_counts.begin(), offset_counts.end());

    std::reverse(list_a.begin(), list_a.end());
    offset.clear();

    for (int i = 0; i < k; ++i) {
        auto it = std::find(list_b.begin(), list_b.end(), list_a[i]);
        if (it != list_b.end()) {
            int index = std::distance(list_b.begin(), it);
            if (index - i < 0) offset.push_back(index - i + k);
            else offset.push_back(index - i);
        }
    }

    std::sort(offset.begin(), offset.end());
    length = offset.size();
    offset_counts.clear();
    count = 0;
    if (length != 0) {
        for (int i = 0; i < length - 1; ++i) {
            if (offset[i] == offset[i + 1]) count++;
            else {
                count++;
                offset_counts.push_back(count);
                count = 0;
            }
        }
        count++;
        offset_counts.push_back(count);
    }
    answer = length == 0 ? 0 : std::max(answer, not_inc + *std::max_element(offset_counts.begin(), offset_counts.end()));

    std::cout << answer << std::endl;

    return 0;
}

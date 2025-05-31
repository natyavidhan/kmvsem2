// Write a program to remove the duplicates from an array.

#include <iostream>
int main()
{
    int n;
    std::cout << "Enter size of array: ";
    std::cin >> n;
    int a[1000];
    for (int i = 0; i < n; ++i)
        std::cin >> a[i];

    int out[1000], out_size = 0;
    for (int i = 0; i < n; ++i) {
        bool found = false;
        for (int j = 0; j < out_size; ++j) {
            if (out[j] == a[i]) {
                found = true;
                break;
            }
        }
        if (!found) {
            out[out_size++] = a[i];
        }
    }
    std::cout << "Array after removing duplicates:\n";
    for (int i = 0; i < out_size; ++i)
        std::cout << out[i] << ' ';
    std::cout << '\n';
}
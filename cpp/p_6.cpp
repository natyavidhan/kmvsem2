// Write a program to search a given element in a set of N numbers using
// Binary Search
// a. with recursion
// b. without recursion.

#include <iostream>
int recBS(const int *v, int l, int r, int key)
{
    if (l > r)
        return -1;
    int m = (l + r) / 2;
    if (v[m] == key)
        return m;
    if (key < v[m])
        return recBS(v, l, m - 1, key);
    return recBS(v, m + 1, r, key);
}
int iterBS(const int *v, int n, int key)
{
    int l = 0, r = n - 1;
    while (l <= r)
    {
        int m = (l + r) / 2;
        if (v[m] == key)
            return m;
        if (key < v[m])
            r = m - 1;
        else
            l = m + 1;
    }
    return -1;
}
int main()
{
    int n;
    std::cout << "n: ";
    std::cin >> n;
    int v[1000];
    for (int i = 0; i < n; ++i)
        std::cin >> v[i];
    int key;
    std::cout << "key: ";
    std::cin >> key;
    std::cout << "Recursive idx: " << recBS(v, 0, n - 1, key) << "\nIterative idx: " << iterBS(v, n, key) << '\n';
}
// Write a program to merge two ordered arrays to get a single ordered
// array.

#include <iostream>
int main()
{
    int n1, n2;
    std::cout << "n1 n2: ";
    std::cin >> n1 >> n2;
    int a[1000], b[1000];
    for (int i = 0; i < n1; ++i)
        std::cin >> a[i];
    for (int i = 0; i < n2; ++i)
        std::cin >> b[i];
    int c[2000], c_size = 0;
    int i = 0, j = 0;
    while (i < n1 || j < n2)
    {
        if (j == n2 || (i < n1 && a[i] < b[j]))
            c[c_size++] = a[i++];
        else
            c[c_size++] = b[j++];
    }
    for (int k = 0; k < c_size; ++k)
        std::cout << c[k] << ' ';
    std::cout << '\n';
}
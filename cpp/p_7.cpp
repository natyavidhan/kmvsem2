// Write a program to calculate GCD of two numbers
// a. with recursion
// b. without recursion

#include <iostream>
int gcdRec(int a, int b) { return b == 0 ? a : gcdRec(b, a % b); } // Euclid
int gcdIter(int a, int b)
{
    while (b)
    {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}
int main()
{
    int x, y;
    std::cin >> x >> y;
    std::cout << gcdRec(x, y) << ' ' << gcdIter(x, y) << '\n';
}
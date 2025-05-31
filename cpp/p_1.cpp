// Write a program to compute the sum of the first n terms of the following
// series If the command line argument is not found then prompt the user to enter the value of n.

#include <iostream>
#include <iomanip>
#include <cstdlib> // atoi

long long fact(int n)
{
    long long f = 1;
    for (int i = 2; i <= n; ++i)
        f *= i;
    return f;
}

int main(int argc, char *argv[])
{
    int n;
    if (argc >= 2)
    {
        n = std::atoi(argv[1]);
    }
    else
    {
        std::cout << "Enter n: ";
        std::cin >> n;
    }

    double sum = 0.0;
    for (int i = 1; i <= n; ++i)
    {
        double term = 1.0 / fact(i);
        if (i % 2 == 0)
            term = -term;
        sum += term;
    }
    std::cout << std::fixed << std::setprecision(8)
              << "Sum of series = " << sum << '\n';
    return 0;
}
// Create a Triangle class. Add exception handling statements to ensure
// the following conditions: all sides are greater than 0 and sum of any two
// sides is greater than the third side. The class should also have
// overloaded functions for calculating the area of a right angled triangle as
// well as using Heron's formula to calculate the area of any type of
// triangle

#include <iostream>
#include <stdexcept>
#include <cmath>
class Triangle
{
    double a, b, c; // sides
    static void validate(double a, double b, double c)
    {
        if (a <= 0 || b <= 0 || c <= 0)
            throw std::invalid_argument("Sides must be >0");
        if (a + b <= c || a + c <= b || b + c <= a)
            throw std::invalid_argument("Triangle inequality failed");
    }

public:
    Triangle(double a, double b, double c) : a(a), b(b), c(c) { validate(a, b, c); }
    double area() const
    { // Heron
        double s = (a + b + c) / 2;
        return std::sqrt(s * (s - a) * (s - b) * (s - c));
    }
    static double areaRight(double base, double height) { return 0.5 * base * height; } // overloaded
};
int main()
{
    try
    {
        double a, b, c;
        std::cin >> a >> b >> c;
        Triangle t(a, b, c);
        std::cout << "Area = " << t.area() << '\n';
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
    }
}
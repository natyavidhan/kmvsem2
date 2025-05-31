// Create a Matrix class. Write a menu-driven program to perform following
// Matrix operations (exceptions should be thrown by the functions if
// matrices passed to them are incompatible and handled by the main()
// function):
// a. Sum
// b. Product
// c. Transpose

#include <iostream>
#include <stdexcept>
class Matrix
{
    int m[10][10];
    int r, c;

public:
    Matrix(int rows, int cols) : r(rows), c(cols) {}
    int rows() const { return r; }
    int cols() const { return c; }
    int &at(int row, int col) { return m[row][col]; }
    const int &at(int row, int col) const { return m[row][col]; }
    Matrix operator+(const Matrix &b) const
    {
        if (r != b.r || c != b.c)
            throw std::runtime_error("Dim mismatch");
        Matrix res(r, c);
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                res.m[i][j] = m[i][j] + b.m[i][j];
        return res;
    }
    Matrix operator*(const Matrix &b) const
    {
        if (c != b.r)
            throw std::runtime_error("Dim mismatch");
        Matrix res(r, b.c);
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < b.c; ++j)
            {
                int sum = 0;
                for (int k = 0; k < c; ++k)
                    sum += m[i][k] * b.m[k][j];
                res.m[i][j] = sum;
            }
        return res;
    }
    Matrix transpose() const
    {
        Matrix t(c, r);
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                t.m[j][i] = m[i][j];
        return t;
    }
    void read()
    {
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                std::cin >> m[i][j];
    }
    void print() const
    {
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
                std::cout << m[i][j] << ' ';
            std::cout << '\n';
        }
    }
};
int main()
{
    try
    {
        int r1, c1, r2, c2;
        std::cout << "Rows Cols M1: ";
        std::cin >> r1 >> c1;
        Matrix A(r1, c1);
        A.read();
        std::cout << "Rows Cols M2: ";
        std::cin >> r2 >> c2;
        Matrix B(r2, c2);
        B.read();
        int ch;
        do
        {
            std::cout << "\n1.Sum 2.Product 3.Transpose A 0.Exit: ";
            std::cin >> ch;
            if (ch == 1)
                (A + B).print();
            else if (ch == 2)
                (A * B).print();
            else if (ch == 3)
                A.transpose().print();
        } while (ch);
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
    }
}
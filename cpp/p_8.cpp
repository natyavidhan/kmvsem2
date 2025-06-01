// Create a Matrix class. Write a menu-driven program to perform following
// Matrix operations (exceptions should be thrown by the functions if
// matrices passed to them are incompatible and handled by the main()
// function):
// a. Sum
// b. Product
// c. Transpose

#include <iostream>
using namespace std;

class Matrix {
    int data[10][10];
    int rows, cols;

public:
    Matrix(int r, int c) {
        rows = r;
        cols = c;
    }

    void read() {
        cout << "Enter elements (" << rows << "x" << cols << "):\n";
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                cin >> data[i][j];
    }

    void print() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++)
                cout << data[i][j] << " ";
            cout << endl;
        }
    }

    Matrix add(Matrix b) {
        if (rows != b.rows || cols != b.cols)
            throw "Addition not possible (dimension mismatch)";
        Matrix result(rows, cols);
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                result.data[i][j] = data[i][j] + b.data[i][j];
        return result;
    }

    Matrix multiply(Matrix b) {
        if (cols != b.rows)
            throw "Multiplication not possible (invalid sizes)";
        Matrix result(rows, b.cols);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < b.cols; j++) {
                result.data[i][j] = 0;
                for (int k = 0; k < cols; k++)
                    result.data[i][j] += data[i][k] * b.data[k][j];
            }
        }
        return result;
    }

    Matrix transpose() {
        Matrix result(cols, rows);
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                result.data[j][i] = data[i][j];
        return result;
    }

    int getRows() { return rows; }
    int getCols() { return cols; }
};

int main() {
    int r1, c1, r2, c2;
    cout << "Enter rows and columns of Matrix A: ";
    cin >> r1 >> c1;
    Matrix A(r1, c1);
    A.read();

    cout << "Enter rows and columns of Matrix B: ";
    cin >> r2 >> c2;
    Matrix B(r2, c2);
    B.read();

    int choice;
    do {
        cout << "\nMenu:\n1. Add\n2. Multiply\n3. Transpose A\n0. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
    
        try {
            if (choice == 1) {
                Matrix result = A.add(B);
                cout << "Sum:\n";
                result.print();
            } else if (choice == 2) {
                Matrix result = A.multiply(B);
                cout << "Product:\n";
                result.print();
            } else if (choice == 3) {
                Matrix result = A.transpose();
                cout << "Transpose of A:\n";
                result.print();
            }
        } catch (const char* error) {
            cout << "Error: " << error << endl;
        }

    } while (choice != 0);

    return 0;
}

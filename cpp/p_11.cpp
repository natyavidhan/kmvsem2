// Create a class Student containing fields for Roll No., Name, Class, Year
// and Total Marks. Write a program to store 5 objects of Student class in a
// file. Retrieve these records from the file and display them

#include <iostream>
#include <fstream>
using namespace std;

class Student {
    int roll;
    char name[30];
    char cls[10];
    int year;
    int total;

public:
    void read() {
        cout << "Enter Roll No, Name, Class, Year, Total Marks:\n";
        cin >> roll >> name >> cls >> year >> total;
    }

    void display() {
        cout << roll << " " << name << " " << cls << " " << year << " " << total << endl;
    }

    void writeToFile(ofstream &out) {
        out << roll << " " << name << " " << cls << " " << year << " " << total << "\n";
    }

    void readFromFile(ifstream &in) {
        in >> roll >> name >> cls >> year >> total;
    }
};

int main() {
    const char* filename = "students.txt";
    Student students[5];

    // Input 5 students
    for (int i = 0; i < 5; i++) {
        cout << "Student " << (i + 1) << ":\n";
        students[i].read();
    }

    // Write to text file
    ofstream outFile(filename);
    for (int i = 0; i < 5; i++)
        students[i].writeToFile(outFile);
    outFile.close();

    // Read from text file
    ifstream inFile(filename);
    Student temp;
    cout << "\nStored Student Records:\n";
    for (int i = 0; i < 5; i++) {
        temp.readFromFile(inFile);
        temp.display();
    }
    inFile.close();

    return 0;
}

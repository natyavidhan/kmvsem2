// Create a class Student containing fields for Roll No., Name, Class, Year
// and Total Marks. Write a program to store 5 objects of Student class in a
// file. Retrieve these records from the file and display them

#include <iostream>
#include <fstream>
struct Student
{
    int roll;
    char name[30];
    char cls[10];
    int year;
    int total;
};
int main()
{
    const char *fname = "students.dat";
    Student v[5];
    for (int i = 0; i < 5; ++i)
    {
        std::cout << "Roll Name Class Year Total: ";
        std::cin >> v[i].roll >> v[i].name >> v[i].cls >> v[i].year >> v[i].total;
    }
    std::ofstream ofs(fname, std::ios::binary);
    ofs.write((char *)v, 5 * sizeof(Student));
    ofs.close();
    // read back
    Student r[5];
    std::ifstream ifs(fname, std::ios::binary);
    ifs.read((char *)r, 5 * sizeof(Student));
    ifs.close();
    for (int i = 0; i < 5; ++i)
    {
        std::cout << r[i].roll << ' ' << r[i].name << ' ' << r[i].cls << ' ' << r[i].year << ' ' << r[i].total << '\n';
    }
}
// Define a class Person having name as a data member. Inherit two
// classes Student and Employee from Person. Student has additional
// attributes as course, marks and year and Employee has department and
// salary. Write display() method in all the three classes to display the
// corresponding attributes. Provide the necessary methods to show
// runtime polymorphism

#include <iostream>
#include <cstring>
class Person
{
protected:
    char name[100];

public:
    Person(const char *n) { std::strncpy(name, n, 99); name[99] = '\0'; }
    virtual void display() const { std::cout << "Name: " << name << '\n'; }
    virtual ~Person() = default;
};
class Student : public Person
{
    char course[100];
    int marks;
    int year;

public:
    Student(const char *n, const char *c, int m, int y) : Person(n), marks(m), year(y) { std::strncpy(course, c, 99); course[99] = '\0'; }
    void display() const override
    {
        Person::display();
        std::cout << "Course: " << course << "  Marks: " << marks << "  Year: " << year << '\n';
    }
};
class Employee : public Person
{
    char dept[100];
    double salary;

public:
    Employee(const char *n, const char *d, double s) : Person(n), salary(s) { std::strncpy(dept, d, 99); dept[99] = '\0'; }
    void display() const override
    {
        Person::display();
        std::cout << "Dept: " << dept << "  Salary: " << salary << '\n';
    }
};
int main()
{
    Person *p = nullptr;
    int type;
    std::cout << "1.Student 2.Employee: ";
    std::cin >> type;
    std::cin.ignore();
    if (type == 1)
    {
        char n[100], c[100];
        int m, y;
        std::cin >> n >> c >> m >> y;
        p = new Student(n, c, m, y);
    }
    else
    {
        char n[100], d[100];
        double s;
        std::cin >> n >> d >> s;
        p = new Employee(n, d, s);
    }
    p->display();
    delete p;
}
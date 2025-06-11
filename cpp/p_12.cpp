// Copy the contents of one text file to another file, after removing all
// whitespaces.

#include <iostream>
#include <fstream>
#include <cctype>
using namespace std;

int main()
{
    string src, dst;
    cout << "Source file: ";
    cin >> src;
    cout << "Destination file: ";
    cin >> dst;
    ifstream in(src);
    if (!in)
    {
        cerr << "Cannot open src\n";
        return 1;
    }
    ofstream out(dst);
    char ch;
    while (in.get(ch))
    {
        if (!isspace(static_cast<unsigned char>(ch)))
            out << ch;
    }
    cout << "Copied without whitespaces.\n";
}
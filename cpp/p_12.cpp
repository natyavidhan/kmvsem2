// Copy the contents of one text file to another file, after removing all
// whitespaces.

#include <iostream>
#include <fstream>
#include <cctype>
int main()
{
    std::string src, dst;
    std::cout << "Source file: ";
    std::cin >> src;
    std::cout << "Destination file: ";
    std::cin >> dst;
    std::ifstream in(src);
    if (!in)
    {
        std::cerr << "Cannot open src\n";
        return 1;
    }
    std::ofstream out(dst);
    char ch;
    while (in.get(ch))
    {
        if (!std::isspace(static_cast<unsigned char>(ch)))
            out << ch;
    }
    std::cout << "Copied without whitespaces.\n";
}
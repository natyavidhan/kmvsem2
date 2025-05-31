// Write a program that prints a table indicating the number of occurrences
// of each alphabet in the text entered as command line arguments

#include <iostream>
#include <iomanip>
#include <cctype>
int main(int argc, char *argv[])
{
    int freq[26] = {0};
    for (int i = 1; i < argc; ++i)
    {
        for (char *p = argv[i]; *p; ++p)
        {
            char c = *p;
            if (std::isalpha(static_cast<unsigned char>(c)))
            {
                freq[std::toupper(c) - 'A']++;
            }
        }
    }
    std::cout << "Letter  Count\n";
    for (int i = 0; i < 26; ++i)
        std::cout << char('A' + i) << "\t" << freq[i] << '\n';
}
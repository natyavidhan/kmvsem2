// Write a menu driven program to perform string manipulation (without
// using inbuilt string functions):
// 1. Show address of each character in string
// 2. Concatenate two strings.
// 3. Compare two strings
// 4. Calculate length of the string (use pointers)
// 5. Convert all lowercase characters to uppercase
// 6. Reverse the string
// 7. Insert a string in another string at a user specified position

#include <iostream>
#include <cstring>

void show_addresses(const char *s)
{
    for (size_t i = 0; i < std::strlen(s); ++i)
        std::cout << "&s[" << i << "] = " << (void *)(s + i) << " => " << s[i] << '\n';
}

char *concat(char *dest, const char *src)
{
    size_t dlen = std::strlen(dest);
    size_t slen = std::strlen(src);
    for (size_t i = 0; i <= slen; ++i)
        dest[dlen + i] = src[i];
    return dest;
}

int compare(const char *a, const char *b)
{
    size_t i = 0;
    while (a[i] && a[i] == b[i])
        ++i;
    return a[i] - b[i];
}

size_t length(const char *s)
{
    size_t l = 0;
    while (s[l])
        ++l;
    return l;
}

void to_upper(char *s)
{
    for (size_t i = 0; s[i]; ++i)
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] -= 32;
}

void reverse(char *s)
{
    size_t l = length(s);
    for (size_t i = 0; i < l / 2; ++i)
        std::swap(s[i], s[l - 1 - i]);
}
// this is a strings
// 

void insert(char *dest, const char *src, size_t pos)
{
    size_t dlen = length(dest), slen = length(src);
    
    for (size_t i = dlen + 1; i >= pos + 1; --i)
        dest[i + slen - 1] = dest[i - 1];

    for (size_t i = 0; i < slen; ++i)
        dest[pos + i] = src[i];
}

int main()
{
    char s1[256] = "";
    char s2[256] = "";
    std::cout << "Enter first string: ";
    std::cin.getline(s1, 256);
    std::cout << "Enter second string: ";
    std::cin.getline(s2, 256);
    int choice;
    do
    {
        std::cout << "\nMENU\n1.Address\n2.Concat\n3.Compare\n4.Length\n5.ToUpper\n6.Reverse\n7.Insert\n0.Exit\nChoice: ";
        std::cin >> choice;
        std::cin.ignore();
        switch (choice)
        {
        case 1:
            show_addresses(s1);
            break;
        case 2:
            concat(s1, s2);
            std::cout << "Result: " << s1 << '\n';
            break;
        case 3:
            std::cout << "Compare result: " << compare(s1, s2) << '\n';
            break;
        case 4:
            std::cout << "Length: " << length(s1) << '\n';
            break;
        case 5:
            to_upper(s1);
            std::cout << s1 << '\n';
            break;
        case 6:
            reverse(s1);
            std::cout << s1 << '\n';
            break;
        case 7:
            size_t pos;
            std::cout << "Pos: ";
            std::cin >> pos;
            std::cin.ignore();
            insert(s1, s2, pos);
            std::cout << s1 << '\n';
            break;
        }
    } while (choice != 0);
}
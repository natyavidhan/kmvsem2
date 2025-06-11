1. Write a program that takes a character from the keyboard and displays its corresponding ASCII value on the screen.
2. Write a function to swap two numbers using pointer datatype parameters.
3. Write a program that reads a text file and creates an output file, named "out.dnt". The output file is identical to the text file except that every sequence of consecutive blank spaces is replaced by a single space.
4. Create a class `ThreeDim` with integer coordinates `x`, `y`, `z`. Define:  
	(i) Default constructor (initialize to 0)  
	(ii) Parameterized constructor  
	(iii) Function `out()` to display coordinates
5. Write a program to print the area of a square and circle using function overloading.
6. Define a class `Complex` with:  
	(i) Private data members  
	(ii) Default and parameterized constructors  
	(iii) Member function to add another complex number  
7. Write a function to compare two equal-sized arrays for equality (return `true`/`false`).
8. Write a function `UpperTriangle()` that converts a square matrix to upper triangular by setting elements below the diagonal to 0.
9. Write a code snippet to:
	- Declare `str` (a pointer to `char`) initialized to `"NITIN"`.
	- Display the ASCII value of each character in `str`.
10. Define `void concatenate(char a[], char b[], int n, int m)` to append elements of `b` to `a`.
11. Write a program to:
	- Copy content from `"A1.txt"` to `"A2.txt"` word by word.
	- Display the number of words copied.
12. Program to compute the series:  
	[ s = x - \frac{x^3}{3!} + \frac{x^5}{5!} \pm \frac{x^7}{7!} + \cdots ]  
	where `x` and `n` (number of terms) are command-line inputs.
13. For class `Bankaccount`:
	- Declare data members: `name`, `aceno`, `balance`.
	- Define:  
	    **(i)** Default and parameterized constructors.  
	    **(ii)** `void input()`: Reads user input.  
	    **(iii)** `void withdraw(double x)`: Debits `x` if `balance - x >= 500`.  
	    **(iv)** `void deposit(double x)`: Credits `x`.  
	    **(v)** `void display()`: Prints account details.
	- Write `main()` to demonstrate functionality.
14. Rewrite class `Vector` using templates:

```c
class Vector { int a[20]; int n; ... };  
```

	Define:  
	**(i)** Default and copy constructors.  
	**(ii)** `void input(int n)`: Reads `n` values.  
	**(iii)** `Vector add(...)`: Adds two vectors element-wise.  
	**(iv)** `void display()`: Prints elements.
15. Define `void sort(int a[], int n)` to sort an array. Show step-by-step execution for `[34, 56, 71, 1, 2]`.
16. Class `Box` with static `count` to track objects created/destroyed.
17. Write a function `swap()` to interchange the values of two numbers using call by reference. 
18. Write a function in C++ that takes a number `n` as input and returns its factorial if `n` is even; otherwise, returns `0`
19. Write a C++ program to display the following pattern (example for 5 rows):

```
A
BB
CCC
DDDD
EEEEE
```
20. Create a class `Complex` with:
	- Data members: integer `a` (real), float `b` (imaginary).
	- Member functions:
	    - Default constructor (initializes `a`, `b` to `0`).
	    - Parameterized constructor (initializes `a`, `b` to passed values).
	    - `print()` to display the number as `a + ib` (e.g., `4 + i5` for `a=4`, `b=5`)
21. Write a C++ program to open a text file and display its total number of characters.
22. Write a C++ function for linear search in an array. Rewrite it using templates.
23. Write a program to check if a given string is a palindrome or not.
24. Consider the class definition:

```c
class circle {
    float radius;
};
```

	Define the following member functions:  
	(i) A default constructor that initializes `radius` to zero.  
	(ii) A parameterized constructor that assigns the input value to `radius`.  
	(iii) A function `areaofcircle()` to compute the area of a circle.  
	Create an object of class `circle` and call these functions in `main()`.
25. Creates a file `File1` and writes the line:  
	`"The biggest adventure is to live a life of your dreams."`  
	Counts the number of characters in `File1` and prints this value.
26. Write a program to find the Least Common Multiple (LCM) of two numbers `a` and `b` taken as input from the user.
27. Write a program to print a pattern taking the number of lines as input from the user.
```
   *
  ***
 *****
*******
```
28. Write a program that defines a function template to:  
	(i) Accept one `int` and one `char` type argument.  
	(ii) Accept one `int` and one `float` type argument.  
	(iii) Accept two `float` type arguments.
29. Write a program to read an array of `n` elements (input `n` from the user), multiply every element by 10, and print the resultant array.
30. Write a C++ program to print the pattern:

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
```
31. Write a C++ program to reverse an input string.
32. Write a C++ program to swap two integers and two floats using function overloading.
33. Write a C++ program to count spaces in a text file. 
34. Write a C++ program to check if a number is even or odd.
35. function `findHCF` to find the HCF of two numbers using Euclid's algorithm
36. read numbers from `numbers.txt` 1 number from each line, write all the even numbers in `even.txt` one number per line.
37. template function to sort an array of any data type in ascending order.
38. try block to throw a char value, catch block to handle that, and another catch block to handle any exception.
39. base class Numbers with a and b data members. default and parameterized constructors and a `display()` function displaying "Displaying Numbers"
	a derived class `GreaterNumber` that publicly inherits from Numbers, default and parameterized constructors, function `findGreaterNum()` finding greater of a and b with ternary operator. `display` function to show the greater number.
40. program to ask the user for numbers till -1 is entered, print the number of positive negative and zero numbers entered except -1.
41. nested for loop structure to print the following pattern
```
1
2 4
3 6 9
4 8 12 16
```
42. `sumArr()` that accepts an integer array and size of the array, return the sum of all the array elements.
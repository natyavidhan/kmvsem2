
1.
```cpp
int main() {
	char a;
	cin >> a;
	cout << int(a) << endl;
}
```
2.
```cpp
#include <iostream>

using namespace std;

void swapNums(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = *temp;
}

int main() {
	int a, b;
	cin >> a;
	cin >> b;
	swapNums(&a, &b);
	return 0;
}
```
3.
```cpp
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream in("file.txt");
	ofstream out("out.dat");
	
	char ch;
	bool lastSpace = false;
	
	while (in.get(ch)) {
		if (ch == ' ') {
			if (!lastSpace){
				out.put(' ');
				lastSpace = true;
			}
				
		} else {
			out.put(ch);
			lastSpace = false;
		}
	}
	
	return 0;
}
```
4.
```cpp
class ThreeDim {
	int x, y, z;
	public:
		ThreeDim(): x(0), y(0), z(0) {}
		ThreeDim(int x_, int y_, int z_) {
			x = x_;
			y = y_;
			z = z_;
		}
		void out() {
			cout << x << y << z << endl;
		}
};
```
5.
```cpp
class Area {
public:
    void area(float s) {
        float sa = s * s;
        cout << "Area of Square: " << sa << endl;
    }

    void area(float r, bool circ) {
        float ca = 3.14159 * r * r;
        cout << "Area of Circle: " << ca << endl;
    }
};
```
6.
```cpp
class Complex {
	private:
		float real;
		float imag;
	public:
		Complex() {
			real = 0;
			imag = 0;
		}
		Complex(float r, float i) {
			real = r;
			imag = i;
		}
		void add(Complex c) {
			real += c.real;
			imag += c.imag;
		}
};
```
7.
```cpp
bool compareArr(int arr1[], int arr2[], int n) {
	for (int i = 0; i < n; i++) {
		if (arr1[i] != arr2[i]) 
			return false;
	}
	return true;
}
```
8.
```cpp
void UpperTriangle(int** arr1, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++){
			arr1[i][j] = 0;
		}
	}
}
```
9.
```cpp
int main() {
	const char *str = "NITIN";
	while (*str != '\0') {
		cout << *str << ": " << int(*str) << endl;
		str++;
	}
	return 0;
}
```
10.
```cpp
void concatenate(char a[], char b[], int n, int m) {
	for (int i = 0; i < m; i++)
		a[n + i] = b[i];
	a[m + n] = '\0';
}
```
11.
```cpp
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main() {
	ifstream in("A1.txt");
	ofstream out("A2.txt");
	
	string word;
	int count = 0;
	
	while (in >> word) {
		out << word << " ";
		count++;
	}
	cout << count;
	return 0;
}
```
12. 
```cpp
#include <iostream>

using namespace std;

double fact(int x) {
	double result = 1;
	for (int i=x; i > 0; i--) {
		result = result * i;
	}
	return result;
}

double pow(int base, int exp) {
	double result = 1;
	for (int i = 0; i < exp; i++) {
		result = result * base;
	}
	return result;
}

int main() {
	int x;
	int n;
	cin >> x;
	cin >> n;
	
	double s;
	int sign = 1;
	
	for (int i = 1; i <= n*2; i=i+2) {
		s = s + (sign * pow(x, i) / fact(i));
		sign = sign * -1;
	}
	
	cout << s << endl;
	
    return 0;
}
```
13.
```cpp
#include <iostream>
#include <string>

using namespace std;

class Bankaccount {
	string name;
	long long int accno;
	double balance;
	
	public:
		Bankaccount() {
			name = "John Doe";
			accno = 100100100100;
			balance = 500;
		}
		Bankaccount(string n, long long int an, double b) {
			name = n;
			accno = an;
			balance = b;
		}
		void input() {
			cout << "Name: ";
			getline(cin, name);
			cout << "Account No.: ";
			cin >> accno;
			cout << "Balance: ";
			cin >> balance;
		}
		void withdrawl(double x) {
			if (balance - x >= 500) {
				balance-=x;
			} else {
				cout << "Insufficient Funds.";
			}
		}
		void deposit(double x) {
			balance += x;
		}
		void display() {
			cout << "Name: " << name << "\nAccount No.: " << accno << "\nBalance: " << balance;
		}
};

int main() {
	Bankaccount b;
	b.display();
}
```
14.
```cpp
template<typename T>
class Vector {
	T a[20];
	int n;
	public:
		Vector() {
			n = 0
		}
		Vector(const Vector<T>& v) {
			n = v.n;
			for (int i = 0; i < n; i++) {
				a[i] = v.a[i];
			}
		}
		
		void input() {
			for (int i = 0; i < n; i++) {
				cin >> a[i];
			}
		}
		
		Vector<T> add(Vector<T>& v) {
			Vector<T> result;
			result.n = n;
			for (int i=0; i<n; i++){
				result.a[i] = a[i] + v.a[i];
			}
			return result;
		}
		void display() {
	        for (int i = 0; i < n; i++) {
	            cout << a[i] << " ";
	        }
	        cout << endl;
    	}
};
```
15.
```cpp
#include <iostream>
#include <string>

using namespace std;

void bubbleSort(int arr[], int n) {
	for (int i=0; i<n; i++){
		for (int j=0; j<n-i-1; j++){
			if (arr[j] > arr[j+1]) swap(arr[j+1], arr[j]);	
		}
	}
}

int main() {
	int nums[5] = {34, 56, 71, 1, 2};
	bubbleSort(nums, 5);
	for (int i=0; i<5; i++)
		cout << nums[i] << " ";
	return 0;
}
```
16.
```cpp
#include <iostream>
#include <string>

using namespace std;

class Box{
	static int count;
	public:
		Box() {
			count++;
			cout << count << endl;
		}
		~Box() {
			count--;
			cout << count << endl;
		}
};

int Box::count = 0;

int main() {
	Box b1, b2, b3;
	return 0;
}
```
17.
```cpp
#include <iostream>

using namespace std;

void swap(int &a, int &b) {
	int temp = a;
	a = b;
	b = temp;
}

int main() {
	int a = 5;
	int b = 4;
	swap(a, b);
	cout << a << " " << b << endl;
}
```
18.
```cpp
int fact(int n) {
	int res = 1;
	for (int i=1; i <=n; i++)
		res*=i;
	if (res%2==0) {
		return res;
	} else {
		return 0;
	}
}
```
19.
```cpp
int main() {
	int n=5;
	for (int i = 0; i<n; i++){
		for (int j = 0; j<=i; j++)
			cout << char(65+i);
		cout << endl;
	}
	return 0;
}
```
20.
```cpp
class Complex {
	private:
		float a;
		float b;
	public:
		Complex() {
			a = 0;
			b = 0;
		}
		Complex(float r, float i) {
			a = r;
			b = i;
		}
		void print(Complex c) {
			cout << a << " + i" << b;
		}
};
```
21.
```cpp
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream in("file.txt");
	
	char ch;
	int count = 0;
	while (in.get(ch)) {
		count++;
	}
	cout << count;
	return 0;
}
```

22.
```cpp
int search(int arr[], int n, int key) {
	for (int i = 0; i < n; i++){
		if (arr[i] == key) return i;
	}
	return -1;
}

template<typename T>
int search(T arr[], int n, T key) {
	for (int i = 0; i < n; i++){
		if (arr[i] == key) return i;
	}
	return -1;
}
```
23.
```cpp
bool isPalindrome(const string& str) {
	int start = 0;
	int end = str.length() -1;
	
	while (start < end) {
		if (str[start] != str[end])
			return false;
		start++;
		end--;
	}
	return true;
}
```
24.
```cpp
#include <iostream>

using namespace std;

class circle {
    float radius;
    public:
    	circle() {
    		radius = 0;
		}
		circle(float rad) {
			radius = rad;
		}
		void areaofcircle() {
			float area = 3.14 * radius * radius;
			cout << area;
		}
};

int main() {
	circle circ(5);
	circ.areaofcircle();
	return 0;	
}
```
25.
```cpp
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream out("File1.txt");
	out << "The biggest adventure is to live a life of your dreams.";
	out.close();
	
	ifstream in("File1.txt");
	char ch;
	int count = 0;
	while (in.get(ch)) {
		count++;
	}
	cout << count << endl;
	return 0;
}
```
26.
```cpp

```
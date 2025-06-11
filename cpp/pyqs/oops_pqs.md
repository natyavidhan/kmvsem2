### 1.
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

### 2.
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

### 3.
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

### 4.
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

### 5.
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

### 6.
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

### 7.
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

### 8.
```cpp
#include <iostream>
#include <fstream>

using namespace std;


template<typename T>
void sort(T arr[], int n) {
    for (int i=0; i<n; i++){
        for (int j=0; j<n-i-1; j++){
            if (arr[j] > arr[j+1]) swap(arr[j], arr[j+1]);
        }
    }
}

int main() {
    int arr[5] = {5, 6, 8, 3, 4};
    sort<int>(arr, 5);
    
    for (int i = 0; i<5; i++)
        cout << arr[i] << endl;
    
    return 0;
}
```

### 9.
```cpp
#include <iostream>

using namespace std;

class Numbers {
    public:
        int a;
        int b;
        Numbers(): a(0), b(0) {}
        Numbers(int a_, int b_) {
            a=a_;
            b=b_;
        }
        virtual void display() {
            cout << "Displaying numbers\n";
        }
};

class GreaterNumber: public Numbers {
    public:
        GreaterNumber();
        GreaterNumber(int a_, int b_) {
            a = a_;
            b = b_;
        }
        int findGreaterNum() {
            int max = a > b ? a : b;
            return max;
        }
        
        void display() override {
            cout << findGreaterNum() << endl;
        }
            
};

int main() {
    GreaterNumber num(5, 4);
    num.display();
    return 0;
}
```
#include <iostream>
#include <iomanip>
using namespace std;


inline double square(double x) {
    return x * x;
}

double power(double base, int exponent = 2) {
    double result = 1;
    for (int i = 0; i < exponent; i++)
        result *= base;
    return result;
}


double calc(double a, double b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0) {
                cout << "Error: divide by zero" << endl;
                return 0;
            }
            return a / b;
        default:
            cout << "Invalid operator!" << endl;
            return 0;
    }
}

double calc(int a, int b, char op) {
    return calc((double)a, (double)b, op);
}

int main() {
    double a, b;
    char op;
    cin >> a >> b >> op;

    cout << fixed << setprecision(2);
    cout << "square(" << a << ") = " << square(a) << endl;
    cout << "power(" << a << ") = " << power(a) << endl;
    cout << "calc(" << a << ", " << b << ", '" << op << "') = " << calc(a, b, op) << endl;
    return 0;
}

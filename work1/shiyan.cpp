#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string name;
        double chinese, math, english;
        cin >> name >> chinese >> math >> english;
        double avg = (chinese + math + english) / 3;
        cout << fixed << setprecision(2);
        cout << left << setw(10) << name
             << setw(8) << chinese
             << setw(8) << math
             << setw(8) << english
             << setw(8) << avg;
        if (avg >= 90)
            cout << "Excellent";
        cout << endl;
    }
    return 0;
}

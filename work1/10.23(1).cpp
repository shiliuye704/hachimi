#include <iostream>
#include <cctype>
using namespace std;

int countVowels(const char* p) {
    int count = 0;
    while (*p) {
        char ch = tolower(*p);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            count++;
        p++;
    }
    return count;
}

int main() {
    char str[100];
    cin.getline(str, 100);
    cout << "Number of vowels: " << countVowels(str);
    return 0;
}

#include <iostream>
#include <string>
using namespace std;

static inline bool check_luhn(string card_number) {

    int n_sum = 0;
    size_t num_digits = card_number.length();
    bool is_second = false;

    for (int i = num_digits - 1; i >= 0; i--) {

        char zero_char = '0';
        int d = (int)card_number[i] - (int)zero_char;

        if (is_second == true) {
            d *= 2;
        }

        n_sum += d / 10;
        n_sum += d % 10;

        is_second = !is_second;
    }

    if (n_sum % 10 == 0) {
        return true;
    }
    else {
        return false;
    }
}

int main(int argc, char* argv[]) {

    if (argc != 2) {
        cerr << "Required one argument: <card_number>" << endl;
    }

    string card_number = argv[1];
    bool result;

    result = check_luhn(card_number);

    if (result == true) {
        cout << "valid" << endl;
    }
    else {
        cout << "invalid" << endl;
    }
}

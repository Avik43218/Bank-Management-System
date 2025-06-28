#include <iostream>
#include <random>
#include <string>
using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cerr << "Required 2 arguments: <aadhar> <phone>" << endl;
        return 1;
    }

    string aadhar = argv[1];
    string phone = argv[2];

    int digits = 17;
    string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string result;

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(0, charset.size() - 1);

    for (int i = 0; i < digits; ++i) {
        result += charset[dist(gen)];
    }

    string client_id = result + aadhar.substr(aadhar.size() - 6) + phone.substr(1, 7);

    cout << client_id << endl;

    return 0;
}

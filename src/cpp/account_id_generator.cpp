#include <iostream>
#include <random>
#include <string>
#include <cmath>
using namespace std;

int main(int argc, char* argv[]) {

    if (argc != 4) {
        cerr << "Required 2 argument: <account_type> <aadhar> <client_id>" << endl;
        return 1;
    }

    string account_type = argv[1];
    string aadhar = argv[2];
    string client_id = argv[3];
    string prefix;

    if (account_type == "savings") {
        prefix = "SAV";
    }
    else if (account_type == "current") {
        prefix = "CUR";
    }
    else if (account_type == "business") {
        prefix = "BUS";
    }

    int digits = 10;
    int bank_id = 502;

    int lower = pow(10, digits - 1);
    int upper = pow(10, digits) - 1;

    random_device rd;  // Hardware based seed
    mt19937 gen(rd());  // Mersenne Twister Random Number Generator
    uniform_int_distribution<uint32_t> dist(lower, upper);

    string id = prefix + to_string(bank_id) + aadhar.substr(aadhar.size() - 4) +
     client_id.substr(0, 5) + to_string(dist(gen));

    cout << id << endl;

    return 0;

}

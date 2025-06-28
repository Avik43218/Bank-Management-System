#include <iostream>
#include <random>
#include <string>
#include <iomanip>
#include <sstream>
#include <ctime>
using namespace std;

string get_timestamp() {
    time_t now = time(nullptr);
    tm* ptm = localtime(&now);

    ostringstream oss;
    oss << put_time(ptm, "%y%m%d%H%M%S");
    return oss.str();
}

int main(int argc, char* argv[]) {
    // [txn_type]
    if (argc != 2) {
        cerr << "Required one argument: <txn_type>" << endl;
        return 1;
    }

    const string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string txn_type = argv[1];
    string prefix;
    string timestamp = get_timestamp();

    if (txn_type == "withdraw") {
        prefix = "WDR";
    }
    else if (txn_type == "deposit") {
        prefix = "DEP";
    }
    else if (txn_type == "transfer") {
        prefix = "TRF";
    }
    else if (txn_type == "payment") {
        prefix = "PAY";
    }
    else if (txn_type == "refund") {
        prefix = "RFD";
    }
    else if (txn_type == "loan repayment") {
        prefix = "LRP";
    }
    else if (txn_type == "loan credit") {
        prefix = "LCR";
    }

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(0, charset.size() - 1);

    string txn_id;
    for (int i = 0; i < 15; ++i) {
        txn_id += charset[dist(gen)];
    }

    string final_txn_id = prefix + '-' + timestamp + '-' + txn_id;

    cout << final_txn_id << endl;

    return 0;

}

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <random>
#include <cmath>
using namespace std;

struct Client {
    string id;
    string name;
    string age;
    string email;
    string contact;
    string aadhar;
    string balance;
};

string file_path = "data_file.txt";
string new_file_path = "new_file.txt";


// Split comma separated values
vector<string> split(string &s, char delimiter) {

    vector<string> tokens;
    stringstream ss(s);
    string item;

    while(getline(ss, item, delimiter)) {
        tokens.push_back(item);
    }
    return tokens;

}


string create_entry(string name, string age, string email, string contact, string aadhar) {

    // Create a data file
    fstream data_file(file_path, ios::app);

    // Generate a unique ID
    int digits = 9;

    int lower = pow(10, digits - 1);
    int upper = pow(10, digits) - 1;

    random_device rd;  // Hardware based seed
    mt19937 gen(rd());  // Mersenne Twister Random Number Generator
    uniform_int_distribution<uint32_t> dist(lower, upper);

    string id = to_string(dist(gen)) + to_string(dist(gen));
    uniform_int_distribution<int> lastDigit(1, 9);

    id += to_string(lastDigit(gen));

    // Append the user data
    vector<Client> clients;
    char balance = '0';
    string str(1, balance);
    clients.push_back({id, name, age, email, contact, aadhar, str});

    // Write to file
    if (data_file.fail()) {

        cout << "Error! File not found!";
        exit(0);
        
    }
    else if (data_file.is_open()) {

        for (const Client& client : clients) {
            data_file << client.id << "," << client.name << "," << client.age << "," << client.email
            << "," << client.contact << "," << client.aadhar << "," << client.balance << "\n";
        }
    }

    data_file.close();
    return id;

}

// 9630524637245587747

void read_data(string id) {

    string name;
    string age;
    string email;
    string contact;
    string aadhar;
    string balance;

    fstream file(file_path, ios::in);
    string client_data;

    if (file.fail()) {
        cout << "Error! File not found!";
        exit(0);
    }

    while (!file.eof()) {
        cin.ignore();
        getline(file, client_data);
        vector<string> tokens = split(client_data, ',');

        if (tokens.size() < 7) continue;

        if (id == tokens[0]) {
            name = tokens[1];
            age = tokens[2];
            email = tokens[3];
            contact = tokens[4];
            aadhar = tokens[5];
            balance = tokens[6];

            cout << "Here's your account details: " << endl;
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
            cout << "Email: " << email << endl;
            cout << "Contact: " << contact << endl;
            cout << "Aadhar: " << aadhar << endl;
            cout << "Balance: " << balance << endl;
            break;
        }
    }

}

bool deposit_money(string id) {

    ifstream my_file(file_path, ios::in);
    ofstream new_file(new_file_path, ios::app);


    if (my_file.fail()) {
        cout << "Error! File not found!";
        return false;
    }

    string client_data;
    string deposit;
    bool found = false;

    while (getline(my_file, client_data)) {
        vector<string> tokens = split(client_data, ',');  // split() doesn't return any error

        if (tokens.size() < 7) continue;

        if (id == tokens[0]) {
            cout << "Enter deposit amount: ";
            getline(cin, deposit);


            int current_balance = stoi(tokens[6]);
            int new_deposit = stoi(deposit);

            int updated_balance = current_balance + new_deposit;

            tokens[6] = to_string(updated_balance);
            found = true;

        }


        new_file << tokens[0] << "," << tokens[1] << "," << tokens[2] << "," << tokens[3]
        << "," << tokens[4] << "," << tokens[5] << "," << tokens[6] << '\n';

    }

    my_file.close();
    new_file.close();

    remove(file_path.c_str());
    rename(new_file_path.c_str(), file_path.c_str());

    if (!found) return false;

    ifstream read_data(new_file_path, ios::in);
    string data;

    while (getline(read_data, data)) {
        vector<string> elements = split(data, ',');

        if (elements.size() < 7) continue;

        if (id == elements[0]) {
            read_data.close();
            return !(elements[6] == "0");

        }
    }

    return false;

}


int main() {

    int i = 1;
    while (i == 1) {
        cout << "Welcome to XYZ Bank Terminal!" << endl;
        cout << "What do you want to perform?" << endl;
        cout << endl;
        cout << "1. Add account" << endl;
        cout << "2. Check account data" << endl;
        cout << "3. Deposit amount" << endl;
        cout << endl;

        int choice;
        cout << "Enter your choice: ";
        cin >> choice;

        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input!\n";
            cin >> choice;
        }
        
        cout << endl;
        
        if (choice == 1) {

            fstream write_file(file_path, ios::in);

            string name;
            string age;
            string email;
            string contact;
            string aadhar;

            cout << "Enter your name: ";
            cin.ignore();   // Ignores the newline character in the input buffer
            getline(cin, name);
            cout << "\nEnter your age: ";
            getline(cin, age);
            cout << "\nEnter your email: ";
            getline(cin, email);
            cout << "\nEnter your contact number: ";
            getline(cin, contact);
            cout << "\nEnter your aadhar number: ";
            getline(cin, aadhar);

            string account_id = create_entry(name, age, email, contact, aadhar);

            if (!write_file.fail()) {
                cout << "Account created successfully!" << endl;
                cout << "Your Account ID is: " << account_id << endl;
            }

            write_file.close();
        }

        else if (choice == 2) {

            string acc_id;
            cout << "Enter your Account ID: ";
            cin.ignore();
            getline(cin, acc_id);
            cout << endl;

            read_data(acc_id);

        }

        else if (choice == 3) {

            string acc_id;
            cout << "Enter your Account ID: ";
            cin.ignore();
            getline(cin, acc_id);
            cout << endl;

            bool result = deposit_money(acc_id);

            if (result) {
                cout << "Amount successfully deposited!" << endl;
            }
            else {
                cout << "There was problem! Please try again!" << endl;
            }

        }

        cout << "Continue? [1/0] ";
        cin >> i;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << endl;
    }
    return 0;
}

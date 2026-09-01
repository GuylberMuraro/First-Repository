#include <iostream>

using namespace std;

int main() {
    int S, M, T;
    
    cout << "Type the students amount:" << endl;
    cin >> S;
    cout << "Type the monitors amount:" << endl;
    cin >> M;

    T = S + M;

    if (T > 50 || T < 0) {
        cout << "No way to get on the cable car" << endl;
    } else if (T <= 50 || T > 0 || M < 1) {
        cout << "No way! No monitors, no cable car" << endl;
    } else {
        cout << "Okay" << endl;
    }

    return 0;
}
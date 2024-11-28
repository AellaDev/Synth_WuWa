#include <iostream>
using namespace std;

void synthesizeItems(int &A, int &B, int &C, int &D) {
    int cFromD = D / 3;
    C += cFromD; 
    D %= 3;       

    int bFromC = C / 3;
    B += bFromC;  
    C %= 3;       

    int aFromB = B / 3;
    A += aFromB;   
    B %= 3;       
}

int main() {
    int A = 0, B = 0, C = 0, D = 0; 
    char choice;

    do {
        int addA, addB, addC, addD;

        cout << "Enter the number of new A items to add: ";
        cin >> addA;
        cout << "Enter the number of new B items to add: ";
        cin >> addB;
        cout << "Enter the number of new C items to add: ";
        cin >> addC;
        cout << "Enter the number of new D items to add: ";
        cin >> addD;

        A += addA;
        B += addB;
        C += addC;
        D += addD;

        synthesizeItems(A, B, C, D);

        cout << "Updated number of A items: " << A << endl;
        cout << "Updated number of B items: " << B << endl;
        cout << "Updated number of C items: " << C << endl;
        cout << "Updated number of D items: " << D << endl;

        cout << "Would you like to add more items? (y/n): ";
        cin >> choice;

    } while (choice == 'y' || choice == 'Y');

    cout << "Final counts - A: " << A << ", B: " << B << ", C: " << C << ", D: " << D << endl;
    return 0;
}

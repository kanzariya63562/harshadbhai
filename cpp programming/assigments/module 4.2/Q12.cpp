#include <iostream>
using namespace std;

  //Write a program to find the max number from given two numbers using friend function.
int main()
{
    int x, y;
    cout << "Enter two numbers: ";
    cin >> x >> y;
    if (x > y)
    {
        cout << "Max is " << x;
    }
    else
    {
        cout << "Max is " << y;
    }
    return 0;
}
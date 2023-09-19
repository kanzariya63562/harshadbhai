#include<iostream>
#include<cmath>
using namespace std;

  /*Write a program to calculate the area of circle, rectangle and triangle using Function Overloading
 Rectangle: Area * breadth
 Triangle: ½ *Area* breadth
 Circle: Pi * Area *Area.*/


void area(float, float, float);
void area(float, float);
void area(float);
int main() {
    int choice;
    float r, l, b, x, y, z;
    cout<<"Whose area you want to calculate?"<<endl;
    cout<<"1 - Area of circle"<<endl;
    cout<<"2 - Area of rectangle"<<endl;
    cout<<"3 - Area of triangle"<<endl;
    cin>>choice;
    switch (choice)
    {
    case 1:
        cout<<"Enter the radius of circle."<<endl;
        cin>>r;
        area(r);
        break;
    
    case 2:
        cout<<"Enter the sides of rectangle."<<endl;
        cin>>l>>b;
        area(l,b);
        break;
    case 3:
        cout<<"Enter the sides of triangle."<<endl;
        cin>>x>>y>>z;
        area(x,y,z);
        break;
    default:
        cout<<"Choose from 1, 2, 3"<<endl;
        break;
    }
    return 0;
}
void area(float r) {
    float pi = 3.14;
    cout<<"Area of circle is "<<pi*r*r<<endl;
}
void area(float l, float b) {
    cout<<"Area of rectangle is "<<l*b<<endl;
}
void area(float a, float b, float c) {
    float s, area;
    if((a+b)>c && (b+c)>a && (a+c)>b) {
        s = (a+b+c)/2;
        area = sqrt(s*(s-a)*(s-b)*(s-c));
        cout<<"Area of triangle is "<<area<<endl;
    }
    else cout<<"Triangle does not form"<<endl;
}
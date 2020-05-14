#include <cstdlib>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <cmath>
#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

double f(double val) {
	return 1.8*val*val - sin(10 * val);
}

double df(double val) {
	return 3.6*val - 10 * cos(10 * val);
}

double ddf(double val) {
	return 3.6 + 100 * sin(10 * val);
}

void methodKombi() {
	double a, b, eps=0.001;
	double temp = 0;
	double x = 0;
	cout << "Input EPS:\n";
	cin >> eps;

	do {
	cin >> a;
	cin >> b;
	if (f(a)*f(b) > 0){  // must also be but doent work || df(a)*df(b) < 0) {
		cout << "enter correct value\n";
	}
	} while (f(a)*f(b) > 0);// must also be but doent work|| df(a)*df(b) < 0);


	do
	{
		if (f(a)*ddf(a) < 0)
		{
			temp = a;
			a = b;
			b = temp;
		}

		x = b - ((f(b)) / (df(b)));
		if (fabs(x-b)<eps)
		{
			cout <<endl << endl << x << endl;
			system("pause");
		}
		temp = b;
		b = x;

		x = a - ((f(a)*(temp-a)) / (f(temp)-f(a)));
		if (fabs(x - a) < eps)
		{
			cout << endl << endl << x << endl;
			system("pause");
		}
		a = x;

	} while (true);

}



void main() {

	//SetConsoleCP(CP_UTF8);
	//SetConsoleOutputCP(CP_UTF8);


	methodKombi();

	cout << endl;
	system("pause"); //щоб вікно не закрилося
}
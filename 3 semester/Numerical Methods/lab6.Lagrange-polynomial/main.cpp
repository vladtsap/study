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
const int n = 5;

double methodLangr(double X[n], double Y[n], double t) {
	double res, numerator, denominator;
	res = 0;
	for (int j = 0; j < n; j++) {
		numerator = 1;
		denominator = 1;
		for (int i = 0; i < n; i++) {
			if (i != j) {
				numerator = numerator * (t - X[i]);
				denominator = denominator * (X[j] - X[i]);
			}
		}
		res = res + Y[j] * numerator / denominator;
	}
	return res;
}

void main() {
	double X[n] = { -5, -1.6, -0.8, -0.2, 0.6 };
	double Y[n] = { -2.31, -1.25, -0.73, -0.2, 0.57 };
	double inpt = 0;
	cout << "Enter x:\n";
	cin >> inpt;
	cout << "Ln (x) = " << methodLangr(X, Y, inpt) << endl;
	system("pause");
}
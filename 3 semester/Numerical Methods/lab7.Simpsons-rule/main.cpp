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
	return (val * pow(2.71, (0.7*val)))/pow((1+0.7*val),2);
	//return (pow(val, 2)) / (1.2+0.9*pow(2.71, 0.35*val));
}

double a = 0.3, b=1.5;
//double a = 0.2, b=1.2;

double methodSimpson(int n) {
	double h = (b - a) / (2 * n);
	double s = f(a) - f(b);
	int e = 1;
	for (int i = 0; i < 2*n; i++)
	{
		s += (3 + e)*f(a + i * h);
		e = -1 * e;
	}
	return s * (h / 3);
}


void main() {

	//SetConsoleCP(CP_UTF8);
	//SetConsoleOutputCP(CP_UTF8);
	double s1 = methodSimpson(1);
	int n = 1;
	n *= 2;
	double s2 = methodSimpson(n);
	while (fabs(s2 - s1) > 0.5*0.000001)
	{
		n *= 2;
		s1 = s2;
		s2 = methodSimpson(n);
	}
	cout << s2 << endl << n << endl;

	system("pause"); //stop after ended
}
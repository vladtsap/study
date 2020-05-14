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

const int ourLimit = 100;
int sizeMatrix;
double roots[ourLimit] = {};
double tempX[ourLimit] = {};
double arr[ourLimit][ourLimit] = {};
double Barr[ourLimit] = {};
double eps;
double w;
double norma;
int itr = 0;


void printSystem() {
	cout << "System:\n";
	for (int i = 0; i < sizeMatrix; i++)
	{
		for (int j = 0; j < sizeMatrix; j++)
		{
			cout << arr[i][j] << " ";
			
		}
		cout << "| " << Barr[i] << endl;
	}
	cout << endl;
}

void printAnswer() {
	double max = 0, h;
	for (int i = 0; i < sizeMatrix; ++i)
	{ 
		cout << "x" << i + 1 << " = " << roots[i] << endl;
		
	}
	
}

void readFromFile() {
	string input;
	ifstream readfile;
	readfile.open("input.txt");
	readfile >> input;
	//Читання з файлу розміру матриці
	sizeMatrix = stoi(input);
	//Заповнення матриці елементами з файлу
	for (int i = 0; i < sizeMatrix; ++i)
	{
		for (int j = 0; j < sizeMatrix; j++)
		{
			readfile >> input;
			arr[i][j] = stoi(input);
		}
		readfile >> input;
		Barr[i] = stoi(input);
	}
	readfile.close();
}

void methodRelax() {
	int k = 0;
	do {
		itr++;
		norma = 0;
		for (int i = 0; i < sizeMatrix; i++) {
			roots[i] = Barr[i];
			for (int j = 0; j < sizeMatrix; j++) {
				if (i != j)
					roots[i] = roots[i] - arr[i][j] * roots[j];
			}
			roots[i] /= arr[i][i];

			roots[i] = w * roots[i] + (1 - w)*tempX[i];

			if (fabs(roots[i] - tempX[i]) > norma)
				norma = fabs(roots[i] - tempX[i]);
			tempX[i] = roots[i];
		}
	} while (norma > eps);
}

void checkDiagonal() {
	double tempsum = 0;
	for (int i = 0; i < sizeMatrix; ++i)
	{
		tempsum = 0;
		for (int j = 0; j < sizeMatrix; ++j)
		{
			if (i != j)
			{
				tempsum += fabs(arr[i][j]);
			}
		}
		if (fabs(arr[i][i]) < tempsum)
		{
			cout << "NEMA DIAGONALNOI PEREVAGY\n";
			system("pause");
			exit(0);
		}
	}
}

void main() {

	//SetConsoleCP(CP_UTF8);
	//SetConsoleOutputCP(CP_UTF8);

	readFromFile();

	printSystem();

	cout << "INPUT EPS:\n";
	//cin >> eps;
	eps = 0.00001;

	cout << "INPUT w:\n";
	//cin >> w;
	w = 0.5;

	checkDiagonal();

	methodRelax();

	printAnswer();
	cout << "iter = " << itr << endl;
	cout << endl;
	system("pause"); //щоб вікно не закрилося
}
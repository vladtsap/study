#include <cstdlib>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
const int ourLimit = 100;
int sizeMatrix;
int orderOfRoots[ourLimit + 1] = {};
double det = 1;
double roots[ourLimit] = {};
double arr[ourLimit][ourLimit] = {};
double Barr[ourLimit] = {};

void printSystem() {
	cout << "System:\n";
	for (int i = 0; i < sizeMatrix; i++)
	{
		for (int  j = 0; j < sizeMatrix; j++)
		{
			cout << arr[i][j] << " ";
		}
		cout << "| " << Barr[i] << endl;
	}
	cout << endl;
}

void printAnswer() {
	if (!isnan(det)) {
	cout << "Answer:\n";
	for (int i = 0; i < sizeMatrix; ++i) {
		for (int j = 0; j < sizeMatrix; j++) {
			if (i == orderOfRoots[j]) { //Розставляєм корені по порядку
				cout << "x" << i + 1 << " = " << roots[j] << "\n";
				break;
			}
		}
	}

		cout << endl << "Determinant: " << det << endl;
	}
	else {
		cout << "THERE IS NO SOLUTION\n";
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

void writeToFile() {
	ofstream writefile;
	writefile.open("output.txt");

	if (!isnan(det)) {
		writefile << "Answer:\n";
		for (int i = 0; i < sizeMatrix; ++i) {
			for (int j = 0; j < sizeMatrix; j++) {
				if (i == orderOfRoots[j]) { //Розставляєм корені по порядку
					writefile << "x" <<i+1<< " = " << roots[j] << "\n";
					break;
				}
			}
		}

		writefile <<endl << "Determinant: " << det << endl;
	}
	else {
		writefile << "THERE IS NO SOLUTION\n";
	}
	
	writefile.close();
}

void cleanFile() {
	ofstream cleanfile;
	cleanfile.open("output.txt");
	cleanfile.close();
}

void impossFile() {
	ofstream impossfile;
	impossfile.open("output.txt");
	impossfile << "NEMA ODNOZNA4NOGO ROZVYAZKU\n";
	impossfile.close();
}

void mainElem(int k) {
	int maxI = k;
	int maxJ = k;
	double temp;
	int i, j;
	//Шукаємо найбільший елемент по всій матриці
	for (int i = k; i < sizeMatrix; i++)
	{
		for (int j = k; j < sizeMatrix; j++)
		{
			if (arr[maxI][maxJ] < arr[i][j])
			{
				maxI = i;
				maxJ = j;
			}
		}
	}
	
	if (fabs(arr[maxI][maxJ]) <= 0.0001)
	{
		cout << "NEMA ODNOZNA4NOGO ROZVYAZKU\n";
		impossFile();
		system("pause");
		exit(0);
	}

	if (maxI != k)
	{
		det *= -1;
	}
	if (maxJ != k) {
		det *= -1;
	}

	//Переставляємо рядки
	for (j = k; j < sizeMatrix; j++)
	{
		temp = arr[k][j];
		arr[k][j] = arr[maxI][j];
		arr[maxI][j] = temp;


	}
	//Переставляємо стовпці
	for (i = 0; i < sizeMatrix; i++)
	{
		temp = arr[i][k];
		arr[i][k] = arr[i][maxJ];
		arr[i][maxJ] = temp;
		
	}


	temp = Barr[k];
	Barr[k] = Barr[maxI];
	Barr[maxI] = temp;

	//Міняємо порядок коренів
	i = orderOfRoots[k];
	orderOfRoots[k] = orderOfRoots[maxJ];
	orderOfRoots[maxJ] = i;

	
}

void methodGauss() {
	double m;

	//Спочатку порядок один для всіх
	for (int i = 0; i < sizeMatrix; i++)
	{
		orderOfRoots[i] = i;
	}

	//Прямий хід Гауса
	
	for (int k = 0; k < sizeMatrix - 1; k++)
	{
		mainElem(k);
		
		if (fabs(arr[k][k]) < 0.0001)
		{
			cout << "NEMA ODNOZNA4NOGO ROZVYAZKU\n";
			impossFile();
			system("pause");
			exit(0);
			break;
		}


		for (int i = k + 1; i < sizeMatrix; i++){
			m = (arr[i][k]) / (arr[k][k]);
			Barr[i] -= Barr[k] * m;
			for (int j = k+1; j < sizeMatrix; j++)
			{
				arr[i][j] -= arr[k][j]*m;
			}
		}	

	}
	for (int i = 0; i < sizeMatrix;i++)
	{
		det *= arr[i][i];

	}

	//Зворотний хід Гауса	
	roots[sizeMatrix - 1] = Barr[sizeMatrix - 1] / arr[sizeMatrix - 1][sizeMatrix - 1];
	for (int k = sizeMatrix - 1; k >= 0; k--) {
		m = 0;
		for (int j = k + 1; j < sizeMatrix; j++)
			m += arr[k][j] * roots[j];
		roots[k] = (Barr[k] - m) / arr[k][k];
	}
}





void main() {

	readFromFile();
	
	printSystem();

	methodGauss();
	
	printAnswer();

	writeToFile();

	cout << endl;
	system("pause"); //щоб вікно не закрилося
}
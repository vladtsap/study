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
			//printf("%.2f  ", arr[i][j]);
		}
		cout << "| "<< Barr[i] << endl;
	}
	cout << endl;
}

void printAnswer() {
	double max = 0, h;
	for (int i = 0; i < sizeMatrix; ++i)
	{
		h=0;
		for (int j = 0; j < sizeMatrix; ++j)
			h += roots[j]*arr[i][j];
		if (max < fabs(Barr[i]-h))
			max = fabs(Barr[i]-h);
		cout << "x" << i+1 << " = " << roots[i] << endl;
		//printf("x[%i]=%.3f  ", i, roots[i]);
	}
	//cout << endl << "Max nevyazka: " << max << endl;
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

void printDet() {
	double det = 1;
	for (int i = 0; i < sizeMatrix; i++)
	{
		det *= arr[i][i];
	}
	cout << "Determminat = " << det << endl;
}


void methodPovorot() {
	
	double c;
	double s;
	double arrKJ, arrIJ, BarrK, BarrI;
	int countCalcSC = 0;

	//Прямий хід
	for (int k = 0; k < sizeMatrix - 1; ++k)
	{
		
		for (int i = k+1; i < sizeMatrix; ++i)
		{
			
			c = arr[k][k] / (sqrt(pow(arr[k][k],2)+pow(arr[i][k], 2)));
			s = arr[i][k] / (sqrt(pow(arr[k][k],2)+pow(arr[i][k], 2)));
			countCalcSC++;
			for (int j = 0; j < sizeMatrix; ++j)
			{
				arrKJ = arr[k][j];
				arrIJ = arr[i][j];

				arr[k][j] = c*arrKJ + s*arrIJ;
				arr[i][j] = -s*arrKJ + c*arrIJ;
			}
			BarrK = Barr[k];
			BarrI = Barr[i];
			Barr[k] = c*BarrK + s*BarrI;
			Barr[i] = -s*BarrK + c*BarrI;
		}

	}
	printDet();
	cout << "Count of calculations S and C = " << countCalcSC << endl;
//Зворотний хід
	double h;
	roots[sizeMatrix - 1] = Barr[sizeMatrix - 1] / arr[sizeMatrix - 1][sizeMatrix - 1];
	for (int l = sizeMatrix - 1; l >= 1; l--) {
		h = Barr[l - 1];
		for (int k = (l + 1); k <= sizeMatrix; k++)
			h = h - roots[k - 1] * arr[l - 1][k - 1];
		roots[l - 1] = h / arr[l - 1][l - 1];
	}
}

void main() {

	//SetConsoleCP(CP_UTF8);
	//SetConsoleOutputCP(CP_UTF8);

	readFromFile();
	
	printSystem();

	methodPovorot();

	printAnswer();

	cout << endl;
	system("pause"); //щоб вікно не закрилося
}
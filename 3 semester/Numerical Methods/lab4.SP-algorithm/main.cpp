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
double arr[ourLimit][ourLimit] = {};
double E[ourLimit][ourLimit] = {};
double startVector[ourLimit]={};
double eps = 0.0001;
int itr = 0;
double lambda = 0;

void printSystem() {
	cout << "System:\n";
	for (int i = 0; i < sizeMatrix; i++)
	{
		for (int j = 0; j < sizeMatrix; j++)
		{
			cout << arr[i][j] << " ";

		}
		cout << endl;
	}
	cout << endl;
}

void printE() {
	cout << "E:\n";
	for (int i = 0; i < sizeMatrix; i++)
	{
		for (int j = 0; j < sizeMatrix; j++)
		{
			cout << E[i][j] << " ";

		}
		cout << endl;
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
	}
	readfile.close();

	//Задаємо початковий вектор (за умовою)
	for (int i = 0; i < sizeMatrix; ++i)
	{
		startVector[i]=1;
	}

	//Створюємо одиничну матрицю
	for (int i = 0; i < sizeMatrix; i++)
		for (int j = 0; j < sizeMatrix; j++)
			if (i == j)
				E[i][j] = 1;
			else
				E[i][j] = 0;
}




void Metod_Gaussa()
{
	double r, res;
	for (int k = 0; k < sizeMatrix; k++)
	{
		//if (arr[k][k]==0)
		{
			int z = arr[k][k];
			int i = k;

			for (int j = k; j < sizeMatrix; j++)
				if (abs(arr[j][k]) > abs(z))
				{
					z = arr[j][k];
					i = j;
				}
			if (i > k)
				for (int j = k; j < sizeMatrix; j++)
				{
					swap(arr[i][j], arr[k][j]);

				}
			for (int j = 0; j < sizeMatrix; j++)
				swap(E[i][j], E[k][j]);
		}


		for (int i = k + 1; i < sizeMatrix; i++)
		{
			res = arr[i][k];
			for (int z = 0; z < sizeMatrix; z++)
			{
				arr[i][z] = arr[i][z] - arr[k][z] / arr[k][k] * res;
				E[i][z] = E[i][z] - E[k][z] / arr[k][k] * res;
			}

		}

		//cout << "k = " << k << endl;
		//printE();
		//printSystem();
	}




	double sum;
	for (int i = 0; i < sizeMatrix; i++)
	{
		for (int j = sizeMatrix - 1; j >= 0; j--)
		{
			sum = 0;
			for (int k = sizeMatrix - 1; k > j; k--)
			{
				sum += arr[j][k] * E[k][i];
			}

			E[j][i] = (E[j][i] - sum) / arr[j][j];
		}
	}


}
void Sp()
{
	double c = 0;
	double p = 0;
	double *x = new double[sizeMatrix];
	double *x1 = new double[sizeMatrix];
	double s = 0;
	double dob, t = 0, liamda1;
	for (int i = 0; i < sizeMatrix; ++i)
	{
		dob = startVector[i] * startVector[i];
		s = s + dob;
	}
	for (int i = 0; i < sizeMatrix; ++i)
	{
		x1[i] = startVector[i] / sqrt(s);
	}
	for (int i = 0; i < sizeMatrix; ++i)
	{
		x[i] = x1[i];
	}
	do
	{
		liamda1 = lambda;
		for (int i = 0; i < sizeMatrix; ++i)
		{
			x1[i] = x[i];
		}
		for (int i = 0; i < sizeMatrix; ++i)
		{
			startVector[i] = 0;
			for (int j = 0; j < sizeMatrix; ++j)
			{
				startVector[i] += E[i][j] * x1[j];
			}
		}
		s = 0;
		for (int i = 0; i < sizeMatrix; ++i)
		{
			dob = startVector[i] * startVector[i];
			s = s + dob;
		}
		t = 0;
		for (int i = 0; i < sizeMatrix; ++i)
		{
			dob = startVector[i] * x1[i];
			t = t + dob;
		}
		for (int i = 0; i < sizeMatrix; ++i)
		{
			x[i] = startVector[i] / sqrt(s);
		}
		lambda = s / t;
	} while (!(fabs(liamda1 - lambda) < eps));

	cout << "L_min=" << 1 / lambda << endl;
	for (int i = 0; i < sizeMatrix; ++i)
	{
		cout << "x[" << i + 1 << "]= " << x[i] << endl;
	}
}
void main()
{
	
	readFromFile();

	cout << "enter eps:\n"; cin >> eps;
	

	Metod_Gaussa();


	Sp();


	system("pause");
}
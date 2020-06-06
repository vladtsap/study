#include <iostream>
#include <omp.h>
#include <cmath>
#include <vector>

using namespace std;

const int N = 10000;

double omp_get_wtime(void);

long double A_matrix(int i, int j) {
    return sin(i+j);
}

long double B_vector(int i) {
    return cos(i);
}

int main() {
    double start_time;
    vector<long double> a[N];
    vector<long double> b(N);
    long double result[N];


    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            a[i].push_back(A_matrix(i, j));
        }
        b[i] = B_vector(i);
    }

    start_time = omp_get_wtime();

    int i, j;
#pragma omp parallel for private(i, j) shared(a, b, result) num_threads(16)
    for (i = 0; i < N; ++i) {
        for (j = 0; j < N; ++j) {
            result[i] += (a[i][j] * b[i]);
        }
    }
    cout << omp_get_wtime() - start_time << endl;
    return 1;
}

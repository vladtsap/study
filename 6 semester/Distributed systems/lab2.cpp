#include <iostream>
#include <omp.h>
#include <cmath>
#include <vector>

using namespace std;

const int N = 10000;
#define th 8

double omp_get_wtime(void);

vector<int> v[N];

vector<int> dynamic_solve() {
    vector<int> res(N);
    res.assign(N, 0);
    double start_time = omp_get_wtime();
#pragma omp parallel shared(res) num_threads(th)
    {
#pragma omp for schedule(dynamic, 6)
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (v[i][j] > 0)
                {
                    res[i] += v[i][j];
                }
            }
        }
    }
    cout << "Time for dynamic = " << omp_get_wtime() - start_time << ", chunk = 6" << ", n = " << N << endl;
    return res;
}


vector<int> guided_solve() {
    vector<int> res(N);
    res.assign(N, 0);
    double start_time = omp_get_wtime();

#pragma omp parallel shared(res) num_threads(th)
    {
#pragma omp for schedule(guided, 8)
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (v[i][j] > 0)
                {
                    res[i] += v[i][j];
                }
            }
        }
    }
    cout << "Time for guided = " << omp_get_wtime() - start_time << ", chunk = 8" << ", n = " << N << endl;
    return res;
}


int main() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            v[i].push_back(rand() % 1000);
        }
    }


    vector<int> res_dynamic = dynamic_solve();
    cout << endl;

    vector<int> res_guided = guided_solve();
    cout << endl;
    return 0;
}

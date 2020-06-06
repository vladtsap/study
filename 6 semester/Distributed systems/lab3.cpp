#include <stdio.h>
#include <iostream>
#include <math.h>
#include <omp.h>
#include <unistd.h>

using namespace std;

#define A 1.5
#define B 2.5

double F(double x) {
    return (sqrt((0.7 * x + 6.1) / (0.8 * x + 3))) * ((x * x) / (6.1 + x));
}

double calc(double a, double b, double dx) {
    double res = 0;
    for (double x = a; x < b; x += dx) {
        res += dx * (F(x) + F(x + dx)) / 2.0;
    }
    return res;
}

int main() {

    double t1, t2;
    omp_lock_t lock;
    omp_init_lock(&lock);

    for (int k: {1, 2, 4, 6, 8}) {
        omp_set_num_threads(k);
        for (double dx: {0.1, 0.001, 0.00002}) {

            double total = 0;
            t1 = omp_get_wtime();

#pragma omp parallel for shared(total, dx)
            for (int i = 0; i < k; i++) {
                double h = double(B - A) / double(k);
                double res = calc(A + double(i) * h, A + double(i + 1) * h, dx);

                while (!omp_test_lock(&lock)) {
                    // printf("The section is closed!\n");
                    usleep(10);
                }

                total += res;

                /*
                printf("The beginning of the closed section... %d\n", i);
                printf(" - partial: %f\n", res);
                if (omp_get_thread_num() == 0) printf("Author: Vladyslav Tsap, KN-310\n");
                 printf("The end of the closed section... %d\n", i);
                 */

                omp_unset_lock(&lock);
            }

            t2 = omp_get_wtime();
            printf("–––––––––––––––––––––––––––––––––––––––\n");
            printf(" - total:        %f\n", (total));
            printf(" - threads:      %d\n", (k));
            printf(" - dx:           %f\n", (dx));
            printf(" - elapsed time: %f seconds.\n", (t2 - t1));
            printf("–––––––––––––––––––––––––––––––––––––––\n");
        }
    }

    omp_destroy_lock(&lock);
}
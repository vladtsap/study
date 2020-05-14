#include <stdio.h>
#include <cs50.h>
#include <time.h>
int main(void) {
	float money;//reshta
	float random;//coffee price
	int fif = 0, twf = 0, ten = 0, fiv = 0, one = 0;
	srand(time(NULL));
	printf("Input your money: ");
	float input = GetFloat();
	money = input * 50;//perevid v kopiyky + polovyna
	do {
		random = rand();
	} while ((random<1) || (random >= money));
	random = random / 100;//perevid v cash
	printf("Coffee price: %f\b\b\b\b dollars\n", random);
	money = input - random;
	money = money * 100;//perevid v kopiyky
	do {
		if (money >= 50) {
			money = money - 50;
			fif++;
		}else if (money >= 25) {
			money = money - 25;
			twf++;
		}else if (money >= 10) {
			money = money - 10;
			ten++;
		}else if (money >= 5) {
			money = money - 5;
			fiv++;
		}else {
			money = money - 1;
			one++;
		}
	} while (money >= 1);
	if (fif != 0) {
		printf("50c x%d\n", fif);
	} if (twf != 0) {
		printf("25c x%d\n", twf);
	} if (ten != 0) {
		printf("10c x%d\n", ten);
	} if (fiv != 0) {
		printf("5c x%d\n", fiv);
	} if (one != 0) {
		printf("1c x%d\n", one);
	}
}
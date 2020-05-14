#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{   
    printf("Input your name & surname: ");
    string s = GetString();
    printf("Your initials are: %c.", toupper(s[0]));
    for (int i = 0, n=strlen(s); i<n; ++i) {
            if (s[i] == ' '){
            printf("%c.", toupper(s[i + 1]));
            }
    }
    printf("\nHello, ");
    for (int i = 0, n=strlen(s); i<n; ++i) {
        if(s[i] == ' '){
           break;
        }
           printf("%c", s[i]);
    }
    printf("!\nMy name is Vladyslav. I'm from CS-110\n");
}
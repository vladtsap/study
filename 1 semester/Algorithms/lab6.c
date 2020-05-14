#include <stdio.h>
#include <cs50.h>
#include <string.h>
int main(void){
    printf("Input encrypt code: ");
    int key = GetInt();
    while(key>26){
        key=key-26;
    }
    printf("Input your text:\n");
    string s=GetString();
    printf("Your encrypted text:\n");
    for (int i = 0, n=strlen(s); i < n; ++i)
    {
        if (s[i]>=65 && s[i] <= 90)
        {
            if ((s[i]+key)>=91)
            {
                printf("%c", (s[i]+key-26));
            }else{
                printf("%c", (s[i]+key));
            }
        }else if (s[i]>=97 && s[i] <= 122)
        {
            if ((s[i]+key)>=123)
            {
                printf("%c", (s[i]+key-26));
            }else{
                printf("%c", (s[i]+key));
            }
        }else{
            printf("%c", s[i]);
        }
    }
    printf("\n");
}

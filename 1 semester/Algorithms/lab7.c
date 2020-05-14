#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(void){
    int temp;
    printf("Input key:\n");
    string key = GetString();
    for (int i = 0; i < strlen(key); ++i)
    {
       key[i]=tolower(key[i]);
    }
    printf("Input your text:\n");
    string s=GetString();
    printf("Your encrypted text:\n");
    for (int i = 0,j=0; i < strlen(s); ++i)
    {
       if ((isalpha(s[i]))&&(s[i]>=65)&&s[i]<=90)
       {
           temp=s[i]+key[j]-97;
           while(temp>90){
            temp=temp-26;
           }
           printf("%c",temp);
           j++;
       }else if ((isalpha(s[i]))&&(s[i]>=97)&&s[i]<=122)
       {
             temp=s[i]+key[j]-97;
            while(temp>122){
                temp=temp-26;
            }
             printf("%c",temp);
             j++;
       }else{
        printf("%c",s[i]);
       }
       if (j==strlen(key))
       {
           j=0;
       }
    }
    printf("\n\n");

    printf("Input key:\n");
    string key2 = GetString();
    for (int i = 0; i < strlen(key2); ++i)
    {
       key2[i]=tolower(key2[i]);
    }
    printf("Input your encrypted text:\n");
    string s2=GetString();
    printf("Your text:\n");
    for (int i = 0,j=0; i < strlen(s2); ++i)
    {
       if ((isalpha(s2[i]))&&(s2[i]>=65)&&s2[i]<=90)
       {
           temp=s2[i]-key2[j]+97;
           while(temp<65){
            temp=temp+26;
           }
           printf("%c",temp);
           j++;
       }else if ((isalpha(s2[i]))&&(s2[i]>=97)&&s2[i]<=122)
       {
             temp=s2[i]-key2[j]+97;
            while(temp<97){
                temp=temp+26;
            }
             printf("%c",temp);
             j++;
       }else{
        printf("%c",s2[i]);
       }
       if (j==strlen(key2))
       {
           j=0;
       }
    }
    printf("\n");
}

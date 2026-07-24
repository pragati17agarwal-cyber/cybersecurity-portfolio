// A q a 1 z Q
#include<stdio.h>
int main()
{
    // name = get_string("What's your name: "); if had cs50
    /*char name[50];
    printf("What's your name? ");
    fgets(name, sizeof(name),stdin);
    printf("Hello, %s", name);*/
    char name[50];
    printf("What's your name?");
    scanf("%s",&name);
    printf("Hello, %s",name);
    return 0;
}
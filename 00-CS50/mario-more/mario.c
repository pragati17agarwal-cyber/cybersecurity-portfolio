// A q a 1 z Q
#include<stdio.h>
#include<string.h>
int main()
{
    /*int n;
    do
    {  
        printf("Choose number between 1 to 8: ");
        scanf("%d",&n);
    }while(n < 1 || n > 8);
    for(int i=1; i<=n; i++)
    {
       for(int j=n-i;j>=1;j--)
       {
        printf(" ");
       }
       for(int k=1; k<=i; k++)
       {
        printf("#"); // first attempt wrote printf("#  #")
       }
       printf("  ");
       for(int l=1; l<=i; l++)
       {
        printf("#");
       }
    printf("\n");
    }
return 0;*/
// OR
int n;
    do
    {  
        printf("Choose number between 1 to 8: ");
        scanf("%d",&n);
    }while(n < 1 || n > 8);
    char hashes[9] = {0}; //Declares an array of 9 characters, all initialized to 0 (i.e., '\0', the null terminator).
// Why 9 and not 8? Because if n = 8, the longest row needs 8 # characters plus 1 extra slot for the '\0' that ends the string. So size 9 covers the worst case safely.
    for (int i = 1; i <= n; i++) {
        memset(hashes, '#', i); //Fills the first i bytes of hashes with '#'.
        //Example: if i = 3, then hashes becomes {'#','#','#', 0, 0, 0, 0, 0, 0}
        hashes[i] = '\0'; //Places a null terminator right after the i-th hash.
        printf("%*s%s  %s\n", n - i, "", hashes, hashes); /*%*s — prints a string right-justified in a field of width given by the next argument. We pass n - i as that width and "" (empty string) as the string to print. An empty string right-justified in a field of width w is just w spaces. So this prints n - i leading spaces.
%s — prints hashes (the left triangle of #s).
   — two literal spaces, the gap between the two triangles.
%s — prints hashes again (the right triangle).
\n — newline to end the row.*/
    }
return 0;
}
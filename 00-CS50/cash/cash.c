// A q a 1 z Q !
#include<stdio.h>
int main()
{
    int change;
    int valid;
    do
    { 
    printf("Changes owed: ");
    valid = scanf("%d", &change);
    // if scanf failed to read an int, clear the bad input
        if (valid != 1) {
            while (getchar() != '\n');  // flush the rest of the bad line
            change = -1;                 // force the loop to repeat
        }
    }while(valid != 1 || change < 0);

    int cnt=0;
    while(change != 0)
    {
       /*if(change >= 25){
        change -= 25;
        cnt += 1;
       }
       else if(change >= 10 ){
        change -= 10;
        cnt += 1;
       }
       else if(change >= 5 ){
        change -= 5;
        cnt += 1;
       }
       else if(change >= 1 ){
        change -= 1;
        cnt += 1;
       }*/
      if (change >= 25)      { change -= 25; cnt++; }
        else if (change >= 10) { change -= 10; cnt++; }
        else if (change >= 5)  { change -= 5;  cnt++; }
        else                   { change -= 1;  cnt++; }
    }
    printf("Count: %d", cnt);
return 0;
}
#include <stdio.h>
int main()
{
  int year;
  printf("Enter the Year (YYYY) : ");
  scanf("%d",&year);
  if(year%4==0 && year%100!=0 || year%400==0)
    printf("\nThe Given year %d is a Leap Year", year);
  else
    printf("\nThe Given year %d is Not a Leap Year", year);

    return 0;
}


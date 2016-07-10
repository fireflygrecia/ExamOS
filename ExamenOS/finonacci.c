#include<stdio.h>


#———————————————————
# ——Fibonacci——
#———————————————————
#By Marisol_Martinez_Madrigal



 
int main()
{
   int n, n1 = 0, n2 = 1, nxt, i;
 
   printf(“Add the number of terms that wishes to visualize of the series of Fibonacci \n");
   scanf("%d",&n);
 
   printf(“n1 %d Fibonacci series are : \n",n);
 
   for (i = 0 ; i < n ; i++)
   {
      if (i <= 1)
         nxt = i;
      else
      {
         nxt = n1 + n2;
         n1 = n2;
         n2 = nxt;
      }
      printf("%d\n", next number);
   }
 
   return 0;
}

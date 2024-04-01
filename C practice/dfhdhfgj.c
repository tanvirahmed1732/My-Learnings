#include<stdio.h>
void BS(int ar[], int n)
{
    int temp;
    for(int i=0; i<=n-1; i++)
    {
        for(int j=0; j<=n-2; j++)
        {
            if(ar[j]> ar[j+1])
            {
                temp = ar[j];
                ar[j] = ar[j+1];
                ar[j+1] = temp;
            }
        }
    }
    for(int i=0; i<n; i++)
        printf("%d ", ar[i]);
}
void main()
{
    int ar[] = {2, 4, 1, 3, 9, 5};
    int n = sizeof (ar)/ sizeof (ar[0]);
    BS(ar, n);
}

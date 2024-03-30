#include<stdio.h>
void Delete(int ar[], int *n, int k)
{
    int j = k;
    while (j<*n)
    {
        ar[j] = ar[j+1];
        j = j+1;
    }
    *n= *n-1;
}
int main()
{
    int ar[] = {1,2,3,4,5,6,7};
    int n = sizeof (ar)/ sizeof (ar[0]);
    int k, item;
    printf("Enter which position(1-7) you want to delete:");
    scanf("%d", &k);
    item = ar[k];
    Delete (ar, &n, k);
    printf("The item %d is deleted.\n", item);
    for(int i=0; i<n; i++)
        printf("%d ", ar[i]);
}


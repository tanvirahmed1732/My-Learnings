#include<stdio.h>
#include<stdbool.h>
bool compare(int *ar1, int *ar2, int n)
{
    for(int i=0; i<n; i++)
    {
        if(*(ar1+i)!=*(ar2+i))
        {
            return false;
            break;
        }
    }
    return true;
}

int main()
{
    int n;
    printf("Enter the size: ");
    scanf("%d", &n);
    int ar1[n], ar2[n];
    printf("Enter the first array: ");
    for(int i=0; i<n; i++)
        scanf("%d", &ar1[i]);
    printf("Enter the second array: ");
    for(int i=0; i<n; i++)
        scanf("%d", &ar2[i]);
    //compare(ar1, ar2, n);
    if(compare(ar1, ar2, n)== true)
        printf("Both array are same. ");
    else printf("Arrays are not same.");
    return 0;
}

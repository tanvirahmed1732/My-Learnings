#include<stdio.h>
int BS (int ar[], int lb, int ub, int n, int item)
{
    int beg = lb, end = ub;
    int mid = (beg + end)/2;
    while (beg<=end && ar[mid] != item)
    {
        if(item<ar[mid])
            end = mid -1;
        else
            beg = mid +1;
        mid = (beg+end)/2;
    }
    if(item==ar[mid])
        return mid;
    else
        return -1;
}
int main()
{
    int ar[] = {1,2,3,4,5,6,7,8,9};
    int n = sizeof (ar)/ sizeof(ar[0]);
    int item;
    int lb = 0, ub = n-1;
    printf("Enter the item you want to search: ");
    scanf("%d", &item);
    int ind = BS(ar, lb, ub, n, item);
    if (ind == -1)
        printf("Item not found");
    else
        printf("Item index is %d", ind);
}

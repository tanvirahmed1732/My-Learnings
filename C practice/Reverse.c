// Take a two digits numbers from the user. Reverse it
#include<stdio.h>
int main()
{
    int n, a, b, rn;
    printf("Enter a two digits number:");
    scanf("%d", &n);
    a = n % 10;
    n = n / 10;

    b = n % 10;

    rn = a * 10 + b * 1;
    printf("Reverse of the number: %d", rn);
    return 0;
}

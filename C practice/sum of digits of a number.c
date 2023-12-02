#include<stdio.h>
int main()
{
    int n, a, b, c, sum;
    printf("Enter a 3 digit number:");
    scanf("%d", &n);
    a = n%10;
    n = n / 10;

    b = n%10;
    n = n / 10;

    c = n%10;

    sum = a + b + c;

    printf("Sum of the digits: %d", sum);
    return 0;
}

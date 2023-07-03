#include<stdio.h>
int main()
{
    float a, b, sum;
    printf("Enter two numbers:");
    scanf("%f %f", &a, &b);
    sum = a + b;
    printf("The sum of two numbers: %.2f", sum);
    return 0;
}

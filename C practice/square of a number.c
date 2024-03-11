#include<stdio.h>
int main()
{
    float a;
    printf("Enter a number:");
    scanf("%f", &a);
    a = a * a;
    printf("Square of number: %f", a);
    return 0;
}

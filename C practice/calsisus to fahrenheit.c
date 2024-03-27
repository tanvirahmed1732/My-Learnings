#include<stdio.h>
int ftoc(int c)
{
    int f;
    f = (c*9/5) +32;
    return f;
}
int main()
{
    int c;
    printf("Enter a celsius  value: ");
    scanf("%d", &c);
    printf("The fahrenheit value is: %d", ftoc(c));
}

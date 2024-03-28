#include<stdio.h>
struct student {
    int id;
    char arr[51];
    int mark;
}ar[100];
int indx=0;
void add(int x)
{
    printf("Enter student's id: ");
    scanf("%d", &ar[x].id);
    fflush(stdin);
    printf("Enter student's name: ");
    gets(ar[x].arr);
    printf("Enter mark: ");
    scanf("%d", &ar[x].mark);
}

void search ()
{
    int i;
    printf("Enter id: ");
    scanf("%d", &i);
    for(int j=0; j<indx; j++)
    {
        if(i==ar[j].id)
        {
            puts(ar[j].arr);
            printf("%d \n", ar[j].mark);
            break;
        }
    }
}

void deletee ()
{
    int i, k;
    printf("Enter id: ");
    scanf("%d", &i);
    for(int j=0; j<indx; j++)
    {
        if(i==ar[j].id)
        {
            k =j;
        }
    }
    for(int j=k; j<indx; j++)
        ar[j] = ar[j+1];
}
int main()
{
    int n;
    do
    {
        printf("Choose a option: \n"
                  "1: Add information.\n"
                  "2: Search.\n"
                  "3: Delete. \n");
        scanf("%d", &n);
        switch (n)
        {
        case 1:
            add(indx++);
            break;
        case 2:
            search();
            break;
        case 3:
            deletee ();
            break;
        }
    printf("If you want to continue press 1 otherwise press 0 ");
    scanf("%d", &n);
    }
    while (n == 1);
}

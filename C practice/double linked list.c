#include<stdio.h>

struct node
{
    int data;
    struct node *prev, *next;
}*head = NULL;

void insertatfirst (int v)
{
    struct node *newnode;
    newnode = malloc(sizeof (struct node));
    newnode->data = v;
    newnode->next = NULL;
    newnode->next = head;
    head = newnode;
}
void insertatend (int k)
{
    struct node *newnode;
    newnode = malloc (sizeof(struct node));
    newnode->data = k;
    newnode->next = NULL;
    if (head == NULL)
    {
        newnode->prev = NULL;
        head = newnode;
    }
    else
    {
    struct node *temp = head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newnode;
    newnode->prev = temp;
    }
}

void display ()
{
    struct node *temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
}
int main()
{
    int v1 = 5, v2 = 6, v3 = 7;
    insertatfirst(v1);
    insertatfirst(v2);
    insertatfirst(v3);
    int k1 = 11, k2 = 12, k3 = 13;
    insertatend(k1);
    insertatend(k2);
    insertatend(k3);
    display();
    return 0;
}


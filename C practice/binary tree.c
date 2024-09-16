#include<stdio.h>
#include<stdlib.h>

struct node {
    int k;
    struct node *left, *right;
};

struct node *newnode(int x)
{
    struct node *t = malloc(sizeof(struct node));
    t->k = x;
    t->left = t->right = NULL;
    return t;
}

void preorder(struct node *r)
{
    if (r != NULL)
    {
        preorder(r->left);
        printf("%d \n", r->k);
        preorder(r->right);
    }
}

struct node * insert(struct node *node, int k)
{
    if (node==NULL)
        return newnode(k);
    if (k<=node->k)
        node->left = insert(node->left, k);
    else if (k>node->k)
        node->right = insert(node->right, k);
    return node;
}

int main()
{
    struct node *root = NULL;
    root = insert (root, 100);
    insert(root, 110);
    insert(root, 100);
    insert(root, 90);
    insert(root, 120);
    insert(root, 80);
    preorder(root);
}

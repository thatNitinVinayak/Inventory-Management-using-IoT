#include <stdio.h>

void main()
{
    int n;
    printf ("Number of Inputs : "); scanf ("%d", &n);
    int num[n];
    printf ("Enter the Numbers : ");
    for (int i = 0; i < n; i++)
        scanf ("%d", &num[i]);
    
    for (int i = 0; i < n; i++)
    {
        int alphabet = 0;
        alphabet = num[i] + 64;
        printf ("%c", alphabet);
    }
}
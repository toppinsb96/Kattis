#include <cstdio>
long int p[200005];


long int findNodes(long int a)
{
    while(a != p[a]) a = p[a];
    return a;
}

void unionNodes(long int a, long int b)
{
    a = findNodes(a);
    b = findNodes(b);
    if (a >= b) p[a] = b;
    if (a < b)  p[b] = a;
}

int main()
{
    
    return 0;
}

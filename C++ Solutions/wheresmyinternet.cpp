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
    long int N, M, a, b;
    bool all = true;


    scanf("%ld %ld", &N, &M);
    // fill p
    for (long int i = 1; i < N + 1; i++) p[i] = i;
    long int startHome = findNodes(1);
     
    for(long int i = 0; i < M; i++)
    {
        scanf("%ld %ld", &a, &b);
        unionNodes(a, b);
    }
    for(long int i = 2; i <= N; i++)
    {
        if(findNodes(i) != startHome)
        {
            all = false;
            printf("%ld\n", i);
        }
    }

    if(all) printf("Connected\n");
    return 0;
}

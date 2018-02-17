#include <cstdio>

long long tree[5000005];

void update(int i, long long value, int N)
{
    while(i <= N)
    {
        tree[i] += value;
        i += i & -i;
    }
}
long long sum(int i)
{
     long long sum = 0;

     while (i > 0)
     {
        sum += tree[i];
        i -= i & (-i);
     }
     return sum;
}


int main()
{

    long long value;
    int N, Q, i;
    char c;
    scanf("%d%d", &N, &Q);

    for(int j = 0; j < Q; j++)
    {
        scanf(" %c ", &c);


        if (c == '+')
        {
            scanf("%d%lld", &i, &value);
            update(i + 1, value, N);
        }

        if (c == '?')
        {
            scanf("%d", &i);
            printf("%lld\n", sum(i));
        }
    }

    return 0;
}

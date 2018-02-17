#include <cstdio>
#include <cstring>


// A maximum size to expand the fenwick tree and loops to max size available.
const long long maxSize = 100005;

long long tree[2 * maxSize];
long long location[maxSize];


void update(int index, long long value)
{
    int i = index;

    while(i < 2 * maxSize)
    {
      tree[i] += value;
      i += i & -i;
    }
}

long long sum(int index)
{
     long long sum = 0;
     int i = index;

     while (i > 0)
     {
        sum += tree[i];
        i -= i & (-i);
     }
     return sum;
}

int main() {
    int Q;
    int m, r;
    int key, index;

    std::scanf("%d", &Q);

    for(int j = 0; j < Q; j++)
    {
        memset(tree, 0, sizeof(tree));
        std::scanf("%d %d", &m, &r);

        for (int i = 1; i <= m; i++)
        {
            update(i, 1);
            location[i] = m - i + 1;
        }

        for (int i = m + 1; i <= m + r; i++)
        {
            std::scanf("%d", &key);

            index = location[key];

            std::printf("%lld ", m - sum(index));

            update(index, -1);
            update(i, 1);


            location[key] = i;
        }
        std::puts("");
    }

    return 0;
}

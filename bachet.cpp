#include <stdio.h>
#include <string.h>
int main()
{
    while(true)
    {
        long int n, m;
        long int move[100];
        int stan[1000000];


        stan[0] = 0;
        scanf("%ld %ld", &n, &m);
        if(feof(stdin))
            return 0;

        for(long int i = 0; i < m; i++)
            scanf("%ld", &move[i]);


        for(long int i = 1; i < n+1; i++)
        {
            stan[i] = 0;
            for(long int j = 0; j < m; j++)
            {
                if(i-move[j] < 0)
                    continue;
                if(!stan[i-move[j]])
                {
                    stan[i] = 1;
                    break;
                }
            }
        }



        if(stan[n])
            printf("Stan wins\n");
        else
            printf("Ollie wins\n");
    }
}

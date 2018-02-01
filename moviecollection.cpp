class FenwickTree
{
private: vi ft;
    int rsq(int b)
    {
        int sum = 0; for (; b; b -= LSOne(b)) sum += ft[b];
        return sum;
    }

    int rsq(int a, int b)
    {
        return rsq(b) - (a == 1 ? 0 : rsq(a - 1));
    }

    void adjust(int k, int v)
    {
        for (; k < (int)ft.size(); k += LSOne(k)) ft[k] += v;
    }


    int main()
    {
        int f[] = { 2,4,5,5,6,6,6,7,7,8,9 };
        printf("%d\n", ft.rsq(1, 1)); printf("%d\n", ft.rsq(1, 2)); printf("%d\n", ft.rsq(1, 6)); printf("%d\n", ft.rsq(1, 10)); printf("%d\n", ft.rsq(3, 6)); ft.adjust(5, 2); printf("%d\n", ft.rsq(1, 10));
    }
}

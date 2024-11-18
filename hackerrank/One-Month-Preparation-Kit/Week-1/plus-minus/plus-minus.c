#include <stdio.h>

void plusMinus(int arr_count, int *arr)
{
    int i = 0;
    float positive = 0;
    float minus = 0;
    float zero = 0;
    for (int i = 0; i < arr_count; i++)
    {
        if (arr[i] > 0)
        {
            positive++;
        }
        else if (arr[i] < 0)
        {
            minus++;
        }
        else
        {
            zero++;
        }
    }

    printf("%.6f\n", (positive / arr_count));
    printf("%.6f\n", (minus / arr_count));
    printf("%.6f\n", (zero / arr_count));
}

int main()
{
    int arr[] = {-4, 3, -9, 0, 4, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    plusMinus(n, arr);

    return 0;
}

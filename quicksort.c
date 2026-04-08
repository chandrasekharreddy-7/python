#include <stdio.h>
 void swap(int *a, int *b)
 {
    int temp = *a;
    *a = *b;
    *b = temp;
 }

 int partition(int arr[],int low, int high)
 {
    int pivot = arr[high];
    int i = low - 1;
    for(int j = low;j < high;j++)
    {
        if(arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
 }

 void quicksort(int arr[], int low, int high)
 {
    if(low < high)
    {
        int p = partition(arr, low, high);
        quicksort(arr, low, p - 1);
        quicksort(arr, p + 1, high);
    }
 }

 int main()
 {
    int arr[50], n;
    printf("enter the size of array :");
    scanf("%d",&n);
    for(int j = 0;j < n;j++)
    {
        printf("enter element %d :", j+1);
        scanf("%d",&arr[j]);
    }
    quicksort(arr, 0, n - 1);
    printf("sorted array :\n");
    for (int i = 0;i < n;i++)
    {
        printf("%d\t", arr[i]);
    }
    return 0;
 }
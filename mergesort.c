#include <stdio.h>

void merge(int a[], int left, int mid, int right) {
    int i = left;
    int j = mid + 1;
    int k = left;
    int temp[100];
    while(i <= mid && j <= right) {
        if(a[i] <= a[j]) {
            temp[k] = a[i];
            i++;
        } else {
            temp[k] = a[j];
            j++;
        }
        k++;
    }
    while(i <= mid) {
        temp[k] = a[i];
        i++;
        k++;
    }
    while(j <= right) {
        temp[k] = a[j];
        j++;
        k++;
    }
    for(i = left; i <= right; i++) {
        a[i] = temp[i];
    }
}

void mergesort(int a[], int left, int right) {
    if(left < right) {
        int mid = left + (right - left) / 2; 
        mergesort(a, left, mid);
        mergesort(a, mid + 1, right);
        merge(a, left, mid, right); 
    }
}

int main() {
    int arr[50], n;
    printf("enter the size of array :");
    if (scanf("%d", &n) != 1 || n > 50) return 1;
    for(int j = 0; j < n; j++) {
        printf("enter element %d :", j + 1);
        scanf("%d", &arr[j]);
    }
    mergesort(arr, 0, n - 1);
    printf("sorted array :\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t", arr[i]);
    }
    return 0;
}
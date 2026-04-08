#include <stdio.h>
#include <stdbool.h>
#include "array_utils.h"

void bubble_sort(int arr[], int n) {
    bool swapped;

    do {
        swapped = false;

        for(int i = 0; i < n - 1; ++i) {
            int j = i + 1;
            if(arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                swapped = true;
            }
        }
    } while(swapped);
}

int main() {
    int data[] = {64, 25, 12, 22, 11};
    int n = sizeof(data) / sizeof(data[0]);

    printf("Original array: ");
    print_array(data, n);

    bubble_sort(data, n);

    printf("Sorted array: ");
    print_array(data, n);
    return 0;
}
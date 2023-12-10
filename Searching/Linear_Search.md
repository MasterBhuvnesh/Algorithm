 # Linear Search
 
**Linear search** is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found. It is the simplest searching algorithm.

## How Linear Search Works?
The following steps are followed to search for an element ``k = 1`` in the list below.
<img src="https://github.com/MasterBhuvnesh/Algorithm/assets/99537126/131835a0-abbd-4e3b-9a5d-82edde1fa6d2" alt="Linear Search Initial Array" width="400"/>

1. Start from the first element, compare``k`` with each element ``x``.
<img width="400" alt="linear-search-comparisons" src="https://github.com/MasterBhuvnesh/Algorithm/assets/99537126/c79a8c8d-f668-4198-b1f1-be9513d63aaa">

2. If ``x == k``, return the index.
<img width="377" alt="linear-search-found" src="https://github.com/MasterBhuvnesh/Algorithm/assets/99537126/3d0c654e-c97a-4fc4-b628-323a6e9561ec">

3. Else, return ``not found``.

#  Linear Search Algorithm

```bash
LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index
```
# Linear Search Complexities

- Time Complexity: ``O(n)``
- Space Complexity: ``O(1)``

# Linear Search Code 
```bash
// Linear Search in C

#include <stdio.h>

int search(int array[], int n, int x) {
  
  // Going through array sequencially
  for (int i = 0; i < n; i++)
    if (array[i] == x)
      return i;
  return -1;
}

int main() {
  int array[] = {2, 4, 0, 1, 9};
  int x = 1;
  int n = sizeof(array) / sizeof(array[0]);

  int result = search(array, n, x);

  (result == -1) ? printf("Element not found") : printf("Element found at index: %d", result);
}
```

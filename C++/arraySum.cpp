#include <iostream>
using namespace std;

int main() {
  // initialise array
  int arr[] =  {10, 2, 8, 6, 1, 0, 7, 25, 26, 5, 90};
  int size = 11;

  // initialise sum to zero
  int sum = 0;

  // for loop runs from 0 to size - 1
  for(int i = 0; i < size; i++)
  {
    sum = sum + arr[i];
  }

  cout << "The sum of the elements in the array: " << sum;
}

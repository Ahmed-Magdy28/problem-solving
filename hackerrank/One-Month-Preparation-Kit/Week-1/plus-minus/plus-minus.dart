void main() {
  List<int> arr = [-4, 3, -9, 0, 4, 1];
  plusMinus(arr);
}

void plusMinus(List<int> arr) {
  int positive = 0;
  int minus = 0;
  int zero = 0;

  for (int i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      positive++;
    } else if (arr[i] < 0) {
      minus++;
    } else {
      zero++;
    }
  }
  print((positive / arr.length).toDouble());
  print((minus / arr.length).toDouble());
  print((zero / arr.length).toDouble());
}

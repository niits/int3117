import unittest
import random


def binarySearch(array, index,  x):
    if len(array) > 1000 or len(array) < 1 or index < 0 or index > len(array) - 1:
        return -1
    else:
        l = index
        r = len(array) -1
        while l <= r:
            mid = int(l + (r - l)/2)

            if array[mid] == x:
                return mid
            elif array[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

    return -1


class BinarySearchTest(unittest.TestCase):
    def test_case_01(self):
        # Kiểm thử với mảng rỗng
        self.assertEqual(binarySearch([], 0, 1), -1)

    def test_case_02(self):
        # Kiểm thử với mảng có 1 phần tử
        self.assertEqual(binarySearch([1], 0, 1), 0)

    def test_case_03(self):
        # Kiểm thử với mảng có 10 phần tử
        self.assertEqual(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 5), 4)

    def test_case_04(self):
        # Kiểm thử với mảng có 999 phần tử
        arr = [random.random() for _ in range(999)]
        arr.sort()
        search_value = arr[30]
        self.assertEqual(binarySearch(arr, 0, search_value), 30)

    def test_case_05(self):
        # Kiểm thử với mảng có 1000 phần tử
        arr = [random.random() for _ in range(1000)]
        arr.sort()
        search_value = arr[30]
        self.assertEqual(binarySearch(arr, 0, search_value), 30)
    
    def test_case_06(self):
        # Kiểm thử với mảng có 1000 phần tử
        arr = [random.random() for _ in range(1001)]
        arr.sort()
        search_value = arr[30]
        self.assertEqual(binarySearch(arr, 0, search_value), -1)

    def test_case_07(self):
        # Kiểm thử với vị trí bắt đầu là -1
            self.assertEqual(binarySearch([1, 2], -1, 1), -1)

    def test_case_08(self):
        # Kiểm thử với vị trí bắt đầu là 0
            self.assertEqual(binarySearch([1, 2], 0, 1), 0)
    
    def test_case_09(self):
        # Kiểm thử với vị trí bắt đầu là bất kì trong khoảng
            self.assertEqual(binarySearch([1, 2, 3, 4, 5], 3, 1), -1)
    
    def test_case_10(self):
        # Kiểm thử với vị trí bắt đầu là áp chót
            self.assertEqual(binarySearch([1, 2, 3, 4, 5, 6], 4, 6), 5)

    def test_case_11(self):
        # Kiểm thử với vị trí bắt đầu là vị trí cuối
            self.assertEqual(binarySearch([1, 2, 3, 4, 5, 6], 5, 6), 5)
    
    def test_case_12(self):
        # Kiểm thử với vị trí bắt đầu là vị trí ngay sau vị trí cuối
            self.assertEqual(binarySearch([1, 2, 3, 4, 5, 6], 6, 6), -1)
    
    def test_case_13(self):
        # Kiểm thử tìm kiếm giá trị có trong mảng
            self.assertEqual(binarySearch([1, 2, 3, 4, 5, 6], 0, 6), 5)

    def test_case_14(self):
        # Kiểm thử tìm kiếm giá trị không có trong mảng
            self.assertEqual(binarySearch([1, 2, 3, 4, 5, 6], 0, 60), -1)


if __name__ == "__main__":
    unittest.main()

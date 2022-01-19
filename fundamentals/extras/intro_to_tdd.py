import unittest
# reverseList - Write a function that reverses the values in the list (without creating a temporary array).
def reverseList(li):
    for idx in range(int(len(li)/2)):
        li[idx], li[len(li)-idx-1] = li[len(li)-idx-1], li[idx]
    return li


class reverseListTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])

    def testTwo(self):
        self.assertIs(type(reverseList([1,3,5])), list)

    def testThree(self):
        self.assertEqual(reverseList([]),[])

    def testFour(self):
        self.assertEqual(reverseList([1,5,34,2,25231]), [25231,2,34,5,1])

    def setUp(self):
        print("setting up tests for reverse list")

    def tearDown(self):
        print("tearing down for reverse list")

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).
def isPalindrome(test_string):
    for idx in range(int(len(test_string)/2)):
        if test_string[idx] != test_string[len(test_string)-idx-1]:
            return False
    return True

class isPalindromeTest(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome("racecar"))
    def testTwo(self):
        self.assertFalse(isPalindrome("rabcr"))
    def testThree(self):
        self.assertTrue(isPalindrome("tacocat"))
    def testFour(self):
        self.assertFalse(isPalindrome("Tacocat"))
    def testFive(self):
        self.assertTrue(isPalindrome("123454321"))
    def testSix(self):
        self.assertTrue(isPalindrome("a"))
    def testSeven(self):
        self.assertTrue(isPalindrome(""))
    def setUp(self):
        print("setting up is palindrome tests")
    def tearDown(self):
        print("tearing down is palindrome tests")


# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.
def coins(cents_value):
    coins_array = [0,0,0,0]
    coins_values = [25,10,5,1]
    for idx in range(4):
        coins_array[idx] = int(cents_value/coins_values[idx])
        cents_value = cents_value % coins_values[idx]
    return coins_array

class coinsTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    def testTwo(self):
        self.assertEqual(coins(187), [7,1,0,2])
    def testThree(self):
        self.assertEqual(coins(25), [1,0,0,0])
    def testFour(self):
        self.assertEqual(coins(10), [0,1,0,0])
    def testFive(self):
        self.assertEqual(coins(5), [0,0,1,0])
    def testSix(self):
        self.assertEqual(coins(1), [0,0,0,1])
    def setUp(self):
        print("setting up for coins test")
    def tearDown(self):
        print("tearing down coins test")

if __name__ == "__main__":
    unittest.main()
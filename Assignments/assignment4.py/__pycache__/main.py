#main
# main.py
import my_program as mp

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Armstrong Number")
        print("2. Swap Two Numbers")
        print("3. Count Vowels in String")
        print("4. GCD of Two Numbers")
        print("5. Reverse a Number")
        print("6. Sum of Digits")
        print("7. Count Words in a Sentence")
        print("8. Convert String to Title Case")
        print("9. Fibonacci Series")
        print("10. Prime Number Check")
        print("11. Factorial of a Number")
        print("12. Palindrome String Check")
        print("13. Convert Decimal to Binary")
        print("14. Largest of Three Numbers")
        print("15. Custom Sort")
        print("0. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice == "1":
            mp.armstrong_number()
        elif choice == "2":
            mp.swap_numbers()
        elif choice == "3":
            mp.count_vowels()
        elif choice == "4":
            mp.gcd_two_numbers()
        elif choice == "5":
            mp.reverse_number()
        elif choice == "6":
            mp.sum_of_digits()
        elif choice == "7":
            mp.count_words()
        elif choice == "8":
            mp.string_title_case()
        elif choice == "9":
            mp.fibonacci_series()
        elif choice == "10":
            mp.prime_check()
        elif choice == "11":
            mp.factorial_number()
        elif choice == "12":
            mp.palindrome_string()
        elif choice == "13":
            mp.decimal_to_binary()
        elif choice == "14":
            mp.largest_of_three()
        elif choice == "15":
            mp.custom_sort()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
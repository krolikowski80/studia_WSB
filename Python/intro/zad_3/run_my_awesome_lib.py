from my_awesome_lib import text_processing, math_tools, data_utils

# Test funkcji z text_processing
text = "Ala ma kota"
print("Liczba słów:", text_processing.count_words(text))
print("Odwrócony tekst:", text_processing.reverse_string(text))
print("Czy palindrom:", text_processing.is_palindrome("kajak"))

# Test funkcji z math_tools
print("Silnia 5:", math_tools.factorial(5))
print("Średnia:", math_tools.mean([1, 2, 3, 4, 5]))
print("Czy 7 jest pierwsza:", math_tools.is_prime(7))

# Test funkcji z data_utils
data = [["1", "2"], ["3", "4"], ["5", "6"]]
filtered = data_utils.filter_data(data, lambda row: int(row[0]) > 2)
print("Przefiltrowane dane:", filtered)
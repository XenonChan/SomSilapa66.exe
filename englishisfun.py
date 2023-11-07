def number_to_word(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= number < 20:
        return ones[number]
    elif 20 <= number < 100:
        return tens[number // 10] + " " + ones[number % 10]
    elif 100 <= number < 1000:
        return ones[number // 100] + " hundred " + number_to_word(number % 100)
    elif 1000 <= number < 1000000:
        return number_to_word(number // 1000) + " thounsand " + number_to_word(number%1000)
    elif 1000000 <= number < 1000000000:
        return number_to_word(number//1000000) + " million " + number_to_word(number%1000000)
    
number = int(input())
result = number_to_word(number)
print(result)
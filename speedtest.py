# source: Google Gemini "Script that evaluates python speed"

import time

def speed_test(iterations):
	start_time = time.time()
	result = 0
	for _ in range(iterations):
		result += (_ * _)
		result /= 2
		result *= 1.00001
	end_time = time.time()
	return end_time - start_time

def complex_calculation(n):
	my_list = [i for i in range(n)]
	result = 0
	for x in my_list:
		result += x*x
	return result

def string_test(n):
	my_string = ""
	for i in range(n):
		my_string += str(i)
	return len(my_string)

if __name__ == "__main__":
	# speed test
	iterations = 1000000
	execution_time = speed_test(iterations)
	print(f"Iterations: {iterations}")
	print(f"Execution time: {execution_time:.4f} seconds")

	# complex test
	start_complex = time.time()
	complex_calculation(5000)
	end_complex = time.time()
	print(f"Complex calculation time: {end_complex - start_complex:.4f}")

	# string test
	start_string = time.time()
	string_test(10000)
	end_string = time.time()
	print(f"String test time: {end_string - start_string:.4f} seconds")

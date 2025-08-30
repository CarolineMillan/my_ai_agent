from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file


def main():
    print("in main test function")
    
    # GET_FILES_INFO()
    # print("TESTING GET_FILES_INFO()...")
    
    # CALCULATOR TEST 1
    #expected_str1 = "- main.py: file_size=576 bytes, is_dir=False\n- tests.py: file_size=1343 bytes, is_dir=False\n- pkg: file_size=128 bytes, is_dir=True"
    #actual_str1 = get_files_info("calculator", ".")
    ##str = f"Result for current directory:\n"
    ##if (actual_str1 == expected_str1):
    #    print("Test 1: PASSED")
    #    print(f"{str + actual_str1}")
    #else:
    #    print(f"Test 1: FAILED\nActual output: {str + actual_str1}\nExpected output: {str + expected_str1}")
#
#    # CALCULATOR /PKG TEST
#    expected_str2 = "- calculator.py: file_size=1738 bytes, is_dir=False\n- render.py: file_size=767 bytes, is_dir=False"
#    actual_str2 = get_files_info("calculator", "pkg")
#    str = f"Result for pkg directory:\n"
#    if (actual_str2 == expected_str2):
#        print("Test 2: PASSED")
#        print(f"{str + actual_str2}")
#    else:
#        print(f"Test 2: FAILED\nActual output: {str + actual_str2}\nExpected output: {str + expected_str2}")
#
#    # CALCULATOR /BIN TEST
#    expected_str3 = "Error: Cannot list \"/bin\" as it is outside the permitted working directory"
#    actual_str3 = get_files_info("calculator", "/bin")
#    str = f"Result for /bin directory:\n"
#    if (actual_str3 == expected_str3):
#        print("Test 3: PASSED")
#        print(f"{str + actual_str3}")
#    else:
#        print(f"Test 3: FAILED\nActual output: {str + actual_str3}\nExpected output: {str + expected_str3}")
#
#   
#    # CALCULATOR ../ TEST
#    expected_str4 = "Error: Cannot list \"../\" as it is outside the permitted working directory"
#    actual_str4 = get_files_info("calculator", "../")
#    str = f"Result for ../ directory:\n"
#    if (actual_str4 == expected_str4):
#        print("Test 4: PASSED")
#        print(f"{str + actual_str4}")
#    else:
#        print(f"Test 4: FAILED\nActual output: {str + actual_str4}\nExpected output: {str + expected_str4}")

#    # GET_FILES_CONTENT()
#    print("TESTING GET_FILE_CONTENT()...")
#    
#    suffix = "...File \"{filepath}\" truncated at 10000 characters"
#    
#    # TEST 1
#    
#    actual_str1 = get_file_content("calculator", "lorem.txt")
#    if (actual_str1.endswith(suffix)):
#        print("TEST 1: PASSED")
#    else:
#        print("TEST 1: FAILED")
#    
#    # TEST 2 
#    actual_str2 = get_file_content("calculator", "main.py")
#    print(actual_str2)
#    
#    # TEST 3
#    actual_str3 = get_file_content("calculator", "pkg/calculator.py")
#    print(actual_str3)
#    
#    # TEST 4
#    actual_str4 = get_file_content("calculator", "/bin/cat") # this should return an error string
#    print(actual_str4)
#    
#    # test 5
#    actual_str5 = get_file_content("calculator", "pkg/does_not_exist.py") # this should return an error string
#    print(actual_str5)

    # testing write_file()
    
    # test 1
#    
#    test1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#    test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#    test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#    
#    print(test1)
#    print(test2)
#    print(test3)

    # TESTING RUN_PYTHON
    
    test1 = run_python_file("calculator", "main.py")
    test2 = run_python_file("calculator", "main.py", ["3 + 5"])
    test3 = run_python_file("calculator", "tests.py")
    test4 = run_python_file("calculator", "../main.py")
    test5 = run_python_file("calculator", "nonexistent.py")
    
    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print(test5)
    
    
   
    
    
if __name__ == "__main__":
    main()

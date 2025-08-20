from functions.get_files_info import get_files_info


def main():
    print("in main() tests.py")
    
    # CALCULATOR TEST 1
    expected_str1 = "Result for current directory:\n- main.py: file_size=576 bytes, is_dir=False\n- tests.py: file_size=1343 bytes, is_dir=False\n- pkg: file_size=92 bytes, is_dir=True"
    actual_str1 = get_files_info("calculator", ".")
    if (actual_str1 == expected_str1):
        print("Test 1: PASSED")
    else:
        print(f"Test 1: FAILED\nActual output: {actual_str1}\nExpected output: {expected_str1}")

    # CALCULATOR /PKG TEST
    expected_str2 = "Result for 'pkg' directory:\n- calculator.py: file_size=1739 bytes, is_dir=False\n- render.py: file_size=768 bytes, is_dir=False"
    actual_str2 = get_files_info("calculator", "pkg")
    if (actual_str2 == expected_str2):
        print("Test 2: PASSED")
    else:
        print(f"Test 2: FAILED\nActual output: {actual_str2}\nExpected output: {expected_str2}")


    
    # CALCULATOR /BIN TEST
    
    # CALCULATOR ../ TEST
    
    
    
if __name__ == "__main__":
    main()

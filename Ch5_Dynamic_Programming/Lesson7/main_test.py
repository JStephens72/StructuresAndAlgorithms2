from main import fibonacci

run_cases: list[tuple[int, int]] = [
    (10, 34),
    (20, 4181),
    (50, 7778742049),
]

submit_cases: list[tuple[int, int]] = run_cases + [(75, 1304969544928657)]


def test(n: int, expected: int) -> bool:
    print("---------------------------------")
    print(f"Running `fibonacci` from 0 to {n}")
    print(f"Expecting: {expected}")
    try:
        result = None
        for i in range(n):
            result = fibonacci(i)
        print(f"Actual: {result}\n")
        if result != expected:
            print("Fail")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

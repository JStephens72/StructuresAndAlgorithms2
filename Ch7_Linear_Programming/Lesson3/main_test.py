from main import calculate_profit

TestCase = tuple[int, int, int]

run_cases: list[TestCase] = [
    (100, 200, 700),
    (250, 200, -1),
    (150, 150, 900),
    (50, 250, -1),
]

submit_cases: list[TestCase] = run_cases + [
    (250, 50, 1300),
    (300, 0, -1),
    (250, 25, 1275),
]


def test(num_cakes: int, num_cookies: int, expected: int) -> bool:
    print("---------------------------------")
    print(f"Cakes: {num_cakes}")
    print(f"Cookies: {num_cookies}\n")

    try:
        profit = calculate_profit(num_cakes, num_cookies)

        if expected == -1:
            print("Expected: -1 (constraint violated)")
        else:
            print(f"Expected profit: {expected}")

        if profit == -1:
            print("Actual: -1 (constraint violated)")
        else:
            print(f"Actual profit: {profit}")

        print()

        if profit != expected:
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


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

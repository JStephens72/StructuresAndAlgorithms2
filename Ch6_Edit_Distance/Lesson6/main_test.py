from main import edit_distance

TestCase = tuple[str, str, int]

run_cases: list[TestCase] = [
    ("burger king", "burger king", 0),
    ("mcdonalds", "mc donalds", 1),
    ("docter office", "doctors office", 2),
]

submit_cases: list[TestCase] = run_cases + [
    ("park", "parc", 1),
    ("moms house", "moms hows", 2),
    ("abracadabra", "abracad", 4),
    ("abracadabra", "konkadonk", 9),
    ("Mount Kilimanjaro in Tanzania", "Everest the mountain in the himalayas", 26),
]


def test(a: str, b: str, expected: int) -> bool:
    print("---------------------------------")
    print(f"Calculating edit distance between: '{a}' and '{b}'")
    try:
        print(f"Expecting: {expected}")
        result = edit_distance(a, b)
        print(f"Actual: {result}\n")
        if result == expected:
            print("Pass")
            return True
        print("Fail")
        return False
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

from main import Tile

TestCase = tuple[tuple[int, int], int]

run_cases: list[TestCase] = [
    ((2, 2), 24),
    ((5, 2), 21),
]

submit_cases: list[TestCase] = run_cases + [
    ((2, 7), 7),
    ((8, 8), 17),
    ((50, 50), 23),
]


def test(tile_inputs: tuple[int, int], expected_output: int) -> bool:
    print("---------------------------------")
    try:
        tile = Tile(*tile_inputs)
        print(f"- Tile Coordinates: {tile}")
        print(f"Expected Cost: {expected_output}")
        result = tile.cost()
        print(f"Actual Cost: {result}\n")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main():
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

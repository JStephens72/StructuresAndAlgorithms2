from main import MinHeap

TestCase = tuple[list[tuple[int, str]], list[tuple[int, str]]]

run_cases: list[TestCase] = [
    (
        [(7, "East Pass"), (5, "Kingsroad"), (1, "Skirling Pass"), (3, "The Hook")],
        [(1, "Skirling Pass"), (3, "The Hook"), (5, "Kingsroad"), (7, "East Pass")],
    ),
    (
        [
            (5, "Street of Steel"),
            (3, "Kingsroad"),
            (7, "Skirling Pass"),
            (1, "The Hook"),
        ],
        [
            (1, "The Hook"),
            (3, "Kingsroad"),
            (5, "Street of Steel"),
            (7, "Skirling Pass"),
        ],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        [
            (10, "Goldroad"),
            (3, "Kingsroad"),
            (8, "Godsway"),
            (6, "East Pass"),
            (2, "Boneway"),
            (1, "River Row"),
            (7, "The Hook"),
            (5, "Street of Steel"),
        ],
        [
            (1, "River Row"),
            (2, "Boneway"),
            (3, "Kingsroad"),
            (5, "Street of Steel"),
            (6, "East Pass"),
            (7, "The Hook"),
            (8, "Godsway"),
            (10, "Goldroad"),
        ],
    ),
]


def test(
    push_inputs: list[tuple[int, str]], expected_pops: list[tuple[int, str]]
) -> bool:
    print("---------------------------------")
    try:
        min_heap = MinHeap()
        for priority, value in push_inputs:
            print(f'- Pushing "{value}" with priority {priority}')
            min_heap.push(priority, value)

        print("\n")
        for expected_output in expected_pops:
            print("- Popping Heap:")
            print(f"Expecting: {expected_output}")
            result = min_heap.pop()
            print(f"Actual: {result}\n")
            if result != expected_output:
                print("Fail")
                return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
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

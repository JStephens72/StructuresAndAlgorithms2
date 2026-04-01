from main import bellman_ford

TestCase = tuple[dict[str, dict[str, int]], tuple[list[str | int], ...]]

run_cases: list[TestCase] = [
    (
        {
            "Thaylen City": {"Kholinar": 5, "Shinovar": -2},
            "Kholinar": {"Urithiru": 1},
            "Urithiru": {"Jah Keved": -1, "Shadesmar": 3},
            "Shinovar": {"Kholinar": 2, "Urithiru": 4, "Jah Keved": 3},
            "Jah Keved": {"Shadesmar": 1},
            "Shadesmar": {},
        },
        (
            ["Thaylen City", "Shadesmar", 1],
            ["Kholinar", "Shadesmar", 1],
            ["Urithiru", "Shadesmar", 0],
            ["Shadesmar", "Shadesmar", 0],
        ),
    ),
    (
        {
            "Kholinar": {"Urithiru": -1},
            "Urithiru": {"Shinovar": -2},
            "Shinovar": {"Kholinar": -1, "Jah Keved": 3},
            "Jah Keved": {},
        },
        (["Kholinar", "Jah Keved", "negative cycle detected!"],),
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        {
            "Shadesmar": {"Kholinar": 5, "Shinovar": -2},
            "Kholinar": {"Urithiru": 1},
            "Urithiru": {
                "Jah Keved": -1,
            },
            "Shinovar": {"Kholinar": 2, "Urithiru": 4, "Jah Keved": 8},
            "Jah Keved": {"Shinovar": 7, "Kholinar": -4},
        },
        (
            ["Shadesmar", "Jah Keved", "negative cycle detected!"],
            ["Kholinar", "Shinovar", "negative cycle detected!"],
            ["Jah Keved", "Kholinar", "negative cycle detected!"],
        ),
    ),
]


def test(graph, tests):
    print("---------------------------------")
    print("Graph:")
    for node in graph:
        print(f" - Node {node}: {graph[node]}")
    print("\n")
    try:
        for test in tests:
            try:
                src = test[0]
                dest = test[1]
                expected_path = test[2]
                print(f"Source node: {src}")
                print(f"Destination node: {dest}")
                print(f"Expecting: {expected_path}")
                result = bellman_ford(graph, src, dest)
                print(f"Actual: {result}\n")
                if result != expected_path:
                    print("\nFail")
                    return False
            except Exception as e:
                print(f"Actual: {str(e)}\n")
                if str(e) != test[2]:
                    print("\nFail")
                    return False
        print("\nPass")
        return True
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

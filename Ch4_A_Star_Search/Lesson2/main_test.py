from main import Tile, TrafficGrid

TestCase = tuple[tuple[int, int], tuple[int, int], bool, list[tuple[int, int]]]

run_cases: list[TestCase] = [
    ((5, 5), (2, 2), True, [(3, 2), (1, 2), (2, 1), (2, 3)]),
    ((5, 5), (6, 5), False, []),
]

submit_cases: list[TestCase] = run_cases + [
    ((1, 1), (0, 0), True, []),
    ((5, 5), (1, 1), True, [(2, 1), (0, 1), (1, 0), (1, 2)]),
    ((10, 10), (5, 5), True, [(6, 5), (4, 5), (5, 4), (5, 6)]),
    ((5, 5), (4, 4), True, [(3, 4), (4, 3)]),
    ((5, 5), (0, 0), True, [(1, 0), (0, 1)]),
]


def test(
    traffic_grid_inputs: tuple[int, int],
    tile_inputs: tuple[int, int],
    expected_in_bounds: bool,
    expected_neighbors: list[tuple[int, int]],
) -> bool:
    print("---------------------------------")
    try:
        traffic_grid = TrafficGrid(*traffic_grid_inputs)
        tile = Tile(*tile_inputs)
        print(
            f"TrafficGrid: width: {traffic_grid.width}, height: {traffic_grid.height}"
        )
        print(traffic_grid)
        print(f"in_bounds{tile}")
        print(f"Expected: {expected_in_bounds}")
        in_bounds_result = traffic_grid.in_bounds(tile)
        print(f"Actual: {traffic_grid.in_bounds(tile)}\n")
        if in_bounds_result != expected_in_bounds:
            print("Fail")
            return False

        print(f"neighbors{tile}")
        expected_neighbors_tiles = [Tile(x, y) for x, y in expected_neighbors]
        print(f"Expected: {expected_neighbors_tiles}")
        neighbors_result = traffic_grid.neighbors(tile)
        print(f"Actual: {list(traffic_grid.neighbors(tile))}\n")

        if list(neighbors_result) != expected_neighbors_tiles:
            print("Fail")
            return False
        print("Pass")
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

from main import Tile, TrafficGrid, a_star_search
import traceback

GridDimensions = tuple[int, int]
TileCoords = tuple[int, int]
# i.e., grid dimensions, src, dest, expected path
TestCase = tuple[GridDimensions, TileCoords, TileCoords, list[TileCoords]]

run_cases: list[TestCase] = [
    ((4, 4), (0, 0), (3, 3), [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3)]),
    (
        (8, 8),
        (0, 4),
        (7, 4),
        [
            (0, 4),
            (0, 3),
            (0, 2),
            (0, 1),
            (1, 1),
            (2, 1),
            (2, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (6, 2),
            (7, 2),
            (7, 3),
            (7, 4),
        ],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        (10, 10),
        (0, 0),
        (9, 9),
        [
            (0, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (3, 5),
            (4, 5),
            (5, 5),
            (5, 6),
            (5, 7),
            (5, 8),
            (6, 8),
            (6, 9),
            (7, 9),
            (8, 9),
            (9, 9),
        ],
    ),
]


def test(
    grid_dims: GridDimensions,
    src_coords: TileCoords,
    dest_coords: TileCoords,
    expected_path: list[TileCoords],
) -> bool:
    print("---------------------------------")
    try:
        grid = TrafficGrid(*grid_dims)
        src = Tile(*src_coords)
        dest = Tile(*dest_coords)

        print(f"TrafficGrid: width {grid.width}, height {grid.height}")
        print(grid)

        print(f"Shortest path from {src} to {dest}")
        print(f"Expected: {expected_path}")

        actual_path = a_star_search(grid, src, dest)
        print(f"Actual:   {actual_path}\n")

        if actual_path == expected_path:
            print("Pass")
            return True

        print("Fail")
        return False
    except Exception as e:
        traceback.print_exc()
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

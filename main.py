from typing import Dict, List, Union

StudentDict = Dict[str, Union[str, int, Dict[str, str]]]


def merge_lists(list_1: List[StudentDict], list_2: List[StudentDict]) -> List[StudentDict]:
    """
    Merges the information from list_1 and list_2 to create a new list, which has
    all the information about each student from both lists in one single dict.

    :param list_1: List of dictionaries containing student information
    :param list_2: List of dictionaries containing student information
    :return: Merged list of dictionaries containing student information
    """
    # Create a dictionary to store the merged student information
    merged_dict: Dict[str, StudentDict] = {}

    # Merge values from list_1
    for student in list_1:
        id_ = student["id"]
        if id_ not in merged_dict:
            merged_dict[id_] = student
        else:
            merged_dict[id_].update(student)

    # Merge values from list_2
    for student in list_2:
        id_ = student["id"]
        if id_ not in merged_dict:
            merged_dict[id_] = student
        else:
            merged_dict[id_].update(student)

    # Convert merged dictionary to a list of dicts
    result: List[StudentDict] = list(merged_dict.values())

    return result


def test_merge_lists():
    """
    Tests the merge_lists function.
    """

    test_cases = [
        {
            # Default test case
            "input": (
                 [
                     {"id": "1", "name": "Shrey", "age": 25},
                     {"id": "3", "age": 10, "name": "Hello"},
                     {"id": "2", "name": "World", "age": 24},
                 ],
                [
                     {"id": "1", "marks": 100},
                     {
                         "id": "3",
                         "marks": 90,
                         "roll_no": 11,
                         "extra_info": {
                             "hello": "world",
                         },
                     },
                 ],
            ),
            "expected_output": [
                {"id": "1", "name": "Shrey", "age": 25, "marks": 100},
                {"id": "3", "age": 10, "name": "Hello", "marks": 90,
                 "roll_no": 11, "extra_info": {"hello": "world"}},
                {"id": "2", "name": "World", "age": 24},
            ],
        },
        {
            # Test case with duplicate keys
            "input": (
                [
                    {"id": "1", "name": "Alice", "age": 23},
                    {"id": "2", "name": "Bob", "age": 27},
                    {"id": "3", "name": "Charlie", "age": 25},
                ],
                [
                    {"id": "1", "score": 90},
                    {"id": "3", "score": 80, "gender": "male"},
                ],
            ),
            "expected_output": [
                {"id": "1", "name": "Alice", "age": 23, "score": 90},
                {"id": "2", "name": "Bob", "age": 27},
                {"id": "3", "name": "Charlie", "age": 25,
                    "score": 80, "gender": "male"},
            ],
        },
        {
            # Both lists are empty
            "input": (
                [],
                [],
            ),
            "expected_output": [],
        },
        {
            # One list is empty and the other has one item
            "input": (
                [],
                [{"id": "1", "name": "John", "age": 20}],
            ),
            "expected_output": [{"id": "1", "name": "John", "age": 20}],
        },
        {
            # Both lists have one item with the same ID
            "input": (
                [{"id": "1", "name": "John", "age": 20}],
                [{"id": "1", "marks": 80}],
            ),
            "expected_output": [{"id": "1", "name": "John", "age": 20, "marks": 80}],
        },
        {
            # Both lists have one item with different IDs
            "input": (
                [{"id": "1", "name": "John", "age": 20}],
                [{"id": "2", "marks": 80}],
            ),
            "expected_output": [{"id": "1", "name": "John", "age": 20}, {"id": "2", "marks": 80}],
        },
        {
            # Both lists have multiple items with some matching IDs
            "input": (
                [
                    {"id": "1", "name": "John", "age": 20},
                    {"id": "2", "name": "Jane", "age": 22},
                    {"id": "3", "name": "Bob", "age": 25},
                ],
                [
                    {"id": "2", "marks": 90},
                    {"id": "3", "marks": 80},
                    {"id": "4", "name": "Alice", "age": 21},
                ],
            ),
            "expected_output": [
                {"id": "1", "name": "John", "age": 20},
                {"id": "2", "name": "Jane", "age": 22, "marks": 90},
                {"id": "3", "name": "Bob", "age": 25, "marks": 80},
                {"id": "4", "name": "Alice", "age": 21},
            ],
        },
        {
            # Both lists have multiple items with all matching IDs
            "input": (
                [
                    {"id": "1", "name": "John", "age": 20},
                    {"id": "2", "name": "Jane", "age": 22},
                    {"id": "3", "name": "Bob", "age": 25},
                ],
                [
                    {"id": "1", "marks": 80},
                    {"id": "2", "marks": 90},
                    {"id": "3", "marks": 80},
                ],
            ),
            "expected_output": [
                {"id": "1", "name": "John", "age": 20, "marks": 80},
                {"id": "2", "name": "Jane", "age": 22, "marks": 90},
                {"id": "3", "name": "Bob", "age": 25, "marks": 80},
            ],
        },
    ]

    print("\nTesting on different test cases...\n")

    test_cases_passed = 0
    test_cases_failed = 0

    for test_case in test_cases:
        list_1 = test_case["input"][0]
        list_2 = test_case["input"][1]
        expected_output = test_case["expected_output"]

        try:
            assert merge_lists(list_1, list_2) == expected_output
            test_cases_passed += 1
        except AssertionError:
            test_cases_failed += 1

    print(f"Test cases passed: {test_cases_passed}")
    print(f"Test cases failed: {test_cases_failed}")


if __name__ == "__main__":
    test_merge_lists()

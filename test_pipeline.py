import os
import pandas as pd

def test_dataset_exists():
    """
    Asserts that the benchmark dataset is in the correct location.
    """
    assert os.path.exists("dataset.csv"), "Error: dataset.csv is missing from the repository root!"
    print("Test Passed: dataset.csv exists.")

def test_dataset_integrity():
    """
    Validates that the dataset loads correctly and contains the expected data.
    """
    df = pd.read_csv("dataset.csv")
    assert not df.empty, "Error: The dataset is empty!"
    print(f"Test Passed: Dataset integrity verified. Current Shape: {df.shape}")

if __name__ == "__main__":
    print("Running automated repository tests...")
    test_dataset_exists()
    test_dataset_integrity()
    print("All tests completed successfully!")
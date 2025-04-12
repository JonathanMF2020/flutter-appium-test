import pytest
import os

def main():
    """Entry point to run the tests."""
    tests_path = os.path.join(os.path.dirname(__file__), "tests")

    print("🚀 Running all the tests...")
    pytest.main([tests_path])


if __name__ == "__main__":
    main()
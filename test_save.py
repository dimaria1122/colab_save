"""
Simple tests for the save module.
Run with: python test_save.py
"""

import os
import json
import shutil
from save import save_text, save_json, save_with_timestamp, save_something


def test_save_text():
    """Test saving text to a file."""
    print("Testing save_text...")
    test_dir = "test_saved_data"
    content = "Test content"
    filename = "test.txt"
    
    filepath = save_text(content, filename, directory=test_dir)
    
    # Verify file exists
    assert os.path.exists(filepath), f"File not created: {filepath}"
    
    # Verify content
    with open(filepath, 'r') as f:
        saved_content = f.read()
    assert saved_content == content, f"Content mismatch: {saved_content} != {content}"
    
    print("✓ save_text works correctly")
    return test_dir


def test_save_json():
    """Test saving JSON data to a file."""
    print("Testing save_json...")
    test_dir = "test_saved_data"
    data = {"name": "test", "value": 42, "items": [1, 2, 3]}
    filename = "test.json"
    
    filepath = save_json(data, filename, directory=test_dir)
    
    # Verify file exists
    assert os.path.exists(filepath), f"File not created: {filepath}"
    
    # Verify content
    with open(filepath, 'r') as f:
        saved_data = json.load(f)
    assert saved_data == data, f"Data mismatch: {saved_data} != {data}"
    
    print("✓ save_json works correctly")
    return test_dir


def test_save_with_timestamp():
    """Test saving with timestamp."""
    print("Testing save_with_timestamp...")
    test_dir = "test_saved_data"
    content = "Timestamped content"
    base_filename = "note.txt"
    
    filepath = save_with_timestamp(content, base_filename, directory=test_dir)
    
    # Verify file exists
    assert os.path.exists(filepath), f"File not created: {filepath}"
    
    # Verify filename contains timestamp
    assert base_filename in filepath, f"Base filename not in path: {filepath}"
    
    print("✓ save_with_timestamp works correctly")
    return test_dir


def test_save_something():
    """Test automatic save function."""
    print("Testing save_something...")
    test_dir = "test_saved_data"
    
    # Test with string
    filepath1 = save_something("Test string", "auto_test.txt", directory=test_dir)
    assert os.path.exists(filepath1), f"File not created: {filepath1}"
    
    # Test with dict (should be saved as JSON)
    filepath2 = save_something({"key": "value"}, "auto_test.json", directory=test_dir)
    assert os.path.exists(filepath2), f"File not created: {filepath2}"
    
    # Test with auto-generated filename
    filepath3 = save_something("Auto filename", directory=test_dir)
    assert os.path.exists(filepath3), f"File not created: {filepath3}"
    
    print("✓ save_something works correctly")
    return test_dir


def run_tests():
    """Run all tests."""
    print("=== Running Tests ===\n")
    
    test_dirs = set()
    
    try:
        test_dirs.add(test_save_text())
        test_dirs.add(test_save_json())
        test_dirs.add(test_save_with_timestamp())
        test_dirs.add(test_save_something())
        
        print("\n=== All tests passed! ===")
        
    finally:
        # Cleanup test directories
        for test_dir in test_dirs:
            if os.path.exists(test_dir):
                shutil.rmtree(test_dir)
                print(f"\nCleaned up test directory: {test_dir}")


if __name__ == "__main__":
    run_tests()

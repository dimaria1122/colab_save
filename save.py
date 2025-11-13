"""
Simple save functionality for Google Colab files.
This module provides functions to save data to files.
"""

import os
import json
from datetime import datetime
from typing import Any, Union


def save_text(content: str, filename: str, directory: str = "saved_data") -> str:
    """
    Save text content to a file.
    
    Args:
        content: The text content to save
        filename: Name of the file to save to
        directory: Directory to save the file in (default: "saved_data")
    
    Returns:
        str: Full path to the saved file
    """
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Create full path
    filepath = os.path.join(directory, filename)
    
    # Save the content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully saved to: {filepath}")
    return filepath


def save_json(data: Any, filename: str, directory: str = "saved_data") -> str:
    """
    Save data as JSON to a file.
    
    Args:
        data: The data to save (must be JSON serializable)
        filename: Name of the file to save to
        directory: Directory to save the file in (default: "saved_data")
    
    Returns:
        str: Full path to the saved file
    """
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Create full path
    filepath = os.path.join(directory, filename)
    
    # Save the data as JSON
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully saved JSON to: {filepath}")
    return filepath


def save_with_timestamp(content: Union[str, Any], base_filename: str, 
                       directory: str = "saved_data", as_json: bool = False) -> str:
    """
    Save content with a timestamp in the filename.
    
    Args:
        content: The content to save
        base_filename: Base name for the file (timestamp will be prepended)
        directory: Directory to save the file in (default: "saved_data")
        as_json: If True, save as JSON; otherwise save as text
    
    Returns:
        str: Full path to the saved file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{base_filename}"
    
    if as_json:
        return save_json(content, filename, directory)
    else:
        return save_text(str(content), filename, directory)


def save_something(content: Any, filename: str = None, directory: str = "saved_data") -> str:
    """
    Save something - automatically determines the best save method.
    
    Args:
        content: The content to save
        filename: Optional filename (auto-generated if not provided)
        directory: Directory to save the file in (default: "saved_data")
    
    Returns:
        str: Full path to the saved file
    """
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"saved_{timestamp}.txt"
    
    # Determine save method based on content type
    if isinstance(content, str):
        return save_text(content, filename, directory)
    else:
        # Try to save as JSON for non-string types
        if not filename.endswith('.json'):
            filename = filename.rsplit('.', 1)[0] + '.json'
        return save_json(content, filename, directory)


if __name__ == "__main__":
    # Example usage
    print("=== Save Module Examples ===\n")
    
    # Example 1: Save simple text
    save_text("Hello, this is a test!", "test.txt")
    
    # Example 2: Save JSON data
    data = {"name": "Test", "value": 42, "items": [1, 2, 3]}
    save_json(data, "test.json")
    
    # Example 3: Save with timestamp
    save_with_timestamp("Timestamped content", "note.txt")
    
    # Example 4: Save something (automatic)
    save_something("Just save this!")
    save_something({"auto": "save", "works": True})
    
    print("\n=== All files saved successfully! ===")

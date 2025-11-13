"""
Example script demonstrating the save functionality.
This can be run in Google Colab or locally.
"""

from save import save_text, save_json, save_with_timestamp, save_something

def main():
    print("=== Colab Save Examples ===\n")
    
    # Example 1: Save a simple note
    print("1. Saving a simple text note...")
    save_text("This is my first saved note from Colab!", "my_note.txt")
    print()
    
    # Example 2: Save experimental results
    print("2. Saving experimental results...")
    results = {
        "experiment": "Model Training",
        "accuracy": 0.95,
        "loss": 0.05,
        "parameters": {
            "learning_rate": 0.001,
            "epochs": 100
        }
    }
    save_json(results, "experiment_results.json")
    print()
    
    # Example 3: Save with timestamp (for logging)
    print("3. Saving with timestamp...")
    save_with_timestamp("Training completed successfully", "training_log.txt")
    print()
    
    # Example 4: Quick save (automatic detection)
    print("4. Quick save (automatic)...")
    save_something("Quick note: Remember to review the model!")
    save_something({"status": "completed", "time": "2025-11-11"}, "status.json")
    print()
    
    print("=== All examples completed! ===")
    print("Check the 'saved_data' directory for your saved files.")

if __name__ == "__main__":
    main()

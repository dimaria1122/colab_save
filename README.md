# colab_save
A simple Python module for saving data from Google Colab or local environments.

## Features

- **Save text files** - Save text content to files
- **Save JSON data** - Save Python objects as JSON
- **Timestamp support** - Automatically add timestamps to filenames
- **Automatic detection** - Smart save function that detects content type
- **Easy to use** - Simple API with sensible defaults

## Installation

Simply copy `save.py` to your project or Google Colab environment.

## Usage

### Quick Start

```python
from save import save_something

# Save anything quickly
save_something("Hello, World!")
save_something({"name": "test", "value": 42})
```

### Save Text

```python
from save import save_text

save_text("This is my note", "my_note.txt")
```

### Save JSON

```python
from save import save_json

data = {
    "experiment": "Model Training",
    "accuracy": 0.95,
    "loss": 0.05
}
save_json(data, "results.json")
```

### Save with Timestamp

```python
from save import save_with_timestamp

# Text file with timestamp
save_with_timestamp("Training completed", "training_log.txt")

# JSON file with timestamp
save_with_timestamp({"status": "done"}, "status.json", as_json=True)
```

## Examples

Run the example script to see all features in action:

```bash
python example.py
```

## Directory Structure

All files are saved to the `saved_data/` directory by default. You can specify a different directory:

```python
save_text("Content", "file.txt", directory="my_data")
```

## License

MIT

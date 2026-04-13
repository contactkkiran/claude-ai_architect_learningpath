# Claude API Mastery

This project is a simple Python example that shows how to call the Anthropic Claude API using the official Python SDK.

It currently includes:

- Loading environment variables with `python-dotenv`
- Creating an `Anthropic` client with `ANTHROPIC_API_KEY`
- Sending a basic Claude request with a system prompt
- Sending a second request with a more implementation-focused prompt
- Printing the model responses and token usage for the first example

## Project Structure

```text
claude-api-mastery/
├── code module1.py
├── README.md
└── venv/
```

## Requirements

- Python 3.10+
- An Anthropic API key

## Install Dependencies

If you are using the existing virtual environment:

```bash
source venv/bin/activate
```

Then install the required packages:

```bash
pip install anthropic python-dotenv
```

## Environment Setup

Create a `.env` file inside `claude-api-mastery/`:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

## Run the Script

From inside the project folder:

```bash
python "code module1.py"
```

## What the Script Does

`code module1.py`:

1. Loads environment variables using `load_dotenv()`
2. Reads `ANTHROPIC_API_KEY` from `.env`
3. Creates an Anthropic client
4. Sends a first prompt asking `What is AI?`
5. Prints the model response and token counts
6. Sends a second prompt asking how to build a simple API using FastAPI
7. Prints the second model response

## Notes

- Make sure your API key is valid before running the script.
- The file name contains a space, so keep the quotes when running it from the terminal.
- The `venv/` folder is local environment setup and is usually not committed to version control.

## Possible Next Improvements

- Add `requirements.txt`
- Rename `code module1.py` to `code_module1.py`
- Add basic error handling for missing API keys
- Print token usage for both examples

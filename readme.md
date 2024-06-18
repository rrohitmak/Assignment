# FastAPI Assignment Project

A brief description of your project, what it does, and its main features.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- Python 3.x
- pip
- IDE i.e. VS Code

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/rrohitmak/Assignment
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Quick Start
To start the FastAPI server:
```bash
uvicorn main:app --reload

import requests

### body
{
"batchid": "id0101",
"payload": [[5, 3], [4, 2]]
}
### API Request
response = requests.post("http://127.0.0.1:8000/get-sum",headers = {},data=body)
print(response.json())

### Response:

{
  "batchid": "id0101",
  "response": [8,6],
  "status": "complete",
  "started_at": "2024-06-11T12:15:01.100Z",
  "completed_at": "2024-06-11T12:15:01.100Z"
}


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Day 1 Assessment
- **Name:** Pankaj Sharma
- **College/Year:** Maharaja Agrasen University, Passout 2026
- **Programming languages:** Java, Python, HTML, CSS, Sql
- **Technologies worked with:** VS Code, GitHub, Tableau
- **Current AI/ML Knowledge:** Basic understanding of LLM integration, RAG pipelines, text splitter
- **Goals for this Internsip:** To deepen knowledge of AI/ML systems, build production-ready agents, and improve backend engineering skills. 

## How to Run the Project Locally

### 1. Setup Virtual Environment & Install Dependencies
'''bash
python -m venv venv

# On Windows Powershell:
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Task 4 : Debugging assessment

### Original Code
    def find_largest(numbers):    
        largest = 0    
         
        for number in numbers:    
            if number < largest:    
                largest = number    
         
        return largest

1. What was wrong?
    The comparison operator used was < (less than) instead of > (greater than).
    largest was initialized to 0, which causes failures when working with negative numbers.

2. Why did it produce incorrect results?
    Using < caused the code to track smaller values rather than larger ones.
    Initializing largest = 0 meant that for negative inputs (e.g., [-10, -5, -20, -3]), no number would ever be greater than 0, incorrectly returning 0 instead of -3.

3. What change did you make?
    Changed if number < largest: to if number > largest:.
    Initialized largest = numbers[0] to correctly handle negative numbers and single-element lists.
    Added a safeguard if not numbers: to handle empty list inputs cleanly.
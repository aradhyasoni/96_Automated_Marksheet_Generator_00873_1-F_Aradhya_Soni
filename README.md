# Automated Marksheet Generator

**University Project:** PS No. 96  
**Language:** Python 3  
**Library:** Pandas

## 1. Project description
This program reads student marks from `marks.csv` using Pandas. It calculates the total (out of 300), percentage, grade and pass/fail result, then prints a formatted marksheet for the roll number entered by the user.

A student fails if even one subject has marks below 40. Invalid CSV rows are skipped with a warning.

## 2. Folder structure

```text
96_Automated_Marksheet_Generator/
|
|-- Testcases/
|   |-- README_Testcases.txt
|   |-- test_case_1_anita.txt
|   |-- test_case_2_rahul.txt
|   |-- test_case_3_invalid_input.txt
|   |-- test_case_4_suman.txt
|
|-- Codebase/
|   |-- marksheet.py
|   |-- marks.csv
|   |-- README.md
```

## 3. Requirements
- Python 3
- Pandas

Install Pandas in the VS Code terminal:

```powershell
py -m pip install pandas
```

If `py` does not work, use:

```powershell
python -m pip install pandas
```

## 4. How to run in VS Code
1. Extract the project ZIP file.
2. Open the extracted project folder in VS Code.
3. Open **Terminal > New Terminal**.
4. Move into the Codebase folder:

```powershell
cd Codebase
```

5. Run the program:

```powershell
py marksheet.py
```

If needed, use `python marksheet.py` instead.
6. Enter one of the roll numbers: `101`, `102`, `103` or `104`.

Keep `marks.csv` in the same folder as `marksheet.py`.

## 5. Sample CSV data

| Roll No. | Name | Maths | Physics | Programming |
|---:|---|---:|---:|---:|
| 101 | Anita | 85 | 90 | 80 |
| 102 | Rahul | 40 | 45 | 50 |
| 103 | Suman | 35 | 70 | 60 |
| 104 | Vikas | 100 | 100 | 100 |

## 6. Grading system

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| 40 to below 50 | E |
| Below 40 | F |

**Pass rule:** Every subject must have at least 40 marks. Otherwise, the result is FAIL.

## 7. Test cases
The four test-case output files are in the `Testcases` folder. Run the program for each roll number and capture a screenshot of the actual VS Code terminal output. Save those screenshots in `Testcases`.

For Test Case 3, temporarily add this row to the bottom of `marks.csv`:

```csv
106,Kiran,105,60,70
```

Run the program and enter `999`. The program should warn that roll 106 was skipped and report that roll number 999 was not found. Remove the extra row after the test.

## 8. Concepts used
- Pandas and CSV file handling
- Functions
- Conditional statements
- Loops
- Input validation
- Exception handling
- String formatting

## 9. Submission reminder
The university asks for a **public GitHub repository** with two folders named `Testcases` and `Codebase`. `Codebase` must contain the Python code and this README file. `Testcases` must contain screenshots of the test runs.

Before submitting, rename the GitHub repository using the exact format supplied by your faculty:

`96_Automated Marksheet Generator_ERP_Section_FullName`

Replace `ERP`, `Section` and `FullName` with your own official details. Do not guess your ERP number or section.

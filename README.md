# Employee Pension Plans Management System

A Python CLI application for managing employee pension plans with features for viewing employee data and generating enrollment reports.

## Project Structure

```
employee_pension_app/
├── main.py                          # Entry point with CLI menu
├── models/
│   ├── employee.py                  # Employee class
│   └── pension_plan.py              # PensionPlan class
├── services/
│   └── pension_service.py           # Business logic for pension management
├── utils/
│   └── json_formatter.py            # JSON output formatting utilities
├── tests/
│   └── test_pension_service.py      # Unit tests
├── requirements.txt                 # Project dependencies
└── README.md                        # This file
```

## Requirements

- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Navigate to the project directory:
```bash
cd employee_pension_app
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Running the Application

Execute the main application with:
```bash
python main.py
```

This will display an interactive CLI menu with the following options:

1. **Print All Employees** - Displays all employees in JSON format, sorted by salary (descending) and last name (ascending)
2. **Print Quarterly Upcoming Enrollees Report** - Shows employees who will be eligible for pension enrollment in the next quarter
3. **Exit** - Terminates the application

## Features

### Feature 1: Print All Employees
- Lists all employees with their complete information
- Includes pension plan details if enrolled
- JSON output sorted by:
  - Primary: Yearly salary (descending)
  - Secondary: Last name (ascending)
- All dates formatted as "YYYY-MM-DD"
- All monetary values formatted with 2 decimal places

### Feature 2: Quarterly Upcoming Enrollees Report
- Identifies employees eligible for pension enrollment in the upcoming quarter
- Criteria for eligibility:
  1. Employee must NOT have an active pension plan
  2. Employee's 3-year employment milestone must fall within the next quarter
- Results sorted by employment date (descending)
- Quarter definitions:
  - Q1: January 1 – March 31
  - Q2: April 1 – June 30
  - Q3: July 1 – September 30
  - Q4: October 1 – December 31

### Feature 3: CLI Menu
- Simple, user-friendly command-line interface
- Option to view reports or exit the application

## Running Tests

Execute the unit tests with:
```bash
python -m pytest tests/test_pension_service.py
```

Or using unittest:
```bash
python -m unittest tests.test_pension_service
```

## Test Coverage

The test suite includes:
- Employee data loading verification
- Sorting by salary and last name
- Pension plan validation
- Quarterly eligibility calculation
- Employee sorting by employment date

## Preloaded Data

The application comes with 6 preloaded employees:

| ID | Name | Salary | Employed Since | Pension Plan |
|----|------|--------|-----------------|--------------|
| 1 | Daniel Agar | $105,945.50 | 2023-01-17 | None |
| 2 | Bernard Shaw | $197,750.00 | 2022-09-03 | Plan Reference: (none) |
| 3 | Carly Agar | $842,000.75 | 2014-05-16 | SM2307 |
| 4 | Wesley Schneider | $74,500.00 | 2023-07-21 | None |
| 5 | Anna Wiltord | $85,750.00 | 2023-03-15 | None |
| 6 | Yosef Tesfalem | $100,000.00 | 2024-10-31 | None |

## Output Format

### All Employees (JSON)
```json
[
  {
    "employeeId": 3,
    "firstName": "Carly",
    "lastName": "Agar",
    "employmentDate": "2014-05-16",
    "yearlySalary": 842000.75,
    "pensionPlan": {
      "planReferenceNumber": "SM2307",
      "enrollmentDate": "2017-05-17",
      "monthlyContribution": 1555.50
    }
  }
]
```

### Quarterly Upcoming Enrollees (JSON)
```json
{
  "quarterlyUpcomingEnrollees": [
    {
      "employeeId": 1,
      "firstName": "Daniel",
      "lastName": "Agar",
      "employmentDate": "2023-01-17",
      "yearlySalary": 105945.50
    }
  ]
}
```

## Architecture

- **Models**: Define the data structures (`Employee`, `PensionPlan`)
- **Services**: Implement business logic for data retrieval and calculations
- **Utils**: Provide formatting and output utilities
- **Tests**: Comprehensive unit tests using Python's unittest framework

## Notes

- All dates are handled using Python's `datetime.date` class
- JSON output uses `json.dumps()` with 2-space indentation
- The application uses only Python standard library modules (no external dependencies)


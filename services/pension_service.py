from datetime import date
from typing import Optional
from models.employee import Employee
from models.pension_plan import PensionPlan


class PensionService:
    """Service for managing pension plans and employee data."""

    def __init__(self):
        self.employees = []
        self._load_preloaded_data()

    def _load_preloaded_data(self):
        """Load the preloaded employee and pension plan data."""
        # Employee 1: Daniel Agar - no pension plan
        emp1 = Employee(
            employee_id=1,
            first_name="Daniel",
            last_name="Agar",
            employment_date=date(2025, 8, 17),
            yearly_salary=105945.50,
            pension_plan=None,
        )
        self.employees.append(emp1)

        # Employee 2: Benard Shaw - with pension plan
        emp2 = Employee(
            employee_id=2,
            first_name="Benard",
            last_name="Shaw",
            employment_date=date(2025, 2, 3),
            yearly_salary=197750.00,
            pension_plan=PensionPlan(
                plan_reference_number="EX0089",
                enrollment_date=date(2026, 2, 3),
                monthly_contribution=450.00,
            ),
        )
        self.employees.append(emp2)

        # Employee 3: Carly Jones - with pension plan
        emp3 = Employee(
            employee_id=3,
            first_name="Carly",
            last_name="Jones",
            employment_date=date(2024, 5, 16),
            yearly_salary=842000.75,
            pension_plan=PensionPlan(
                plan_reference_number="SM2307",
                enrollment_date=date(2025, 5, 17),
                monthly_contribution=1555.50,
            ),
        )
        self.employees.append(emp3)

        # Employee 4: Wesley Schneider - no pension plan
        emp4 = Employee(
            employee_id=4,
            first_name="Wesley",
            last_name="Schneider",
            employment_date=date(2025, 4, 30),
            yearly_salary=174500.00,
            pension_plan=None,
        )
        self.employees.append(emp4)

        # Employee 5: Anna Wiltord - no pension plan
        emp5 = Employee(
            employee_id=5,
            first_name="Anna",
            last_name="Wiltord",
            employment_date=date(2025, 9, 15),
            yearly_salary=185750.00,
            pension_plan=None,
        )
        self.employees.append(emp5)

        # Employee 6: Yosef Tesfalem - no pension plan
        emp6 = Employee(
            employee_id=6,
            first_name="Yosef",
            last_name="Tesfalem",
            employment_date=date(2025, 7, 31),
            yearly_salary=100000.00,
            pension_plan=None,
        )
        self.employees.append(emp6)

        # Employee 7: Johnny Edwards - no pension plan
        emp7 = Employee(
            employee_id=7,
            first_name="Johnny",
            last_name="Edwards",
            employment_date=date(2025, 7, 9),
            yearly_salary=95500.00,
            pension_plan=None,
        )
        self.employees.append(emp7)

    def get_all_employees(self):
        """
        Get all employees sorted by yearly_salary (DESC) then last_name (ASC).

        Returns:
            List of Employee objects sorted by the specified criteria.
        """
        return sorted(
            self.employees,
            key=lambda e: (-e.yearly_salary, e.last_name),
        )

    def get_quarterly_upcoming_enrollees(self):
        """
        Get employees who will be eligible for pension enrollment in the next quarter.

        An employee qualifies if:
        1. They have NO pension plan enrolled
        2. Their employment_date + 3 years falls ON OR BETWEEN the first and last day of the next quarter

        Returns:
            List of Employee objects sorted by employment_date (DESC).
        """
        from datetime import datetime

        # Determine the next quarter
        today = date.today()
        current_month = today.month

        if current_month <= 3:
            next_quarter_start = date(today.year, 4, 1)
            next_quarter_end = date(today.year, 6, 30)
        elif current_month <= 6:
            next_quarter_start = date(today.year, 7, 1)
            next_quarter_end = date(today.year, 9, 30)
        elif current_month <= 9:
            next_quarter_start = date(today.year, 10, 1)
            next_quarter_end = date(today.year, 12, 31)
        else:  # current_month <= 12
            next_quarter_start = date(today.year + 1, 1, 1)
            next_quarter_end = date(today.year + 1, 3, 31)

        qualifying_employees = []

        for emp in self.employees:
            # Check if employee has no pension plan
            if emp.pension_plan is not None:
                continue

            # Calculate eligibility date (employment_date + 3 years)
            try:
                eligibility_date = emp.employment_date.replace(
                    year=emp.employment_date.year + 3
                )
            except ValueError:
                # Handle edge case of Feb 29 in leap year
                eligibility_date = emp.employment_date.replace(
                    year=emp.employment_date.year + 3, day=28
                )

            # Check if eligibility date falls within the next quarter
            if next_quarter_start <= eligibility_date <= next_quarter_end:
                qualifying_employees.append(emp)

        # Sort by employment_date descending
        return sorted(qualifying_employees, key=lambda e: e.employment_date, reverse=True)


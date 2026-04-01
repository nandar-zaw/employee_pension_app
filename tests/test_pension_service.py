import unittest
from datetime import date
from services.pension_service import PensionService
from models.employee import Employee
from models.pension_plan import PensionPlan


class TestPensionService(unittest.TestCase):
    """Unit tests for PensionService class."""

    def setUp(self):
        """Set up test fixtures."""
        self.service = PensionService()

    def test_get_all_employees_count(self):
        """Test that all 8 preloaded employees are loaded."""
        employees = self.service.get_all_employees()
        self.assertEqual(len(employees), 8)

    def test_get_all_employees_sorted_by_salary_descending(self):
        """Test that employees are sorted by salary descending."""
        employees = self.service.get_all_employees()
        # Verify the first employee has the highest salary
        self.assertEqual(employees[0].employee_id, 3)  # Carly Jones with 842000.75
        self.assertEqual(employees[0].yearly_salary, 842000.75)
        # Verify the last employee has the lowest salary
        self.assertEqual(employees[-1].employee_id, 7)  # Johnny Edwards with 95500.00
        self.assertEqual(employees[-1].yearly_salary, 95500.00)

    def test_get_all_employees_secondary_sort_by_lastname_ascending(self):
        """Test that employees are sorted by salary descending, then last_name ascending."""
        employees = self.service.get_all_employees()
        # Verify the sorting is correct
        # Check that salaries are in descending order
        for i in range(len(employees) - 1):
            self.assertGreaterEqual(employees[i].yearly_salary, employees[i + 1].yearly_salary)
            # If salaries are equal, check last names are in ascending order
            if employees[i].yearly_salary == employees[i + 1].yearly_salary:
                self.assertLessEqual(employees[i].last_name, employees[i + 1].last_name)

    def test_employee_without_pension_plan(self):
        """Test that employees without pension plans have None for pension_plan field."""
        employees = self.service.get_all_employees()
        emp_without_plan = next(
            (e for e in employees if e.employee_id == 1), None
        )
        self.assertIsNotNone(emp_without_plan)
        self.assertIsNone(emp_without_plan.pension_plan)

    def test_employee_with_pension_plan(self):
        """Test that employees with pension plans have correct plan details."""
        employees = self.service.get_all_employees()
        emp_with_plan = next(
            (e for e in employees if e.employee_id == 3), None
        )
        self.assertIsNotNone(emp_with_plan)
        self.assertIsNotNone(emp_with_plan.pension_plan)
        self.assertEqual(emp_with_plan.pension_plan.plan_reference_number, "SM2307")
        self.assertEqual(
            emp_with_plan.pension_plan.enrollment_date, date(2025, 5, 17)
        )
        self.assertEqual(emp_with_plan.pension_plan.monthly_contribution, 1555.50)

    def test_quarterly_upcoming_enrollees_no_pension_plan_required(self):
        """Test that quarterly enrollees report only includes employees without pension plans."""
        upcoming = self.service.get_quarterly_upcoming_enrollees()
        # All returned employees should not have a pension plan
        for emp in upcoming:
            self.assertIsNone(emp.pension_plan)

    def test_quarterly_upcoming_enrollees_eligibility_date_calculation(self):
        """Test that eligibility dates are calculated correctly (employment_date + 3 years)."""
        upcoming = self.service.get_quarterly_upcoming_enrollees()
        # Verify that each employee's 3-year eligibility date falls within the next quarter
        from datetime import datetime
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
        else:
            next_quarter_start = date(today.year + 1, 1, 1)
            next_quarter_end = date(today.year + 1, 3, 31)

        for emp in upcoming:
            try:
                eligibility_date = emp.employment_date.replace(
                    year=emp.employment_date.year + 3
                )
            except ValueError:
                eligibility_date = emp.employment_date.replace(
                    year=emp.employment_date.year + 3, day=28
                )
            self.assertGreaterEqual(eligibility_date, next_quarter_start)
            self.assertLessEqual(eligibility_date, next_quarter_end)

    def test_quarterly_upcoming_enrollees_sorted_by_employment_date(self):
        """Test that upcoming enrollees are sorted by employment_date descending."""
        upcoming = self.service.get_quarterly_upcoming_enrollees()
        if len(upcoming) > 1:
            for i in range(len(upcoming) - 1):
                self.assertGreaterEqual(
                    upcoming[i].employment_date,
                    upcoming[i + 1].employment_date,
                )


if __name__ == "__main__":
    unittest.main()

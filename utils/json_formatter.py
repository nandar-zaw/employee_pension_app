import json
from typing import Any, List
from models.employee import Employee


class JsonFormatter:
    """Utility class for formatting JSON output."""

    @staticmethod
    def format_employees(employees: List[Employee]) -> str:
        """
        Format a list of employees as JSON.

        Args:
            employees: List of Employee objects

        Returns:
            JSON string representation of employees
        """
        employees_data = []
        for emp in employees:
            emp_dict = {
                "employeeId": emp.employee_id,
                "firstName": emp.first_name,
                "lastName": emp.last_name,
                "employmentDate": emp.employment_date.strftime("%Y-%m-%d"),
                "yearlySalary": round(emp.yearly_salary, 2),
            }

            if emp.pension_plan is not None:
                emp_dict["pensionPlan"] = {
                    "planReferenceNumber": emp.pension_plan.plan_reference_number,
                    "enrollmentDate": emp.pension_plan.enrollment_date.strftime("%Y-%m-%d"),
                    "monthlyContribution": round(emp.pension_plan.monthly_contribution, 2),
                }
            else:
                emp_dict["pensionPlan"] = None

            employees_data.append(emp_dict)

        return json.dumps(employees_data, indent=2)

    @staticmethod
    def format_quarterly_upcoming_enrollees(employees: List[Employee]) -> str:
        """
        Format a list of employees as a quarterly upcoming enrollees report in JSON.

        Args:
            employees: List of Employee objects

        Returns:
            JSON string representation of the report
        """
        employees_data = []
        for emp in employees:
            emp_dict = {
                "employeeId": emp.employee_id,
                "firstName": emp.first_name,
                "lastName": emp.last_name,
                "employmentDate": emp.employment_date.strftime("%Y-%m-%d"),
                "yearlySalary": round(emp.yearly_salary, 2),
            }
            employees_data.append(emp_dict)

        report = {"quarterlyUpcomingEnrollees": employees_data}
        return json.dumps(report, indent=2)


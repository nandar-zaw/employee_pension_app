from datetime import date
from typing import Optional
from .pension_plan import PensionPlan


class Employee:
    """Represents an employee with pension plan information."""

    def __init__(
        self,
        employee_id: int,
        first_name: str,
        last_name: str,
        employment_date: date,
        yearly_salary: float,
        pension_plan: Optional[PensionPlan] = None,
    ):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.employment_date = employment_date
        self.yearly_salary = yearly_salary
        self.pension_plan = pension_plan


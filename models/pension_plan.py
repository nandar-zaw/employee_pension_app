from datetime import date


class PensionPlan:
    """Represents a pension plan enrolled by an employee."""

    def __init__(self, plan_reference_number: str, enrollment_date: date, monthly_contribution: float):
        self.plan_reference_number = plan_reference_number
        self.enrollment_date = enrollment_date
        self.monthly_contribution = monthly_contribution


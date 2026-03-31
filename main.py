import sys
from services.pension_service import PensionService
from utils.json_formatter import JsonFormatter


def print_all_employees():
    """Print all employees in JSON format."""
    service = PensionService()
    employees = service.get_all_employees()
    output = JsonFormatter.format_employees(employees)
    print("\n" + output + "\n")


def print_quarterly_upcoming_enrollees():
    """Print quarterly upcoming enrollees report in JSON format."""
    service = PensionService()
    employees = service.get_quarterly_upcoming_enrollees()
    output = JsonFormatter.format_quarterly_upcoming_enrollees(employees)
    print("\n" + output + "\n")


def show_menu():
    """Display the CLI menu and handle user input."""
    while True:
        print("=" * 50)
        print("Employee Pension Plans Management System")
        print("=" * 50)
        print("1. Print All Employees")
        print("2. Print Quarterly Upcoming Enrollees Report")
        print("3. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print_all_employees()
        elif choice == "2":
            print_quarterly_upcoming_enrollees()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    show_menu()


from typing import List, Tuple


# Reference for Abbreviations:
# MIG: Monthly Income Generated
# HR: Hourly Rate
# AH: Allocated Hours
# AW: Annual Wage
# MEP: Monthly Employee Profitability
# AEP: Annual Employee Profitability

def compute_annual_employee_wage(
    hourly_rate: float, allocated_hours: float,
) -> float:
    """Compute Annual Employee Wage from Hourly Rate
       and Allocated Hours plus Bonuses from allowances
       and overtime for a single Employee.

    Args:
        hourly_rate (float): Hourly Employee Rate in Currency per Hour.
        allocated_hours (float): Allocated Hours per day for the Employee.

    Raises:
        ValueError: Hourly Rate is Negative.
        ValueError: Allocated Hours doesn't fit a day or negative.

    Returns:
        float: Annual Employee Wage.
    """
    # Check if Hourly Rate is Positive.
    if hourly_rate < 0.00:
        raise ValueError("Hourly Rate must be positive.")
    # Check if Allocated Hours fit a day or is Positive.
    if allocated_hours < 0.0 or allocated_hours > 24.0:
        raise ValueError("Allocated Hours must not",
                         "exceed 24 hours or be negative.")

    # Compute Daily Wage.
    if allocated_hours > 8.0:
        daily_wage = hourly_rate * (8.0 + (allocated_hours - 8.0) * 1.2)
    elif allocated_hours <= 4.0:
        daily_wage = hourly_rate * allocated_hours + 5.00
    else:
        daily_wage = hourly_rate * allocated_hours

    # Computer Yearly Wage. Cannot compute Monthly Wage yet
    # because 4 weeks is not automatically 1 month.
    weekly_wage = daily_wage * 5
    annual_wage = (weekly_wage * 2 + 10) * 26

    return annual_wage


def compute_monthly_employee_profitability(
    monthly_income_generated: float,
    hourly_rate: float,
    allocated_hours: float,
) -> float:
    """Compute Monthly Employee Profitability from the Income
       Generated and Salary of a single Employee.

    Args:
        monthly_income_generated (float): Monthly Income Generated in Currency.
        hourly_rate (float): Hourly Employee Rate in Currency per Hour.
        allocated_hours (float): Allocated Hours per day for the Employee.

    Returns:
        float: Monthly Employee Profitability.
    """
    annual_wage = compute_annual_employee_wage(hourly_rate, allocated_hours)
    monthly_wage = annual_wage / 12
    monthly_employee_profitability = monthly_income_generated - monthly_wage

    return monthly_employee_profitability


def compute_employee_profitability(
    mig_l: List[float], hr_l: List[float], ah_l: List[float]
) -> Tuple[List[float], List[float]]:
    """Compute the Monthly and Annual Profitability of a list
       of Employees given the Monthly Income Generated

    Args:
        mig_l (List[float]): Monthly Income Generated for each Employee in
                             Currency.
        hr_l (List[float]): Hourly Rate for each Employee in Currency per
                            Hour.
        ah_l (List[float]): List of Allocated Hours per day for each Employee.

    Raises:
        ValueError: The input lists does not match in length.

    Returns:
        List[float]: List of Monthly Employee Profitability.
        List[float]: List of Annual Employee Profitability.
    """
    # Check if the lists match in length.
    if not(len(mig_l) == len(hr_l) == len(ah_l)):
        raise ValueError("Input Lists does not match.")

    monthly_employee_profitability = [
        compute_monthly_employee_profitability(mig, hr, ah)
        for mig, hr, ah in zip(mig_l, hr_l, ah_l)
    ]
    annual_employee_profitability = [
        mep * 12 for mep in monthly_employee_profitability
    ]

    return monthly_employee_profitability, annual_employee_profitability


if __name__ == "__main__":
    # Simple Test Cases
    test_cases = {
        # Case Name                      MIG      HR    AH
        "Unpaid Intern":               (0.00,   0.00,  4.0),
        "Fresh Hire":                  (0.00,   7.25,  8.0),
        "Hardworking Fresh Hire":   (2000.00,   7.25,  9.5),
        "Midlevel Employee":        (6000.00,  15.00,  9.0),
        "Quiet Quitting Employee":  (2334.59,  15.25,  7.0),
        "Kleptomaniac Employee":    (-500.00,  15.25,  7.0),
        "Senior Consultant":       (10000.00, 140.00,  4.0),
        "Nepo Baby Consultant":        (0.00, 140.00, 12.0),
    }
    test_mig = [info[0] for info in test_cases.values()]
    test_hr = [info[1] for info in test_cases.values()]
    test_ah = [info[2] for info in test_cases.values()]

    test_mep, test_aep = compute_employee_profitability(
        test_mig, test_hr, test_ah
    )

    # Display the results.
    CURRENCY = "$"
    def money_str(value: float) -> str:
        money_str = f"{CURRENCY}{abs(value):.2f}"
        return f"-{money_str}" if value < 0.00 else money_str

    for i, (key, value) in enumerate(test_cases.items()):
        print(
            f"For the {key} who earns {money_str(value[0])} for the Company,",
            f"is paid {money_str(value[1])} per hour, and works for",
            f"{value[2]:.1f} hours a day, he/she earns the company",
            f"{money_str(test_mep[i])} monthly and",
            f"{money_str(test_aep[i])} annually.\n"
        )

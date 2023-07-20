from challenge_2 import (
    compute_employee_profitability,
    compute_monthly_employee_profitability,
    compute_annual_employee_wage
)
from unittest import TestCase


TEST_CASES = (
    #     MIG      HR    AH        MEP         AEP         AW
    (    0.00,   0.00,  4.0,   -130.00,   -1560.00,   1560.00),
    (    0.00,   7.25,  8.0,  -1278.33,  -15340.00,  15340.00),
    ( 2000.00,   7.25,  9.5,    438.92,    5267.00,  18733.00),
    ( 6000.00,  15.00,  9.0,   2988.33,   35860.00,  36140.00),
    ( 2334.59,  15.25,  7.0,      0.01,       0.08,  28015.00),
    ( -500.00,  15.25,  7.0,  -2834.58,  -34015.00,  28015.00),
    (10000.00, 140.00,  4.0,  -2263.33,  -27160.00, 147160.00),
    (    0.00, 140.00, 12.0, -38848.33, -466180.00, 466180.00),
)


class TestComputeEmployeeProfitability(TestCase):
    def setUp(self):
        self.test_func = compute_employee_profitability

    def test_success_compute(self):
        test_mig = [case[0] for case in TEST_CASES]
        test_hr = [case[1] for case in TEST_CASES]
        test_ah = [case[2] for case in TEST_CASES]
        test_mep = [case[3] for case in TEST_CASES]
        test_aep = [case[4] for case in TEST_CASES]

        res_mep, res_aep = self.test_func(
            test_mig, test_hr, test_ah
        )

        for t_mep, t_aep, r_mep, r_aep in zip(
            test_mep, test_aep, res_mep, res_aep
        ):
            self.assertAlmostEqual(t_mep, r_mep, places=2)
            self.assertAlmostEqual(t_aep, r_aep, places=2)

    def test_error_input_list_not_matching(self):
        test_mig = [0.00, 0.00, 0.00]
        test_hr = [0.00, 0.00, 0.00, 0.00]
        test_ah = [0.0, 0.0, 0.0]
        with self.assertRaises(ValueError) as exception_context:
            self.test_func(test_mig, test_hr, test_ah)
            self.assertEqual(
                str(exception_context.exception),
                "Input Lists does not match.",
            )

    def test_hourly_rate_is_negative(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func([0.00], [-1.00], [0.0])
            self.assertEqual(
                str(exception_context.exception),
                "Hourly Rate must be positive.",
            )

    def test_allocated_hours_exceed_24_hours(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func([0.00], [0.00], [25.0])
            self.assertEqual(
                str(exception_context.exception),
                "Allocated Hours must not exceed 24 hours or be negative.",
            )

    def test_allocated_hours_is_negative(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func([0.00], [0.00], [-5.0])
            self.assertEqual(
                str(exception_context.exception),
                "Allocated Hours must not exceed 24 hours or be negative.",
            )


class TestComputeMonthlyEmployeeProfitability(TestCase):
    def setUp(self):
        self.test_func = compute_monthly_employee_profitability

    def test_success_compute(self):
        test_mig = [case[0] for case in TEST_CASES]
        test_hr = [case[1] for case in TEST_CASES]
        test_ah = [case[2] for case in TEST_CASES]
        test_mep = [case[3] for case in TEST_CASES]

        for t_mig, t_hr, t_ah, t_mep in zip(
            test_mig, test_hr, test_ah, test_mep
        ):
            self.assertAlmostEqual(
                self.test_func(t_mig, t_hr, t_ah), t_mep, places=2
            )

    def test_hourly_rate_is_negative(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func(0.00, -1.00, 0.0)
            self.assertEqual(
                str(exception_context.exception),
                "Hourly Rate must be positive.",
            )

    def test_allocated_hours_exceed_24_hours(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func(0.00, 0.00, 25.0)
            self.assertEqual(
                str(exception_context.exception),
                "Allocated Hours must not exceed 24 hours or be negative.",
            )

    def test_allocated_hours_is_negative(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func(0.00, 0.00, -5.0)
            self.assertEqual(
                str(exception_context.exception),
                "Allocated Hours must not exceed 24 hours or be negative.",
            )


class TestComputeAnnualEmployeeWage(TestCase):
    def setUp(self):
        self.test_func = compute_annual_employee_wage

    def test_success_compute(self):
        test_hr = [case[1] for case in TEST_CASES]
        test_ah = [case[2] for case in TEST_CASES]
        test_aw = [case[5] for case in TEST_CASES]

        for t_hr, t_ah, t_aw in zip(
            test_hr, test_ah, test_aw
        ):
            self.assertAlmostEqual(
                self.test_func(t_hr, t_ah), t_aw, places=2
            )

    def test_hourly_rate_is_negative(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func(-1.00, 0.0)
            self.assertEqual(
                str(exception_context.exception),
                "Hourly Rate must be positive.",
            )

    def test_allocated_hours_exceed_24_hours(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func(0.00, 25.0)
            self.assertEqual(
                str(exception_context.exception),
                "Allocated Hours must not exceed 24 hours or be negative.",
            )

    def test_allocated_hours_is_negative(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_func(0.00, -5.0)
            self.assertEqual(
                str(exception_context.exception),
                "Allocated Hours must not exceed 24 hours or be negative.",
            )
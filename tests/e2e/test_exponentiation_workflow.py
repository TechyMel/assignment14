import pytest
import requests
from uuid import uuid4


@pytest.mark.e2e
def test_exponentiation_calculation_workflow(page, fastapi_server):
    """
    End-to-end test of the exponentiation feature through the real UI:
    log in, select "Exponentiation", enter inputs, click Calculate, and
    confirm the displayed result.
    """
    base_url = fastapi_server.rstrip("/")

    # Register a fresh user via the API so the test is self-contained.
    user_data = {
        "first_name": "Playwright",
        "last_name": "Exponent",
        "email": f"pw.exp{uuid4()}@example.com",
        "username": f"pw_exp_{uuid4()}",
        "password": "SecurePass123!",
        "confirm_password": "SecurePass123!",
    }
    reg_response = requests.post(f"{base_url}/auth/register", json=user_data)
    assert reg_response.status_code == 201, f"Registration failed: {reg_response.text}"

    # Log in through the actual login form.
    page.goto(f"{base_url}/login")
    page.fill('#username', user_data["username"])
    page.fill('#password', user_data["password"])
    page.click('#loginForm button[type="submit"]')

    page.wait_for_url(f"{base_url}/dashboard", timeout=10000)

    # Select "Exponentiation", enter inputs, and submit the calculation form.
    page.select_option('#calcType', 'exponentiation')
    page.fill('#calcInputs', '2, 3')
    page.click('#calculationForm button[type="submit"]')

    # Confirm the success alert reports the correct result.
    page.wait_for_selector('#successAlert:not(.hidden)', timeout=10000)
    success_text = page.inner_text('#successMessage')
    assert 'Calculation complete: 8' in success_text, f"Unexpected success message: {success_text}"

    # Confirm the new row appears in the calculation history table.
    page.wait_for_selector('#calculationsTable tr', timeout=10000)
    table_text = page.inner_text('#calculationsTable')
    assert 'exponentiation' in table_text.lower(), f"Table did not show exponentiation row: {table_text}"

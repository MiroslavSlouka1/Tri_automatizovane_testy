import pytest
from playwright.sync_api import Page, expect


# Test zobrazení title
def test_title(page: Page):
    page.goto("https://engeto.cz/")
    expected_title = "Kurzy programování a dalších IT technologií | ENGETO"
    expect(page).to_have_title(expected_title)


# Test click na cookies
def test_cookies_click(page: Page):
    page.goto("https://engeto.cz/")
    page.click("#cookiescript_accept")
    expect(page.locator("#cookiescript_injected")).to_be_hidden()


# Test zadání špatného mailu
def test_bad_mail_input(page: Page):
    page.goto("https://engeto.cz/")

    # Cookies
    accept_button = page.locator("#cookiescript_accept")
    if accept_button.is_visible():
        accept_button.click()

    # Neplatný email
    email_input = page.get_by_placeholder("Zadej svůj e-mail")
    expect(email_input).to_be_visible()
    email_input.fill("1111")

    # Klik na "Odebírat"
    subscribe_button = page.get_by_role("link", name="Odebírat")
    expect(subscribe_button).to_be_visible()
    subscribe_button.click()

    # Ověření chybové hlášky
    error_message = page.locator("span.error-message")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Prosím zadejte validní emailovou adresu")

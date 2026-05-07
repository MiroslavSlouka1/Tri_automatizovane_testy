from playwright.sync_api import Page, expect, sync_playwright
import pytest


@pytest.fixture(scope="session")
def custom_page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        yield page

# Test zobrazeni title
def test_title(custom_page):
    custom_page.goto("https://engeto.cz/")
    expected_title = "Kurzy programování a dalších IT technologií | ENGETO"
    expect(custom_page).to_have_title(expected_title)

# Test click na cookis
def test_cookisclick(custom_page):
    custom_page.goto("https://engeto.cz/")
    custom_page.click("#cookiescript_accept")
    expect(custom_page.locator("#cookiescript_injected")).to_be_hidden()



# Test zadani spatneho mailu
def test_bad_mail_input(custom_page):
    custom_page.goto("https://engeto.cz/")

    # Cookies
    accept_button = custom_page.locator("#cookiescript_accept")
    if accept_button.is_visible():
        accept_button.click()

    # Neplatný email
    email_input = custom_page.get_by_placeholder("Zadej svůj e-mail")
    expect(email_input).to_be_visible()
    email_input.fill("1111")

    # Klik na "Odebírat" 
    subscribe_button = custom_page.get_by_role("link", name="Odebírat")
    expect(subscribe_button).to_be_visible()
    subscribe_button.click()

    # Ověření chybové hlášky
    error_message = custom_page.locator("span.error-message")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text(
        "Prosím zadejte validní emailovou adresu"
    )
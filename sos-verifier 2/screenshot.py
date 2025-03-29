from playwright.sync_api import sync_playwright
import os

def capture_screenshot(business_name, state, opportunity_id):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            if state.upper() == 'CA':
                page.goto('https://bizfileonline.sos.ca.gov/search/business')
                page.fill('input[placeholder="Search by entity name"]', business_name)
                page.press('input[placeholder="Search by entity name"]', 'Enter')
                page.wait_for_timeout(3000)  # wait for results
                page.screenshot(path=f'{opportunity_id}_sos.png')
            else:
                print(f'Unsupported state: {state}')
                return False

            browser.close()
        return True
    except Exception as e:
        print(f'Error: {e}')
        return False


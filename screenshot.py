from playwright.async_api import async_playwright
import asyncio

async def capture_screenshot(business_name, state, opportunity_id):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            if state.upper() == 'CA':
                await page.goto("https://bizfileonline.sos.ca.gov/search/business")
                await page.fill('input[placeholder="Search by entity name"]', business_name)
                await page.press('input[placeholder="Search by entity name"]', "Enter")
                await page.wait_for_timeout(3000)
                await page.screenshot(path=f"{opportunity_id}_sos.png")
            else:
                print(f"Unsupported state: {state}")
                return False

            await browser.close()
            return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False



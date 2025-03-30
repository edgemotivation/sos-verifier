from playwright.async_api import async_playwright
import asyncio
import base64
import os

async def capture_screenshot(business_name, state, opportunity_id):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            context = await browser.new_context()
            page = await context.new_page()
            page.set_default_timeout(20000)  # global timeout = 20 seconds

            if state.upper() == 'CA':
                await page.goto("https://bizfileonline.sos.ca.gov/search/business")

                # Wait for the search input to load before interacting
                await page.wait_for_selector('input[placeholder="Search by entity name"]', timeout=15000)

                await page.fill('input[placeholder="Search by entity name"]', business_name)
                await page.press('input[placeholder="Search by entity name"]', "Enter")

                # Wait for results or at least loading to finish
                await page.wait_for_timeout(3000)

                filename = f"{opportunity_id}_sos.png"
                await page.screenshot(path=filename)

                await browser.close()
            else:
                print(f"Unsupported state: {state}")
                return None

        # Convert the screenshot to base64
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        os.remove(filename)
        return encoded_string

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


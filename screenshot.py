from playwright.async_api import async_playwright
import asyncio
import base64
import os

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
                filename = f"{opportunity_id}_sos.png"
                await page.screenshot(path=filename)
            else:
                print(f"Unsupported state: {state}")
                return None

            await browser.close()

        # Read and encode file
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        os.remove(filename)
        return encoded_string

    except Exception as e:
        print(f"Error: {str(e)}")
        return None



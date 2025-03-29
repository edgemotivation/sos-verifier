from fastapi import FastAPI, Request
from screenshot import capture_screenshot

app = FastAPI()

@app.post('/screenshot')
async def run_screenshot(req: Request):
    data = await req.json()
    business_name = data.get('businessName')
    state = data.get('state')
    opportunity_id = data.get('opportunityId')

    if not business_name or not state or not opportunity_id:
        return {'error': 'Missing required fields'}

    result = capture_screenshot(business_name, state, opportunity_id)
    return {'status': 'success' if result else 'failure'}


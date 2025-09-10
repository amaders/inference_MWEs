import json


def get_price(response):
    with open("models_response.json") as f:
        models = json.load(f)['data']
    pricing = next(m['pricing'] for m in models if m['id'] == response.json()['model'])
    pt, ct = response.json()['usage']['prompt_tokens'], response.json()['usage']['completion_tokens']
    total_cost = pt * float(pricing['prompt']) + ct * float(pricing['completion'])
    return f"${total_cost:.8f}"
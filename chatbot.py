responses = {

    "solar": "Solar energy comes from sunlight.",

    "wind": "Wind energy is generated using wind turbines.",

    "renewable": "Renewable energy includes solar, wind and hydro power.",

    "sdg 7": "SDG 7 means Affordable and Clean Energy."
}

def chatbot_response(user_input):

    user_input = user_input.lower()

    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    return "Please ask about solar, wind, renewable energy or SDG 7."
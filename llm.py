import guidance
import json
from guidance import system, user, assistant, models, gen, instruction
from typing import Optional
import os
import multiprocessing

@guidance
def generate_object(
    llm,
    prompt: str
):
    with system():
            llm += """
            You are a helpful assistant that parses text and extracts key information to make a database entry in the form of a JSON object.
            You will be given a text and you will need to extract the following information:
            - company
                This must always be completed and must be a valid company name that is a sponsor of the event.
                Only focus on the primary company in the text.
            - event
                This can be empty if at least one of team, athlete, or sport is completed, but if not it must be a valid event name.
                Use as specific of a name as possible.
                Include the year of the event if possible.
            - team
                This can be empty if at least one of event, athlete, or sport is completed, but if not it must be a valid team name.
            - athlete
                This can be empty if at least one of event, team, or sport is completed, but if not it must be a valid athlete name.
            - sport
                This can be empty if at least one of event, team, or athlete is completed, but if not it must be a valid sport name.
            - year
                This must always be completed and must be a valid year of the beginning of the sponsorship.
            - start_date
                This must always be completed and must be a valid date of the beginning of the sponsorship.
                Use the format YYYY-MM-DD.
            - end_date
                This may be empty if the sponsorship is ongoing, and must be a valid date of the end of the sponsorship if it is not ongoing.
                Use the format YYYY-MM-DD.

            respond in the following JSON format:
            {{
                "company": "",
                "event": "",
                "team": "",
                "athlete": "",
                "sport": "",
                "year": "",
                "start_date": "",
                "end_date": ""
            }}
            """
    with user():
        llm += prompt
    with assistant():    
        llm += gen('response')
    return llm

def call_openai_api(prompt: str,
                    model: str = "gpt-4o-mini") -> str:
    """
    Makes an API call to OpenAI's API using the guidance package.
    
    Args:
        prompt (str): The input prompt to send to the API
        model (str): The model to use, defaults to gpt-4o-mini
        max_tokens (int, optional): Maximum tokens in the response
        
    Returns:
        str: The response text from the API
    """
    try:
        # Get API key from environment variables
        llm = models.OpenAI(model)
        generation = llm + generate_object(prompt)
        print(generation)
        return json.loads(generation.__str__().split("<|im_start|>assistant")[1])

    except Exception as e:
        print(f"Error calling OpenAI API via guidance: {str(e)}")
        return ""

page = '''
Capitals Announce Capital One As Their First Helmet Entitlement Sponsor
Posted on December 22, 2020 by Harrison Brown
Photo: Sports Business Journal
The Washington Capitals announced that Capital One will be their first helmet advertisement partner for the 2020-21 season. The 2.25” x 3.75” decal will be placed on the left and right side of the helmets.

Players will have advertisements on their helmets to make up for revenue lost during the season as many teams will not be able to host fans for at least the start of the upcoming season.

The New Jersey Devils were the first team to announce their primary helmet ad partner: Prudential.

From The Caps

The Washington Capitals and Capital One announced today a season-long partnership that makes the financial corporation the first company to serve as the Capitals official helmet entitlement partner with the placement of Capital One branding on the team’s helmet.

The helmet will be worn for home and away games, as well as during playoffs and practices throughout the season. The 2.25” x 3.75” Capital One decal will be positioned on the left and right sides of the helmet.

“Monumental Sports & Entertainment has a long-standing relationship with Capital One, and we are thrilled to add a valuable piece of real estate to their portfolio as the Capitals helmet entitlement partner,” said Jim Van Stone, Monumental Sports & Entertainment President of Business Operations and Chief Commercial Officer. “We are excited to further grow our relationship with Capital One through a unique, first-of-a-kind opportunity in hockey that greatly showcases the brand across local, national and international audiences.”

In addition to becoming the Capitals official helmet entitlement partner, Capital One will serve as the first presenting partner of the Capitals adidas Reverse Retro jersey, which will be worn for select games during the 20-21 season as the Reverse Retro from adidas presented by Capital One.


'''
if __name__ == '__main__':
    multiprocessing.freeze_support()
    print(call_openai_api(page))
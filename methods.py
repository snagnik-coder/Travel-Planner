import numpy as np
import openai
from flask import Flask, redirect, url_for, request, render_template

openai.api_key = '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'

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.template_filter(name='linebreaksbr')
def linebreaksbr_filter(text):
    return text.replace('\n', '<br>')


@app.route('/travel', methods=['GET'])
def travel():
    return render_template("travel.html")


@app.route('/makePlan', methods=['POST'])
def makePlan():
    place = request.form["place"]
    days = request.form["days"]

    prompt = f"Answer in only one word. Yes or No. Is {place} a real place?"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=4000,
        temperature=0.6,
        n=1,
        stop=None
    )

    if response["choices"][0]["text"].strip().lower() == "yes":

        prompt = f"Make me a travel plan for {days} days to {place}. Also, please send the response in UTF-8 charset only"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            temperature=0.6,
            n=1,
            stop=None
        )

        fill_text = response["choices"][0]["text"]
        print(fill_text)
        print(type(fill_text))
        return render_template("travel.html", travel_plan=fill_text)

    else:
        fill_text = "The place you entered does not seem valid. Sorry, I couldn't be of help."

        with open('templates/travel.html', 'r') as file:
            text = file.read()
        text = text.replace("{travel_plan}", fill_text)

        return render_template("travel.html", travel_plan=fill_text)


if __name__ == "__main__":
    app.run(debug=True)

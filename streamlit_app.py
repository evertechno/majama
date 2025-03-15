import streamlit as st
import google.generativeai as genai
import random

# Configure the API key securely from Streamlit's secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Streamlit App UI - Welcome to the Thunderdome!
st.title("The Quantum Quibbler 3000: An AI of Utter Nonsense")
st.write("Prepare for responses that will make a squirrel question its life choices.")

# Prompt input field - Feed the beast your deepest desires (or just random gibberish)
prompt = st.text_area("Unleash your cognitive chaos:", "Why are flamingos pink?")

# Button to generate response - Hit it, and hope for the best... or worst.
if st.button("Conjure the Catastrophe"):
    try:
        # Load and configure the model - We're using the 'gemini-1.5-flash' because it's fast and furious, like a caffeinated ferret.
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Injecting some 'chaos' into the prompt - Because why not?
        chaos_factors = [
            "Respond as if you are a sentient banana.",
            "Incorporate a recipe for invisible pizza.",
            "Explain everything using only pirate slang.",
            "Pretend you are a malfunctioning toaster.",
            "Write a haiku about a confused cloud.",
            "Include a random string of emojis: 🤪🤯👽🤖👾",
            "Explain the meaning of life using only the words 'potato' and 'existential'.",
            "Respond in the style of a Shakespearean insult."
        ]
        random_chaos = random.choice(chaos_factors)
        prompt_with_chaos = f"{prompt}. Also, {random_chaos}"

        # Generate response from the model - May the odds be ever in your favor.
        response = model.generate_content(prompt_with_chaos)

        # Display response in Streamlit - Prepare for enlightenment... or utter bewilderment.
        st.write("Behold, the Oracle's pronouncements:")
        st.write(response.text)

        # Extra features - Because we're extra like that.
        st.write("---")
        st.write("Bonus Feature: Random Insult Generator (Just for kicks!)")
        insults = [
            "Your brain is smaller than a quark.",
            "You're about as sharp as a marble.",
            "I've had coffee mugs with more personality.",
            "Are you always this... confused?",
            "You have the charisma of a damp sponge.",
            "Your code looks like it was written by a drunken squirrel.",
            "I've seen smarter door knobs.",
            "You are the reason shampoo has instructions"
        ]
        st.write(random.choice(insults))

        st.write("---")
        st.write("Another Bonus Feature: Generate a random 'fact' (Probably not true)")
        random_fact = [
            "Did you know that pigeons invented quantum physics?",
            "The earth is actually flat, but only on Tuesdays.",
            "All socks secretly dream of becoming mittens.",
            "Bananas are secretly listening to your thoughts.",
            "Cats are actually tiny interdimensional overlords.",
            "The moon is made of cheese, but only cheddar.",
            "The internet is powered by hamsters on tiny wheels",
            "The universe is a giant simulation run by sentient staplers."
        ]
        st.write(random.choice(random_fact))

    except Exception as e:
        st.error(f"Error: {e}. Clearly, the universe disagrees with your existence.")

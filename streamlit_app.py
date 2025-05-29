


import streamlit as st
import speech_recognition as sr

# Set page configuration
st.set_page_config(page_title="Project Madhulika", page_icon="🌙", layout="wide")

# Custom CSS to hide Streamlit header/menu/footer for a cleaner look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("🌙 Project Madhulika")

# --- Global Resources Dictionary ---
resources = {
    "Emergency Services": {
        "Global": [
            ("112", "Universal emergency number in many countries.", "https://en.wikipedia.org/wiki/112_(emergency_telephone_number)"),
            ("911", "Emergency number in the USA and Canada.", "https://en.wikipedia.org/wiki/9-1-1"),
            ("999", "Emergency number in the UK and several other countries.", "https://en.wikipedia.org/wiki/999_(emergency_telephone_number)")
        ]
    },
    "Mental Health Support": {
        "Global": [
            ("7 Cups", "Free online text chat with trained listeners.", "https://www.7cups.com/"),
            ("IMAlive", "Online crisis chat service.", "https://www.imalive.org/"),
            ("Headspace", "Meditation and mindfulness app.", "https://www.headspace.com/")
        ]
    },
    "Legal Assistance": {
        "Global": [
            ("International Justice Mission", "Protecting people in poverty from violence.", "https://www.ijm.org/"),
            ("Legal Aid Services", "Directory of legal aid providers worldwide.", "https://www.hg.org/legal-aid.html")
        ]
    },
    "Medical Services": {
        "Global": [
            ("Doctors Without Borders", "Medical aid where it's needed most.", "https://www.doctorswithoutborders.org/"),
            ("International Federation of Red Cross", "Humanitarian aid and emergency response.", "https://www.ifrc.org/")
        ]
    },
    "Food Assistance": {
        "Global": [
            ("Feeding America", "Nationwide network of food banks.", "https://www.feedingamerica.org/"),
            ("Action Against Hunger", "Global hunger relief organization.", "https://www.actionagainsthunger.org/")
        ]
    },
    "Shelter Services": {
        "Global": [
            ("ShelterBox", "Emergency shelter for disaster-affected families.", "https://www.shelterbox.org/"),
            ("Habitat for Humanity", "Building homes and communities.", "https://www.habitat.org/")
        ]
    },
    "Educational Resources": {
        "Global": [
            ("Coursera", "Online courses from top universities.", "https://www.coursera.org/"),
            ("edX", "Access to free online courses.", "https://www.edx.org/"),
            ("Khan Academy", "Free online educational resources.", "https://www.khanacademy.org/")
        ]
    },
    "Self-Defense Resources": {
        "Global": [
            ("Guardian Girls International", "Women's self-defense programs.", "https://guardiangirls.org/"),
            ("Women’s Self-Defense Network", "Resources and training programs.", "https://www.wsdn.org/")
        ]
    },
    "Finance": {
        "Global": [
            ("Kiva", "Microloans for entrepreneurs.", "https://www.kiva.org/"),
            ("Grameen Bank", "Microfinance organization.", "http://www.grameen.com/")
        ]
    }
}

# Sidebar: Country and Category Selection
st.sidebar.header("🌍 Select Your Country and Category")
country = st.sidebar.selectbox("Select your country", ["Global", "USA", "UK", "Canada", "Australia"])
category = st.sidebar.selectbox("Select a category", list(resources.keys()))

# Initialize session state for voice input
if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""

# Voice to text input
st.header("🎙️ Speak or type your query")

# Text input
query = st.text_input("Type your question or need here:", value=st.session_state.voice_text)

# Voice input using speech_recognition
if st.button("🎤 Record voice input"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak clearly.")
        try:
            audio = recognizer.listen(source, timeout=5)
            voice_input = recognizer.recognize_google(audio)
            st.session_state.voice_text = voice_input
            st.success(f"You said: {voice_input}")
        except sr.UnknownValueError:
            st.warning("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")

# Display resources based on selection
def display_resources(selected_category, selected_country):
    st.subheader(f"Resources for {selected_category} in {selected_country}")
    country_resources = resources[selected_category].get(selected_country, [])
    global_resources = resources[selected_category].get("Global", [])
    combined_resources = country_resources + global_resources

    if combined_resources:
        for name, description, link in combined_resources:
            st.markdown(f"- **{name}**: {description} [🔗 Link]({link})")
    else:
        st.info("No resources found for the selected category and country.")

# If query is provided, search for matching resources
if query:
    found = False
    for cat, countries in resources.items():
        for ctry, res_list in countries.items():
            for name, description, link in res_list:
                if query.lower() in name.lower() or query.lower() in description.lower():
                    st.subheader(f"Found in {cat} - {ctry}")
                    st.markdown(f"- **{name}**: {description} [🔗 Link]({link})")
                    found = True
    if not found:
        st.warning("No matching resources found. Please try different keywords.")
else:
    display_resources(category, country)


    

   
       
                

        

import streamlit as st

# Set page configuration
st.set_page_config(page_title="Project Madhulika", page_icon="🌙", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("🌙 Project Madhulika: Global Support Resources")

# Define the resources
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
            ("HG Legal Aid Directory", "Directory of legal aid providers worldwide.", "https://www.hg.org/legal-aid.html")
        ]
    },
    "Medical Services": {
        "Global": [
            ("Doctors Without Borders", "Medical aid where it's needed most.", "https://www.doctorswithoutborders.org/"),
            ("International Red Cross", "Humanitarian aid and emergency response.", "https://www.ifrc.org/")
        ]
    },
    "Food Assistance": {
        "Global": [
            ("Action Against Hunger", "Global hunger relief organization.", "https://www.actionagainsthunger.org/"),
            ("Feeding America", "Food bank network (mainly USA).", "https://www.feedingamerica.org/")
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
            ("Coursera", "Free and paid courses from global universities.", "https://www.coursera.org/"),
            ("edX", "Free online courses from top institutions.", "https://www.edx.org/"),
            ("Khan Academy", "Free online learning platform.", "https://www.khanacademy.org/")
        ]
    },
    "Self-Defense Resources": {
        "Global": [
            ("Guardian Girls", "Women's self-defense programs globally.", "https://guardiangirls.org/"),
            ("WSDN", "Women’s Self-Defense Network.", "https://www.wsdn.org/")
        ]
    },
    "Finance": {
        "Global": [
            ("Kiva", "Crowdfunded microloans globally.", "https://www.kiva.org/"),
            ("Grameen Bank", "Microfinance in developing countries.", "http://www.grameen.com/")
        ]
    }
}

# Sidebar: Select country and category
st.sidebar.header("🌍 Where are you and what do you need?")
country = st.sidebar.selectbox("Select your region", ["Global"])
category = st.sidebar.selectbox("Select a category", list(resources.keys()))

# Input section
st.header("💬 Ask for help (type your issue or keywords)")
query = st.text_input("You can type or paste speech-to-text input here:")

# Show relevant resources based on category
def show_resources(category_name, region_name="Global"):
    st.subheader(f"Resources for {category_name}")
    entries = resources.get(category_name, {}).get(region_name, [])
    if entries:
        for name, desc, link in entries:
            st.markdown(f"- **{name}**: {desc} [🔗 Link]({link})")
    else:
        st.info("No resources found for this category and region.")

# Keyword matching
if query:
    st.subheader("🔍 Search Results")
    found = False
    for cat, cat_data in resources.items():
        for region, res_list in cat_data.items():
            for name, desc, link in res_list:
                if query.lower() in name.lower() or query.lower() in desc.lower():
                    st.markdown(f"**Category**: {cat}  \n- **{name}**: {desc} [🔗 Link]({link})")
                    found = True
    if not found:
        st.warning("No matching resources found. Try different keywords.")
else:
    show_resources(category, country)




       
                

        

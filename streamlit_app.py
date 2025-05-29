import streamlit as st
import geocoder
import re
import speech_recognition as sr

# Set page config with your moon logo and baby pink theme colors applied in .streamlit/config.toml
st.set_page_config(page_title="Project Madhulika", page_icon="your_logo.png", layout="wide")

# Custom CSS to hide Streamlit header/menu/footer for a cleaner look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Title with moon emoji
st.title("🌙 Project Madhulika")

# --- Resources dictionary ---
resources = {
    "📞 Emergency Services": [
        ("SAPS Emergency", "Dial 10111 for police emergencies.", "https://www.saps.gov.za/talk/talk.php"),
        ("Ambulance Services", "Dial 10177 for medical emergencies.", "https://trekmedics.org/database/south_africa/"),
        ("Childline South Africa", "24/7 support at 0800 55 555.", "https://www.childlinesa.org.za/contact-us/"),
        ("National GBV Command Centre", "Call 0800 428 428 or use *120*7867#.", "https://gbv.org.za/about-us/")
    ],
    "🧠 Mental Health Support": [
        ("SADAG", "24/7 helpline at 0800 567 567.", "https://www.sadag.org/index.php?Itemid=114&id=11&option=com_content&view=article"),
        ("LifeLine Johannesburg", "Counselling services at 0861 322 322.", "https://lifelinesa.co.za/"),
        ("TEARS Foundation", "Support via *134*7355# or call 08000 83277.", "https://tears.co.za/")
    ],
    "⚖️ Legal Assistance": [
        ("Legal Aid South Africa", "Free legal services at 0800 110 110.", "https://legal-aid.co.za/"),
        ("ProBono.Org Johannesburg", "Access to pro bono lawyers at 011 339 6080.", "https://probono.org.za/contact/"),
        ("Women’s Legal Centre", "Legal support for gender justice.", "https://wlce.co.za/"),
        ("Lawyers Against Abuse (LvA)", "Legal and psychosocial support at 072 031 1840.", "https://lva.org.za/"),
        ("Black Sash", "Paralegal support at 072 663 3739.", "https://paralegaladvice.org.za/"),
        ("Advice Desk for the Abused", "Legal advice and support.", "https://www.facebook.com/p/Advice-Desk-for-the-Abused-100067114147271/"),
        ("Gender Equity Office (University of Pretoria)", "GBV legal support.", "https://www.chr.up.ac.za/units/womens-rights-unit")
    ],
    "🏥 Medical Services": [
        ("Charlotte Maxeke Hospital", "Contact at 011 488 4911.", "https://www.wits.ac.za/clinicalmed/departments/paediatrics-and-child-health/contact-us/charlotte-maxeke-johannesburg-academic-hospital/"),
        ("Hillbrow Community Health Centre", "Local health services.", "https://joburg.org.za/services_/Pages/Emergency-Services.aspx"),
        ("Marie Stopes South Africa", "Reproductive health services.", "https://www.mariestopes.org.za/"),
        ("AIDS Helpline", "Support at 0800 012 322.", "https://lifelinesa.co.za/"),
        ("Anova Health Institute", "Health services and support.", "https://www.anovahealth.co.za/"),
        ("Dignity Dreams Pads Distribution", "Access to sanitary products.", "https://dignitydreams.com/"),
        ("The Pad Princess SA", "Free pads distribution.", "https://thepadprincess.co.za/")
    ],
    "🍲 Food Assistance": [
        ("FoodForward SA", "Food distribution services.", "https://foodforwardsa.org/"),
        ("Community Food Kitchens", "Available in Yeoville & Braamfontein.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"),
        ("Ladles of Love", "Contact at 071 747 7311.", "https://ladlesoflove.org.za/")
    ],
    "🏠 Shelter Services": [
        ("People Opposing Women Abuse (POWA)", "Support services. Call 011 642 4345/6", "https://www.powa.co.za/"),
        ("Frida Hartley Shelter", "Support for women and children.", "https://fridahartley.org/"),
        ("Ikhaya Lethemba Women’s Shelter", "Contact at 011 242 2530.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"),
        ("Bethany Home for Abused Women", "Contact at 011 614 3245.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"),
        ("National Shelter Movement of South Africa (NSMSA)", "Contact at 0800 001 005 or 082 057 8600.", "https://nationalshelter.co.za/")
    ],
    "📚 Educational Resources": [
        ("FunDza Literacy Trust", "Free online reading resources.", "https://www.fundza.co.za/"),
        ("UJ Adult Learning Centre", "Literacy and numeracy programs.", "https://www.uj.ac.za/faculties/education/adult-education/"),
        ("Coursera Free Courses", "Various online courses.", "https://www.coursera.org/"),
        ("GirlCodeZA", "Coding bootcamps for women.", "https://girlcode.co.za/"),
        ("dorKk", "South African school curriculum video lessons.", "https://www.dorkk.online/"),
        ("Learn the Net", "Basic computer and internet skills.", "http://www.learnthenet.com/"),
        ("YALI Network", "Courses on leadership and business.", "https://yali.state.gov/"),
        ("Women Techmakers (Google)", "Tech talks and resources.", "https://www.womentechmakers.com/")
    ],
    "🛡️ Self-Defense Resources": [
        ("Mothers Against Crime", "Community safety and self-defense workshops.", "https://mothersagainstcrime.co.za/"),
        ("Women's Safety and Self-Defense Classes", "Find local self-defense classes and resources.", "https://www.selfdefense.co.za/"),
        ("SAPS Crime Prevention", "Police advice and safety tips for personal protection.", "https://www.saps.gov.za/services/crime_prevention.php"),
        ("Watch this", "Basic self-defense tutorial", "https://www.youtube.com/watch?v=kWPXXPNN9Ts")
    ],
    "💵 Finance": [
        ("Women’s Development Bank", "", "https://www.wdb.co.za/"),
        ("South African Social Security Agency (SASSA)", "Social grants", "https://www.sassa.gov.za/"),
        ("Unemployment Insurance Fund (UIF)", "", "https://www.labour.gov.za/uif"),
        ("FNB eWallet (No bank account needed)", "Mobile money transfer", "https://www.online.fnb.co.za/send-money/eWallet.html"),
        ("Learn how to grow a business", "Goldman Sachs 10,000 Women (Free on Coursera)", "https://www.coursera.org/collections/goldman-sachs-10000-women")
    ]
}

# Sidebar: Filter category
category_filter = st.sidebar.selectbox("Filter by category", ["All"] + list(resources.keys()))

# Sidebar: Location detection
st.sidebar.markdown("### 🌍 Detect your city")
if st.sidebar.button("Detect My Location"):
    g = geocoder.ip('me')
    st.session_state.city = g.city if g.city else "Unknown"
    st.sidebar.success(f"Detected city: {st.session_state.city}")

# Voice to text input (using microphone)
st.header("🎙️ Speak or type your query")

if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""

# Microphone button and recognition
recognizer = sr.Recognizer()
mic = sr.Microphone()

try:
    if st.button("🎤 Record voice input"):
        with mic as source:
            st.info("Listening... Please speak clearly.")
            audio = recognizer.listen(source, timeout=5)
            voice_input = recognizer.recognize_google(audio)
            st.session_state.voice_text = voice_input
            st.success(f"You said: {voice_input}")
except Exception as e:
    st.warning(f"Voice recognition error: {e}")

# Text input box to also accept manual queries
query = st.text_input("Or type your question/need here:", value=st.session_state.voice_text)

# Helper: filter and display services
def display_services(services):
    for service in services:
        if len(service) == 3:
            name, description, link = service
            st.markdown(f"- **{name}**: {description} [🔗 Link]({link})")
        else:
            st.markdown(f"- {service}")

# If user types a query, try to find matches using simple keywords
if query and query.strip() != "":
    query_lower = query.lower()

    # Try to find a matching category or keyword in services
    found = False
    for category, services in resources.items():
        # Basic keyword check: category name or services descriptions/names
        if category.lower() in query_lower or any(query_lower in service[0].lower() or query_lower in service[1].lower() for service in services):
            st.subheader(f"🔎 Search results in: {category}")
            display_services(services)
            found = True
            break

    if not found:
        st.warning("No matching service found. Please try different keywords or use the filter.")
else:
    # Show full or filtered resource list
    if category_filter == "All":
        for category, services in resources.items():
            st.subheader(category)
            display_services(services)
    else:
        st.subheader(category_filter)
        services = resources.get(category_filter, [])
        display_services(services)




    

   
       
                

        

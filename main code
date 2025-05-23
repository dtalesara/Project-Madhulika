import streamlit as st

# Page config
st.set_page_config(page_title="Project Madhulika", page_icon="💕", layout="wide")

# Title and description
st.title("🌙 Project Madhulika")
st.markdown("_Empowering women with support, resources, and strength._")

# Sidebar for filtering resource categories
categories = ["All", "Emergency", "Mental Health", "Legal", "Medical", "Food", "Shelter", "Education", "Self-Defense"]
selected_category = st.sidebar.selectbox("Filter resources by category", categories)

# Inputs: location and need
location = st.text_input("Enter your city or region:").strip().lower()
need = st.text_input("What kind of support do you need? (e.g., mental health, shelter)").strip().lower()

# Resource database
resources = {
    "emergency": [
        "📞 SAPS Emergency: 10111",
        "🚑 Ambulance: 10177",
        "Childline SA (24/7 for abuse, rape, trafficking): 0800 055 555",
        "National GBV Command Centre: 0800 428 428 or *120*7867#"
        
    ],
    "mental health": [
        "🧠 SADAG (24/7 help): 0800 567 567",
        "🧠 Lifeline Johannesburg: 0861 322 322",
        "🧠 TEARS Foundation 1347355# (free from any mobile phone) or  +27 66 435 3108"
    ],
    "legal": [
        "⚖️ Legal Aid South Africa – Free legal services for low-income individuals: 0800 110 110 | https://www.legal-aid.co.za/",
        "📋 ProBono.Org Johannesburg – Access to pro bono lawyers: 011 339 6080 | https://probono.org.za/",
        "👩‍⚖️ Women’s Legal Centre – Legal support for gender justice: https://wlce.co.za/",
        "🛡️ Lawyers Against Abuse (LvA) – Legal and psychosocial support for GBV survivors (Diepsloot): 010 590 3308 | https://www.lva.org.za/",
        "📱 Black Sash – Paralegal support for social grants and human rights: 072 663 3739 | https://www.blacksash.org.za/",
        "💬 Advice Desk for the Abused – Legal advice, protection orders, support: 011 640 3151 | http://www.advicedesk.org.za/",
        "📑 Gender Equity Office (University of Pretoria) – GBV legal support for students & public: https://www.up.ac.za/genderequity"

       
    ],
    "medical": [
        "🏥 Charlotte Maxeke Hospital: 011 488 4911",
        "🏥 Hillbrow Community Health Centre",
        "🏥 Marie Stopes SA: https://www.mariestopes.org.za/",
        "🧬 AIDS Helpline: 0800 012 322",
        "🧪 Anova Health Institute: https://anovahealth.co.za/",
        "🩸 Dignity Dreams Pads Distribution: https://www.dignitydreams.com/",
        "🩸 The Pad Princess SA (Free pads): https://www.padprincess.co.za/",
        
    ],
    "food": [
        "🍲 FoodForward SA: https://foodforwardsa.org/",
        "🍲 Community food kitchens in Yeoville & Braamfontein",
        "🍲 Ladles of Love 071 747 7311"
    ],
    "shelter": [
        "🏠 Frida Hartley Shelter: https://fridahartley.org.za/",
        "🏠 Ikhaya Lethemba Women’s Shelter: 011 242 2530",
        "🏠 People Opposing Women Abuse (POWA): https://www.powa.co.za/",
        "🏠 Bethany Home for Abused Women  +27 11 614 3245",
        "🏠 National Shelter Movement of South Africa (NSMSA)   0800 001 005 or 082 057 8600"
    ],
    "education": [
        "📚 FunDza Literacy Trust – Free online reading and writing resources: https://fundza.co.za/",
        "🎓 UJ Adult Learning Centre – Literacy, numeracy & high school equivalency: https://www.uj.ac.za/faculties/education/adult-education-centre/",
        "🧵 Learn How to Sew – Free beginner-friendly sewing tutorials: https://learnhowtosew.net/",
        "💻 Coursera Free Courses – Life skills, coding, business & more: https://www.coursera.org/courses?query=free",
        "📱 GirlCodeZA – Coding bootcamps for South African women: https://girlcode.co.za/",
        "📘 dorKk – South African school curriculum video lessons: https://dorkk.online/",
        "📗 Siyavula – Free CAPS-aligned Maths & Science textbooks: https://www.siyavula.com/",
        "👩‍🏫 Learn the Net – Basic computer and internet skills: https://learnthenet.org/",
        "👩‍🎓 YALI Network – Courses on leadership, business, and civic engagement: https://yali.state.gov/courses/",
        "🚀 Women Techmakers (Google) – Online tech talks, resources, and scholarships: https://www.womentechmakers.com/",
        
    
        
    ],
    "self-defense": [
        "🛡️ Women Empowered Self-Defense: https://wesa.org.za/",
        "🛡️ Free Krav Maga classes – JHB inner city Fridays",
        "🛡️ https://www.youtube.com/watch?v=KVpxP3ZZtAc",
        "🛡️ SAPS Victim Empowerment Programme ,0860 10111 (SAPS National Crime Stop) ,https://www.saps.gov.za/",
    ],
   
        "finance" : [
            
            "💵 Women’s Development Bank: https://www.wdb.co.za/",
            "🛡️ South African Social Security Agency (SASSA) – Social grants: https://www.sassa.gov.za/",
            "🛡️ Unemployment Insurance Fund (UIF): https://www.labour.gov.za/uif",
            "📱 FNB eWallet(No bank account needed) – Mobile money transfer: https://www.fnb.co.za/ewallet/index.html",
            "Learn how to grow a business https://www.coursera.org/learn/10k-women-1 or https://www.coursera.org/learn/10k-women-2",
            
            
]
        
}

# Default resources if location unknown
default_resources = {
    "emergency": ["📞 Call local police or emergency line in your country."],
    "mental health": ["🧠 Try Befrienders Worldwide: https://www.befrienders.org/"],
    "legal": ["⚖️ Global Legal Aid Directory: https://www.globallegalaid.org/"],
    "medical": ["🏥 Find a public health clinic nearby via local listings."],
    "food": ["🍲 Try foodpantries.org or local churches/mosques."],
    "shelter": ["🏠 National homeless shelter directory: https://shelterlistings.org/"],
    "education": ["📚 Coursera, Khan Academy, or your local community centre."],
    "self-defense": ["🛡️ Search 'free women self-defense classes near me' on Google."],
}

def get_resources(category, need_filter):
    """Get filtered resources by category and need keyword."""
    if category == "All":
        res_list = []
        for cat_resources in resources.values():
            res_list.extend(cat_resources)
    else:
        res_list = resources.get(category.lower(), [])

    if need_filter:
        res_list = [r for r in res_list if need_filter in r.lower()]

    return res_list if res_list else ["No matching resources found."]

# Display resources section
if location:
    st.markdown(f"### Resources for **{location.capitalize()}**")
    filtered_resources = get_resources(selected_category, need)
    for res in filtered_resources:
        st.markdown(f"- {res}")
else:
    st.info("Please enter your location to view relevant support resources.")

# Show default resources if no specific location resources found or none input
known_locations = ["johannesburg", "cape town", "durban", "pretoria"]
if not location or location.lower() not in known_locations:
    general_resources = get_resources(selected_category, need)
    for res in general_resources:
        st.markdown(f"- {res}")

# Supportive AI-inspired message based on need
if need:
    st.markdown("---")
    st.subheader("A little support just for you 💬")
    if "mental" in need:
        st.write(
            "You're not alone. It’s okay to ask for help — your feelings matter and there are people ready to listen and support you. 💜"
        )
    elif "emergency" in need:
        st.write(
            "If you are in immediate danger, please call emergency services or someone you trust right now. Your safety comes first!"
        )
    elif "legal" in need:
        st.write(
            "Legal issues can be tough. Reach out to professionals or organizations who can guide and protect your rights."
        )
    else:
        st.write(
            "Remember, you are strong, and support is available. Whatever you’re going through, you don’t have to face it alone."
        )

# Footer / encouragement
st.markdown("---")
st.markdown("🌙 **Project Madhulika** — empowering women with support and strength.")

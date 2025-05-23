import streamlit as st
import re

# Page config
st.set_page_config(page_title="Project Madhulika", page_icon="💕", layout="wide")

# Title and description
st.title("🌙 Project Madhulika")
st.markdown("_Empowering women with support, resources, and strength._")

# Categories dictionary (keys should match resource keys)
categories = {
    "all": "All",
    "emergency": "Emergency",
    "mental health": "Mental Health",
    "legal": "Legal",
    "medical": "Medical",
    "food": "Food",
    "shelter": "Shelter",
    "education": "Education",
    "self-defense": "Self-Defense",
    "finance": "Finance",
}

# Sidebar for filtering resource categories
selected_category = st.sidebar.selectbox("Filter resources by category", list(categories.values()))

# Inputs: location and need keyword
location = st.text_input("Enter your city or region:").strip().lower()
need = st.text_input("What kind of support do you need? (e.g., mental health, shelter)").strip().lower()

# Your resource database (as before)
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
        "🧠 TEARS Foundation 1347355# (free from any mobile phone) or +27 66 435 3108"
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
    "finance": [
        "💵 Women’s Development Bank: https://www.wdb.co.za/",
        "🛡️ South African Social Security Agency (SASSA) – Social grants: https://www.sassa.gov.za/",
        "🛡️ Unemployment Insurance Fund (UIF): https://www.labour.gov.za/uif",
        "📱 FNB eWallet(No bank account needed) – Mobile money transfer: https://www.fnb.co.za/ewallet/index.html",
        "Learn how to grow a business https://www.coursera.org/learn/10k-women-1 or https://www.coursera.org/learn/10k-women-2",
    ],
}

known_locations = ["johannesburg", "cape town", "durban", "pretoria"]

# Helper function to convert phone numbers to clickable tel: links in markdown
def make_clickable_phone(text):
    # Regex to find phone numbers (basic pattern)
    pattern = r'(\+?\d[\d\s\-#]*)'
    def replacer(match):
        number = match.group(1).strip().replace(' ', '').replace('-', '')
        # Make clickable tel: link
        return f"[{match.group(1)}](tel:{number})"
    # Replace phone numbers only if preceded by ": " or whitespace
    # We try to avoid changing URLs
    # Also convert URLs to clickable links
    # Convert URLs first:
    url_pattern = r'(https?://[^\s]+)'
    text = re.sub(url_pattern, r'[\1](\1)', text)
    # Then phone numbers:
    return re.sub(pattern, replacer, text)

# Function to get resources based on category + keyword filter
def get_resources(category_key, keyword_filter):
    if category_key == "all":
        res_list = []
        for res in resources.values():
            res_list.extend(res)
    else:
        res_list = resources.get(category_key, [])

    if keyword_filter:
        keywords = keyword_filter.split()
        res_list = [r for r in res_list if all(k in r.lower() for k in keywords)]

    return res_list if res_list else ["No matching resources found."]

# Determine category key from selected category name
def get_key_from_value(val):
    for k, v in categories.items():
        if v == val:
            return k
    return None

category_key = get_key_from_value(selected_category)

# Display resources once, filtered by location and category + need
st.markdown("---")

if location and location.lower() not in known_locations:
    st.warning(f"Resources may be less accurate — '{location}' not in known locations.")

if category_key:
    st.markdown(f"### Support Resources: {categories[category_key]}")

    # Filter resources by category and need keyword
    filtered_resources = get_resources(category_key, need)

    # Optionally: if location is in known locations, show a note
    if location and location.lower() in known_locations:
        st.markdown(f"*Showing resources for {location.capitalize()}.*")

    # Print each resource with clickable phone numbers/URLs
    for res in filtered_resources:
        st.markdown(f"- {make_clickable_phone(res)}")

else:
    st.info("Please select a support category.")

# Show encouraging/supportive message based on need input
if need:
    st.markdown("---")
    st.subheader("A little support just for you 💬")
    if "mental" in need:
        st.write(
            "You're not alone. It’s okay to ask for help — your feelings matter and there are people ready to listen and support you."
        )
    elif "emergency" in need or "danger" in need or "help" in need:
        st.write(
            "If you're in immediate danger, please call emergency services right away. Your safety is the priority."
        )
    else:
        st.write("Stay strong. We're here to support you.")





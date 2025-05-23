


import streamlit as st

# Set page configuration
st.set_page_config(page_title="GBV Support Finder", page_icon=":female-police-officer:", layout="wide")

st.title("🛡️ Gender-Based Violence (GBV) Support Finder")

# Description
st.markdown("""
Welcome to the GBV Support Finder. This tool helps you quickly find contact information for support services across South Africa.
Just select the category of help you need, and we’ll provide relevant resources.
""")

# Select type of support
categories = {
    "emergency": "🚨 Emergency",
    "mental_health": "🧠 Mental Health",
    "legal": "⚖️ Legal Aid",
    "shelter": "🏠 Shelter Services",
    "trauma": "💔 Trauma Counseling",
    "youth": "🧒 Youth Support"
}
selected_category = st.selectbox("What type of support do you need?", list(categories.values()))

# Keyword search bar
need = st.text_input("Search by keyword (e.g., counseling, shelter, abuse):").strip().lower()

# Define support resources
resources = {
    "emergency": [
        "📞 SAPS Emergency: [10111](tel:10111)",
        "🚑 Ambulance: [10177](tel:10177)",
        "📱 Childline SA (24/7 for abuse, rape, trafficking): [0800 055 555](tel:0800055555)",
        "📱 National GBV Command Centre: [0800 428 428](tel:0800428428) or [*120*7867#](tel:*120*7867#)"
    ],
    "mental_health": [
        "📞 Lifeline: [0861 322 322](tel:0861322322) – 24/7 counseling",
        "📱 SADAG Suicide Crisis Line: [0800 567 567](tel:0800567567)",
        "🧠 SADAG WhatsApp Line: [076 882 2775](tel:0768822775)",
        "💬 Therapy Route: therapyroute.com/therapists/za"
    ],
    "legal": [
        "⚖️ Legal Aid SA: [0800 110 110](tel:0800110110)",
        "📧 Legal Resources Centre: info@lrc.org.za",
        "🌐 Lawyers for Human Rights: lhr.org.za/contact",
        "📱 Women's Legal Centre: [021 424 5660](tel:0214245660)"
    ],
    "shelter": [
        "🏠 Saartjie Baartman Centre for Women and Children: [021 633 5287](tel:0216335287)",
        "🚨 NISAA Institute for Women's Development: [011 854 5804](tel:0118545804)",
        "📞 Tshwaranang Shelter Network: [0800 150 150](tel:0800150150)",
        "🛏️ People Opposing Women Abuse (POWA): [011 642 4345](tel:0116424345)"
    ],
    "trauma": [
        "💔 Rape Crisis Cape Town Trust: [021 447 9762](tel:0214479762)",
        "📞 Tears Foundation (24/7): [010 590 5920](tel:0105905920)",
        "📱 National Trauma Helpline: [0800 205 026](tel:0800205026)",
        "🧠 Trauma Centre for Survivors of Violence and Torture: [021 465 7373](tel:0214657373)"
    ],
    "youth": [
        "🧒 Childline SA: [0800 055 555](tel:0800055555)",
        "📱 Teddy Bear Clinic (support for child victims): [011 484 4554](tel:0114844554)",
        "💬 LoveLife Youth Helpline: [0800 121 900](tel:0800121900)",
        "🌍 Youth Against Violence: youthagainstviolence.org.za"
    ]
}

# Get resources based on selection and filter
def get_resources(category_key, keyword_filter):
    res_list = resources[category_key]
    if keyword_filter:
        keywords = keyword_filter.split()
        res_list = [r for r in res_list if all(k in r.lower() for k in keywords)]
    return res_list

# Match category_key from selection
def get_key_from_value(val):
    for k, v in categories.items():
        if v == val:
            return k
    return None

category_key = get_key_from_value(selected_category)

# Display results
if category_key:
    st.markdown(f"### Support Resources: {categories[category_key]}")
    filtered_resources = get_resources(category_key, need)

    if filtered_resources:
        for res in filtered_resources:
            st.markdown(f"- {res}")
    else:
        st.warning("No matching resources found. Try a different keyword.")
else:
    st.info("Please select a support category.")

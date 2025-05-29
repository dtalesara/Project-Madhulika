import streamlit as st
import speech_recognition as sr

# Set page config
st.set_page_config(page_title="Project Madhulika", page_icon="🌙", layout="wide")

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
    "South Africa": {
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
    },
    "United States": {
        "📞 Emergency Services": [
            ("Emergency Services", "Dial 911 for police, fire, or medical emergencies.", "https://www.usa.gov/emergency-services")
        ],
        "🧠 Mental Health Support": [
            ("National Suicide Prevention Lifeline", "Call 988 or 1-800-273-8255 for 24/7 support.", "https://suicidepreventionlifeline.org/"),
            ("Crisis Text Line", "Text HOME to 741741 for 24/7 crisis support.", "https://www.crisistextline.org/"),
            ("The Trevor Project", "Call 1-866-488-7386 or text START to 678678 for LGBTQ+ youth support.", "https://www.thetrevorproject.org/")
        ],
        "⚖️ Legal Assistance": [
            ("Legal Services Corporation", "Find legal aid in your area.", "https://www.lsc.gov/what-legal-aid/find-legal-aid")
        ],
        "🏥 Medical Services": [
            ("HealthCare.gov", "Find health insurance options.", "https://www.healthcare.gov/")
        ],
        "🍲 Food Assistance": [
            ("Feeding America", "Find local food banks.", "https://www.feedingamerica.org/find-your-local-foodbank")
        ],
        "🏠 Shelter Services": [
            ("National Coalition for the Homeless", "Resources for homeless individuals.", "https://nationalhomeless.org/")
        ],
        "📚 Educational Resources": [
            ("Coursera", "Free online courses.", "https://www.coursera.org/"),
            ("edX", "Free online courses from top universities.", "https://www.edx.org/")
        ],
        "🛡️ Self-Defense Resources": [
            ("RAINN", "Support for sexual assault survivors.", "https://www.rainn.org/")
        ],
        "💵 Finance": [
            ("Consumer Financial Protection Bureau", "Resources for financial education.", "https://www.consumerfinance.gov/")
        ]
    },
    "United Kingdom": {
        "📞 Emergency Services": [
            ("Emergency Services", "Dial 999 for police, fire, or medical emergencies.", "https://www.gov.uk/contact-police")
        ],
        "🧠 Mental Health Support": [
            ("Samaritans", "Call 116 123 for 24/7 support.", "https://www.samaritans.org/"),
            ("SHOUT", "Text SHOUT to 85258 for 24/7 crisis support.", "https://giveusashout.org/")
        ],
        "⚖️ Legal Assistance": [
            ("Citizens Advice", "Free legal advice.", "https://www.citizensadvice.org.uk/")
        ],
        "🏥 Medical Services": [
            ("NHS", "National Health Service information.", "https://www.nhs.uk/")
        ],
        "🍲 Food Assistance": [
            ("Tr
::contentReference[oaicite:0]{index=0}
 

       
                

        

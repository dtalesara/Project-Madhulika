
import streamlit as st

st.title("📚 Support Resources")

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
        ("Frida Hartley Shelter", "Support for women and children.", "https://fridahartley.org/"),
        ("Ikhaya Lethemba Women’s Shelter", "Contact at 011 242 2530.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"),
        ("People Opposing Women Abuse (POWA)", "Support services.", "https://www.powa.co.za/"),
        ("Bethany Home for Abused Women", "Contact at 011 614 3245.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"),
        ("National Shelter Movement of South Africa (NSMSA)", "Contact at 0800 001 005 or 082 057 8600.", "https://nationalshelter.co.za/")
    ],
    "📚 Educational Resources": [
        ("FunDza Literacy Trust", "Free online reading resources.", "https://www.fundza.co.za/"),
        ("UJ Adult Learning Centre", "Literacy and numeracy programs.", "https://www.uj.ac.za/faculties/education/adult-education/"),
        ("Learn How to Sew", "Beginner-friendly sewing tutorials.", "https://www.youtube.com/@LearnHowToSew/videos"),
        ("Coursera Free Courses", "Various online courses.", "https://www.coursera.org/"),
        ("GirlCodeZA", "Coding bootcamps for women.", "https://girlcode.co.za/"),
        ("dorKk", "South African school curriculum video lessons.", "https://www.dorkk.online/"),
        ("Siyavula", "Free Maths & Science textbooks.", "https://www.siyavula.com/"),
        ("Learn the Net", "Basic computer and internet skills.", "http://www.learnthenet.com/"),
        ("YALI Network", "Courses on leadership and business.", "https://yali.state.gov/"),
        ("Women Techmakers (Google)", "Tech talks and resources.", "https://www.womentechmakers.com/")
    ]
}

for category, services in resources.items():
    st.subheader(category)
    for name, description, link in services:
        st.markdown(f"- **{name}**: {description} [🔗 Link]({link})")


       
    
   

   


   




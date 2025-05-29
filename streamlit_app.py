


import streamlit as st

st.set_page_config(page_title="Project Madhulika", page_icon="🌙")

# Title and image
st.title("🌙 Project Madhulika") [6]

# Corrected resources dictionary with consistent data structure
resources = {

"📞 Emergency Services": [
("SAPS Emergency", "Dial 10111 for police emergencies.", "https://www.saps.gov.za/talk/talk.php"), [6]
("Ambulance Services", "Dial 10177 for medical emergencies.", "https://trekmedics.org/database/south_africa/"), [6]
("Childline South Africa", "24/7 support at 0800 55 555.", "https://www.childlinesa.org.za/contact-us/"), [6]
("National GBV Command Centre", "Call 0800 428 428 or use *120*7867#.", "https://gbv.org.za/about-us/") [7]
],

"🧠 Mental Health Support": [
("SADAG", "24/7 helpline at 0800 567 567.", "https://www.sadag.org/index.php?Itemid=114&id=11&option=com_content&view=article"), [7]
("LifeLine Johannesburg", "Counselling services at 0861 322 322.", "https://lifelinesa.co.za/"), [7]
("TEARS Foundation", "Support via *134*7355# or call 08000 83277.", "https://tears.co.za/") [7]
],

"⚖️ Legal Assistance": [
("Legal Aid South Africa", "Free legal services at 0800 110 110.", "https://legal-aid.co.za/"), [8]
("ProBono.Org Johannesburg", "Access to pro bono lawyers at 011 339 6080.", "https://probono.org.za/contact/"), [8]
("Women’s Legal Centre", "Legal support for gender justice.", "https://wlce.co.za/"), [8]
("Lawyers Against Abuse (LvA)", "Legal and psychosocial support at 072 031 1840.", "https://lva.org.za/"), [8]
("Black Sash", "Paralegal support at 072 663 3739.", "https://paralegaladvice.org.za/"), [8]
("Advice Desk for the Abused", "Legal advice and support.", "https://www.facebook.com/p/Advice-Desk-for-the-Abused-100067114147271/"), [8]
("Gender Equity Office (University of Pretoria)", "GBV legal support.", "https://www.chr.up.ac.za/units/womens-rights-unit") [9]
],

"🏥 Medical Services": [
("Charlotte Maxeke Hospital", "Contact at 011 488 4911.", "https://www.wits.ac.za/clinicalmed/departments/paediatrics-and-child-health/contact-us/charlotte-maxeke-johannesburg-academic-hospital/"), [9]
("Hillbrow Community Health Centre", "Local health services.", "https://joburg.org.za/services_/Pages/Emergency-Services.aspx"), [9]
("Marie Stopes South Africa", "Reproductive health services.", "https://www.mariestopes.org.za/"), [9]
("AIDS Helpline", "Support at 0800 012 322.", "https://lifelinesa.co.za/"), [3]
("Anova Health Institute", "Health services and support.", "https://www.anovahealth.co.za/"), [3]
("Dignity Dreams Pads Distribution", "Access to sanitary products.", "https://dignitydreams.com/"), [3]
("The Pad Princess SA", "Free pads distribution.", "https://thepadprincess.co.za/") [3]
],

"🍲 Food Assistance": [
("FoodForward SA", "Food distribution services.", "https://foodforwardsa.org/"), [3]
("Community Food Kitchens", "Available in Yeoville & Braamfontein.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"), [4]
("Ladles of Love", "Contact at 071 747 7311.", "https://ladlesoflove.org.za/"), [4]
# The duplicate entry for FoodForward SA has been removed here. [4]
],

"🏠 Shelter Services": [
("People Opposing Women Abuse (POWA)", "Support services.", "011 642 4345/6"), [4]
("Frida Hartley Shelter", "Support for women and children.", "https://fridahartley.org/"), [10]
("Ikhaya Lethemba Women’s Shelter", "Contact at 011 242 2530.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"), [10]
("Bethany Home for Abused Women", "Contact at 011 614 3245.", "https://www.joburg.org.za/services_/Pages/Emergency-Services.aspx"), [10]
("National Shelter Movement of South Africa (NSMSA)", "Contact at 0800 001 005 or 082 057 8600.", "https://nationalshelter.co.za/") [10]
],

"📚 Educational Resources": [
("FunDza Literacy Trust", "Free online reading resources.", "https://www.fundza.co.za/"), [10]
("UJ Adult Learning Centre", "Literacy and numeracy programs.", "https://www.uj.ac.za/faculties/education/adult-education/"), [11]
("Coursera Free Courses", "Various online courses.", "https://www.coursera.org/"), [11]
("GirlCodeZA", "Coding bootcamps for women.", "https://girlcode.co.za/"), [11]
("dorKk", "South African school curriculum video lessons.", "https://www.dorkk.online/"), [11]
("Learn the Net", "Basic computer and internet skills.", "http://www.learnthenet.com/"), [11]
("YALI Network", "Courses on leadership and business.", "https://yali.state.gov/"), [11]
("Women Techmakers (Google)", "Tech talks and resources.", "https://www.womentechmakers.com/") [12]
],

"🛡️ Self-Defense Resources": [
("Mothers Against Crime", "Community safety and self-defense workshops.", "https://mothersagainstcrime.co.za/"), [12]
("Women's Safety and Self-Defense Classes", "Find local self-defense classes and resources.", "https://www.selfdefense.co.za/"), [1]
("SAPS Crime Prevention", "Police advice and safety tips for personal protection.", "https://www.saps.gov.za/services/crime_prevention.php"), [1]
("Watch this", "Basic self-defense tutorial", "https://www.youtube.com/watch?v=kWPXXPNN9Ts") [1]
],

" 💵Finance": [
("💵 Women’s Development Bank", "", "https://www.wdb.co.za/"), # Reformatted [1, 2]
("🛡️ South African Social Security Agency (SASSA)", "Social grants", "https://www.sassa.gov.za/"), # Reformatted [2]
("🛡️ Unemployment Insurance Fund (UIF)", "", "https://www.labour.gov.za/uif"), # Reformatted [2]
("📱 FNB eWallet (No bank account needed)", "Mobile money transfer", "https://www.online.fnb.co.za/send-money/eWallet.html"), # Reformatted [2]
("📈 Learn how to grow a business", "Goldman Sachs 10,000 Women (Free on Coursera)", "https://www.coursera.org/collections/goldman-sachs-10000-women") # Reformatted [2]
]
} # The closing curly brace is not shown in the source for the resources dictionary [1-4, 6-12], but is necessary for valid Python.

# Sidebar filter
category_filter = st.sidebar.selectbox("Filter by category", ["All"] + list(resources.keys())) [2]

if category_filter == "All":
# Show all categories
for category, services in resources.items(): [2]
st.subheader(category) [2]
# Now that data is consistent, we can assume service is always a 3-tuple
for service in services: [2]
name, description, link = service
st.markdown(f"- **{name}**: {description} [🔗 Link]({link})") [2]
else:
# Show only selected category
services = resources.get(category_filter, []) [5]
st.subheader(category_filter) [5]
# Now that data is consistent, we can assume service is always a 3-tuple
for service in services: [5]
name, description, link = service
st.markdown(f"- **{name}**: {description} [🔗 Link]({link})") [5]
        

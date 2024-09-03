import requests
import streamlit as st
from countryinfo import CountryInfo


st.set_page_config(layout="wide")

background_css = """
<style>
    .stApp {
        background-image: url('https://getwallpapers.com/wallpaper/full/d/f/6/664124.jpg');
        background-size: cover;
        background-position: center;
    }
    .content {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
    }

    }
    h1 {
        color: #ff4757; /* Title color */
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
    }

    h3 {
        color: #ff4757;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    h5 {
        color: #1e90ff;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    p {
        color: #2ed573;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    a {
        color: #ffa502;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    .capital {
        color: #ff6347; /* Tomato */
    }
    .currencies {
        color: #00ff80; /* Steel Blue */
    }
    .calling-codes {
        color: #FFFF00; /* Lime Green */
    }
    .population {
        color: #ff4500; /* Orange Red */
    }
    .languages {
        color: #48c9b0; /* Dodger Blue */
    }
    .borders {
        color: #ff69b4; /* Hot Pink */
    }
    .alt-spellings {
        color: #ff1493; /* Deep Pink */
    }
    .area {
        color: #00ced1; /* Dark Turquoise */
    }
    .more-info {
        color: #ff8c00; /* Dark Orange */
    }
</style>
"""


st.markdown(background_css, unsafe_allow_html=True)
st.balloons()
st.markdown("<h1 style='text-align: center; color: orange; font-size: 70px;'>ᴄᴏᴜɴᴛʀʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰɪɴᴅᴇʀ</h1>", unsafe_allow_html=True)




countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde",
    "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo Free State",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia",
    "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
    "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
    "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
    "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea",
    "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
    "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]







custom_input = st.checkbox("𝐄𝐧𝐭𝐞𝐫 𝐚 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 𝐌𝐚𝐧𝐮𝐚𝐥𝐥𝐲")

with st.container():
    if custom_input:
        with st.form(key="country_form"):
            country_name = st.text_input("𝐄𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐍𝐚𝐦𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐂𝐨𝐮𝐧𝐭𝐫𝐲")
            submit_button = st.form_submit_button(label="𝐒𝐮𝐛𝐦𝐢𝐭")
            ##URL = 'https://history.state.gov/countries/all'
            st.markdown(f"<h6 class='more-info'>Countries List: <a href='{URL}'>Click Here..</a></h5>", unsafe_allow_html=True)
    else:
        country_name = st.selectbox("𝐒𝐞𝐥𝐞𝐜𝐭 𝐚 𝐂𝐨𝐮𝐧𝐭𝐫𝐲", ["Select Countries"] + countries)
        submit_button = True

    if submit_button and country_name and country_name != "Select Countries":
        country_info = CountryInfo(country_name)

        try:
            capital = country_info.capital()
            currencies = country_info.currencies()
            populations = country_info.population()
            calling_codes = country_info.calling_codes()
            languages = country_info.languages()
            borders = country_info.borders()
            Regions = country_info.region()
            area = country_info.area()
            wiki_link = country_info.wiki()
            URL = 'https://history.state.gov/countries/all'

            def get_country_flag(country_name):
                url = f"https://restcountries.com/v3.1/name/{country_name}"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    flag_url = data[0]['flags']['svg']
                    return flag_url
                else:
                    return None

            flag_url = get_country_flag(country_name)

            with st.container():
                st.markdown("<div class='content'>", unsafe_allow_html=True)

                if flag_url:
                    st.markdown(
                        f"""
                        <div style='text-align:center'>
                            <img src='{flag_url}' width='190'>
                            <p style='margin-top:10px;'>{country_name} Flag</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    
                else:
                    st.error("Flag not found.")

                formatted_codes = [f"+{code}" for code in calling_codes]

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f"<h3>𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐟𝐨𝐫 {country_name}</h3>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='capital'>ᴄᴀᴘɪᴛᴀʟ: <span>{capital}</span></h5>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='currencies'>ᴄᴜʀʀᴇɴᴄɪᴇꜱ: <span>{', '.join(currencies)}</span></h5>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='calling-codes'>ᴄᴀʟʟɪɴɢ ᴄᴏᴅᴇꜱ: <span>{', '.join(formatted_codes)}</span></h5>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='population'>ᴘᴏᴘᴜʟᴀᴛɪᴏɴ: <span>{populations}</span></h5>", unsafe_allow_html=True)

                with col2:
                    st.markdown("<h3>𝐀𝐝𝐝𝐢𝐭𝐢𝐨𝐧𝐚𝐥 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧</h3>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='languages'>ʟᴀɴɢᴜᴀɢᴇ: <span>{', '.join(languages)}</span></h5>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='borders'>ʙᴏʀᴅᴇʀꜱ: <span>{borders if borders else 'No land borders'}</span></h5>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='alt-spellings'>ʀᴇɢɪᴏɴ: <span>{Regions}</span></h5>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='area'>ᴀʀᴇᴀ: <span>{area} sq km</span></h5>", unsafe_allow_html=True)
                    st.markdown(f"<h5 class='more-info'>ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ: <a href='{wiki_link}'>Wikipedia</a></h5>", unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        except KeyError:
            st.error("Country not found. Please check the spelling and try again.")















import streamlit as st
import requests

api_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
response = requests.get(api_url)
data = response.json()["data"]

card_types = set(card["type"] for card in data)

st.title("Yu-Gi-Oh! Card Explorer")  #1 New
st.image("images/yugioh.jpg", use_column_width=True)
st.write("instructions: Filter down to the specific Yu-Gi-Oh! card that you want for information about the card.")

selected_type = st.selectbox("Filter by Card Type", ["All"] + sorted(card_types))  #2 New

attack_power = st.number_input("Attack Power", min_value=0, value=0) #3 New
defense_power = st.number_input("Defense Power", min_value=0, value=0)

filtered_cards = [
    card for card in data
    if (selected_type == "All" or card["type"] == selected_type) and
       (attack_power is None or card.get('atk', 0) >= attack_power) and
       (defense_power is None or card.get('def', 0) >= defense_power)
]

selected_card = st.selectbox("Select a Yu-Gi-Oh! Card", sorted(set(card["name"] for card in filtered_cards)))

selected_card_data = next((card for card in filtered_cards if card["name"] == selected_card), None)

if selected_card_data:
    st.subheader("Card Details:")
    st.write(f" **Name:** {selected_card_data['name']}")
    st.write(f" **Type:** {selected_card_data['type']}")
    st.write(f" **Attack Power:** {selected_card_data.get('atk', 'N/A')}")
    st.write(f" **Defense Power:** {selected_card_data.get('def', 'N/A')}")
    st.write(" **image:** ")
    st.image(selected_card_data['card_images'][0]['image_url'], caption="Card Image", width=650)








# -*- coding: utf-8 -*-
import streamlit as st
import random

st.set_page_config(page_title="FreeStream Hub Pro", layout="wide")

# Tasarım ve Arama Kutusu Stili
st.markdown("""
    <style>
    .main { background-color: #141414; color: white; }
    .stTextInput>div>div>input { background-color: #333; color: white; border-radius: 10px; }
    .stButton>button { background-color: #E50914; color: white; width: 100%; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 FreeStream Pro: Akıllı İzleme Merkezi")

# --- YENİ: ARAMA ÇUBUĞU ---
arama = st.text_input("🔍 Arşivde Film Ara...", placeholder="Örn: Men in Black")

filmler = [
    {"ad": "Men in Black", "platform": "Tubi", "tur": "Bilim Kurgu"},
    {"ad": "The IT Crowd", "platform": "Pluto TV", "tur": "Komedi"},
    {"ad": "Arrival", "platform": "Tubi", "tur": "Dram/Gizem"},
    {"ad": "Spaceballs", "platform": "YouTube", "tur": "Parodi"},
    {"ad": "Inception", "platform": "Prime", "tur": "Bilim Kurgu"}
]

if arama:
    sonuclar = [f for f in filmler if arama.lower() in f['ad'].lower()]
    if sonuclar:
        for s in sonuclar:
            st.write(f"✅ **{s['ad']}** bulundu! Platform: **{s['platform']}**")
    else:
        st.warning("Bulunamadı, ama listeye ekleyebilirsin!")

st.divider()

# --- ÖNERİ BUTONU ---
if st.button("🎰 Rastgele Film Öner"):
    secilen = random.choice(filmler)
    st.balloons()
    st.info(f"Bugünkü Tercihin: **{secilen['ad']}** ({secilen['platform']})")

# --- İNTERNETE HAZIRLIK: DOSYA OLUŞTURMA ---
st.sidebar.info("💡 Bu uygulamayı internete yüklemek için yanına bir 'requirements.txt' dosyası açmalısın.")
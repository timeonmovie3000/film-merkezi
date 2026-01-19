# -*- coding: utf-8 -*-
import streamlit as st
import random

# Sayfa Ayarları ve Yeni İsim
st.set_page_config(page_title="TimeOnMovie | Akıllı İzleme Merkezi", layout="wide", page_icon="🎬")

# Stil Ayarları (Koyu Tema ve Tasarım)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 20px; border: none; transition: 0.3s; }
    .stButton>button:hover { background-color: #ff1a1a; transform: scale(1.02); }
    .movie-card { background-color: #262730; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# Başlık Bölümü
st.title("🎬 TimeOnMovie")
st.write("---")

# Veritabanı (Burayı dilediğin kadar büyütebilirsin)
filmler = [
    {"ad": "Men in Black", "platform": "Tubi", "tur": "Bilim Kurgu"},
    {"ad": "The IT Crowd", "platform": "Pluto TV", "tur": "Komedi"},
    {"ad": "Arrival", "platform": "Tubi", "tur": "Dram"},
    {"ad": "Spaceballs", "platform": "YouTube", "tur": "Komedi"},
    {"ad": "Inception", "platform": "Prime", "tur": "Aksiyon"},
    {"ad": "The Boys", "platform": "Prime", "tur": "Aksiyon"},
    {"ad": "Severance", "platform": "Apple TV", "tur": "Bilim Kurgu"}
]

# --- ÜST BÖLÜM: AKILLI FİLTRELER ---
col1, col2 = st.columns([2, 1])

with col1:
    arama = st.text_input("🔍 Arşivde Film veya Tür Ara...", placeholder="Örn: Aksiyon veya Inception")

with col2:
    tur_listesi = ["Hepsi"] + sorted(list(set(f['tur'] for f in filmler)))
    secilen_tur = st.selectbox("🎯 Türe Göre Filtrele", tur_listesi)

# --- FİLM LİSTELEME MANTIĞI ---
st.subheader("📺 İzleme Listesi")

# Arama ve Tür filtresini uygula
filtrelenmis = [f for f in filmler if 
                (arama.lower() in f['ad'].lower() or arama.lower() in f['tur'].lower()) and 
                (secilen_tur == "Hepsi" or f['tur'] == secilen_tur)]

if filtrelenmis:
    for f in filtrelenmis:
        with st.container():
            st.markdown(f"""
            <div class="movie-card">
                <h4>{f['ad']}</h4>
                <p>📍 Platform: <b>{f['platform']}</b> | 🏷️ Tür: <b>{f['tur']}</b></p>
            </div><br>
            """, unsafe_allow_html=True)
else:
    st.warning("Eşleşen bir film bulunamadı.")

# --- ALT BÖLÜM: ŞANSINI DENE ---
st.divider()
if st.button("🎲 Bana Rastgele Bir Şey Öner"):
    onerilen = random.choice(filmler)
    st.balloons()
    st.success(f"Bugünkü şanslı içeriğin: **{onerilen['ad']}**")

# --- YAN PANEL: ZAMAN YÖNETİMİ ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3172/3172658.png", width=100)
    st.header("TimeOnMovie Panel")
    st.write("Zamanını akıllı yönet!")
    limit = st.slider("Günlük Limit", 30, 300, 120)
    st.info(f"Bugün için {limit} dakika hedefledin.")
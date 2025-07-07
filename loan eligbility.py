import streamlit as st

st.set_page_config(page_title="Loan Eligibility Tool", layout="centered")

st.title("🏡 Loan Eligibility Matcher - Ejen Hartanah")
st.caption("Professional tool untuk tapis kelayakan buyer & padan dengan bank")

st.markdown("---")

# Input buyer
st.subheader("🔍 Maklumat Kewangan Buyer")

property_price = st.number_input("Harga Hartanah (RM)", min_value=50000, value=500000, step=10000)
margin = st.slider("Margin Pembiayaan (%)", 70, 100, 90)
tenure = st.slider("Tempoh Pinjaman (Tahun)", 5, 35, 30)

loan_amount = property_price * margin / 100

col1, col2 = st.columns(2)
with col1:
    income = st.number_input("Gaji Bersih Bulanan (RM)", min_value=1000, value=5000, step=100)
with col2:
    commitment = st.number_input("Komitmen Bulanan (RM)", min_value=0, value=1500, step=100)

# Kiraan DSR
dsr = (commitment / income) * 100

# Bank policies (boleh tambah ikut keperluan)
bank_dsr = {
    "Maybank": 70,
    "CIMB": 60,
    "RHB": 65,
    "Ambank": 60,
    "Bank Rakyat": 70,
    "Public Bank": 65,
    "BSN": 60
}

# Logic matching bank
matched = [bank for bank, max_dsr in bank_dsr.items() if dsr <= max_dsr]

st.markdown("---")
st.subheader("📊 Keputusan Padanan Bank")

st.write(f"**DSR Buyer:** {dsr:.2f}%")

if matched:
    st.success("Buyer berpotensi lulus dengan bank berikut:")
    for bank in matched:
        st.markdown(f"- ✅ **{bank}** (DSR ≤ {bank_dsr[bank]}%)")
else:
    st.error("Maaf, DSR terlalu tinggi. Tiada bank padan buat masa ini.")

st.markdown("---")

# Info tambahan
st.caption("💡 Nota: Kadar faedah & polisi DSR mungkin berbeza mengikut masa. Sila semak dengan pegawai bank semasa submission.")
st.markdown("Made with ❤️ untuk ejen hartanah.")

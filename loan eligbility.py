import streamlit as st
import math

st.set_page_config(page_title="Loan Eligibility Tool", layout="centered")

st.title("🏡 Loan Eligibility Matcher - Ejen Hartanah")
st.caption("Versi lengkap dengan kiraan ansuran dan DSR sebenar berdasarkan kadar bank")

st.markdown("---")

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

st.markdown("---")

st.subheader("🏦 Keputusan Kelayakan Bank")

# Senarai bank dan kadar faedah
banks = {
    "CIMB": 3.20,
    "MAYBANK": 3.20,
    "RHB": 3.10,
    "MBSB": 4.00,
    "B.ISLAM": 3.45,
    "MUAMALAT": 4.20,
    "HONG LEONG": 3.15,
    "RAKYAT": 3.50,
    "ALLIANCE": 3.15,
    "STANDCHART": 3.30,
    "AMBANK": 3.50
}

# Fungsi kira installment
def calculate_installment(P, annual_rate, years):
    r = (annual_rate / 100) / 12
    n = years * 12
    if r == 0:
        return P / n
    return P * r * (1 + r) ** n / ((1 + r) ** n - 1)

# Simulasi bank-bank
results = []
for bank, rate in banks.items():
    installment = calculate_installment(loan_amount, rate, tenure)
    total_commitment = commitment + installment
    dsr = (total_commitment / income) * 100

    result = {
        "Bank": bank,
        "Interest Rate (%)": rate,
        "Installment (RM)": round(installment, 2),
        "Total Commitment (RM)": round(total_commitment, 2),
        "DSR (%)": round(dsr, 2),
        "Status": "APPROVE" if dsr <= 70 else "DECLINE"
    }
    results.append(result)

# Papar hasil
for res in results:
    status_color = "✅" if res["Status"] == "APPROVE" else "❌"
    st.markdown(f"**{status_color} {res['Bank']}**  ")
    st.write(f"Kadar Faedah: {res['Interest Rate (%)']}%  |  Ansuran: RM{res['Installment (RM)']:,}  |  DSR: {res['DSR (%)']:.2f}% → **{res['Status']}**")
    st.markdown("---")

st.caption("💡 Nota: Sila semak dengan bank sebenar kerana kadar faedah dan polisi DSR mungkin berbeza ikut profil buyer.")

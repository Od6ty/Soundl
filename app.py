import streamlit as st
from content import MAHABARATA_TEXT


def init_session_state():
    """Pastikan key penting tersedia di session_state."""
    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""


def login_form():
    """Form login admin sederhana."""
    st.title("Login Admin")
    st.write("Masukkan username dan password untuk masuk sebagai admin.")

    # Untuk contoh sederhana, kredensial dikodekan langsung
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)
    with col1:
        login_clicked = st.button("Login")
    with col2:
        reset_clicked = st.button("Reset")

    if reset_clicked:
        st.session_state.is_authenticated = False
        st.session_state.username = ""
        st.rerun()

    if login_clicked:
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state.is_authenticated = True
            st.session_state.username = username
            st.success("Login berhasil!")
            st.rerun()
        else:
            st.error("Username atau password salah.")


def admin_dashboard():
    """Halaman utama setelah login admin."""
    st.title("Dashboard Admin")
    st.write(f"Halo, **{st.session_state.username}**! Anda berhasil login sebagai admin.")

    st.write("---")
    st.subheader("Contoh Konten Admin")
    st.write(
        "Ini adalah contoh sederhana dashboard admin. "
        "Anda bisa menambahkan fitur lain seperti upload data, "
        "tabel laporan, grafik, dan lain-lain."
    )

    st.write("---")
    st.subheader("Legenda Mahabarata")
    st.write(MAHABARATA_TEXT)

    if st.button("Logout"):
        st.session_state.is_authenticated = False
        st.session_state.username = ""
        st.rerun()


def main():
    st.set_page_config(page_title="Aplikasi Admin Sederhana", page_icon="🔐", layout="centered")
    init_session_state()

    # Sidebar info
    st.sidebar.title("Menu")
    if st.session_state.is_authenticated:
        st.sidebar.success(f"Login sebagai: {st.session_state.username}")
    else:
        st.sidebar.info("Belum login")

    st.sidebar.markdown("---")
    st.sidebar.caption("Contoh aplikasi Streamlit dengan fitur login admin sederhana.")

    # Routing tampilan utama
    if not st.session_state.is_authenticated:
        login_form()
        st.write("---")
        st.subheader("Legenda Mahabarata")
        st.write(MAHABARATA_TEXT)
    else:
        admin_dashboard()


if __name__ == "__main__":
    main()



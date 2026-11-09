from collections import Counter
from html import escape

import streamlit as st


st.set_page_config(
    page_title="Sugar & Sprinkles Candy Shop",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="collapsed",
)


CANDIES = [
    {"number": 1, "name": "Gummy bears", "price": 6.00, "unit": "bag", "art": "bears"},
    {"number": 2, "name": "Strawberry gummies", "price": 5.00, "unit": "bag", "art": "strawberries"},
    {"number": 3, "name": "Cola bottle gummies", "price": 5.00, "unit": "bag", "art": "cola"},
    {"number": 4, "name": "Jelly beans", "price": 4.00, "unit": "cup", "art": "beans"},
]


ARTWORK = {
    "bears": """
    <svg viewBox="0 0 180 150" role="img" aria-label="Pink and golden gummy bears">
      <defs>
        <linearGradient id="bearPink" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#ff9bb5"/><stop offset="1" stop-color="#ec477a"/>
        </linearGradient>
        <linearGradient id="bearGold" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#ffe68c"/><stop offset="1" stop-color="#ffad43"/>
        </linearGradient>
      </defs>
      <ellipse cx="91" cy="132" rx="57" ry="9" fill="#e7b4bb" opacity=".36"/>
      <g transform="translate(16 22) rotate(-9 50 55)">
        <circle cx="27" cy="19" r="12" fill="url(#bearGold)"/>
        <circle cx="67" cy="19" r="12" fill="url(#bearGold)"/>
        <ellipse cx="47" cy="59" rx="30" ry="34" fill="url(#bearGold)"/>
        <ellipse cx="47" cy="37" rx="25" ry="21" fill="url(#bearGold)"/>
        <ellipse cx="23" cy="63" rx="12" ry="22" fill="url(#bearGold)" transform="rotate(25 23 63)"/>
        <ellipse cx="71" cy="63" rx="12" ry="22" fill="url(#bearGold)" transform="rotate(-25 71 63)"/>
        <ellipse cx="34" cy="91" rx="13" ry="18" fill="url(#bearGold)"/>
        <ellipse cx="60" cy="91" rx="13" ry="18" fill="url(#bearGold)"/>
        <ellipse cx="39" cy="35" rx="6" ry="13" fill="#fff4bf" opacity=".35"/>
        <circle cx="39" cy="38" r="2.1" fill="#74403d"/>
        <circle cx="55" cy="38" r="2.1" fill="#74403d"/>
        <ellipse cx="47" cy="46" rx="4" ry="2.7" fill="#df7e53"/>
      </g>
      <g transform="translate(83 28) rotate(10 40 50)">
        <circle cx="31" cy="17" r="10" fill="url(#bearPink)"/>
        <circle cx="65" cy="17" r="10" fill="url(#bearPink)"/>
        <ellipse cx="48" cy="54" rx="26" ry="31" fill="url(#bearPink)"/>
        <ellipse cx="48" cy="34" rx="22" ry="18" fill="url(#bearPink)"/>
        <ellipse cx="27" cy="57" rx="10" ry="19" fill="url(#bearPink)" transform="rotate(22 27 57)"/>
        <ellipse cx="69" cy="57" rx="10" ry="19" fill="url(#bearPink)" transform="rotate(-22 69 57)"/>
        <ellipse cx="37" cy="83" rx="11" ry="16" fill="url(#bearPink)"/>
        <ellipse cx="59" cy="83" rx="11" ry="16" fill="url(#bearPink)"/>
        <ellipse cx="41" cy="32" rx="5" ry="11" fill="#ffd7df" opacity=".45"/>
        <circle cx="41" cy="35" r="1.8" fill="#71354b"/>
        <circle cx="55" cy="35" r="1.8" fill="#71354b"/>
        <ellipse cx="48" cy="42" rx="3.5" ry="2.2" fill="#c65b78"/>
      </g>
    </svg>
    """,
    "strawberries": """
    <svg viewBox="0 0 180 150" role="img" aria-label="Glossy strawberry-shaped gummies">
      <defs>
        <linearGradient id="berryA" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#ff9ba5"/><stop offset=".55" stop-color="#fa5e76"/><stop offset="1" stop-color="#d9345a"/>
        </linearGradient>
        <linearGradient id="berryB" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#ffbdca"/><stop offset="1" stop-color="#ed6385"/>
        </linearGradient>
      </defs>
      <ellipse cx="90" cy="133" rx="56" ry="8" fill="#e7b4bb" opacity=".36"/>
      <g transform="translate(18 23) rotate(-12 45 55)">
        <path d="M48 28 C21 16 14 40 22 65 C28 85 41 104 48 111 C56 103 72 81 77 61 C83 37 71 17 48 28Z" fill="url(#berryA)"/>
        <path d="M48 30 C40 20 28 21 23 27 C33 26 39 32 43 37 C41 24 55 19 62 25 C56 29 53 34 52 39 C64 28 72 32 76 38 C66 35 59 39 53 44Z" fill="#66b77d"/>
        <path d="M34 47 C29 56 32 72 38 80" fill="none" stroke="#ffd1d5" stroke-width="6" stroke-linecap="round" opacity=".44"/>
        <g fill="#ffe28d">
          <ellipse cx="37" cy="54" rx="2" ry="3"/><ellipse cx="57" cy="50" rx="2" ry="3"/>
          <ellipse cx="47" cy="65" rx="2" ry="3"/><ellipse cx="63" cy="69" rx="2" ry="3"/>
          <ellipse cx="35" cy="78" rx="2" ry="3"/><ellipse cx="53" cy="84" rx="2" ry="3"/>
          <ellipse cx="44" cy="98" rx="2" ry="3"/>
        </g>
      </g>
      <g transform="translate(89 31) rotate(12 35 48)">
        <path d="M38 27 C15 16 9 37 15 58 C20 76 31 94 38 101 C45 94 59 76 64 57 C70 36 59 17 38 27Z" fill="url(#berryB)"/>
        <path d="M38 28 C31 19 21 21 17 26 C26 25 31 31 35 36 C34 25 45 21 51 25 C46 29 43 33 42 38 C52 29 60 33 63 38 C55 35 48 39 43 43Z" fill="#78c98c"/>
        <path d="M26 45 C22 53 25 66 29 72" fill="none" stroke="#fff0f2" stroke-width="5" stroke-linecap="round" opacity=".5"/>
        <g fill="#ffe28d">
          <ellipse cx="29" cy="52" rx="1.8" ry="2.6"/><ellipse cx="46" cy="49" rx="1.8" ry="2.6"/>
          <ellipse cx="37" cy="63" rx="1.8" ry="2.6"/><ellipse cx="51" cy="67" rx="1.8" ry="2.6"/>
          <ellipse cx="28" cy="76" rx="1.8" ry="2.6"/><ellipse cx="42" cy="82" rx="1.8" ry="2.6"/>
        </g>
      </g>
    </svg>
    """,
    "cola": """
    <svg viewBox="0 0 180 150" role="img" aria-label="Cola bottle gummies">
      <defs>
        <linearGradient id="colaBottle" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#9b503b"/><stop offset=".45" stop-color="#63342f"/><stop offset="1" stop-color="#3b292b"/>
        </linearGradient>
        <linearGradient id="colaBottle2" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#b96b50"/><stop offset="1" stop-color="#5a302c"/>
        </linearGradient>
      </defs>
      <ellipse cx="91" cy="132" rx="54" ry="8" fill="#d5aaa1" opacity=".36"/>
      <g transform="translate(20 16) rotate(-9 45 60)">
        <path d="M34 12 H59 V33 C59 39 70 43 75 53 C79 61 77 93 74 109 C72 120 64 125 47 125 C30 125 22 120 20 109 C17 93 15 61 19 53 C24 43 34 39 34 33Z" fill="url(#colaBottle)" stroke="#56312e" stroke-width="2"/>
        <path d="M36 15 H56 V32 H36Z" fill="#f8dfb7" opacity=".72"/>
        <path d="M27 56 C23 68 25 91 28 104" fill="none" stroke="#e2aa88" stroke-width="6" stroke-linecap="round" opacity=".38"/>
        <path d="M28 77 Q48 70 69 77 L68 89 Q48 84 29 90Z" fill="#f5d77f"/>
        <path d="M33 79 Q48 76 64 79 L63 84 Q48 82 34 85Z" fill="#d97456"/>
      </g>
      <g transform="translate(94 26) rotate(11 37 55)">
        <path d="M28 10 H49 V28 C49 34 59 38 63 47 C67 54 65 81 62 96 C60 106 53 111 39 111 C25 111 18 106 16 96 C13 81 11 54 15 47 C19 38 28 34 28 28Z" fill="url(#colaBottle2)" stroke="#67382f" stroke-width="2"/>
        <path d="M30 13 H47 V28 H30Z" fill="#f8dfb7" opacity=".7"/>
        <path d="M22 51 C19 63 21 80 24 89" fill="none" stroke="#e9b297" stroke-width="5" stroke-linecap="round" opacity=".4"/>
        <path d="M20 70 Q39 65 59 70 L58 81 Q39 77 21 83Z" fill="#f7df8c"/>
        <path d="M25 72 Q39 69 55 72 L54 77 Q39 75 26 78Z" fill="#d97456"/>
      </g>
    </svg>
    """,
    "beans": """
    <svg viewBox="0 0 180 150" role="img" aria-label="Colorful jelly beans">
      <defs>
        <linearGradient id="beanRed" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ff91a6"/><stop offset="1" stop-color="#ed466b"/></linearGradient>
        <linearGradient id="beanYellow" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff09b"/><stop offset="1" stop-color="#f4ba40"/></linearGradient>
        <linearGradient id="beanBlue" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#91c9ff"/><stop offset="1" stop-color="#557dd8"/></linearGradient>
        <linearGradient id="beanGreen" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#98dfac"/><stop offset="1" stop-color="#41a978"/></linearGradient>
        <linearGradient id="beanPurple" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#c8a7f5"/><stop offset="1" stop-color="#8d63cf"/></linearGradient>
      </defs>
      <ellipse cx="90" cy="132" rx="58" ry="8" fill="#e7b4bb" opacity=".36"/>
      <g stroke="#fff" stroke-opacity=".18" stroke-width="2">
        <ellipse cx="45" cy="48" rx="17" ry="24" transform="rotate(-34 45 48)" fill="url(#beanRed)"/>
        <ellipse cx="91" cy="39" rx="17" ry="24" transform="rotate(22 91 39)" fill="url(#beanYellow)"/>
        <ellipse cx="135" cy="53" rx="17" ry="24" transform="rotate(39 135 53)" fill="url(#beanBlue)"/>
        <ellipse cx="66" cy="88" rx="17" ry="24" transform="rotate(22 66 88)" fill="url(#beanGreen)"/>
        <ellipse cx="111" cy="91" rx="17" ry="24" transform="rotate(-28 111 91)" fill="url(#beanPurple)"/>
        <ellipse cx="34" cy="104" rx="15" ry="21" transform="rotate(-25 34 104)" fill="url(#beanYellow)"/>
        <ellipse cx="145" cy="101" rx="15" ry="21" transform="rotate(25 145 101)" fill="url(#beanRed)"/>
      </g>
      <g fill="none" stroke="#fff" stroke-linecap="round" stroke-width="4" opacity=".42">
        <path d="M37 37 Q40 30 47 30"/><path d="M84 28 Q89 21 96 25"/>
        <path d="M129 41 Q135 34 141 39"/><path d="M58 78 Q64 71 70 76"/>
        <path d="M105 80 Q110 73 116 76"/><path d="M27 97 Q31 91 36 93"/>
      </g>
    </svg>
    """,
}


st.markdown(
    """
    <style>
      :root {
        --ink: #4c3444;
        --muted: #8d7482;
        --pink: #f8c7d6;
        --pink-deep: #e86f98;
        --yellow: #fff0ad;
        --cream: #fffaf2;
      }
      .stApp {
        background:
          radial-gradient(ellipse at 8% 3%, rgba(255, 222, 232, .75), transparent 31rem),
          radial-gradient(ellipse at 94% 7%, rgba(255, 241, 182, .8), transparent 27rem),
          #fffaf6;
        color: var(--ink);
      }
      [data-testid="stHeader"] { background: rgba(255,250,246,.88); }
      [data-testid="stMainBlockContainer"] {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
      }
      #MainMenu, footer { visibility: hidden; }
      .brand-row {
        display: flex; align-items: center; justify-content: space-between;
        margin: 0 auto 1rem; max-width: 1120px;
      }
      .brand {
        display: flex; align-items: center; gap: .65rem;
        color: #6b4158; font-weight: 850; letter-spacing: .11em;
        font-size: .82rem; text-transform: uppercase;
      }
      .brand-mark {
        display: grid; place-items: center; width: 2.2rem; height: 2.2rem;
        border-radius: 13px; background: #f8d4df; color: #c64c78;
        font-size: 1.2rem; box-shadow: 0 5px 12px rgba(184, 99, 127, .13);
      }
      .open-pill {
        border: 1px solid #f1e1c2; border-radius: 999px; background: #fff8df;
        padding: .43rem .8rem; color: #8a7044; font-size: .75rem; font-weight: 700;
      }
      .hero {
        text-align: center; padding: .7rem .4rem 1.35rem;
      }
      .hero-kicker {
        display: inline-block; color: #c15c7d; background: #ffe8ee;
        border: 1px solid #f8d5df; border-radius: 999px; padding: .35rem .8rem;
        font-size: .72rem; font-weight: 800; letter-spacing: .08em;
        text-transform: uppercase;
      }
      .hero h1 {
        color: #55384a; margin: .75rem 0 .35rem; font-size: clamp(2rem, 4vw, 3.35rem);
        line-height: 1.08; letter-spacing: -.045em; font-weight: 850;
      }
      .hero p { color: #8a7180; margin: 0; font-size: 1rem; }
      .section-heading {
        display: flex; justify-content: space-between; align-items: end;
        gap: 1rem; margin: .25rem 0 .85rem;
      }
      .section-heading h2 {
        margin: 0; color: #55384a; font-size: 1.18rem; letter-spacing: -.02em;
      }
      .section-heading p {
        color: var(--muted); font-size: .83rem; margin: .2rem 0 0;
      }
      .menu-badge {
        background: #fff0b8; color: #806a36; border-radius: 999px;
        padding: .35rem .7rem; font-size: .74rem; font-weight: 750; white-space: nowrap;
      }
      .menu-grid {
        display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: .75rem; margin-bottom: 1rem;
      }
      .candy-card {
        min-height: 142px; display: flex; align-items: center; gap: .45rem;
        padding: .7rem .6rem; border: 1px solid #f3e5e2; border-radius: 22px;
        background: rgba(255,255,255,.9); box-shadow: 0 10px 22px rgba(118, 70, 85, .055);
        position: relative; overflow: hidden;
      }
      .candy-card:after {
        content: ""; position: absolute; right: -24px; top: -27px; width: 83px; height: 83px;
        border-radius: 50%; background: #fff3c5; opacity: .5;
      }
      .candy-art {
        flex: 0 0 40%; min-width: 68px; position: relative; z-index: 1;
        display: flex; align-items: center; justify-content: center;
      }
      .candy-art svg { width: 100%; max-width: 118px; height: 104px; object-fit: contain; }
      .candy-copy { position: relative; z-index: 1; min-width: 0; }
      .candy-number {
        color: #db6e91; font-size: 1.75rem; line-height: 1; font-weight: 900;
        letter-spacing: -.07em; margin-bottom: .42rem;
      }
      .candy-name {
        color: #563e4d; font-size: .87rem; line-height: 1.22;
        font-weight: 780; min-height: 2.15rem;
      }
      .candy-price {
        color: #81676f; font-size: .76rem; font-weight: 700; margin-top: .45rem;
      }
      .menu-note {
        margin: -.35rem 0 .5rem; text-align: center; color: #987d89;
        font-size: .78rem;
      }
      [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #f0dfdf; border-radius: 24px; padding: .5rem .6rem;
        background: rgba(255,255,255,.85); box-shadow: 0 12px 24px rgba(118, 70, 85, .05);
      }
      .panel-title {
        color: #593d4d; font-weight: 820; font-size: 1.08rem; margin: 0 0 .2rem;
      }
      .panel-subtitle { color: #927b86; font-size: .82rem; margin: 0 0 .75rem; }
      .stForm { border: 0; padding: 0; }
      [data-testid="stNumberInput"] label {
        color: #654b58; font-size: .82rem; font-weight: 750;
      }
      [data-testid="stNumberInput"] input {
        background: #fffdfb; border-color: #edd9df; border-radius: 13px;
        min-height: 2.9rem; color: #55384a; font-weight: 700;
      }
      [data-testid="stFormSubmitButton"] button {
        border: 0; border-radius: 13px; min-height: 2.8rem;
        color: #fff; font-weight: 800;
        background: linear-gradient(100deg, #e97096, #df6488);
        box-shadow: 0 7px 15px rgba(218, 96, 136, .2);
        transition: transform .15s ease, box-shadow .15s ease;
      }
      [data-testid="stFormSubmitButton"] button:hover {
        color: #fff; transform: translateY(-1px);
        box-shadow: 0 10px 18px rgba(218, 96, 136, .27);
      }
      [data-testid="stAlert"] { border-radius: 14px; }
      .order-empty {
        border: 1px dashed #edd9df; border-radius: 15px; padding: .9rem;
        text-align: center; color: #9a808b; font-size: .84rem; background: #fffdfb;
      }
      .order-line {
        display: flex; justify-content: space-between; align-items: center;
        gap: .5rem; padding: .55rem 0; border-bottom: 1px solid #f2e7e5;
        color: #614956; font-size: .84rem;
      }
      .order-line:last-of-type { border-bottom: 0; }
      .order-line strong { color: #644454; }
      .order-total {
        display: flex; justify-content: space-between; padding-top: .7rem;
        margin-top: .25rem; border-top: 1px solid #eadad9;
        color: #56384b; font-weight: 850;
      }
      .footer-note {
        text-align: center; margin: .85rem 0 0; color: #a18a94; font-size: .72rem;
      }
      @media (max-width: 520px) {
        [data-testid="stMainBlockContainer"] { padding-left: .8rem; padding-right: .8rem; }
        .menu-grid { gap: .5rem; }
        .candy-card { min-height: 132px; padding: .5rem .4rem; gap: .2rem; }
        .candy-art { flex-basis: 36%; min-width: 48px; }
        .candy-art svg { height: 88px; }
        .candy-number { font-size: 1.45rem; }
        .candy-name { font-size: .75rem; }
        .hero { padding-top: .2rem; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_menu() -> None:
    cards = []
    for candy in CANDIES:
        cards.append(
            f'<article class="candy-card" aria-label="Menu item {candy["number"]}: {escape(candy["name"])}">'
            f'<div class="candy-art">{ARTWORK[candy["art"]]}</div>'
            f'<div class="candy-copy"><div class="candy-number">{candy["number"]}</div>'
            f'<div class="candy-name">{escape(candy["name"])}</div>'
            f'<div class="candy-price">{candy["price"]:.2f} SAR / {candy["unit"]}</div></div></article>'
        )

    st.markdown(
        f"""
        <div class="section-heading">
          <div>
            <h2>Today’s sweet picks</h2>
            <p>Four little favorites, all in one happy place.</p>
          </div>
          <span class="menu-badge">4 candy favorites</span>
        </div>
        <div class="menu-grid">{''.join(cards)}</div>
        <p class="menu-note">Choose by reading the number, then typing it below. The menu is for looking, not clicking.</p>
        """,
        unsafe_allow_html=True,
    )


def render_order(order: list[int]) -> None:
    counts = Counter(order)
    st.markdown(
        '<div class="panel-title">Your little candy haul</div>'
        '<div class="panel-subtitle">Your picks will show up here.</div>',
        unsafe_allow_html=True,
    )
    if not order:
        st.markdown(
            '<div class="order-empty">Your order is waiting for its first sweet pick.</div>',
            unsafe_allow_html=True,
        )
        return

    total = 0.0
    rows = []
    for candy in CANDIES:
        quantity = counts[candy["number"]]
        if quantity == 0:
            continue
        line_total = quantity * candy["price"]
        total += line_total
        rows.append(
            f'<div class="order-line"><span>{escape(candy["name"])} <strong>× {quantity}</strong></span>'
            f'<span>{line_total:.2f} SAR</span></div>'
        )

    st.markdown(
        "".join(rows)
        + f'<div class="order-total"><span>Total</span><span>{total:.2f} SAR</span></div>',
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <div class="brand-row">
      <div class="brand"><span class="brand-mark">✿</span> Sugar &amp; Sprinkles</div>
      <span class="open-pill">A little joy, packed fresh</span>
    </div>
    <div class="hero">
      <span class="hero-kicker">A tiny treat goes a long way</span>
      <h1>Pick your happy.</h1>
      <p>Find your favorite, type its number, and let the sweet stuff begin.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

menu_column, order_column = st.columns([1.12, 0.88], gap="large")
with menu_column:
    render_menu()

with order_column:
    with st.container(border=True):
        st.markdown(
            '<div class="panel-title">Make it a sweet order</div>'
            '<div class="panel-subtitle">Type the number of any candy on the menu.</div>',
            unsafe_allow_html=True,
        )
        with st.form("candy_order_form", clear_on_submit=False):
            candy_number = st.number_input(
                "Enter Candy Number",
                min_value=None,
                max_value=None,
                value=None,
                step=0.1,
                key="candy_number",
                help="Type a whole number from 1 to 4, using the menu above.",
            )
            submitted = st.form_submit_button("Add to my order", use_container_width=True)

    if submitted:
        if candy_number is None:
            st.error("Please enter a candy number.")
        elif isinstance(candy_number, bool) or not float(candy_number).is_integer():
            st.error("Please enter a valid candy number.")
        elif not 1 <= int(candy_number) <= 4:
            st.error("Invalid choice! Please select a number from 1 to 4.")
        else:
            selected = int(candy_number)
            st.session_state.setdefault("candy_order", [])
            st.session_state["candy_order"].append(selected)
            selected_name = next(candy["name"] for candy in CANDIES if candy["number"] == selected)
            st.success(f"Added {selected_name} to your order.")

    with st.container(border=True):
        render_order(st.session_state.get("candy_order", []))

st.markdown(
    '<p class="footer-note">Made with a little sugar and a lot of love.</p>',
    unsafe_allow_html=True,
)

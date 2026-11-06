from html import escape

import streamlit as st


def calculate_recommendation(
    first_name: str,
    last_name: str,
    experience: str | None,
    past_classes_text: str,
    weekly_sessions_text: list[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Validate the form and return a personalized Pilates recommendation."""
    required_values = [
        first_name,
        last_name,
        past_classes_text,
        *weekly_sessions_text,
    ]
    if (
        any(not value.strip() for value in required_values)
        or experience not in {"Yes", "No"}
    ):
        return None, ["Please fill in all fields"]

    try:
        past_classes = int(past_classes_text.strip())
        weekly_sessions = [int(value.strip()) for value in weekly_sessions_text]
    except ValueError:
        return None, ["Error: Please enter a valid positive integer"]

    if past_classes < 0 or any(value < 0 for value in weekly_sessions):
        return None, ["Error: Please enter a valid positive integer"]

    if any(value < 1 or value > 7 for value in weekly_sessions):
        return None, [
            "Error: Planned sessions per week must be between 1 and 7"
        ]

    if experience == "No" or past_classes < 5:
        level = "Beginner"
    elif past_classes > 20:
        level = "Advanced"
    else:
        level = "Intermediate"

    monthly_attendance = sum(weekly_sessions)
    average_weekly_goal = monthly_attendance / 4

    if monthly_attendance <= 4:
        package = "Basic Package"
        reminder = (
            "Every class counts. Keep your weekly rhythm steady and celebrate "
            "showing up for yourself."
        )
    elif monthly_attendance <= 11:
        package = "Silver Package"
        reminder = (
            "You’ve planned a consistent routine. Take it one session at a "
            "time and enjoy the progress."
        )
    else:
        package = "Gold / Unlimited Pass"
        reminder = (
            "That’s a strong monthly plan. Make room for recovery and enjoy "
            "the progress each session brings."
        )

    return {
        "full_name": f"{first_name.strip()} {last_name.strip()}",
        "level": level,
        "average_weekly_goal": f"{average_weekly_goal:.2f}".rstrip("0").rstrip("."),
        "monthly_attendance": str(monthly_attendance),
        "package": package,
        "reminder": reminder,
    }, []


def main() -> None:
    st.set_page_config(
        page_title="Pilates Path",
        page_icon="P",
        layout="centered",
    )

    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(155deg, #f4f7f3 0%, #f8f6f0 100%);
        }
        [data-testid="stMainBlockContainer"] {
            max-width: 900px;
            padding-top: 2.5rem;
            padding-bottom: 3rem;
        }
        .pilates-kicker {
            color: #55776a;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            margin-bottom: 0.35rem;
            text-transform: uppercase;
        }
        .pilates-intro {
            color: #5e6c65;
            font-size: 1.05rem;
            margin-top: -0.45rem;
            margin-bottom: 1.6rem;
        }
        [data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.88);
            border: 1px solid #e1e9e2;
            border-radius: 22px;
            padding: 1.4rem 1.5rem 1.1rem;
            box-shadow: 0 12px 35px rgba(43, 73, 59, 0.06);
        }
        [data-testid="stTextInput"] input {
            min-height: 46px;
            border-radius: 12px;
        }
        [data-testid="stFormSubmitButton"] button {
            min-height: 54px;
            border: 0;
            border-radius: 14px;
            background: #3e6b59;
            color: white;
            font-size: 1.05rem;
            font-weight: 700;
            transition: background 150ms ease, transform 150ms ease;
        }
        [data-testid="stFormSubmitButton"] button:hover {
            background: #315644;
            color: white;
            transform: translateY(-1px);
        }
        [data-testid="stMetric"] {
            min-height: 112px;
            padding: 1rem 1.1rem;
            background: #f7faf7;
            border: 1px solid #e4ece5;
            border-radius: 16px;
        }
        [data-testid="stMetricValue"] {
            color: #315b49;
            font-size: 1.35rem;
        }
        @media (max-width: 640px) {
            [data-testid="stMainBlockContainer"] {
                padding-top: 1.5rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            [data-testid="stForm"] {
                padding: 1rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="pilates-kicker">Pilates Path</div>', unsafe_allow_html=True)
    st.title("Your Pilates plan, made for you")
    st.markdown(
        '<p class="pilates-intro">Share your experience and weekly plans to '
        "find a class level and membership that fit your routine.</p>",
        unsafe_allow_html=True,
    )

    with st.form("pilates_recommendation_form", border=False):
        name_columns = st.columns(2)
        first_name = name_columns[0].text_input(
            "First name",
            placeholder="Enter your first name",
        )
        last_name = name_columns[1].text_input(
            "Last name",
            placeholder="Enter your last name",
        )

        experience_columns = st.columns(2)
        experience = experience_columns[0].radio(
            "Have you practiced Pilates before?",
            options=["Yes", "No"],
            index=None,
            horizontal=True,
        )
        past_classes = experience_columns[1].text_input(
            "Past completed classes",
            placeholder="Enter a whole number",
            help="Enter 0 or more completed classes.",
        )

        st.markdown("**Planned sessions**")
        st.caption("Enter 1 to 7 sessions for each week.")
        week_columns = st.columns(4)
        weekly_sessions = [
            column.text_input(
                f"Week {week_number}",
                placeholder="1–7",
                key=f"week_{week_number}",
            )
            for week_number, column in enumerate(week_columns, start=1)
        ]

        submitted = st.form_submit_button(
            "Calculate my plan",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        recommendation, errors = calculate_recommendation(
            first_name,
            last_name,
            experience,
            past_classes,
            weekly_sessions,
        )
        st.session_state["pilates_recommendation"] = recommendation
        st.session_state["pilates_errors"] = errors

    for error in st.session_state.get("pilates_errors", []):
        st.error(error)

    recommendation = st.session_state.get("pilates_recommendation")
    if recommendation:
        st.markdown("### Your recommendation")
        st.markdown(
            f'<div class="pilates-kicker">Welcome</div><h2>{escape(recommendation["full_name"])}</h2>',
            unsafe_allow_html=True,
        )

        first_row = st.columns(2)
        first_row[0].metric("Recommended level", recommendation["level"])
        first_row[1].metric(
            "Average weekly goal",
            f'{recommendation["average_weekly_goal"]} sessions',
        )
        second_row = st.columns(2)
        second_row[0].metric(
            "Projected monthly attendance",
            f'{recommendation["monthly_attendance"]} sessions',
        )
        second_row[1].metric("Recommended package", recommendation["package"])

        st.markdown("**Motivational reminder**")
        st.info(recommendation["reminder"])


if __name__ == "__main__":
    main()

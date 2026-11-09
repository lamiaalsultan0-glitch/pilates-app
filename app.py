import streamlit as st


def calculate_recommendation(
    first_name: str,
    last_name: str,
    experience: str | None,
    past_classes_text: str,
    weekly_sessions_text: list[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Validate the form and return a personalized Pilates recommendation."""
    if experience not in {"Yes", "No"}:
        return None, ["Please fill in all fields"]

    required_values = [first_name, last_name, *weekly_sessions_text]
    if experience == "Yes":
        required_values.append(past_classes_text)
    if any(not value.strip() for value in required_values):
        return None, ["Please fill in all fields"]

    try:
        past_classes = int(past_classes_text.strip()) if experience == "Yes" else 0
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


def clear_recommendation() -> None:
    st.session_state.pop("pilates_recommendation", None)
    st.session_state.pop("pilates_errors", None)


def main() -> None:
    st.set_page_config(
        page_title="Pilates Path",
        page_icon="P",
        layout="centered",
    )

    st.caption("Pilates Path")
    st.title("Your Pilates plan, made for you")
    st.caption(
        "Share your experience and weekly plans to find a class level and "
        "membership that fit your routine."
    )

    experience = st.radio(
        "Have you practiced Pilates before?",
        options=["Yes", "No"],
        index=None,
        horizontal=True,
        key="prior_pilates_experience",
        on_change=clear_recommendation,
    )

    with st.form("pilates_recommendation_form"):
        name_columns = st.columns(2)
        first_name = name_columns[0].text_input(
            "First name",
            placeholder="Enter your first name",
        )
        last_name = name_columns[1].text_input(
            "Last name",
            placeholder="Enter your last name",
        )

        past_classes = st.text_input(
            "Past completed classes",
            placeholder=(
                "Not needed"
                if experience == "No"
                else "Enter a whole number"
            ),
            help=(
                "Not needed when you select No."
                if experience == "No"
                else "Enter 0 or more completed classes."
            ),
            disabled=experience == "No",
        )

        st.subheader("Planned sessions")
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
        st.subheader("Your recommendation")
        st.subheader(f'Welcome, {recommendation["full_name"]}!')

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

        st.subheader("Motivational reminder")
        st.info(recommendation["reminder"])


if __name__ == "__main__":
    main()

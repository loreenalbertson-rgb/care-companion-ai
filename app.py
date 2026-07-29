import streamlit as st
from datetime import date, datetime

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Care Companion AI",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------------

st.markdown(
    """
    <style>
        .stApp {
            background-color: #f7fbfa;
        }

        .main-title {
            font-size: 3rem;
            font-weight: 700;
            color: #315f5b;
            margin-bottom: 0;
        }

        .subtitle {
            font-size: 1.15rem;
            color: #58716e;
            margin-top: 0.3rem;
            margin-bottom: 2rem;
        }

        .welcome-card {
            background: white;
            border: 1px solid #dcebea;
            border-radius: 18px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 4px 12px rgba(49, 95, 91, 0.08);
        }

        .safety-card {
            background: #fff8e8;
            border-left: 5px solid #d6a84c;
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin: 1rem 0;
        }

        .emergency-card {
            background: #fff0f0;
            border-left: 5px solid #c84f4f;
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin: 1rem 0;
        }

        .result-card {
            background: #ffffff;
            border: 1px solid #d9e8e6;
            border-radius: 16px;
            padding: 1.25rem;
            margin-top: 1rem;
        }

        div[data-testid="stSidebar"] {
            background-color: #eaf4f2;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "symptoms" not in st.session_state:
    st.session_state.symptoms = []

if "medications" not in st.session_state:
    st.session_state.medications = []

# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def create_plain_language_summary(medical_text: str) -> str:
    """Create a structured placeholder summary without diagnosing."""

    cleaned_text = medical_text.strip()

    if not cleaned_text:
        return ""

    return f"""
### Plain-Language Review

**What the note discusses**

This information appears to describe a medical concern, test, diagnosis, treatment, or care recommendation.

**Original information**

{cleaned_text}

**Helpful questions to consider**

- What is the main concern described here?
- What follow-up care is recommended?
- Are there symptoms that should be monitored?
- Are there warning signs that require urgent attention?
- Are medications, treatments, or additional tests mentioned?

**Next step**

Bring this information to a qualified healthcare professional and ask them to explain any unfamiliar terms, recommendations, or risks.
"""


def generate_doctor_questions(
    concern: str,
    symptoms: str,
    goals: str,
) -> list[str]:
    """Generate safe appointment-preparation questions."""

    questions = [
        "What are the most likely explanations for these symptoms or concerns?",
        "Are there tests or evaluations that may help clarify what is happening?",
        "What changes should we watch for at home?",
        "Which symptoms would require urgent or emergency care?",
        "What treatment options are available, and what are their benefits and risks?",
        "Could any current medications be contributing to these symptoms?",
        "When should we schedule follow-up care?",
    ]

    if concern.strip():
        questions.insert(
            0,
            f"How should we understand the concern described as: {concern.strip()}?",
        )

    if symptoms.strip():
        questions.append(
            f"How might these reported symptoms affect the care plan: {symptoms.strip()}?"
        )

    if goals.strip():
        questions.append(
            f"What steps could help us work toward this care goal: {goals.strip()}?"
        )

    return questions


def create_appointment_summary(
    patient_name: str,
    appointment_date: date,
    main_concern: str,
    symptom_notes: str,
    medication_questions: str,
    changes_since_last_visit: str,
    caregiver_questions: str,
) -> str:
    """Create a printable appointment summary."""

    return f"""
CARE COMPANION AI
APPOINTMENT PREPARATION SUMMARY

Patient: {patient_name or "Not provided"}
Appointment date: {appointment_date.strftime("%B %d, %Y")}
Prepared: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}

MAIN CONCERN
{main_concern or "No main concern entered."}

SYMPTOMS AND OBSERVATIONS
{symptom_notes or "No symptom notes entered."}

CHANGES SINCE THE LAST VISIT
{changes_since_last_visit or "No changes entered."}

MEDICATION QUESTIONS
{medication_questions or "No medication questions entered."}

QUESTIONS FOR THE CARE TEAM
{caregiver_questions or "No additional questions entered."}

IMPORTANT
This summary was prepared for organizational and educational purposes.
It is not a diagnosis and does not replace professional medical care.
"""


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("💙 Care Companion AI")

selected_tool = st.sidebar.radio(
    "Choose a caregiver tool",
    [
        "Home",
        "Medical Information Simplifier",
        "Doctor Question Generator",
        "Symptom Journal",
        "Medication Organizer",
        "Appointment Prep",
        "Caregiver Support",
    ],
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
Care Companion AI helps caregivers organize information and prepare for medical conversations.

It does not diagnose, prescribe treatment, or replace a healthcare professional.
"""
)

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if selected_tool == "Home":
    st.markdown(
        '<p class="main-title">Care Companion AI</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="subtitle">A gentle digital toolkit for caregivers and families navigating complex care.</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="welcome-card">
            <h3>Caregiving comes with a lot to remember.</h3>
            <p>
                Care Companion AI helps families organize symptoms, medications,
                appointment questions, and medical notes in one supportive space.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="welcome-card">
                <h3>🩺 Prepare</h3>
                <p>Create clear questions and summaries for medical appointments.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="welcome-card">
                <h3>📝 Organize</h3>
                <p>Keep symptom and medication information easier to review.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="welcome-card">
                <h3>🌿 Understand</h3>
                <p>Break complicated medical information into manageable pieces.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="emergency-card">
            <strong>Emergency warning:</strong>
            This app is not intended for emergencies. Call 911 or seek immediate
            medical care for severe, sudden, or life-threatening symptoms.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# MEDICAL INFORMATION SIMPLIFIER
# ---------------------------------------------------------

elif selected_tool == "Medical Information Simplifier":
    st.header("🌿 Medical Information Simplifier")

    st.write(
        "Paste a medical note, diagnosis description, discharge instruction, or test explanation."
    )

    medical_text = st.text_area(
        "Medical information",
        height=250,
        placeholder=(
            "Paste the information you would like organized into plain language..."
        ),
    )

    if st.button("Simplify Information", type="primary"):
        if not medical_text.strip():
            st.warning("Please enter medical information first.")
        else:
            summary = create_plain_language_summary(medical_text)

            st.markdown(
                '<div class="result-card">',
                unsafe_allow_html=True,
            )

            st.markdown(summary)

            st.markdown("</div>", unsafe_allow_html=True)

            st.warning(
                "This educational summary may miss important medical context. "
                "Always confirm the meaning with a qualified healthcare professional."
            )

# ---------------------------------------------------------
# DOCTOR QUESTION GENERATOR
# ---------------------------------------------------------

elif selected_tool == "Doctor Question Generator":
    st.header("❓ Doctor Question Generator")

    st.write(
        "Turn your concerns and observations into organized questions for the care team."
    )

    concern = st.text_area(
        "Main diagnosis, concern, or topic",
        placeholder="Example: Increased sleepiness after a medication change",
    )

    symptoms = st.text_area(
        "Symptoms or observations",
        placeholder="Describe what you have noticed, including timing and changes.",
    )

    goals = st.text_area(
        "What do you hope to understand or accomplish?",
        placeholder="Example: Understand whether medication changes should be considered",
    )

    if st.button("Generate Questions", type="primary"):
        if not concern.strip() and not symptoms.strip() and not goals.strip():
            st.warning("Please enter at least one concern, symptom, or goal.")
        else:
            questions = generate_doctor_questions(
                concern=concern,
                symptoms=symptoms,
                goals=goals,
            )

            st.subheader("Questions to bring to the appointment")

            for number, question in enumerate(questions, start=1):
                st.write(f"{number}. {question}")

# ---------------------------------------------------------
# SYMPTOM JOURNAL
# ---------------------------------------------------------

elif selected_tool == "Symptom Journal":
    st.header("📝 Symptom Journal")

    st.write(
        "Record observations that may help identify patterns and support medical conversations."
    )

    with st.form("symptom_form"):
        symptom_date = st.date_input("Date", value=date.today())

        symptom_name = st.text_input(
            "Symptom or observation",
            placeholder="Example: Headache, nausea, fatigue, increased alertness",
        )

        severity = st.slider(
            "Severity",
            min_value=1,
            max_value=10,
            value=5,
        )

        timing = st.text_input(
            "Timing and duration",
            placeholder="Example: Started around 2 PM and lasted two hours",
        )

        possible_triggers = st.text_input(
            "Possible triggers or related events",
            placeholder="Example: Medication, meal, activity, poor sleep",
        )

        notes = st.text_area(
            "Additional notes",
            placeholder="Add anything else that may be helpful.",
        )

        submitted = st.form_submit_button("Add Journal Entry")

        if submitted:
            if not symptom_name.strip():
                st.warning("Please enter a symptom or observation.")
            else:
                st.session_state.symptoms.append(
                    {
                        "date": symptom_date.strftime("%B %d, %Y"),
                        "symptom": symptom_name,
                        "severity": severity,
                        "timing": timing,
                        "triggers": possible_triggers,
                        "notes": notes,
                    }
                )

                st.success("Symptom entry added.")

    if st.session_state.symptoms:
        st.subheader("Saved entries")

        for index, entry in enumerate(
            reversed(st.session_state.symptoms),
            start=1,
        ):
            with st.expander(
                f"{entry['date']} · {entry['symptom']} · Severity {entry['severity']}/10"
            ):
                st.write(f"**Timing:** {entry['timing'] or 'Not entered'}")
                st.write(
                    f"**Possible triggers:** {entry['triggers'] or 'Not entered'}"
                )
                st.write(f"**Notes:** {entry['notes'] or 'Not entered'}")

        if st.button("Clear Symptom Journal"):
            st.session_state.symptoms = []
            st.rerun()

# ---------------------------------------------------------
# MEDICATION ORGANIZER
# ---------------------------------------------------------

elif selected_tool == "Medication Organizer":
    st.header("💊 Medication Organizer")

    st.write(
        "Create a temporary list of medications and questions for the care team."
    )

    with st.form("medication_form"):
        medication_name = st.text_input(
            "Medication name",
            placeholder="Example: Levetiracetam",
        )

        dose = st.text_input(
            "Dose",
            placeholder="Example: 500 mg",
        )

        schedule = st.text_input(
            "Schedule",
            placeholder="Example: Twice daily",
        )

        purpose = st.text_input(
            "Purpose",
            placeholder="Why is this medication being taken?",
        )

        medication_notes = st.text_area(
            "Questions or observations",
            placeholder=(
                "Example: Increased sleepiness started after the dose changed"
            ),
        )

        medication_submitted = st.form_submit_button("Add Medication")

        if medication_submitted:
            if not medication_name.strip():
                st.warning("Please enter a medication name.")
            else:
                st.session_state.medications.append(
                    {
                        "name": medication_name,
                        "dose": dose,
                        "schedule": schedule,
                        "purpose": purpose,
                        "notes": medication_notes,
                    }
                )

                st.success("Medication added.")

    if st.session_state.medications:
        st.subheader("Medication list")

        for medication in st.session_state.medications:
            with st.expander(
                f"{medication['name']} · {medication['dose'] or 'Dose not entered'}"
            ):
                st.write(
                    f"**Schedule:** {medication['schedule'] or 'Not entered'}"
                )
                st.write(
                    f"**Purpose:** {medication['purpose'] or 'Not entered'}"
                )
                st.write(
                    f"**Questions or observations:** "
                    f"{medication['notes'] or 'Not entered'}"
                )

        if st.button("Clear Medication List"):
            st.session_state.medications = []
            st.rerun()

# ---------------------------------------------------------
# APPOINTMENT PREP
# ---------------------------------------------------------

elif selected_tool == "Appointment Prep":
    st.header("📋 Appointment Preparation")

    st.write(
        "Organize the most important information into one downloadable summary."
    )

    patient_name = st.text_input("Patient name or initials")

    appointment_date = st.date_input(
        "Appointment date",
        value=date.today(),
    )

    main_concern = st.text_area(
        "Main concern",
        placeholder="What is the most important issue to discuss?",
    )

    symptom_notes = st.text_area(
        "Symptoms and observations",
        placeholder="Include timing, frequency, severity, and recent patterns.",
    )

    changes_since_last_visit = st.text_area(
        "Changes since the last visit",
        placeholder="Include improvements, declines, new symptoms, or care changes.",
    )

    medication_questions = st.text_area(
        "Medication questions",
        placeholder="Include side effects, missed doses, or possible adjustments.",
    )

    caregiver_questions = st.text_area(
        "Questions for the care team",
        placeholder="List anything else you want to remember to ask.",
    )

    if st.button("Create Appointment Summary", type="primary"):
        summary = create_appointment_summary(
            patient_name=patient_name,
            appointment_date=appointment_date,
            main_concern=main_concern,
            symptom_notes=symptom_notes,
            medication_questions=medication_questions,
            changes_since_last_visit=changes_since_last_visit,
            caregiver_questions=caregiver_questions,
        )

        st.text_area(
            "Appointment summary",
            value=summary,
            height=450,
        )

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="care_companion_appointment_summary.txt",
            mime="text/plain",
        )

# ---------------------------------------------------------
# CAREGIVER SUPPORT
# ---------------------------------------------------------

elif selected_tool == "Caregiver Support":
    st.header("💙 Caregiver Support")

    st.markdown(
        """
        <div class="welcome-card">
            <h3>You are carrying a lot.</h3>
            <p>
                Organizing medications, watching symptoms, making calls,
                attending appointments, and advocating for someone you love
                can be physically and emotionally exhausting.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("A gentle check-in")

    st.checkbox("I have eaten something today.")
    st.checkbox("I have had water.")
    st.checkbox("I have taken my own medication, if applicable.")
    st.checkbox("I have written down the most urgent task.")
    st.checkbox("I have asked someone for help where possible.")

    st.info(
        "You do not have to solve every part of the care journey today. "
        "Choose the next clear step."
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.caption(
    "Care Companion AI is an educational and organizational project. "
    "It does not provide medical diagnoses, treatment recommendations, "
    "or emergency services."
)

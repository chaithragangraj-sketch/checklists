import streamlit as st

st.set_page_config(page_title="Full Checklist System", layout="wide")

st.title("📋 Learning Difficulty Checklist (Class 1 - English)")

# -------------------------------
# DETAILS
# -------------------------------
student_name = st.text_input("Student Name")
teacher_name = st.text_input("Teacher Name")

score_map = {"A": 100, "B": 80, "C": 60, "D": 40}

# -------------------------------
# DATA (ALL 7 DOMAINS)
# -------------------------------
data = {
    "Domain 1: Attention & Executive Function": [
        {
            "skill": "Sustains attention during tasks",
            "desc": {
                "A": "Engages continuously in the task for 10 minutes without stopping or shifting to another activity",
                "B": "Pauses task engagement 1–2 times in 10 minutes (e.g., stops writing/working), resumes independently without prompts",
                "C": "Stops task engagement ≥3 times in 10 minutes, requires prompts to resume the task",
                "D": "Stops task engagement within 10 minutes and does not resume, even with repeated prompts"
            }
        },
        {
            "skill": "Maintains focus despite distractions",
            "desc": {
                "A": "Works for 10 minutes with distractions present; resumes immediately without prompts",
                "B": "Shifts 1–2 times; resumes independently",
                "C": "Shifts ≥3 times; needs prompts",
                "D": "Stops within 1–2 minutes; does not resume"
            }
        },
        {
            "skill": "Transition between activities",
            "desc": {
                "A": "Transitions within 10 seconds independently",
                "B": "Transitions within 30 seconds with one prompt",
                "C": "Takes 30–60 seconds with multiple prompts",
                "D": "Unable to transition"
            }
        },
        {
            "skill": "Follows instructions (single-step)",
            "desc": {
                "A": "Follows independently",
                "B": "Follows with one repetition",
                "C": "Requires multiple repetitions",
                "D": "Unable to follow"
            }
        },
        {
            "skill": "Follows instructions (multi-step)",
            "desc": {
                "A": "Follows independently",
                "B": "Follows with prompts",
                "C": "Partial completion",
                "D": "Unable"
            }
        },
        {
            "skill": "Completes tasks within time",
            "desc": {
                "A": "Completes within time independently",
                "B": "Completes with one prompt",
                "C": "Delayed completion",
                "D": "Unable to complete"
            }
        }
    ],

    "Domain 2: Visuo-Motor Integration": [
        {"skill": "Colour identification", "desc": {"A": "Correctly identifies colours independently", "B": "Identifies with prompts", "C": "Inconsistent", "D": "Unable"}},
        {"skill": "Identification of body parts", "desc": {"A": "Identifies all independently", "B": "Minor prompts", "C": "Frequent prompts", "D": "Unable"}},
        {"skill": "Visual discrimination", "desc": {"A": "Differentiates symbols accurately", "B": "Minor errors", "C": "Frequent confusion", "D": "Unable"}},
        {"skill": "Eye-hand coordination", "desc": {"A": "Smooth and accurate", "B": "Minor errors", "C": "Frequent errors", "D": "Unable"}},
        {"skill": "Spacing and alignment", "desc": {"A": "Consistent spacing", "B": "Minor errors", "C": "Irregular", "D": "None"}},
        {"skill": "Sense of direction", "desc": {"A": "Accurate", "B": "Prompt needed", "C": "Frequent errors", "D": "Unable"}},
        {"skill": "Letter formation", "desc": {"A": "Correct", "B": "Minor errors", "C": "Frequent errors", "D": "Unable"}}
    ],

    "Domain 3: Language & Communication": [
        {"skill": "Comprehending oral instructions", "desc": {"A": "Accurate", "B": "Repetition needed", "C": "Partial", "D": "Unable"}},
        {"skill": "Listening comprehension", "desc": {"A": "Answers correctly", "B": "Minor errors", "C": "Partial", "D": "Unable"}},
        {"skill": "Functional communication", "desc": {"A": "Clear expression", "B": "Minor hesitation", "C": "Inconsistent", "D": "Unable"}},
        {"skill": "Sentence formation", "desc": {"A": "Complete sentences", "B": "Minor errors", "C": "Incomplete", "D": "Words only"}},
        {"skill": "Verbal fluency", "desc": {"A": "Smooth speech", "B": "Occasional pause", "C": "Frequent pause", "D": "Limited"}}
    ],

    "Domain 4: Reading": [
        {"skill": "Letter-sound recognition", "desc": {"A": "Accurate", "B": "Minor errors", "C": "Inconsistent", "D": "Unable"}},
        {"skill": "Blending sounds", "desc": {"A": "Accurate", "B": "Minor errors", "C": "Inconsistent", "D": "Unable"}},
        {"skill": "Reading comprehension", "desc": {"A": "90–100%", "B": "70–89%", "C": "40–69%", "D": "<40%"}}
    ],

    "Domain 5: Spelling": [
        {"skill": "Spelling accuracy", "desc": {"A": "Correct", "B": "Minor errors", "C": "Frequent errors", "D": "Unable"}},
        {"skill": "Spelling strategies", "desc": {"A": "Uses strategies", "B": "Minor prompts", "C": "Inconsistent", "D": "None"}}
    ],

    "Domain 6: Writing & Written Expression": [
        {"skill": "Pencil grip", "desc": {"A": "Proper", "B": "Minor issues", "C": "Poor", "D": "Unable"}},
        {"skill": "Sentence writing", "desc": {"A": "Correct", "B": "Minor errors", "C": "Incomplete", "D": "Unable"}}
    ],

    "Domain 7: Socio-Emotional Behaviour": [
        {"skill": "Behaviour during challenging tasks", "desc": {"A": "Persists independently", "B": "Needs prompts", "C": "Gives up", "D": "Refuses"}},
        {"skill": "Task initiation", "desc": {"A": "Starts independently", "B": "Occasional prompts", "C": "Frequent prompts", "D": "Does not start"}},
        {"skill": "Emotional control", "desc": {"A": "Regulates well", "B": "Minor support", "C": "Frequent support", "D": "Unable"}},
        {"skill": "Peer interaction", "desc": {"A": "Positive interaction", "B": "Minor difficulty", "C": "Limited", "D": "Avoids"}},
        {"skill": "Classroom participation", "desc": {"A": "Active", "B": "Occasional prompts", "C": "Limited", "D": "None"}}
    ]
}

# -------------------------------
# UI
# -------------------------------
domain_scores = {}

for d_idx, (domain, items) in enumerate(data.items()):
    st.subheader(domain)
    domain_scores[domain] = []

    for q_idx, item in enumerate(items):

        st.markdown(f"### {item['skill']}")

        with st.expander("View Descriptors"):
            for k, v in item["desc"].items():
                st.markdown(f"**{k}:** {v}")

        key = f"{d_idx}_{q_idx}"
        choice = st.radio("", ["A", "B", "C", "D"], horizontal=True, key=key)

        domain_scores[domain].append(score_map[choice])

# -------------------------------
# RESULTS
# -------------------------------
def get_grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"

if st.button("Submit Evaluation"):

    st.subheader("📊 Domain-wise Results")

    all_scores = []

    for domain, scores in domain_scores.items():
        avg = sum(scores) / len(scores)
        grade = get_grade(avg)
        all_scores.extend(scores)
        st.write(f"{domain} → {avg:.2f}% ({grade})")

    final_avg = sum(all_scores) / len(all_scores)
    final_grade = get_grade(final_avg)

    st.subheader("🏆 Final Evaluation")
    st.write(f"Score: {final_avg:.2f}%")
    st.write(f"Grade: {final_grade}")


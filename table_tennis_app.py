
import streamlit as st

# ============================================================
# TABLE TENNIS COACH
# ============================================================

st.set_page_config(
    page_title="Table Tennis Coach",
    page_icon="🏓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: #f1f5f9;
}

[data-testid="stSidebar"] {
    background-color: #111c31;
}

.hero {
    padding: 35px;
    border-radius: 22px;
    background: linear-gradient(135deg, #172554, #1e3a8a);
    border: 1px solid #334f91;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    color: #cbd5e1;
    font-size: 18px;
}

.lesson-card {
    background-color: #111c31;
    border: 1px solid #263858;
    padding: 24px;
    border-radius: 18px;
    min-height: 140px;
    margin-bottom: 12px;
}

.lesson-card h3 {
    color: white;
}

.lesson-card p {
    color: #cbd5e1;
}

.completed-status {
    color: #22c55e !important;
    font-weight: 700;
}

.incomplete-status {
    color: #cbd5e1 !important;
    font-weight: 600;
}

.section-title {
    font-size: 27px;
    font-weight: 700;
    color: white;
    margin-top: 18px;
    margin-bottom: 12px;
}

.info-box {
    background-color: #172554;
    border-left: 4px solid #60a5fa;
    padding: 18px;
    border-radius: 10px;
    margin: 15px 0;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 45px;
    padding: 20px;
}

div.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = set()

if "selected_grip" not in st.session_state:
    st.session_state.selected_grip = "Handshake Grip"

# ============================================================
# LESSON DATA
# ============================================================

LESSONS = {
    1: {
        "title": "Racket Grips",
        "emoji": "🤝",
        "description": "Learn the handshake grip and pinch grip."
    },
    2: {
        "title": "Types of Spin",
        "emoji": "🔄",
        "description": "Understand topspin, backspin, and sidespin."
    },
    3: {
        "title": "Basic Stance and Body Weight",
        "emoji": "🏓",
        "description": "Learn the ready position and balance."
    },
    4: {
        "title": "Forehand Basics",
        "emoji": "⚡",
        "description": "Learn the fundamentals of the forehand stroke."
    },
    5: {
        "title": "Backhand Basics",
        "emoji": "🎯",
        "description": "Learn the fundamentals of the backhand stroke."
    }
}

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def go_to(page):
    st.session_state.page = page


def mark_completed(lesson_number):
    st.session_state.completed_lessons.add(lesson_number)


def lesson_complete(lesson_number):
    return lesson_number in st.session_state.completed_lessons


def show_header(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_lesson_card(number):
    lesson = LESSONS[number]
    completed = lesson_complete(number)

    if completed:
        status = "✅ Completed"
        status_class = "completed-status"
    else:
        status = "📘 Ready to learn"
        status_class = "incomplete-status"

    st.markdown(
        f"""
        <div class="lesson-card">
            <h3>{lesson["emoji"]} Lesson {number}: {lesson["title"]}</h3>
            <p>{lesson["description"]}</p>
            <p class="{status_class}">{status}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        f"Open Lesson {number} →",
        key=f"open_lesson_{number}",
        use_container_width=True
    ):
        go_to(f"Lesson {number}")
        st.rerun()


def lesson_navigation(number):
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if number == 1:
            previous_page = "Lessons"
            previous_text = "← Back to Lessons"
        else:
            previous_page = f"Lesson {number - 1}"
            previous_text = "← Previous Lesson"

        if st.button(previous_text, use_container_width=True):
            go_to(previous_page)
            st.rerun()

    with col2:
        if st.button(
            f"✅ Complete Lesson {number}",
            use_container_width=True
        ):
            mark_completed(number)
            st.success(f"Lesson {number} completed!")

    st.divider()

    if number < len(LESSONS):
        if st.button("Next Lesson →", use_container_width=True):
            go_to(f"Lesson {number + 1}")
            st.rerun()
    else:
        if st.button("📚 Back to All Lessons", use_container_width=True):
            go_to("Lessons")
            st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🏓 TT COACH")
    st.caption("Train. Learn. Improve.")

    st.divider()

    if st.button("🏠 Home", use_container_width=True):
        go_to("Home")
        st.rerun()

    if st.button("📚 All Lessons", use_container_width=True):
        go_to("Lessons")
        st.rerun()

    if st.button("📊 My Progress", use_container_width=True):
        go_to("Progress")
        st.rerun()

    st.divider()

    st.markdown("### 🏓 Your Training")

    st.caption(
        f"{len(st.session_state.completed_lessons)} lessons "
        "completed this session"
    )

    st.divider()

    st.caption("Table Tennis Coach")
    st.caption("Version 1.0")


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "Home":

    show_header(
        "🏓 Table Tennis Coach",
        "Improve your technique. Build confidence. Play better."
    )

    st.markdown(
        """
        <div class="info-box">
            <h3>👋 Welcome to Table Tennis Coach!</h3>
            <p>
                Follow structured lessons, practise essential
                techniques, and track your table tennis progress.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">📊 Your Training Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Lessons", len(LESSONS))

    with col2:
        st.metric(
            "Completed Lessons",
            len(st.session_state.completed_lessons)
        )

    st.divider()

    if st.button(
        "📚 Open Lesson Library",
        use_container_width=True
    ):
        go_to("Lessons")
        st.rerun()


# ============================================================
# ALL LESSONS
# ============================================================

elif st.session_state.page == "Lessons":

    show_header(
        "📚 Lesson Library",
        "Choose a lesson and start your training."
    )

    st.write("Select any lesson below to begin your training.")

    st.divider()

    for number in LESSONS:
        show_lesson_card(number)


# ============================================================
# LESSON 1: RACKET GRIPS
# ============================================================

elif st.session_state.page == "Lesson 1":

    show_header(
        "🤝 Lesson 1: Racket Grips",
        "Learn the basics of holding a table tennis racket."
    )

    st.markdown("### 🎯 Learning Objectives")

    st.write(
        "Understand the handshake grip and pinch grip."
    )

    st.divider()

    st.markdown("## 🏓 Choose Your Grip")

    selected_grip = st.radio(
        "Select a grip to study:",
        [
            "Handshake Grip",
            "Pinch Grip"
        ],
        key="selected_grip"
    )

    st.divider()

    if selected_grip == "Handshake Grip":

        st.markdown("## 🤝 Handshake Grip")

        st.info(
            "The handshake grip is commonly used in table tennis. "
            "It resembles holding someone's hand."
        )

        st.markdown("### 📖 How to Hold It")

        st.write("""
        1. Hold the racket handle comfortably.
        2. Place your thumb and index finger around the handle.
        3. Keep the remaining fingers around the handle.
        4. Avoid squeezing the racket too tightly.
        5. Practise moving the racket while maintaining control.
        """)

        st.markdown("### ⚠️ Common Mistakes")

        st.write("""
        - Holding the racket too tightly.
        - Bending the wrist unnecessarily.
        - Changing your grip constantly.
        - Ignoring comfort and control.
        """)

    else:

        st.markdown("## 🤏 Pinch Grip")

        st.info(
            "The pinch grip is another way of holding a table "
            "tennis racket. Follow your coaching instructions "
            "for the correct finger positioning."
        )

        st.markdown("### 📖 How to Hold It")

        st.write("""
        1. Start with a relaxed hand.
        2. Position your thumb and index finger comfortably.
        3. Use the remaining fingers to support the racket.
        4. Check that you can hold the racket comfortably.
        5. Practise moving the racket slowly.
        6. Compare your control with your normal grip.
        """)

    lesson_navigation(1)


# ============================================================
# LESSON 2: TYPES OF SPIN
# ============================================================

elif st.session_state.page == "Lesson 2":

    show_header(
        "🔄 Lesson 2: Types of Spin",
        "Understand how spin affects a table tennis ball."
    )

    st.markdown("## 🎯 Learning Objectives")

    st.write(
        "Learn about topspin, backspin, and sidespin."
    )

    st.divider()

    st.markdown("## 🔄 Choose a Spin Type")

    spin_type = st.selectbox(
        "Select a topic:",
        [
            "Topspin",
            "Backspin",
            "Sidespin"
        ]
    )

    st.divider()

    if spin_type == "Topspin":

        st.markdown("## ⬆️ Topspin")

        st.write("""
        Topspin is a type of spin in which the ball rotates
        forward in the direction of its movement.

        It is commonly used in attacking shots and can help
        the ball dip onto the table.
        """)

    elif spin_type == "Backspin":

        st.markdown("## ⬇️ Backspin")

        st.write("""
        Backspin is a type of spin in which the ball rotates
        backward relative to its direction of movement.

        It is often used in defensive, short-game, and
        serving situations.
        """)

    else:

        st.markdown("## ↔️ Sidespin")

        st.write("""
        Sidespin is rotation around a mainly vertical axis.

        It can cause the ball to curve or bounce sideways,
        depending on the direction and amount of spin.
        """)

    st.divider()

    st.markdown("## 🧠 Quick Check")

    spin_answer = st.radio(
        "Which spin rotates forward in the direction of ball movement?",
        [
            "Topspin",
            "Backspin",
            "Sidespin"
        ],
        key="spin_quiz"
    )

    if st.button("Check Spin Answer"):

        if spin_answer == "Topspin":
            st.success("Correct! 🎉")
        else:
            st.warning("Try again. Think about forward rotation.")

    lesson_navigation(2)


# ============================================================
# LESSON 3: BASIC STANCE
# ============================================================

elif st.session_state.page == "Lesson 3":

    show_header(
        "🏓 Lesson 3: Basic Stance and Body Weight",
        "Learn the ready position, balance, and movement."
    )

    st.markdown("## 🎯 Learning Objectives")

    st.write("""
    Learn how to maintain a balanced stance, distribute your
    body weight, and prepare for quick movement during a rally.
    """)

    st.divider()

    st.markdown("## 🏃‍♂️ Basic Stance and body weight distribution")

    st.write("""
    The basic stance in table tennis helps you maintain balance
    and react quickly to your opponent's shots.

    You should stand with your feet approximately shoulder-width
    apart, knees slightly bent, and your body leaning a little
    forward.
    """)

    st.markdown("### 1. Feet Position")

    st.write("""
    - Keep your feet approximately shoulder-width apart.
    - Keep your feet ready to move in either direction.
    - Avoid standing with your feet too close together.
    """)

    st.markdown("### 2. Bend Your Knees")

    st.write("""
    - Keep your knees slightly bent.
    - Avoid standing completely straight.
    - Stay relaxed and ready to move.
    - Lower your centre of gravity for better balance.
    """)

    st.markdown("### 3. Racket Position")

    st.write("""
    - Keep your racket in front of your body.
    - Keep your elbow comfortably bent.
    - Hold your racket around a comfortable ready position.
    - Stay prepared for both forehand and backhand shots.
    """)

    st.markdown("### 4. Body Weight Distribution")

    st.write("""
    Your weight should be distributed between both feet.

    Keep a slight forward lean and stay balanced on the balls
    of your feet. This allows you to move quickly and maintain
    control during rallies.

    Avoid putting all your weight on one foot while waiting
    for your opponent's shot.
    """)

    st.markdown("### ⚠️ Common Mistakes")

    st.write("""
    - Standing too straight.
    - Keeping your feet too close together.
    - Leaning too far forward.
    - Keeping your racket too low.
    - Putting all your weight on one foot.
    - Remaining stationary after hitting the ball.
    """)


    lesson_navigation(3)


# ============================================================
# LESSON 4: FOREHAND BASICS
# ============================================================

elif st.session_state.page == "Lesson 4":

    show_header(
        "⚡ Lesson 4: Forehand Basics",
        "Learn the fundamentals of a controlled forehand stroke."
    )

    st.markdown("## 🎯 Learning Objectives")

    st.write("""
    Learn the basic preparation, forward swing, contact point,
    and follow-through of a forehand shot.
    """)

    st.divider()

    st.markdown("## 🏓 What Is a Forehand?")

    st.write("""
    The forehand is one of the most important strokes in table
    tennis. It can be used for attacking, rallying, and
    controlling the ball.

    A good forehand involves coordination between your body,
    arm, and racket.
    """)

    st.markdown("### 1. Forehand Ready Position")

    st.write("""
    - Stand with your feet apart.
    - Keep your knees slightly bent and torso forward.
    - Hold the racket in front of your body with your elbow slightly bent and down.
    - Keep your body relaxed and balanced.
    - keep your left leg slightly forward (for right-handed players) to prepare for the swing.
    """)

    st.markdown("### 2. Forehand Counter")

    st.write("""
    - Move your racket back and slightly to the side.
    - Keep your elbow bent and comfortable. 
    - swing straight in the direction of the ball towards the net.
    """)

    st.markdown("### 3. Forward Swing")

    st.write("""
    - Rotate your hips and shoulders toward the ball.
    - Move the racket forward in a controlled motion.
    - Contact the ball in front of your body.
    - Use your arm and body together.
    - Adjust the racket angle to control the ball.
    """)

    st.markdown("### 4. Follow-Through")

    st.write("""
    - Continue the racket movement after contact.
    - Keep the movement controlled.
    - Return to the ready position.
    - Prepare for your opponent's next shot.
    """)

    st.markdown("### ⚠️ Common Mistakes")

    st.write("""
    - Using only your arm without body movement.
    - Hitting the ball too late.
    - Swinging too hard.
    - Losing balance during the swing.
    - Forgetting to return to the ready position.
    - Focusing on power instead of consistency.
    """)

    lesson_navigation(4)


# ============================================================
# LESSON 5: BACKHAND BASICS
# ============================================================

elif st.session_state.page == "Lesson 5":

    show_header(
        "🎯 Lesson 5: Backhand Basics",
        "Learn how to perform a controlled backhand stroke."
    )

    st.markdown("## 🎯 Learning Objectives")

    st.write("""
    Learn the basic preparation, swing, contact point, and
    follow-through of a backhand stroke.
    """)

    st.divider()

    st.markdown("## 🏓 What Is a Backhand?")

    st.write("""
    The backhand stroke helps you return balls on the backhand
    side of your body.

    It is useful for maintaining control during rallies and
    returning balls quickly when you have limited time.
    """)

    st.markdown("### 1. Ready Position")

    st.write("""
    - Keep your feet approximately shoulder-width apart.
    - Bend your knees slightly.
    - Hold your racket in front of your body.
    - Stay balanced and watch the ball carefully.
    """)

    st.markdown("### 2. Preparation")

    st.write("""
    - Move your racket slightly toward your body.
    - Keep your elbow bent and comfortable.
    - Keep your racket in a position that allows a quick swing.
    - Stay balanced and prepare for the incoming ball.
    """)

    st.markdown("### 3. Forward Swing")

    st.write("""
    - Once the ball comes close to you, move the racket forward using a controlled movement.
    - Keep your elbow in a comfortable position
    - Use your forearm and wrist naturally.
    - Adjust your racket angle to control the shot.
    - use wrist movement to add spin if needed.
    """)

    st.markdown("### 4. Follow-Through")

    st.write("""
    - Continue the racket movement after contact.
    - Avoid stopping the racket suddenly.
    - Maintain your balance.
    - Return to the ready position.
    - Prepare for the next shot.
    """)

    st.markdown("### ⚠️ Common Mistakes")

    st.write("""
    - Swinging only with the wrist.
    - Keeping the elbow too stiff.
    - Hitting the ball too close to the body.
    - Standing upright during the shot.
    - Using too much force.
    - Forgetting to return to the ready position.
    """)


    lesson_navigation(5)


# ============================================================
# PROGRESS PAGE
# ============================================================

elif st.session_state.page == "Progress":

    show_header(
        "📊 My Progress",
        "Track your completed lessons."
    )

    total_lessons = len(LESSONS)

    completed = len(
        st.session_state.completed_lessons
    )

    st.metric(
        "Lessons Completed",
        f"{completed} / {total_lessons}"
    )

    progress_value = completed / total_lessons

    st.progress(progress_value)

    st.divider()

    for number, lesson in LESSONS.items():

        if lesson_complete(number):

            st.success(
                f"✅ Lesson {number}: "
                f"{lesson['title']} — Completed"
            )

        else:

            st.write(
                f"⬜ Lesson {number}: "
                f"{lesson['title']} — Not completed"
            )

    st.divider()

    st.caption(
        "Progress is currently saved only during the active session."
    )

    if st.button("← Back Home"):

        go_to("Home")
        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">🏓 Table Tennis Coach • Keep Improving</div>',
    unsafe_allow_html=True
)

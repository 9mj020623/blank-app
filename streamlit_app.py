import streamlit as st

st.set_page_config(page_title="눈 건강 자가 진단 테스트", page_icon="👁️", layout="centered")
st.title("👁️ 눈 건강 자가 진단 테스트")

# — 질문 목록
questions = [
    {"question": "하루에 디지털 기기를 얼마나 사용하나요?", "options": [("4시간 이하", 1), ("4시간 이상", 2)]},
    {"question": "디지털 기기를 사용한 후 눈의 피로를 얼마나 느끼나요?", "options": [("거의 느끼지 않음", 1), ("자주 느끼고 있음", 2)]},
    {"question": "눈 건강을 위해 어떤 노력을 하고 있나요?",       "options": [("특별히 신경 쓰지 않음", 1), ("영양소와 운동을 챙김", 2)]},
    {"question": "밝은 빛에 노출될 때 어떤 반응을 보이나요?",     "options": [("괜찮음", 1), ("눈부심을 느낌", 2)]},
    {"question": "눈 건강에 좋은 음식을 얼마나 자주 섭취하나요?", "options": [("가끔 먹음", 1), ("자주 챙겨 먹음", 2)]},
    {"question": "눈의 피로를 줄이기 위해 스트레칭이나 운동을 얼마나 자주 하나요?", 
     "options": [("전혀 하지 않음", 1), ("자주 함", 2)]}
]

# — 세션 상태 초기화
if "q_idx" not in st.session_state:
    st.session_state.q_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# — 테스트 초기화 함수
def restart():
    st.session_state.q_idx = 0
    st.session_state.score = 0

# — 결과 표시 함수
def show_result():
    st.subheader("📝 결과 진단")
    s = st.session_state.score
    if s <= 7:
        st.markdown("### ✅ 초집중 안구형")
        st.write("- **맞춤 영양소**: 루테인\n- **추천 식단**: 시금치 샐러드, 고등어구이\n- **스트레칭 방법**: 눈 마사지, 눈 깜빡이기 운동")
    elif s <= 9:
        st.markdown("### 🌟 빛에 민감한 감성형")
        st.write("- **맞춤 영양소**: 비타민 C\n- **추천 식단**: 과일 스무디, 파프리카 볶음\n- **스트레칭 방법**: 눈 감기 운동, 자연광 노출")
    elif s <= 11:
        st.markdown("### 💪 먹는 거 안 가리는 튼튼형")
        st.write("- **맞춤 영양소**: 오메가-3 지방산\n- **추천 식단**: 견과류 믹스, 연어 스테이크\n- **스트레칭 방법**: 목 스트레칭, 눈 회전 운동")
    else:
        st.markdown("### ⚠️ 디지털 기기 의존형")
        st.write("- **맞춤 영양소**: 비타민 A\n- **추천 식단**: 당근 스틱, 고구마 구이\n- **스트레칭 방법**: 20-20-20 규칙, 눈 깜빡임 운동")
    st.button("🔁 다시 테스트하기", on_click=restart)

# — 메인 로직
if st.session_state.q_idx < len(questions):
    q = questions[st.session_state.q_idx]
    st.subheader(f"Q{st.session_state.q_idx + 1}. {q['question']}")

    # 옵션 버튼: 클릭 즉시 점수 더하고 index 증가 → 앱 rerun
    for i, (label, pts) in enumerate(q["options"]):
        if st.button(label, key=f"opt_{st.session_state.q_idx}_{i}"):
            st.session_state.score += pts
            st.session_state.q_idx += 1
            st.rerun()  # 여기가 한 번만 호출돼도 바로 리렌더링 됩니다
else:
    show_result()

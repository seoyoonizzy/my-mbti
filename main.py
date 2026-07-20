import streamlit as st
import random

st.set_page_config(page_title="MBTI 포켓몬 추천🧚‍♀️", page_icon="🎮")

mbti_pokemon = {
    "INTJ": [("메타몽", "전략적이고 독립적인 INTJ처럼 다재다능하게 변신하는 포켓몬"),
             ("팬텀", "신비롭고 계획적인 면모가 INTJ와 닮았어요")],
    "INTP": [("깨비드릉갈", "탐구심 많고 논리적인 INTP에게 어울려요"),
             ("고오스", "독특한 사고방식을 가진 INTP와 잘 맞아요")],
    "ENTJ": [("갸라도스", "강력한 리더십과 카리스마를 가진 ENTJ와 어울려요"),
             ("리자몽", "목표 지향적이고 열정적인 ENTJ에게 딱이에요")],
    "ENTP": [("치렁이", "재치있고 도전을 즐기는 ENTP와 잘 맞아요"),
             ("또가스", "예측불가능하고 창의적인 ENTP를 닮았어요")],
    "INFJ": [("뮤", "신비롭고 통찰력 있는 INFJ와 어울려요"),
             ("라프라스", "따뜻하고 배려심 깊은 INFJ에게 잘 맞아요")],
    "INFP": [("이브이", "다양한 가능성을 품은 INFP처럼 진화가 다채로워요"),
             ("세레비", "이상주의적이고 순수한 INFP를 닮았어요")],
    "ENFJ": [("피카츄", "사람들을 이끌고 챙기는 ENFJ와 잘 어울려요"),
             ("루카리오", "타인을 돕고 이끄는 ENFJ에게 어울려요")],
    "ENFP": [("치코리타", "밝고 사교적인 ENFP와 잘 맞아요"),
             ("망나뇽", "자유롭고 열정적인 ENFP를 닮았어요")],
    "ISTJ": [("이상해씨", "성실하고 꾸준한 ISTJ와 잘 어울려요"),
             ("딱구리", "책임감 강한 ISTJ에게 어울려요")],
    "ISFJ": [("피츄", "다정하고 헌신적인 ISFJ와 잘 맞아요"),
             ("메리프", "따뜻하고 보호본능이 강한 ISFJ를 닮았어요")],
    "ESTJ": [("코뿌리", "체계적이고 실행력 있는 ESTJ와 어울려요"),
             ("모다피", "리더십이 강한 ESTJ에게 잘 맞아요")],
    "ESFJ": [("푸린", "사람들과 잘 어울리는 ESFJ에게 딱이에요"),
             ("고지", "친화력 좋은 ESFJ와 어울려요")],
    "ISTP": [("탕구리", "손재주 좋고 실용적인 ISTP와 잘 맞아요"),
             ("독침붕", "독립적이고 민첩한 ISTP를 닮았어요")],
    "ISFP": [("토게피", "감성적이고 예술적인 ISFP와 어울려요"),
             ("아르코", "온화하고 개성 있는 ISFP에게 잘 맞아요")],
    "ESTP": [("윙크", "모험을 즐기는 ESTP와 잘 어울려요"),
             ("피죤투", "활동적이고 대담한 ESTP를 닮았어요")],
    "ESFP": [("삐삐", "매력적이고 사교적인 ESFP와 잘 맞아요"),
             ("팽도리", "밝고 에너지 넘치는 ESFP에게 어울려요")],
}

st.title("🔮 MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드려요!")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기"):
    pokemon, reason = random.choice(mbti_pokemon[selected_mbti])
    st.success(f"당신에게 어울리는 포켓몬은 **{pokemon}** 입니다!")
    st.write(reason)
    st.balloons()

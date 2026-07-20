import streamlit as st
import random

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🎮")

# (포켓몬 이름, 도감번호, 추천 이유)
mbti_pokemon = {
    "INTJ": [("메타몽", 132, "전략적이고 독립적인 INTJ처럼 다재다능하게 변신하는 포켓몬"),
             ("팬텀", 94, "신비롭고 계획적인 면모가 INTJ와 닮았어요")],
    "INTP": [("고오스", 92, "탐구심 많고 독특한 사고를 하는 INTP와 잘 맞아요"),
             ("뮤츠", 150, "뛰어난 지적 능력을 가진 INTP를 닮았어요")],
    "ENTJ": [("갸라도스", 130, "강력한 리더십과 카리스마를 가진 ENTJ와 어울려요"),
             ("리자몽", 6, "목표 지향적이고 열정적인 ENTJ에게 딱이에요")],
    "ENTP": [("또가스", 110, "예측불가능하고 창의적인 ENTP를 닮았어요"),
             ("캥카", 115, "에너지 넘치고 임기응변에 강한 ENTP와 잘 맞아요")],
    "INFJ": [("뮤", 151, "신비롭고 통찰력 있는 INFJ와 어울려요"),
             ("라프라스", 131, "따뜻하고 배려심 깊은 INFJ에게 잘 맞아요")],
    "INFP": [("이브이", 133, "다양한 가능성을 품은 INFP처럼 진화가 다채로워요"),
             ("세레비", 251, "이상주의적이고 순수한 INFP를 닮았어요")],
    "ENFJ": [("피카츄", 25, "사람들을 이끌고 챙기는 ENFJ와 잘 어울려요"),
             ("루카리오", 448, "타인을 돕고 이끄는 ENFJ에게 어울려요")],
    "ENFP": [("치코리타", 152, "밝고 사교적인 ENFP와 잘 맞아요"),
             ("망나뇽", 149, "자유롭고 열정적인 ENFP를 닮았어요")],
    "ISTJ": [("이상해씨", 1, "성실하고 꾸준한 ISTJ와 잘 어울려요"),
             ("두두", 84, "책임감 강하고 우직한 ISTJ에게 어울려요")],
    "ISFJ": [("피츄", 172, "다정하고 헌신적인 ISFJ와 잘 맞아요"),
             ("메리프", 179, "따뜻하고 보호본능이 강한 ISFJ를 닮았어요")],
    "ESTJ": [("코뿌리", 111, "체계적이고 실행력 있는 ESTJ와 어울려요"),
             ("텅구리", 105, "강인하고 원칙적인 ESTJ에게 잘 맞아요")],
    "ESFJ": [("푸린", 39, "사람들과 잘 어울리는 ESFJ에게 딱이에요"),
             ("라이츄", 26, "활기차고 친화력 좋은 ESFJ와 어울려요")],
    "ISTP": [("탕구리", 104, "손재주 좋고 실용적인 ISTP와 잘 맞아요"),
             ("독침붕", 15, "독립적이고 민첩한 ISTP를 닮았어요")],
    "ISFP": [("토게피", 175, "감성적이고 예술적인 ISFP와 어울려요"),
             ("에브이", 196, "온화하고 개성 있는 ISFP에게 잘 맞아요")],
    "ESTP": [("피죤투", 18, "모험을 즐기는 ESTP와 잘 어울려요"),
             ("부스터", 136, "활동적이고 열정적인 ESTP를 닮았어요")],
    "ESFP": [("삐삐", 35, "매력적이고 사교적인 ESFP와 잘 맞아요"),
             ("팽도리", 393, "밝고 에너지 넘치는 ESFP에게 어울려요")],
}

SPRITE_URL = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png"

st.title("🔮 MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 이미지와 함께 추천해드려요!")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기"):
    pokemon, dex_num, reason = random.choice(mbti_pokemon[selected_mbti])
    st.success(f"당신에게 어울리는 포켓몬은 **{pokemon}** 입니다!")
    st.image(SPRITE_URL.format(dex_num), caption=f"{pokemon} (No.{dex_num:03d})", width=250)
    st.write(reason)
    st.balloons()

import streamlit as st

# 1. 웹페이지 상단 레이아웃 및 전체 글자 크기 확대를 위한 CSS 주입 (시각 한계 보완)
st.set_page_config(page_title="광주 자치구별 노인복지 알리미", page_icon="👵", layout="centered")

# 어르신들을 위해 전체 폰트 크기를 키우고 스타일을 가독성 있게 조정하는 CSS
st.markdown("""
    <style>
    html, body, [data-testid="stMarkdownContainer"] p {
        font-size: 20px !important;
        line-height: 1.6 !important;
    }
    .stSelectbox label, .stNumberInput label {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #1e3a8a !important;
    }
    h1 {
        font-size: 36px !important;
        color: #1e3a8a !important;
    }
    h3 {
        font-size: 26px !important;
        color: #0f172a !important;
        border-bottom: 2px solid #cbd5e1;
        padding-bottom: 8px;
    }
    .benefit-title {
        font-size: 24px !important;
        color: #b91c1c !important;
        font-weight: bold;
    }
    .highlight-box {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        margin-bottom: 15px;
    }
    .badge-district {
        background-color: #ffe6e6;
        color: #cc0000;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 16px !important;
        font-weight: bold;
        margin-left: 10px;
    }
    .badge-common {
        background-color: #e0f2fe;
        color: #0369a1;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 16px !important;
        font-weight: bold;
        margin-left: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 타이틀 (가독성 향상)
st.title("👵👴 광주광역시 자치구별 맞춤형 노인복지 알리미")
st.write("👉 거주하시는 동네(구), 어르신의 나이, 소득 수준을 차례대로 선택해 주세요.")
st.markdown("---")

# 2. 사용자 입력 인터페이스 개편 (슬라이더 제거 ➡️ 직관적 입력 및 선택 상자)
# 미세 손가락 조작이 힘든 어르신들을 위해 슬라이더를 없애고 숫자 입력 및 버튼 형태로 보완
col1, col2, col3 = st.columns(3)

with col1:
    user_district = st.selectbox(
        "1. 거주하시는 구 선택",
        options=["동구", "서구", "남구", "북구", "광산구"]
    )

with col2:
    # 수전증/슬라이더 조작 오류 보완: 큰 플러스/마이너스 버튼이 제공되는 숫자 입력기 사용
    user_age = st.number_input(
        "2. 어르신 나이 입력 (세)",
        min_value=60,
        max_value=100,
        value=65,
        step=1
    )

with col3:
    user_income = st.selectbox(
        "3. 소득 수준 선택",
        options=["기초생활수급자", "차상위계층", "일반 어르신 (소득 하위 70% 이하)", "일반 어르신 (소득 제한 없음)"]
    )

st.markdown("---")

# 3. 광주광역시 5개 자치구 통합 복지 데이터베이스 (오프라인 연계 및 지참 서류 상세화)
benefits = [
    # [1] 소득 지원 및 저소득층 생활 안정
    {"category": "💰 소득 지원 & 생활 안정", "name": "기초연금 지급", "age": 65, "income_target": ["기초생활수급자", "차상위계층", "일반 어르신 (소득 하위 70% 이하)"], "district_target": "광주공통", "content": "안정적인 노후 지원을 위해 소득인정액 기준 하위 70% 이하 어르신께 매월 정액의 연금을 차등 지급합니다.", "papers": "신분증, 통장 사본, 배우자의 금융정보제공동의서", "contact": "주소지 관할 동 행정복지센터 복지팀 또는 국민연금공단 (국번없이 1355)"},
    {"category": "💰 소득 지원 & 생활 안정", "name": "에너지바우처 (냉·난방비 지원)", "age": 65, "income_target": ["기초생활수급자"], "district_target": "광주공통", "content": "생계·의료급여 수급 어르신 가구에 전기, 도시가스, 등유, 연탄 등을 구입할 수 있는 이용권을 계절별로 차등 지급합니다.", "papers": "신분증, 최근에 나온 전기요금 또는 도시가스 고지서", "contact": "주소지 관할 동 행정복지센터 복지팀"},
    {"category": "💰 소득 지원 & 생활 안정", "name": "정부 양곡(쌀) 대폭 할인 지원", "age": 65, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "광주공통", "content": "기초생활 수급자 및 차상위 어르신 가구를 대상으로 정부 양곡을 50%에서 최대 90%까지 할인된 가격으로 공급합니다.", "papers": "기초생활수급자/차상위계층 증명서 (동주민센터 발급 가능), 신분증", "contact": "주소지 관할 동 행정복지센터 복지팀"},
    
    # 자치구별 바우처 특화 데이터
    {"category": "💰 소득 지원 & 생활 안정", "name": "동구 효도 바우처 (목욕 및 이·미용권) 지원", "age": 70, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "동구", "content": "동구 관내 거주 저소득 어르신의 위생 및 보건 복지 향상을 위해 분기별 효도 바우처 카드를 무상 지급합니다.", "papers": "신분증, 주민등록등본", "contact": "동구청 노인장애인복지과 또는 관할 동 행정복지센터 복지팀"},
    {"category": "💰 소득 지원 & 생활 안정", "name": "서구 노인 목욕비 및 이·미용비 지원", "age": 75, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "서구", "content": "서구 조례에 의거하여 노후 생활 안정을 위해 관내 지정 목욕탕 및 미용실에서 사용 가능한 전용 이용권을 지원합니다.", "papers": "신분증, 수급자/차상위 증명서", "contact": "서구청 노인복지과 또는 관할 동 행정복지센터 복지팀"},
    {"category": "💰 소득 지원 & 생활 안정", "name": "남구 효사랑 목욕권 및 이미용 지원", "age": 70, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "남구", "content": "남구 지역 저소득층 어르신들의 건강 증진을 도모하고자 자치구 자체 예산으로 정기 이용권을 제공합니다.", "papers": "신분증", "contact": "남구청 고령사회정책과 또는 관할 동 행정복지센터 복지팀"},
    {"category": "💰 소득 지원 & 생활 안정", "name": "북구 어르신 실버 위생 바우처", "age": 75, "income_target": ["기초생활수급자"], "district_target": "북구", "content": "북구 관내 생계·의료급여 수급 어르신들을 대상으로 쾌적한 노후를 위한 자치구 특화 위생 바우처를 지급합니다.", "papers": "신분증, 의료급여 수급자 증명서", "contact": "북구청 노인복지과 또는 관할 동 행정복지센터 복지팀"},
    {"category": "💰 소득 지원 & 생활 안정", "name": "광산구 저소득 노인 건강 및 위생 지원", "age": 70, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "광산구", "content": "광산구 관내 취약계층 어르신들의 삶의 질 향상과 보건 위생을 보장하기 위해 구 자체 목욕 및 이용권을 지원합니다.", "papers": "신분증", "contact": "광산구청 노인장애인과 또는 관할 동 행정복지센터 복지팀"},

    # [2] 건강관리 및 의료비 지원
    {"category": "🩺 보건 & 의료 지원", "name": "광주 실버케어 100세 건강 선별검사", "age": 60, "income_target": ["전체"], "district_target": "광주공통", "content": "치매 및 만성질환 예방을 위해 인지선별검사(CIST) 및 맞춤형 건강 상담을 무료로 제공합니다.", "papers": "신분증 (사전 예약 권장)", "contact": "광주광역시 5개 자치구 보건소 치매안심센터"},
    {"category": "🩺 보건 & 의료 지원", "name": "치매 치료관리비 (약제비) 지원", "age": 60, "income_target": ["기초생활수급자", "차상위계층", "일반 어르신 (소득 하위 70% 이하)"], "district_target": "광주공통", "content": "치매 진단 후 약물을 복용 중인 어르신(중위소득 120% 이하)께 월 최대 3만 원의 진료비 및 약제비를 지원합니다.", "papers": "신분증, 치매 진단서 또는 소견서, 당해연도 치매치료약 처방전 및 영수증", "contact": "주소지 관할 보건소 치매안심센터"},
    {"category": "🩺 보건 & 의료 지원", "name": "어르신 인플루엔자(독감) 무료 예방접종", "age": 65, "income_target": ["전체"], "district_target": "광주공통", "content": "겨울철 건강관리를 위해 매년 가을 전국 지정 위탁 의료기관 및 보건소에서 독감 주사를 무료 접종해 드립니다.", "papers": "신분증 (주민등록증 또는 운전면허증)", "contact": "광주광역시 내 지정 병의원 및 보건소"},
    {"category": "🩺 보건 & 의료 지원", "name": "노인 무릎 인공관절 수술비 지원", "age": 60, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "광주공통", "content": "퇴행성 관절염으로 고통받는 저소득층 어르신을 대상으로 한쪽 무릎당 최대 120만 원의 수술비를 지원합니다.", "papers": "신분증, 의사 진단서(소견서), 수급자/차상위 증명서", "contact": "관할 보건소 보건행정과 또는 노인인공관절재단 (1661-6595)"},

    # [3] 교통, 주거 및 문화 여가
    {"category": "🚌 교통·주거 & 여가 문화", "name": "어르신 무임 교통카드 (G-Pass) 발급", "age": 65, "income_target": ["전체"], "district_target": "광주공통", "content": "광주광역시에 거주하시는 어르신들의 이동권 보장을 위해 광주 도시철도(지하철)를 평생 무료로 승차할 수 있는 카드를 발급합니다.", "papers": "신분증, 주민등록등본 (최근 1개월 이내 발급분)", "contact": "광주은행 전 영업점 창구 방문 신청"},
    {"category": "🚌 교통·주거 & 여가 문화", "name": "노인 복지관 평생교육 강좌 수강 지원", "age": 60, "income_target": ["전체"], "district_target": "광주공통", "content": "스마트폰 사용법, 어학, 서예, 건강 댄스 등 다양한 평생교육 프로그램을 무료 또는 매우 저렴하게 수강할 수 있습니다.", "papers": "신분증, 회원증 발급용 증명사진 1매", "contact": "거주지 주변 자치구 노인복지관 또는 종합사회복지관 창구"},
    {"category": "🚌 교통·주거 & 여가 문화", "name": "자치구별 경로당 찾아가는 여가 프로그램 운영", "age": 65, "income_target": ["전체"], "district_target": "광주공통", "content": "동네 경로당을 중심으로 노래교실, 치매 예방 레크리에이션, 건강 실버 체조 프로그램을 무상 연계 및 지원합니다.", "papers": "별도 서류 없음 (경로당 회원 가입 필요)", "contact": "대한노인회 광주광역시연합회 및 구별 지회"},

    # [4] 일상생활 돌봄 및 지역 사회 안전망 (구별 특화)
    {"category": "🤝 일상 돌봄 & 안전망", "name": "노인 맞춤돌봄서비스", "age": 65, "income_target": ["기초생활수급자", "차상위계층", "일반 어르신 (소득 하위 70% 이하)"], "district_target": "광주공통", "content": "독거 및 취약 노인을 대상으로 주 1~2회 가정을 방문하여 생활 안부를 확인하고 든든한 말벗 대화, 가사 지원 등을 종합 제공합니다.", "papers": "신분증, 거동불편 증빙서류(필요시)", "contact": "주소지 관할 동 행정복지센터 복지팀 담당자"},
    {"category": "🤝 일상 돌봄 & 안전망", "name": "독거노인·장애인 응급안전안심서비스", "age": 65, "income_target": ["전체"], "district_target": "광주공통", "content": "홀로 계신 어르신 가구 내에 화재 감지기, 가스 차단기, 활동량 센서 및 응급호출기를 무상 설치하여 위급상황을 실시간 예방합니다.", "papers": "신분증, 독거노인 증빙 가능 서류(주민등록등본)", "contact": "동 행정복지센터 또는 구별 지역노인복지센터"},
    {"category": "🤝 일상 돌봄 & 안전망", "name": "결식 우려 저소득 노인 무료 식사 지원", "age": 60, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "광주공통", "content": "가정 형편상 식사를 거르기 쉬운 소외 계층 어르신들을 대상으로 관내 지정 경로식당 및 복지관에서 따뜻한 점심 식사를 무상 제공합니다.", "papers": "신분증, 수급자 또는 차상위 계층 증명서", "contact": "선택하신 자치구청 노인복지계 및 인근 사회복지관"},
    {"category": "🤝 일상 돌봄 & 안전망", "name": "광산구 특화 '영양가득 행복반찬' 배달 서비스", "age": 65, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "광산구", "content": "광산구 거동불편 독거어르신 가정을 위해 지역 복지 네트워크와 연계하여 밑반찬을 정기 배달하고 안부를 확인하는 특화 사업입니다.", "papers": "신분증, 거동불편 진단서 또는 소견서", "contact": "광산구청 복지정책과 또는 관내 종합사회복지관"},
    {"category": "🤝 일상 돌봄 & 안전망", "name": "서구 특화 'AI 돌봄 로봇(효돌이)' 보급 사업", "age": 65, "income_target": ["기초생활수급자", "차상위계층"], "district_target": "서구", "content": "서구 관내 독거어르신의 우울증 예방과 복약 안내를 위해 인공지능(AI) 반려인형 효돌이를 무상 대여 및 관리해 드립니다.", "papers": "신분증, 독거노인 확인 서류", "contact": "서구청 스마트통합돌봄담당관 또는 관할 동 행정복지센터"},

    # [5] 노인 일자리 및 사회 활동 지원
    {"category": "💼 일자리 & 사회 참여", "name": "공익활동형 노인 일자리 사업", "age": 65, "income_target": ["기초생활수급자", "차상위계층", "일반 어르신 (소득 하위 70% 이하)"], "district_target": "광주공통", "content": "스쿨존 등하교 안전 도우미, 지역사회 환경 개선 등 가벼운 사회적 공익활동 일자리를 연계합니다. (월 30시간 활동 시 수당 지급)", "papers": "신분증, 주민등록등본, 참여신청서(기관 비치)", "contact": "선택하신 자치구 시니어클럽, 노인복지관, 동 행정복지센터"},
    {"category": "💼 일자리 & 사회 참여", "name": "사회서비스형 노인 일자리 사업", "age": 60, "income_target": ["전체"], "district_target": "광주공통", "content": "어르신의 경력과 역량을 활용하여 보육시설 보조, 공공 행정 업무 지원 등 전문성이 높은 일자리를 매칭합니다.", "papers": "신분증, 경력증명서(필요시), 관련 자격증 사본", "contact": "선택하신 자치구 시니어클럽 및 노인일자리창출지원센터"},
    {"category": "💼 일자리 & 사회 참여", "name": "구별 시니어클럽 특화 시장형 사업 (카페 및 작업장)", "age": 60, "income_target": ["전체"], "district_target": "광주공통", "content": "실버 카페, 공동 작업장 등 각 자치구 시니어클럽에서 직접 운영하는 매장 및 제작 일자리를 제공합니다.", "papers": "신분증, 보건증(카페 등 식품 취급 일자리일 경우 필수)", "contact": "선택하신 자치구 시니어클럽 (동구/서구/남구/북구/광산 시니어클럽)"}
]

# 4. 실시간 필터링 제어 및 웹 화면 렌더링 (인지 피로 감소를 위한 직관적 레이아웃)
st.subheader(f"🏠 {user_district} / 🎂 만 {user_age}세 / 💰 {user_income}")
st.write("🔽 아래 카드들을 위에서부터 차례대로 읽어보세요.")

categories = [
    "💰 소득 지원 & 생활 안정", 
    "🩺 보건 & 의료 지원", 
    "🚌 교통·주거 & 여가 문화", 
    "🤝 일상 돌봄 & 안전망",
    "💼 일자리 & 사회 참여"
]

total_benefits_found = 0

for cat in categories:
    cat_benefits = [
        b for b in benefits 
        if b["category"] == cat and user_age >= b["age"] and 
           ("전체" in b["income_target"] or user_income in b["income_target"]) and
           (b["district_target"] == "광주공통" or b["district_target"] == user_district)
    ]
    
    if cat_benefits:
        # 큰 대분류 제목 표시
        st.markdown(f"### 📍 {cat}") 
        for b in cat_benefits:
            # 인지 피로를 줄이기 위한 시각적 구획화 박스 처리
            st.markdown(f"""
                <div class="highlight-box">
                    <div class="benefit-title">
                        🎁 {b['name']}
                        {"<span class='badge-district'>" + user_district + " 특화</span>" if b['district_target'] != '광주공통' else "<span class='badge-common'>공통 혜택</span>"}
                    </div>
                    <div style="margin-top: 10px; font-size: 20px;">
                        <strong>● 무슨 혜택인가요?</strong><br>
                        {b['content']}
                    </div>
                    <div style="margin-top: 10px; font-size: 20px; color: #0284c7;">
                        <strong>📂 동사무소(주민센터) 갈 때 챙겨갈 서류:</strong><br>
                        👉 <span style="background-color: #e0f2fe; padding: 2px 5px; border-radius: 4px; font-weight: bold;">{b['papers']}</span>
                    </div>
                    <div style="margin-top: 10px; font-size: 20px; color: #475569;">
                        <strong>📞 신청 및 문의하는 곳:</strong><br>
                        🏢 {b['contact']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            total_benefits_found += 1

if total_benefits_found == 0:
    st.info("선택하신 조건(나이, 소득 등)에 맞는 복지 혜택이 현재 동네에 없습니다. 나이나 소득 수준을 변경하여 다시 확인해 보세요.")

# 5. 하단 공신력 확보 및 고지
st.markdown("---")
st.caption("ℹ️ 대한민국 보건복지부 복지로 시스템 가이드 및 광주광역시 5개 자치구청 노인복지과 최신 행정 조례 데이터를 기반으로 작동하는 정밀 알리미 시스템입니다.")

# -*- coding: utf-8 -*-

import streamlit as st

def show_team_info():
    st.header("? 팀 소개")
    
    st.subheader("우리 팀의 목표")
    st.write("AI 챗봇을 활용한 효율적인 학습 지원 시스템 구축")
    
    st.subheader("? 팀원 소개 및 역할")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**홍길동**")
        st.markdown("- 프로젝트 리더")
        st.markdown("- Gemini AI 통합")
        
    with col2:
        st.markdown("**김철수**")
        st.markdown("- 프론트엔드 개발")
        st.markdown("- UI/UX 디자인")
        
    with col3:
        st.markdown("**이영희**")
        st.markdown("- 백엔드 개발")
        st.markdown("- 데이터베이스 관리")

# 메인 앱에서 호출
if __name__ == "__main__":
    st.set_page_config(page_title="AI 학습 도우미", layout="wide")
    show_team_info()
    # 나머지 앱 로직...

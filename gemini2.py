import streamlit as st

def show_team_info():
    st.header("? �� �Ұ�")
    
    st.subheader("�츮 ���� ��ǥ")
    st.write("AI ê���� Ȱ���� ȿ������ �н� ���� �ý��� ����")
    
    st.subheader("? ���� �Ұ� �� ����")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**ȫ�浿**")
        st.markdown("- ������Ʈ ����")
        st.markdown("- Gemini AI ����")
        
    with col2:
        st.markdown("**��ö��**")
        st.markdown("- ����Ʈ���� ����")
        st.markdown("- UI/UX ������")
        
    with col3:
        st.markdown("**�̿���**")
        st.markdown("- �鿣�� ����")
        st.markdown("- �����ͺ��̽� ����")

# ���� �ۿ��� ȣ��
if __name__ == "__main__":
    st.set_page_config(page_title="AI �н� �����", layout="wide")
    show_team_info()
    # ������ �� ����...

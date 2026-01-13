import streamlit as st
from chempy import balance_stoichiometry
import re

# ===== CẤU HÌNH TRANG =====
st.set_page_config(
    page_title="Cân Bằng Phương Trình Hóa Học",
    page_icon="⚗️",
    layout="wide"
)

# ===== TIÊU ĐỀ =====
st.title("⚗️ TỰ ĐỘNG CÂN BẰNG PHƯƠNG TRÌNH HÓA HỌC")
st.markdown("**Dự án STEM - Ứng dụng Toán học trong Hóa học**")
st.markdown("---")

# ===== HƯỚNG DẪN =====
with st.expander("📖 Hướng dẫn sử dụng"):
    st.markdown("""
    **Cách nhập phương trình:**
    - Viết các công thức hóa học với chữ in hoa cho nguyên tố (VD: `Fe`, `O2`, `H2SO4`)
    - Sử dụng dấu `->` hoặc `=` để ngăn cách chất phản ứng và sản phẩm
    - VD hợp lệ:
        - `Fe + O2 -> Fe2O3`
        - `C2H5OH + O2 -> CO2 + H2O`
        - `KMnO4 + HCl -> KCl + MnCl2 + Cl2 + H2O`
    """)

# ===== PHẦN NHẬP LIỆU =====
col1, col2 = st.columns([3, 1])

with col1:
    equation_input = st.text_input(
        "Nhập phương trình chưa cân bằng:",
        placeholder="VD: Fe + O2 -> Fe2O3",
        help="Viết công thức theo chuẩn hóa học"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    balance_button = st.button("⚖️ Cân Bằng", type="primary", use_container_width=True)

# ===== XỬ LÝ CÂN BẰNG =====
if balance_button and equation_input:
    try:
        # Tách phương trình thành reactants và products
        if '->' in equation_input:
            reactants_str, products_str = equation_input.split('->')
        elif '=' in equation_input:
            reactants_str, products_str = equation_input.split('=')
        else:
            st.error("❌ Vui lòng sử dụng `->` hoặc `=` để ngăn cách!")
            st.stop()
        
        # Parse reactants và products
        reactants = {}
        products = {}
        
        for compound in reactants_str.split('+'):
            compound = compound.strip()
            if compound:
                reactants[compound] = 1
        
        for compound in products_str.split('+'):
            compound = compound.strip()
            if compound:
                products[compound] = 1
        
        # Gọi ChemPy để cân bằng
        balanced_reactants, balanced_products = balance_stoichiometry(reactants, products)
        
        # ===== HIỂN THỊ KẾT QUẢ =====
        st.success("✅ Đã cân bằng thành công!")
        
        # Tạo chuỗi LaTeX cho phương trình cân bằng
        def format_equation(compounds_dict):
            terms = []
            for compound, coef in compounds_dict.items():
                if coef == 1:
                    terms.append(f"\\ce{{{compound}}}")
                else:
                    terms.append(f"{coef}\\ce{{{compound}}}")
            return " + ".join(terms)
        
        reactants_latex = format_equation(balanced_reactants)
        products_latex = format_equation(balanced_products)
        
        st.markdown("### 🎯 Kết quả:")
        st.latex(f"{reactants_latex} \\longrightarrow {products_latex}")
        
        # Hiển thị chi tiết hệ số
        st.markdown("### 📊 Chi tiết hệ số:")
        col_r, col_p = st.columns(2)
        
        with col_r:
            st.markdown("**Chất phản ứng:**")
            for compound, coef in balanced_reactants.items():
                st.write(f"- `{compound}`: **{coef}**")
        
        with col_p:
            st.markdown("**Sản phẩm:**")
            for compound, coef in balanced_products.items():
                st.write(f"- `{compound}`: **{coef}**")
        
        # ===== PHẦN GIẢI THÍCH TOÁN HỌC =====
        with st.expander("🔬 Giải thích toán học (Dành cho học sinh giỏi)"):
            st.markdown("""
            **Bản chất của cân bằng phương trình:**
            
            Cân bằng phương trình hóa học tương đương với việc giải **hệ phương trình tuyến tính thuần nhất**:
            
            $$\\mathbf{A} \\cdot \\mathbf{x} = \\mathbf{0}$$
            
            Trong đó:
            - $\\mathbf{A}$: Ma trận stoichiometric (mỗi hàng = 1 nguyên tố, mỗi cột = 1 chất)
            - $\\mathbf{x}$: Vector hệ số cần tìm
            
            **Phương pháp giải:**
            1. Tìm **null space** (không gian nghiệm) của ma trận $\\mathbf{A}$
            2. Chọn nghiệm nguyên dương tối giản (chia cho ƯCLN)
            
            **Ví dụ:** $\\ce{Fe + O2 -> Fe2O3}$
            
            Ma trận:
            $$
            \\begin{bmatrix}
            1 & 0 & -2 \\\\
            0 & 2 & -3
            \\end{bmatrix}
            \\cdot
            \\begin{bmatrix}
            x_1 \\\\ x_2 \\\\ x_3
            \\end{bmatrix}
            = \\mathbf{0}
            $$
            
            Giải ra: $x_1 = 4, x_2 = 3, x_3 = 2$
            
            → $4\\ce{Fe} + 3\\ce{O2} \\rightarrow 2\\ce{Fe2O3}$
            """)
    
    except Exception as e:
        st.error(f"❌ Lỗi: {str(e)}")
        st.info("💡 Gợi ý: Kiểm tra lại công thức hóa học (viết hoa đúng, số đúng)")

# ===== FOOTER =====
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Phát triển bởi <b>Thầy Đăng</b> | Dự án STEM cho học sinh giỏi THCS</p>
    <p>Sử dụng thư viện: <code>ChemPy</code>, <code>Streamlit</code></p>
</div>
""", unsafe_allow_html=True)
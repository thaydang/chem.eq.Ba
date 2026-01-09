# ⚗️ Tự Động Cân Bằng Phương Trình Hóa Học

**Dự án STEM - Ứng dụng Đại số Tuyến tính trong Hóa học**

---

## 📖 Giới thiệu

Đây là ứng dụng web giúp **tự động cân bằng phương trình hóa học** sử dụng thư viện `ChemPy` (Python).

**Mục tiêu giáo dục:**
- Giúp học sinh giỏi THCS hiểu **bản chất toán học** của cân bằng phương trình
- Thấy được ứng dụng thực tế của **ma trận** và **hệ phương trình tuyến tính**
- Khuyến khích tư duy **liên môn** (Toán - Hóa)

---

## 🚀 Cài đặt & Chạy ứng dụng

### **Bước 1: Clone repository**
```bash
git clone https://github.com/thaydang/chem.eq.Ba.git
cd chem.eq.Ba
```

### **Bước 2: Cài đặt dependencies**
```bash
pip install -r requirements.txt
```

### **Bước 3: Chạy ứng dụng Streamlit**
```bash
streamlit run app.py
```

Ứng dụng sẽ mở tại: `http://localhost:8501`

---

## 📊 Ví dụ sử dụng

| Phương trình nhập vào | Kết quả cân bằng |
|----------------------|------------------|
| `Fe + O2 -> Fe2O3` | $4\ce{Fe} + 3\ce{O2} \rightarrow 2\ce{Fe2O3}$ |
| `C2H5OH + O2 -> CO2 + H2O` | $\ce{C2H5OH} + 3\ce{O2} \rightarrow 2\ce{CO2} + 3\ce{H2O}$ |
| `KMnO4 + HCl -> KCl + MnCl2 + Cl2 + H2O` | $2\ce{KMnO4} + 16\ce{HCl} \rightarrow 2\ce{KCl} + 2\ce{MnCl2} + 5\ce{Cl2} + 8\ce{H2O}$ |

---

## 🔬 Bản chất toán học

Cân bằng phương trình hóa học tương đương với việc giải **hệ phương trình tuyến tính thuần nhất**:

$$\mathbf{A} \cdot \mathbf{x} = \mathbf{0}$$

Trong đó:
- $\mathbf{A}$: Ma trận stoichiometric
- $\mathbf{x}$: Vector hệ số cần tìm

**Phương pháp:**
1. Xây dựng ma trận $\mathbf{A}$ (mỗi hàng = 1 nguyên tố)
2. Tìm **null space** (không gian nghiệm)
3. Chuẩn hóa thành số nguyên dương

📄 **Xem chi tiết:** [HUONG_DAN_TOAN_HOC.md](HUONG_DAN_TOAN_HOC.md)

---

## 🛠️ Công nghệ sử dụng

- **Streamlit**: Framework web app Python
- **ChemPy**: Thư viện hóa học Python (parsing công thức, cân bằng)
- **NumPy**: Xử lý ma trận

---

## 📚 Tài liệu tham khảo

- [ChemPy Documentation](https://pythonhosted.org/chempy/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- Sách: *Đại số tuyến tính ứng dụng* - Gilbert Strang

---

## 👨‍🏫 Tác giả

**Thầy Đăng** - Giáo viên Khoa học Tự nhiên  
Chuyên luyện thi vào trường chuyên & bồi dưỡng HSG cấp THCS

---

## 📄 License

MIT License - Tự do sử dụng cho mục đích giáo dục
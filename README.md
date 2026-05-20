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
# 🔬 HƯỚNG DẪN TOÁN HỌC: BẢN CHẤT CỦA CÂN BẰNG PHƯƠNG TRÌNH HÓA HỌC

**Dành cho học sinh giỏi cấp THCS & chuyên Toán-Hóa**

---

## 1️⃣ Đặt vấn đề

Khi cân bằng phương trình hóa học, ta cần tìm các hệ số $x_1, x_2, \ldots, x_n$ sao cho:

$$x_1 \ce{A} + x_2 \ce{B} \rightarrow x_3 \ce{C} + x_4 \ce{D}$$

**Điều kiện:**
- Số nguyên tử mỗi nguyên tố ở hai vế phải bằng nhau
- Các hệ số $x_i$ phải là **số nguyên dương**

---

## 2️⃣ Biến đổi thành bài toán đại số tuyến tính

### **Bước 1: Xây dựng ma trận stoichiometric**

Mỗi **cột** ứng với 1 chất, mỗi **hàng** ứng với 1 nguyên tố.

**Ví dụ 1:** $\ce{Fe + O2 -> Fe2O3}$

| Nguyên tố | Fe | O₂ | Fe₂O₃ |
|-----------|----|----|-------|
| Fe        | 1  | 0  | -2    |
| O         | 0  | 2  | -3    |

*(Lưu ý: Sản phẩm mang dấu âm)*

Ma trận:
$$
\mathbf{A} = \begin{bmatrix}
1 & 0 & -2 \\
0 & 2 & -3
\end{bmatrix}
$$

### **Bước 2: Giải hệ phương trình**

Ta cần tìm vector $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ sao cho:

$$\mathbf{A} \cdot \mathbf{x} = \mathbf{0}$$

Tức là:
$$
\begin{cases}
1 \cdot x_1 + 0 \cdot x_2 - 2 \cdot x_3 = 0 \\
0 \cdot x_1 + 2 \cdot x_2 - 3 \cdot x_3 = 0
\end{cases}
$$

Giải ra:
- Từ phương trình (1): $x_1 = 2x_3$
- Từ phương trình (2): $x_2 = \frac{3}{2}x_3$

Chọn $x_3 = 2$ (để các hệ số nguyên):
$$x_1 = 4, \quad x_2 = 3, \quad x_3 = 2$$

**Kết quả:**
$$4\ce{Fe} + 3\ce{O2} \rightarrow 2\ce{Fe2O3}$$

---

## 3️⃣ Ví dụ nâng cao

### **Ví dụ 2:** $\ce{C2H5OH + O2 -> CO2 + H2O}$

**Ma trận stoichiometric:**

| Nguyên tố | C₂H₅OH | O₂ | CO₂ | H₂O |
|-----------|--------|----|----|-----|
| C         | 2      | 0  | -1 | 0   |
| H         | 6      | 0  | 0  | -2  |
| O         | 1      | 2  | -2 | -1  |

$$
\mathbf{A} = \begin{bmatrix}
2 & 0 & -1 & 0 \\
6 & 0 & 0 & -2 \\
1 & 2 & -2 & -1
\end{bmatrix}
$$

Giải hệ:
$$
\begin{cases}
2x_1 - x_3 = 0 \\
6x_1 - 2x_4 = 0 \\
x_1 + 2x_2 - 2x_3 - x_4 = 0
\end{cases}
$$

Nghiệm: $x_1 = 1, x_2 = 3, x_3 = 2, x_4 = 3$

**Kết quả:**
$$\ce{C2H5OH + 3O2 -> 2CO2 + 3H2O}$$

---

## 4️⃣ Khái niệm Null Space (Không gian nghiệm)

Trong đại số tuyến tính, nghiệm của hệ $\mathbf{A} \cdot \mathbf{x} = \mathbf{0}$ tạo thành **null space** (ký hiệu $\text{Null}(\mathbf{A})$).

**Tính chất:**
- Nếu $\text{rank}(\mathbf{A}) = n - 1$ (với $n$ = số chất), null space có **chiều 1**
- Mọi nghiệm đều là bội số của 1 nghiệm cơ sở
- Ta chọn nghiệm nguyên dương có ƯCLN = 1

---

## 5️⃣ Ứng dụng thực tế

### **Tại sao cân bằng phương trình quan trọng?**

1. **Tính toán lượng chất:** Biết được tỉ lệ mol để tính khối lượng, thể tích
2. **Phản ứng oxy hóa-khử:** Cân bằng electron trao đổi
3. **Công nghiệp:** Tối ưu hóa nguyên liệu trong sản xuất

### **Ví dụ thực tế:**

Phản ứng sản xuất amoniac (Haber):
$$\ce{N2 + H2 -> NH3}$$

Cân bằng:
$$\ce{N2 + 3H2 -> 2NH3}$$

→ Để sản xuất 2 mol NH₃ cần **1 mol N₂** và **3 mol H₂**

---

## 6️⃣ Thách thức cho học sinh giỏi

**Bài tập 1:** Cân bằng phương trình khó:
$$\ce{KMnO4 + HCl -> KCl + MnCl2 + Cl2 + H2O}$$

**Bài tập 2:** Viết code Python tự giải hệ phương trình tuyến tính (không dùng ChemPy) bằng NumPy.

**Bài tập 3:** Chứng minh rằng nếu phương trình có nghiệm thì nghiệm đó là duy nhất (sai biệt 1 hằng số nhân).

---

## 7️⃣ Kết luận

Cân bằng phương trình hóa học không chỉ là kỹ năng **ghi nhớ**, mà là ứng dụng tuyệt vời của:
- ✅ **Đại số tuyến tính** (Ma trận, hệ phương trình)
- ✅ **Định luật bảo toàn khối lượng** (Lavoisier)
- ✅ **Tư duy toán học** trong khoa học tự nhiên

**Thông điệp:** Toán học là ngôn ngữ của khoa học! 🚀

---

**Tài liệu tham khảo:**
- *Introduction to Linear Algebra* - Gilbert Strang
- *Chemical Stoichiometry* - ChemPy Documentation
- Chương trình Toán THCS nâng cao (Ma trận, Hệ phương trình)
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

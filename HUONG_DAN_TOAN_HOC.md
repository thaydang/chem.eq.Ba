# 🔬 BẢN CHẤT TOÁN HỌC CỦA CÂN BẰNG PHƯƠNG TRÌNH HÓA HỌC

**Tài liệu dành cho học sinh giỏi THCS - Tích hợp STEM**

---

## 1️⃣ VẤN ĐỀ

Khi cân bằng một phương trình hóa học, ta cần tìm các **hệ số stoichiometric** (hệ số tỉ lượng) sao cho:

> **Số nguyên tử mỗi nguyên tố ở hai vế phương trình bằng nhau**

**Ví dụ:** 

$$\ce{Fe + O2 -> Fe2O3}$$

Cần tìm $x_1, x_2, x_3$ sao cho:

$$x_1\ce{Fe} + x_2\ce{O2} \longrightarrow x_3\ce{Fe2O3}$$

thỏa mãn:
- **Fe:** $x_1 = 2x_3$ (bảo toàn sắt)
- **O:** $2x_2 = 3x_3$ (bảo toàn oxygen)

---

## 2️⃣ CHUYỂN ĐỔI SANG HỆ PHƯƠNG TRÌNH TUYẾN TÍNH

### 🎯 **Bước 1: Xây dựng ma trận Stoichiometric**

Ma trận $\mathbf{A}$ có cấu trúc:
- **Mỗi hàng** = 1 nguyên tố hóa học
- **Mỗi cột** = 1 chất (reactant hoặc product)
- **Phần tử $a_{ij}$** = số nguyên tử của nguyên tố $i$ trong chất $j$

**Quy ước dấu:**
- Chất **reactant** (bên trái): dương (+)
- Chất **product** (bên phải): âm (-)

**Ví dụ:** $\ce{Fe + O2 -> Fe2O3}$

$$
\mathbf{A} = 
\begin{bmatrix}
\text{Fe:} & 1 & 0 & -2 \\
\text{O:} & 0 & 2 & -3
\end{bmatrix}
$$

Cột 1: $\ce{Fe}$ (có 1 Fe, 0 O)  
Cột 2: $\ce{O2}$ (có 0 Fe, 2 O)  
Cột 3: $\ce{Fe2O3}$ (có 2 Fe, 3 O, mang dấu âm vì là product)

---

### 🎯 **Bước 2: Thiết lập hệ phương trình thuần nhất**

Cân bằng phương trình $\Leftrightarrow$ Giải:

$$\mathbf{A} \cdot \mathbf{x} = \mathbf{0}$$

Trong đó:

$$
\mathbf{x} = 
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}
$$

là vector hệ số cần tìm.

**Ví dụ cụ thể:**

$$
\begin{bmatrix}
1 & 0 & -2 \\
0 & 2 & -3
\end{bmatrix}
\cdot
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}
=
\begin{bmatrix}
0 \\ 0
\end{bmatrix}
$$

Khai triển ra:
- $x_1 - 2x_3 = 0 \Rightarrow x_1 = 2x_3$
- $2x_2 - 3x_3 = 0 \Rightarrow x_2 = \frac{3}{2}x_3$

---

### 🎯 **Bước 3: Tìm không gian nghiệm (Null Space)**

Hệ phương trình thuần nhất **luôn có nghiệm không tầm thường** (ngoài nghiệm $\mathbf{x} = \mathbf{0}$).

**Phương pháp giải:**

1. **Chọn biến tự do:** Đặt $x_3 = t$ (tham số)
2. **Biểu diễn các biến khác:**
   - $x_1 = 2t$
   - $x_2 = \frac{3}{2}t$

3. **Vector nghiệm tổng quát:**

$$
\mathbf{x} = t
\begin{bmatrix}
2 \\ \frac{3}{2} \\ 1
\end{bmatrix}
= t \cdot \mathbf{v}
$$

với $\mathbf{v} = \begin{bmatrix} 2 \\ \frac{3}{2} \\ 1 \end{bmatrix}$ là **vector cơ sở của null space**.

---

### 🎯 **Bước 4: Tìm nghiệm nguyên dương tối giản**

Vì hệ số hóa học phải là **số nguyên dương**, ta cần:

1. **Khử phân số:** Nhân với BCNN của các mẫu số
   - $\mathbf{v} = \begin{bmatrix} 2 \\ \frac{3}{2} \\ 1 \end{bmatrix} \xrightarrow{\times 2} \begin{bmatrix} 4 \\ 3 \\ 2 \end{bmatrix}$

2. **Tối giản:** Chia cho ƯCLN (nếu có)
   - $\text{ƯCLN}(4, 3, 2) = 1$ → Đã tối giản!

3. **Kết quả:**

$$\boxed{4\ce{Fe} + 3\ce{O2} \longrightarrow 2\ce{Fe2O3}}$$

---

## 3️⃣ VÍ DỤ PHỨC TẠP HƠN

### **Phản ứng cháy ethanol:**

$$\ce{C2H5OH + O2 -> CO2 + H2O}$$

#### **Bước 1: Ma trận Stoichiometric**

|   | $\ce{C2H5OH}$ | $\ce{O2}$ | $\ce{CO2}$ | $\ce{H2O}$ |
|---|:---:|:---:|:---:|:---:|
| **C** | 2 | 0 | -1 | 0 |
| **H** | 6 | 0 | 0 | -2 |
| **O** | 1 | 2 | -2 | -1 |

$$
\mathbf{A} = 
\begin{bmatrix}
2 & 0 & -1 & 0 \\
6 & 0 & 0 & -2 \\
1 & 2 & -2 & -1
\end{bmatrix}
$$

#### **Bước 2: Giải hệ $\mathbf{A} \cdot \mathbf{x} = \mathbf{0}$**

Khử Gauss:

$$
\begin{bmatrix}
2 & 0 & -1 & 0 \\
6 & 0 & 0 & -2 \\
1 & 2 & -2 & -1
\end{bmatrix}
\xrightarrow{\text{rref}}
\begin{bmatrix}
1 & 0 & 0 & -\frac{1}{3} \\
0 & 1 & 0 & -\frac{3}{2} \\
0 & 0 & 1 & -\frac{2}{3}
\end{bmatrix}
$$

#### **Bước 3: Nghiệm tổng quát**

Đặt $x_4 = t$:

$$
\mathbf{x} = t
\begin{bmatrix}
\frac{1}{3} \\ \frac{3}{2} \\ \frac{2}{3} \\ 1
\end{bmatrix}
\xrightarrow{\times 6}
\begin{bmatrix}
2 \\ 9 \\ 4 \\ 6
\end{bmatrix}
\xrightarrow{\div 1}
\begin{bmatrix}
1 \\ 3 \\ 2 \\ 3
\end{bmatrix}
$$

#### **Kết quả:**

$$\boxed{\ce{C2H5OH + 3O2 -> 2CO2 + 3H2O}}$$

---

## 4️⃣ TẠI SAO PHƯƠNG PHÁP NÀY LUÔN HOẠT ĐỘNG?

### **Định lý Đại số tuyến tính:**

> Một hệ phương trình tuyến tính thuần nhất $\mathbf{A} \cdot \mathbf{x} = \mathbf{0}$ **luôn có nghiệm không tầm thường** nếu số ẩn > số phương trình (rank($\mathbf{A}$) < số cột).

**Áp dụng:**
- Số chất (số cột) thường > Số nguyên tố (số hàng)
- → Luôn tồn tại hệ số cân bằng hợp lệ!

**Ngoại lệ:** Phản ứng viết sai (vi phạm bảo toàn nguyên tố) → Ma trận vô nghiệm.

---

## 5️⃣ THÁCH THỨC CHO HỌC SINH GIỎI

Hãy cân bằng các phương trình sau **bằng tay** rồi kiểm tra với ứng dụng:

### **Bài 1 (Dễ):**
$$\ce{Al + HCl -> AlCl3 + H2}$$

### **Bài 2 (Trung bình):**
$$\ce{KMnO4 + HCl -> KCl + MnCl2 + Cl2 + H2O}$$

### **Bài 3 (Khó):**
$$\ce{Ca3(PO4)2 + SiO2 + C -> CaSiO3 + CO + P4}$$

---

## 6️⃣ MỞ RỘNG: ỨNG DỤNG TRONG THỰC TẾ

1. **Công nghiệp hóa chất:** Tính toán định lượng nguyên liệu
2. **Y học:** Cân bằng phản ứng sinh hóa trong cơ thể
3. **Môi trường:** Tính lượng chất gây ô nhiễm từ phản ứng cháy
4. **Vũ trụ:** Phân tích phản ứng hạt nhân trong sao

---

## 📚 TÀI LIỆU THAM KHẢO

1. Gilbert Strang - *Linear Algebra and Its Applications* (Chương Null Space)
2. ChemPy Documentation: https://github.com/bjodah/chempy
3. Khan Academy - Stoichiometry and Chemical Equations

---

**Phát triển bởi Thầy Đăng | Dự án STEM cho học sinh giỏi**
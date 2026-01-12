# ⚗️ Cân Bằng Phương Trình Hóa Học Tự Động

**Dự án STEM - Ứng dụng Toán học trong Hóa học**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![ChemPy](https://img.shields.io/badge/ChemPy-0.8.4-green?style=for-the-badge)](https://github.com/bjodah/chempy)

---

## 📖 Giới thiệu

Ứng dụng web **tự động cân bằng phương trình hóa học** dành cho học sinh THCS và người học Hóa học, được xây dựng bằng **Streamlit** và thư viện **ChemPy**.

### 🎯 Mục tiêu giáo dục:

✅ Giúp học sinh **hiểu bản chất toán học** của cân bằng phương trình  
✅ **Tích hợp STEM**: Kết nối Hóa học - Toán học (hệ phương trình tuyến tính)  
✅ Rèn luyện **tư duy logic** và kỹ năng giải quyết vấn đề  
✅ Công cụ **kiểm tra nhanh** cho bài tập và đề thi  

---

## 🚀 Tính năng

- 🔍 **Nhập phương trình chưa cân bằng** → Nhận kết quả tức thì
- 📊 **Hiển thị hệ số chi tiết** cho từng chất
- 📐 **Hiển thị LaTeX** đẹp mắt, chuẩn khoa học
- 🧮 **Giải thích toán học** (Ma trận stoichiometric, null space)
- 💡 **Gợi ý lỗi** khi nhập sai công thức

---

## 📦 Cài đặt

### **Yêu cầu hệ thống:**
- Python 3.8+
- pip (Python package manager)

### **Bước 1: Clone repository**

```bash
git clone https://github.com/thaydang/chem.eq.Ba.git
cd chem.eq.Ba
```

### **Bước 2: Cài đặt thư viện**

```bash
pip install -r requirements.txt
```

### **Bước 3: Chạy ứng dụng**

```bash
streamlit run app.py
```

Ứng dụng sẽ mở tự động tại: **http://localhost:8501**

---

## 🎓 Cách sử dụng

### **Ví dụ 1: Phản ứng đơn giản**

**Input:**
```
Fe + O2 -> Fe2O3
```

**Output:**
```
4 Fe + 3 O₂ → 2 Fe₂O₃
```

### **Ví dụ 2: Phản ứng cháy ethanol**

**Input:**
```
C2H5OH + O2 -> CO2 + H2O
```

**Output:**
```
C₂H₅OH + 3 O₂ → 2 CO₂ + 3 H₂O
```

### **Ví dụ 3: Phản ứng oxi hóa - khử phức tạp**

**Input:**
```
KMnO4 + HCl -> KCl + MnCl2 + Cl2 + H2O
```

**Output:**
```
2 KMnO₄ + 16 HCl → 2 KCl + 2 MnCl₂ + 5 Cl₂ + 8 H₂O
```

---

## 🔬 Bản chất toán học

Cân bằng phương trình hóa học = Giải **hệ phương trình tuyến tính thuần nhất**:

$$\mathbf{A} \cdot \mathbf{x} = \mathbf{0}$$

**Trong đó:**
- $\mathbf{A}$: Ma trận stoichiometric
- $\mathbf{x}$: Vector hệ số cần tìm

**Xem chi tiết:** [HUONG_DAN_TOAN_HOC.md](./HUONG_DAN_TOAN_HOC.md)

---

## 📂 Cấu trúc dự án

```
chem.eq.Ba/
│
├── app.py                      # Ứng dụng Streamlit chính
├── requirements.txt            # Danh sách thư viện
├── HUONG_DAN_TOAN_HOC.md      # Tài liệu giải thích toán học
├── .streamlit/
│   └── config.toml            # Cấu hình giao diện
└── README.md                  # File này
```

---

## 🛠️ Công nghệ sử dụng

| Công nghệ | Mục đích |
|-----------|----------|
| **Streamlit** | Framework xây dựng web app |
| **ChemPy** | Thư viện xử lý hóa học (parsing, balancing) |
| **NumPy** | Tính toán ma trận |
| **SymPy** | Giải hệ phương trình tượng trưng |

---

## 📚 Tài liệu học tập

### **Dành cho học sinh:**
1. [HUONG_DAN_TOAN_HOC.md](./HUONG_DAN_TOAN_HOC.md) - Giải thích chi tiết ma trận và null space
2. [ChemPy Documentation](https://github.com/bjodah/chempy) - Tài liệu thư viện

### **Bài tập thực hành:**
- Cân bằng 20+ phương trình từ dễ đến khó
- Thách thức: Viết code cân bằng bằng tay (không dùng ChemPy)

---

## 🎯 Roadmap

- [ ] **Version 2.0:**
  - ✅ Hỗ trợ phản ứng ion (môi trường acid/base)
  - ✅ Tính toán khối lượng chất tham gia/sản phẩm
  - ✅ Export kết quả ra PDF
  - ✅ API endpoint cho tích hợp vào hệ thống khác

- [ ] **Version 3.0:**
  - ✅ Nhận dạng phương trình từ hình ảnh (OCR)
  - ✅ Giải thích chi tiết từng bước cân bằng
  - ✅ Hỗ trợ đa ngôn ngữ (English, Vietnamese)

---

## 👨‍🏫 Tác giả

**Thầy Đăng** - Giáo viên Khoa học Tự nhiên  
📧 Email: [Your Email]  
🌐 GitHub: [@thaydang](https://github.com/thaydang)

---

## 📜 License

Dự án này được phát hành dưới giấy phép **MIT License**.

---

## 🙏 Đóng góp

Mọi đóng góp đều được chào đón! Hãy:
1. Fork repository này
2. Tạo branch mới: `git checkout -b feature/TinhNang`
3. Commit thay đổi: `git commit -m 'Thêm tính năng XYZ'`
4. Push lên branch: `git push origin feature/TinhNang`
5. Tạo Pull Request

---

## ⭐ Hỗ trợ dự án

Nếu em thấy dự án hữu ích, hãy:
- ⭐ **Star** repository này
- 🔗 **Chia sẻ** với bạn bè, thầy cô
- 💬 **Báo lỗi** hoặc góp ý qua [Issues](https://github.com/thaydang/chem.eq.Ba/issues)

---

**Phát triển với ❤️ vì giáo dục STEM Việt Nam**
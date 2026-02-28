[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*Quy trình khởi tạo theo hướng documentation-first • Quy trình làm việc README-first • kế hoạch đa ngôn ngữ đang tích cực.*

| Trọng tâm | Trạng thái hiện tại |
|---|---|
| Mức độ trưởng thành lõi | Khung bootstrap (`README`-first) |
| Đa ngôn ngữ | 10 ngôn ngữ được duy trì trong `i18n/` |
| Nguồn pipeline | `.auto-readme-work/20260301_064213/` |

---

## 📌 Tổng quan

AgInTi hiện tại là một repository khung tài liệu với quy trình làm việc theo README-first và kế hoạch tài liệu đa ngôn ngữ.

Tại thời điểm của bản nháp này, nội dung repository tập trung vào điều phối tài liệu và chuẩn bị ngôn ngữ, chưa phải là một sản phẩm runtime:

- ✅ Chưa phát hiện cây source cấp cao nào.
- ✅ Thư mục `i18n/` chứa các bản README đã dịch.
- ✅ `.auto-readme-work/20260301_064213/` lưu trữ bối cảnh pipeline hoạt động cho lần chạy này.
- ✅ `.auto-readme-work/20260228_184104/` được giữ lại như một tài liệu lịch sử.

### Ảnh chụp nhanh trạng thái repository

| Mục | Trạng thái hiện tại |
|---|---|
| 🧩 Mã nguồn | Chưa được phát hiện |
| ⚙️ Runtime manifests | Chưa được phát hiện |
| 🧪 CI workflows | Chưa được phát hiện |
| 🧭 Không gian làm việc tài liệu | `.auto-readme-work/20260301_064213/` |
| 🌐 Tài liệu đã dịch | 10 ngôn ngữ trong `i18n/` |

---

## 🚦 Trạng thái dự án

Đây là bản draft tiếng Anh đầu tiên đầy đủ, theo hướng cập nhật tăng dần và phản ánh đúng repository.

- Trạng thái vẫn tập trung vào bootstrap/tài liệu.
- Các phần nội dung có tính chất cốt lõi hiện có đã được giữ nguyên và mở rộng thay vì thay thế.
- Các thông tin chưa rõ được đánh dấu rõ ràng và không suy diễn.

Nếu có README bản gốc chuẩn trong một branch hoặc lịch sử khác, các bản cập nhật sau nên hợp nhất theo hướng tăng dần.

---

## ✨ Tính năng

- Repository theo layout documentation-first
- Pipeline quản lý README đa ngôn ngữ tập trung tại `.auto-readme-work/`
- Các mẫu chuyển đổi ngôn ngữ và tệp ánh xạ dịch thuật rõ ràng
- Các snippet lệnh thực hành để kiểm tra và xác minh repository
- Quy trình cập nhật README được theo dõi chặt chẽ với dedupe cho banner/support blocks

---

## 🗂️ Cấu trúc dự án

```text
AgInTi/
├── .auto-readme-work/
│   ├── 20260301_064213/
│   │   ├── language-nav-root.md
│   │   ├── language-nav-i18n.md
│   │   ├── pipeline-context.md
│   │   ├── repo-structure-analysis.md
│   │   └── translation-plan.txt
│   └── 20260228_184104/
│       ├── language-nav-root.md
│       ├── language-nav-i18n.md
│       ├── pipeline-context.md
│       ├── repo-structure-analysis.md
│       ├── translated-files.txt
│       └── translation-plan.txt
├── i18n/
│   ├── README.ar.md
│   ├── README.de.md
│   ├── README.es.md
│   ├── README.fr.md
│   ├── README.ja.md
│   ├── README.ko.md
│   ├── README.ru.md
│   ├── README.vi.md
│   ├── README.zh-Hans.md
│   └── README.zh-Hant.md
└── README.md
```

### Các nguồn tài liệu chính

| Tệp | Mục đích |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | Ràng buộc sinh README và ngữ cảnh cho lần chạy này. |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | Ảnh chụp nhanh cấu trúc đã phát hiện và các khoảng trống dự án. |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | Ánh xạ locale-to-file cho các bản dịch. |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | Dòng chuyển đổi ngôn ngữ chuẩn cho `README.md`. |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | Dòng chuyển đổi ngôn ngữ chuẩn cho các file trong `i18n/`. |

---

## 🧰 Yêu cầu tiên quyết

Không có phụ thuộc runtime nào cần thiết cho trạng thái hiện tại của repository.

Để sử dụng và bảo trì tài liệu, bạn cần:

- `git`
- Một shell tương thích POSIX (ví dụ: `bash`)
- Trình soạn thảo văn bản cho Markdown

---

## 📥 Cài đặt

Hiện chưa có quá trình cài đặt/xây dựng.

Để kiểm tra repository tại máy local:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Cách sử dụng

Mục đích sử dụng hiện tại là bảo trì tài liệu, kiểm toán, và đồng bộ hóa bản địa hóa.

### Common workflows

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Quy trình README thông thường

1. Đọc các artifact ngữ cảnh hiện tại trong `.auto-readme-work/20260301_064213/`.
2. Rà soát nội dung README nguồn và các bản dịch.
3. Áp dụng chỉnh sửa tăng dần để tránh loại bỏ chi tiết cốt lõi đã có.
4. Giữ nhất quán các block chuyển đổi ngôn ngữ và hỗ trợ giữa các locale.

---

## ⚙️ Cấu hình

Hiện chưa có file cấu hình ứng dụng nào.

Cấu hình cấp tài liệu hiện tại được biểu diễn bởi:

- `.auto-readme-work/20260301_064213/translation-plan.txt` cho mục tiêu locale
- Mẫu chuyển đổi ngôn ngữ trong `.auto-readme-work/20260301_064213/language-nav-root.md` và `.../language-nav-i18n.md`
- Bối cảnh cấu trúc repository trong `.auto-readme-work/20260301_064213/repo-structure-analysis.md`

---

## 🧪 Ví dụ

### Ví dụ 1: Xác minh dòng chuyển đổi ngôn ngữ

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Ví dụ 2: Xác nhận phạm vi dịch

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Ví dụ 3: Xác nhận trạng thái scaffold (dự kiến: không có manifests)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Ghi chú phát triển

- Giữ file này làm nguồn tài liệu tiếng Anh chuẩn.
- Bảo toàn các phần cốt lõi khi cập nhật (chính sách chỉnh sửa increment-only).
- Chỉ thêm hướng dẫn runtime khi ứng dụng, manifest và toolchain tương ứng đã có.
- Giữ các block support và banner được khử trùng lặp (chính xác một block mỗi loại).
- Cập nhật roadmap và troubleshooting sớm nhất có thể khi tính năng thực tế được thêm vào.

---

## 🩺 Khắc phục sự cố

### Tôi chỉ thấy các tệp tài liệu

Đây là điều mong đợi trong trạng thái bootstrap; không phát hiện source/runtime manifests.

### Tài liệu ngôn ngữ không nhất quán

Sử dụng kế hoạch dịch mới nhất và chạy lại quy trình đồng bộ README để chuẩn hóa cấu trúc và liên kết.

### Nhánh local bị lạc hậu

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Lộ trình

- Thêm lớp ứng dụng/sản phẩm cụ thể khi mã nguồn được đưa vào.
- Mở rộng hướng dẫn setup, build và run từ manifest thực tế.
- Thêm CI workflows và kiểm tra tài liệu.
- Mở rộng chuẩn đóng góp cho mã nguồn và dịch thuật.
- Giữ các README đa ngôn ngữ đồng bộ và cập nhật.

---

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón.

1. Mở một issue kèm ngữ cảnh và phạm vi thay đổi.
2. Tạo branch chuyên biệt.
3. Giữ nội dung thay đổi có trọng tâm và tăng dần.
4. Bảo toàn các chi tiết kỹ thuật và bối cảnh section hiện có.
5. Mở PR với ghi chú xác minh rõ ràng.

### Quy trình gợi ý

```bash
git checkout -b feat/your-change
# edit README + relevant files
git add README.md

git commit -m "docs: update README"

git push -u origin feat/your-change
```

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📄 License

Chưa có tệp `LICENSE` nào trong repository.

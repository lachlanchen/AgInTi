[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

Kho chứa tài liệu theo định hướng documentation-first để duy trì một README tiếng Anh đầy đủ và tài liệu đa ngôn ngữ được đồng bộ.

## 🧭 Điều hướng nhanh

| Loại | Đích |
|---|---|
| Luồng làm việc repository | [Phạm vi và snapshot](#-scope-and-snapshot) |
| Ví dụ sử dụng | [Usage](#-usage) |
| Hướng dẫn đóng góp | [Contribution](#-contribution) |
| Hỗ trợ dự án này | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 Tóm tắt nhanh

| 🎯 Trọng tâm | 🧩 Giá trị hiện tại |
| --- | --- |
| Mục tiêu repository | Khung tài liệu khởi tạo cho đồng bộ hóa README đa ngôn ngữ |
| Nguyên tắc cốt lõi | Chỉnh sửa gia tăng giữ nguyên lịch sử nội dung | 
| Trạng thái hiện tại | Không phát hiện ứng dụng hoặc dịch vụ chạy được trong snapshot repository |

---

| ✅ Snapshot | 📌 Trạng thái hiện tại |
| --- | --- |
| Giai đoạn repository | Scaffold được điều phối bởi `.auto-readme-work/` |
| Bản địa hóa | 10 biến thể README đã dịch |
| Runtime đã xác nhận | Không phát hiện app/dịch vụ có thể chạy |

## 📌 Tổng quan

AgInTi là một repository **documentation-bootstrap**.

Repository tập trung vào tài liệu README-first, khung địa phương hóa, và pipeline làm việc lặp để sinh ra tài liệu đa ngôn ngữ nhất quán.

- ✅ Chưa phát hiện cây mã nguồn runtime cấp top-level.
- ✅ `i18n/` chứa 10 biến thể README đã dịch.
- ✅ `.auto-readme-work/` lưu trữ artifacts pipeline cho các lần cập nhật tài liệu lặp.
- ✅ Nội dung hiện hữu được giữ nguyên thông qua cập nhật gia tăng.

## ✅ Phạm vi và snapshot

| Mục | Trạng thái hiện tại |
|---|---|
| 🧩 Source code | Chưa phát hiện |
| 🧪 Kiểm thử/CI | Chưa phát hiện |
| 📘 Luồng tài liệu | Dựa vào `.auto-readme-work/` |
| 🌐 Tài liệu đã địa phương hóa | Duy trì 10 locale |
| 🔒 Tệp giấy phép | Không có trong snapshot hiện tại |

## ✨ Tính năng

- Chiến lược tài liệu theo hướng README-first.
- Workflow nhận diện ngôn ngữ với liên kết canonical cho trang gốc và các trang bản địa hóa.
- Dedupe banner và khối hỗ trợ ở đúng vị trí quy định.
- Cập nhật gia tăng mà vẫn giữ các phần nội dung quan trọng.
- Các snippet kiểm tra/điều tra thực tiễn cho người đóng góp tài liệu.

## 🗂️ Cấu trúc dự án

```text
AgInTi/
├── README.md
├── README.md.auto-readme-support
├── README.md.auto-readme-support.filtered
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
└── .auto-readme-work/
    ├── 20260228_184104/
    ├── 20260301_064213/
    ├── 20260301_064740/
    ├── 20260301_065835/
    └── 20260301_070633/
```

## 🧱 Mô hình kiến trúc và workflow

Ở giai đoạn này, “kiến trúc” là pipeline tài liệu của repository:

1. Mỗi lần chạy tạo context và ràng buộc tại `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Các template chuyển đổi ngôn ngữ được tạo trong `language-nav-root.md` / `language-nav-i18n.md`.
3. README được chỉnh sửa theo kiểu incremental để giữ nguyên lịch sử nội dung nền tảng.
4. Các file đã bản địa hóa được đồng bộ từ cùng một template cấu trúc.

## 📚 Đầu vào tài liệu và artifacts đã sinh

| Tệp | Mục đích |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | Ràng buộc và hướng dẫn cho lượt chạy này. |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | Ánh xạ locale cho đồng bộ đa ngôn ngữ. |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | Dòng chuyển ngôn ngữ chuẩn cho `README.md`. |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | Dòng chuyển ngôn ngữ chuẩn cho các README đã dịch trong `i18n/`. |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | Snapshot repository dùng cho lượt sinh lần này. |
| `README.md.auto-readme-support*` | Manifest hỗ trợ dùng trong các pass bootstrap trước. |

## 🧭 Mục tiêu workflow của repository

Repository này được giữ cố tình gọn. Mục tiêu dài hạn là giữ README gốc và các bản dịch đồng bộ mà không làm hồi quy ngữ cảnh kỹ thuật, liên kết, và cấu trúc.

## 🧰 Điều kiện tiên quyết

- `git` để truy cập repository.
- Shell tương thích POSIX (ví dụ dùng `bash`).
- Trình chỉnh sửa hiểu Markdown.

### Giả định runtime

Hiện chưa có yêu cầu build/runtime xác định vì snapshot này chưa phát hiện manifest cho sản phẩm chạy được.

## 📥 Cài đặt

Chưa có quy trình cài nhị phân hoặc build.

```bash
# Clone repository
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Sử dụng

Mục đích sử dụng hiện tại tập trung vào bảo trì tài liệu và tính nhất quán đa ngôn ngữ.

### Các lệnh thông dụng

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### Quy trình đồng bộ README điển hình

1. Xem context chạy trong `.auto-readme-work/20260301_070633/pipeline-context.md`.
2. Kiểm tra template chuyển ngôn ngữ trong `.auto-readme-work/20260301_070633/language-nav-*.md`.
3. Chỉnh sửa `README.md` theo kiểu gia tăng; không xóa các phần nội dung cốt lõi hiện hữu.
4. Giữ banner và support block duy nhất và đúng vị trí yêu cầu.
5. Căn chỉnh các file đã dịch trong `i18n/README.*.md` theo cùng cấu trúc khi cần.

## ⚙️ Cấu hình

Chưa có cấu hình ứng dụng.
Hành vi tài liệu cấp repository được xác định bởi artifacts workflow trong `.auto-readme-work/` và các tệp locale trong `i18n/`.

- `pipeline-context.md` (ràng buộc và mục tiêu)
- `translation-plan.txt` (phạm vi locale và ánh xạ)
- `language-nav-root.md` và `language-nav-i18n.md` (độ nhất quán điều hướng)
- `README.md.auto-readme-support*` (helpers scaffold)

## 🧪 Ví dụ

### Ví dụ 1: Kiểm tra các dòng language selector

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### Ví dụ 2: Xác nhận locales được hỗ trợ và tệp dịch

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### Ví dụ 3: Xác nhận trạng thái scaffold

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Ghi chú phát triển

- Dùng chỉnh sửa gia tăng để giữ ngữ cảnh kỹ thuật đã có.
- Không thêm bước cài/build runtime nếu chưa có manifest ứng dụng phù hợp.
- Đảm bảo banner và khối support chỉ xuất hiện đúng một lần.
- Khi chưa rõ hành vi repository, hãy ghi rõ giả định.
- Giữ ví dụ lệnh gắn với file và thư mục tồn tại.

## 🩺 Khắc phục sự cố

### Tôi chỉ thấy file markdown

Điều này là bình thường trong giai đoạn bootstrap.

### Bộ chọn ngôn ngữ hiển thị không nhất quán

So sánh từng `README.*.md` với dòng ngôn ngữ của root và các file ngữ cảnh pipeline mới nhất trong `.auto-readme-work/20260301_070633/`.

### Nhánh của tôi bị trễ

```bash
git fetch origin
git pull --ff-only
```

### Tôi muốn thêm hướng dẫn code

Chỉ thêm lệnh build/run sau khi thêm manifest cụ thể (ví dụ `package.json`, `pyproject.toml`, `Cargo.toml`, v.v.) và xác nhận các tài nguyên đó tồn tại trong repository.

## 🗺️ Lộ trình

- Bổ sung thành phần ứng dụng/runtime thực tế.
- Mở rộng hướng dẫn cài đặt, runtime và triển khai khi có code và tooling.
- Thêm kiểm tra CI cho chất lượng markdown và sự tương đương locales.
- Giữ quy trình dịch tái tạo được qua các pipeline versioned rõ ràng.
- Bổ sung hướng dẫn đóng góp cho cả tài liệu và những người đóng góp code tương lai.

## 🤝 Đóng góp

Đóng góp luôn được chào đón.

1. Tạo một issue mô tả thay đổi.
2. Mở branch riêng.
3. Giữ thay đổi tối thiểu và gia tăng.
4. Bảo toàn các phần nội dung có ý nghĩa.
5. Nộp pull request kèm ghi chú xác minh ngắn gọn.

### Luồng đề xuất

```bash
git checkout -b docs/your-update
# edit README.md và/hoặc i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 Giấy phép

Giấy phép vẫn chưa được thêm trong snapshot repository này.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 Tổng quan

AgInTi hiện đang ở giai đoạn khởi tạo/dựng khung. Tại thời điểm bản nháp README này được tạo, repository chủ yếu bao gồm:

- Metadata Git (`.git/`)
- Thư mục `i18n/` đã được chuẩn bị cho các tệp README đa ngôn ngữ
- Không gian làm việc `.auto-readme-work/` chứa ngữ cảnh pipeline tạo README và các hiện vật lập kế hoạch ngôn ngữ

Hiện chưa phát hiện mã nguồn ứng dụng, tệp manifest package, entrypoint runtime, hay workflow CI trong cây thư mục làm việc hiện tại.

### Ảnh chụp trạng thái repository

| Mục | Trạng thái hiện tại |
| --- | --- |
| Mã nguồn | Chưa phát hiện |
| Runtime manifests | Chưa phát hiện |
| CI workflows | Chưa phát hiện |
| Không gian làm việc tài liệu | `.auto-readme-work/20260228_184104/` |
| Thư mục i18n | Có (`i18n/`) |

## 🚦 Trạng thái dự án

Đây là **bản nháp README hoàn chỉnh đầu tiên** cho repository.

- Trạng thái repository được quan sát: **chưa có cây mã nguồn cấp cao nhất**
- Baseline README canonical hiện có: **không có trong workspace cục bộ trong lần chạy này**
- Cách tiếp cận tài liệu được dùng ở đây: giữ lại mọi chi tiết chính xác theo repository đã phát hiện và gắn nhãn rõ ràng cho phần chưa biết thay vì xóa hoặc bịa nội dung

Nếu có README canonical lịch sử ở nhánh/lịch sử từ xa, bản nháp này nên được hợp nhất tăng dần với nội dung đó thay vì thay thế các phần quan trọng.

## ✨ Tính năng (Hiện tại)

Các khả năng hiện tại của repository tập trung vào tài liệu/pipeline:

- Không gian làm việc pipeline tạo README dưới `.auto-readme-work/`
- Lập kế hoạch mục tiêu README đa ngôn ngữ (11 ngôn ngữ bao gồm tiếng Anh)
- Mẫu điều hướng ngôn ngữ cho thư mục gốc và `i18n/`

Các tính năng sản phẩm/runtime dự kiến hiện chưa xác định ở giai đoạn này.

## 🗂️ Cấu trúc dự án

```text
AgInTi/
├── .auto-readme-work/
│   └── 20260228_184104/
│       ├── pipeline-context.md
│       ├── repo-structure-analysis.md
│       ├── language-nav-root.md
│       ├── language-nav-i18n.md
│       └── translation-plan.txt
├── .git/
└── i18n/
```

### Các đầu vào tài liệu chính

| Tệp | Mục đích |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | Xác định các ràng buộc README và ngữ cảnh quy trình tạo cho lần chạy này. |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | Tóm tắt cấu trúc repository đã phát hiện và các khoảng trống đã biết. |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | Dòng chuyển ngôn ngữ canonical cho `README.md` ở thư mục gốc. |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | Dòng chuyển ngôn ngữ canonical cho các tệp dịch trong `i18n/`. |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | Ánh xạ locale-tệp cho các bản dịch. |

## 🧰 Điều kiện tiên quyết

Hiện không yêu cầu điều kiện runtime nào để sử dụng nội dung repository như hiện trạng.

Đối với quy trình tài liệu và thao tác repository, bạn nhiều khả năng cần:

- `git`
- Một shell tương thích POSIX (ví dụ dùng `bash`)
- Trình soạn thảo văn bản

## 📥 Cài đặt

Do chưa có manifest ứng dụng/package, hiện chưa có bước cài đặt/build.

Clone repository:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Sử dụng

Cách sử dụng thực tế hiện tại là kiểm tra repository và làm việc với tài liệu README/i18n.

Ví dụ:

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ Cấu hình

Hiện chưa phát hiện tệp cấu hình ứng dụng nào.

Các tín hiệu cấu hình repository đã biết:

- Git remote được cấu hình là `origin git@github.com:lachlanchen/AgInTi.git`
- Điều hướng README đa ngôn ngữ và ánh xạ locale mục tiêu trong `.auto-readme-work/20260228_184104/`

## 🧪 Ví dụ

### Ví dụ 1: Xác thực tính nhất quán của điều hướng ngôn ngữ README

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### Ví dụ 2: Xác nhận tập mục tiêu bản dịch

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### Ví dụ 3: Xác minh repository chưa có runtime manifests

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ Ghi chú phát triển

- Repository có vẻ đang ở giai đoạn bootstrap ban đầu.
- Thiết lập README-first đang được tiến hành, với cấu trúc đa ngôn ngữ đã được chuẩn bị.
- Không phát hiện lịch sử commit cục bộ trong quá trình phân tích cấu trúc (`No commits yet on main` đã được ghi nhận trong ngữ cảnh phân tích).
- Khi thêm mã nguồn, hãy cập nhật README này với hướng dẫn thiết lập, sử dụng và cấu hình cụ thể.

## 🩺 Khắc phục sự cố

### `README.md` bị thiếu trong các bản cục bộ/cũ

Nếu bản clone cục bộ của bạn trước đó không có `README.md`, hãy đồng bộ từ trạng thái nhánh mới nhất:

```bash
git fetch origin
git pull --ff-only
```

### `i18n/` tồn tại nhưng thiếu các tệp dịch

Đây là điều được dự kiến ở giai đoạn bản nháp sớm. Các mục tiêu bản dịch được định nghĩa trong:

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### Không rõ stack runtime của dự án

Nếu bạn không thấy `src/`, manifest, hoặc entrypoint, điều này khớp với trạng thái hiện được quan sát. Hãy bổ sung chi tiết stack khi các tệp triển khai được thêm vào.

## 🗺️ Lộ trình

Các mục tiêu ngắn hạn cho tài liệu và bootstrap dự án:

- Hoàn thiện README tiếng Anh baseline với mục đích và kiến trúc dự án thực tế
- Thêm các tệp README đã dịch trong `i18n/` theo kế hoạch dịch
- Bổ sung bố cục mã nguồn ứng dụng và (các) runtime manifest
- Bổ sung lệnh thiết lập và chạy có thể tái lập
- Thêm kiểm tra CI (lint/test/docs validation) khi codebase đã tồn tại

## 🤝 Đóng góp

Đóng góp luôn được chào đón. Vì repository đang ở giai đoạn thiết lập ban đầu:

1. Mở một issue mô tả thay đổi đề xuất (tài liệu, cấu trúc, hoặc bố cục mã ban đầu).
2. Tạo một feature branch.
3. Giữ thay đổi tập trung và có tài liệu.
4. Cập nhật tài liệu README/i18n bất cứ khi nào hành vi hoặc cấu trúc thay đổi.
5. Gửi pull request với ngữ cảnh rõ ràng và các bước xác minh.

Quy trình làm việc cục bộ được đề xuất:

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 Hỗ trợ

Hiện chưa có kênh hỗ trợ, tài trợ hoặc quyên góp chuyên dụng nào được khai báo trong các tệp repository.

Nếu sau này có thêm liên kết hỗ trợ, hãy thêm vào đây và giữ nguyên qua các lần chỉnh sửa README.

## 📄 Giấy phép

Thông tin giấy phép chưa được khai báo trong nội dung repository hiện tại.

- Trạng thái: `TBD`
- Bước tiếp theo được khuyến nghị: thêm tệp `LICENSE` và cập nhật mục này với định danh SPDX chính xác.

## 🧾 Giả định và ghi chú bảo toàn

- Bản nháp này được xây dựng từ các tệp repository hiện có trong `/home/lachlan/ProjectsLFS/AgInTi`.
- README canonical có sẵn từ trước không có trong môi trường cục bộ tại thời điểm tạo; vì vậy không thể nhập nội dung quan trọng nào từ đó.
- Theo chính sách bảo toàn, các chi tiết chưa biết hoặc còn thiếu được đánh dấu rõ ràng thay vì đoán hoặc lược bỏ.

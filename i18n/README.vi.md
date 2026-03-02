[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#-cau-truc-du-an)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#-pham-vi-va-anh-chup-hien-trang)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#-giay-phep)
[![Principle-Sear%20Creation-ef4444?style=flat-square&logo=firefox&logoColor=white)](#-tong-quan)
[![Principle-Self--Healing-10b981?style=flat-square&logo=wrench&logoColor=white)](#-tinh-nang)
[![Principle-Chain%20of%20Prompt%20Tools-3b82f6?style=flat-square&logo=chainlink&logoColor=white)](#-kien-truc)

Kho mã scaffold theo hướng tài liệu trước, dùng để duy trì một README tiếng Anh đầy đủ và bộ tài liệu đa ngôn ngữ luôn đồng bộ, được dẫn dắt bởi ba nguyên tắc vận hành cốt lõi: **sear creation tools**, **self-healing tools** và **chain of prompt tools**.

## 🧭 Điều hướng nhanh

| Loại | Đích đến |
| --- | --- |
| Tóm tắt dự án | [Tổng quan](#-tong-quan) |
| Năng lực cốt lõi | [Tính năng](#-tinh-nang) |
| Thiết kế pipeline | [Kiến trúc](#-kien-truc) |
| Tóm tắt triết lý | [Triết lý trong một bảng](#triet-ly-trong-mot-bang) |
| Quy trình cộng tác | [Ghi chú phát triển](#-ghi-chu-phat-trien) |
| Định hướng tương lai | [Lộ trình](#-lo-trinh) |
| Ủng hộ dự án | [Support](#-support) |

---

## 📌 Phạm vi và ảnh chụp hiện trạng

| Hạng mục | Trạng thái hiện tại |
| --- | --- |
| Giai đoạn kho mã | Scaffold bootstrap cho tài liệu |
| Mã runtime | Chưa phát hiện trong snapshot hiện tại |
| Pipeline kiểm thử/CI | Chưa phát hiện trong snapshot hiện tại |
| Tài liệu bản địa hóa | 10 tệp locale dưới `i18n/` |
| Artifact pipeline | Các lần chạy có timestamp dưới `.auto-readme-work/` |
| Tệp license | Chưa có tệp độc lập (badge README: TBD) |
| Nền tảng triết lý | Sear creation + self-healing + chain of prompt tools |

## 🌍 Tổng quan

Hiện tại, AgInTi hoạt động như một pipeline vòng đời README và bản địa hóa, thay vì một ứng dụng runtime. `README.md` ở thư mục gốc là nguồn chuẩn (canonical), và các bản dịch trong `i18n/` được đồng bộ từ cấu trúc chuẩn này.

Triết lý dự án là yếu tố vận hành rõ ràng, không phải trang trí. Mỗi lần cập nhật README cần đáp ứng đủ cả ba nguyên tắc:

1. **Sear creation tools**: quy trình tạo nội dung sắc bén, có chủ đích, tạo ra tài liệu thực dụng và giàu tín hiệu từ bằng chứng kho mã còn giới hạn.
2. **Self-healing tools**: cơ chế thiên về sửa chữa để khắc phục độ lệch, loại bỏ trùng lặp và khôi phục tính nhất quán cấu trúc.
3. **Chain of prompt tools**: luồng prompt theo từng giai đoạn, có thể truy vết, để giữ được quan hệ ngữ cảnh-đầu ra xuyên suốt các lần chạy pipeline.

Kho mã này giữ lại nội dung lịch sử quan trọng thông qua cập nhật tăng dần, đồng thời bảo toàn liên kết, lệnh và metadata hỗ trợ.

### Triết lý trong một bảng

| Nguyên tắc | Mục đích | Kết quả vận hành |
| --- | --- | --- |
| **Sear creation tools** | Tạo tài liệu giàu tín hiệu từ bằng chứng giới hạn. | Các mục luôn thực dụng, cụ thể và bám vào kho mã. |
| **Self-healing tools** | Sửa lệch, trùng lặp và cấu trúc lỗi thời. | README chuẩn và README bản địa hóa luôn đồng bộ, gọn sạch. |
| **Chain of prompt tools** | Giữ các giai đoạn sinh nội dung rõ ràng, truy vết được. | Artifact pipeline lưu lại ngữ cảnh và bàn giao có thể tái lập. |

## ✨ Tính năng

- Chiến lược tài liệu README-first với tài liệu gốc chuẩn duy nhất.
- Đồng bộ đa ngôn ngữ cho 10 biến thể README trong i18n.
- Biên soạn theo pipeline thông qua artifact `.auto-readme-work/<run-id>/`.
- Bất biến một banner và một support panel để tránh lặp khối hiển thị.
- Kỷ luật cập nhật tăng dần nhằm giữ lại lịch sử kỹ thuật có giá trị.

### Ánh xạ nguyên tắc vào tính năng

| Nguyên tắc cốt lõi | Biểu hiện trong tính năng hiện tại |
| --- | --- |
| **Sear creation tools** | Soạn README chính xác từ bằng chứng kho mã và khung mục ổn định. |
| **Self-healing tools** | Kiểm tra chống trùng cho banner/support lặp, tham chiếu cũ và trôi cấu trúc. |
| **Chain of prompt tools** | Chuỗi artifact theo từng lần chạy (`pipeline-context`, template điều hướng, kế hoạch dịch) để tạo đầu ra có thể tái lập. |

## 🗂️ Cấu trúc dự án

```text
AgInTi/
├── README.md
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
    ├── 20260301_070633/
    ├── 20260302_120620/
    └── 20260302_124338/
```

## 🏗️ Kiến trúc

Ở giai đoạn này, kiến trúc ở đây là kiến trúc pipeline tài liệu, không phải kiến trúc runtime ứng dụng.

### Luồng pipeline

1. Ngữ cảnh theo từng lần chạy được ghi vào `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Tạo template điều hướng ngôn ngữ (`language-nav-root.md` và `language-nav-i18n.md`).
3. Nội dung README chuẩn được cập nhật tăng dần trong `README.md`.
4. Các README bản địa hóa trong `i18n/` được căn chỉnh theo cấu trúc chuẩn.
5. Kiểm tra chất lượng cấu trúc đảm bảo chống trùng lặp, nhất quán liên kết và bảo toàn chi tiết kỹ thuật.

### Nguyên tắc cốt lõi trong kiến trúc

- **Sear creation tools**: áp dụng ở bước tạo nội dung để các mục luôn cụ thể, đầy đủ và đúng với kho mã.
- **Self-healing tools**: áp dụng ở bước kiểm tra để loại bỏ khối trùng, sửa tham chiếu run đã cũ và khôi phục tính tương đương cấu trúc.
- **Chain of prompt tools**: áp dụng xuyên suốt artifact để mỗi giai đoạn sinh nội dung luôn rõ ràng và có thể kiểm toán.

### Điểm kiểm nguyên tắc theo giai đoạn pipeline

| Giai đoạn | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| Thu thập ngữ cảnh | Đặt ràng buộc sinh nội dung sắc bén. | Cảnh báo sớm đầu vào thiếu/không hợp lệ. | Lưu prompt nguồn và metadata lần chạy. |
| Soạn bản chuẩn | Xây dựng đầy đủ các mục README từ bằng chứng kho mã. | Ngăn hồi quy và mất nội dung ngoài ý muốn. | Giữ liên kết giữa đầu ra từng bước và artifact trước đó. |
| Căn chỉnh i18n | Duy trì đồng đều cấu trúc và chi tiết kỹ thuật giữa các locale. | Sửa độ lệch giữa tệp gốc và tệp i18n. | Mang đúng ý định từ bản chuẩn sang từng bản dịch. |
| Kiểm tra cuối | Đảm bảo khả năng đọc và bảo toàn chi tiết. | Loại bỏ banner/support bị lặp và tham chiếu cũ. | Để lại dấu vết artifact có thể kiểm toán cho lần chạy. |

## 🧾 Đầu vào tài liệu và artifact được tạo

| Tệp | Mục đích |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | Ràng buộc và mục tiêu nguồn cho lần sinh nội dung này. |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | Tóm tắt quét kho mã và trạng thái kỹ thuật suy luận được. |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | Dòng tùy chọn ngôn ngữ chuẩn cho `README.md` gốc. |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | Dòng tùy chọn ngôn ngữ chuẩn cho README trong i18n. |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | Ánh xạ locale và kế hoạch tệp i18n đích. |
| `.auto-readme-work/<older-run-id>/...` | Ngữ cảnh lịch sử cho các lần chạy pipeline README trước đó. |

## 🔧 Yêu cầu trước

- `git`
- POSIX shell (ví dụ dùng `bash`)
- Trình soạn thảo hỗ trợ Markdown

### Giả định

- Chưa có manifest dịch vụ hoặc ứng dụng chạy được trong snapshot kho mã này.
- Vì vậy hướng dẫn cài đặt/build/start hiện tại tập trung vào quy trình tài liệu.

## 📥 Cài đặt

Hiện chưa định nghĩa gói nhị phân hoặc bước build runtime.

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Cách dùng

Cách dùng hiện tại là bảo trì tài liệu và đồng bộ đa ngôn ngữ.

### Các lệnh kiểm tra thường dùng

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Quy trình đồng bộ README chuẩn

1. Đọc `.auto-readme-work/20260302_124338/pipeline-context.md`.
2. Xác minh template bộ chọn ngôn ngữ từ `language-nav-root.md` và `language-nav-i18n.md`.
3. Cập nhật `README.md` theo hướng tăng dần như nguồn sự thật.
4. Căn chỉnh các tệp `i18n/README.*.md` theo cùng cấu trúc và các chi tiết kỹ thuật quan trọng.
5. Xác nhận chỉ có đúng một banner và đúng một support panel.

## ⚙️ Cấu hình

Hiện chưa có cấu hình runtime. Hành vi tài liệu được điều khiển bởi artifact trong kho mã.

- `pipeline-context.md`: mục tiêu và ràng buộc lần chạy.
- `repo-structure-analysis.md`: bằng chứng snapshot và khoảng trống.
- `language-nav-root.md` và `language-nav-i18n.md`: tính nhất quán điều hướng.
- `translation-plan.txt`: mục tiêu locale và ánh xạ.

## 🧪 Ví dụ

### Ví dụ 1: Xác minh template điều hướng ngôn ngữ

```bash
cat .auto-readme-work/20260302_124338/language-nav-root.md
cat .auto-readme-work/20260302_124338/language-nav-i18n.md
```

### Ví dụ 2: Kiểm tra kế hoạch locale

```bash
cat .auto-readme-work/20260302_124338/translation-plan.txt
```

### Ví dụ 3: Xác nhận không có runtime manifest (snapshot hiện tại)

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Ghi chú phát triển

- Giữ lại các mục và liên kết có nội dung quan trọng từ lịch sử README chuẩn.
- Ưu tiên chỉnh sửa tăng dần thay vì viết lại phá hủy.
- Chỉ giữ một banner và một khối support.
- Giữ cấu trúc README gốc và i18n luôn đồng bộ.
- Nêu rõ giả định khi chưa chắc chi tiết runtime hoặc hạ tầng.
- Áp dụng bộ ba triết lý như rào chắn vận hành chủ động:
  - **Sear creation tools** cho biên soạn giàu tín hiệu.
  - **Self-healing tools** cho sửa chữa tính nhất quán.
  - **Chain of prompt tools** cho bàn giao tái lập giữa các giai đoạn pipeline.

## 🚑 Khắc phục sự cố

### Tôi chỉ thấy tệp Markdown và artifact pipeline

Đây là trạng thái dự kiến cho giai đoạn bootstrap hiện tại.

### Dòng chọn ngôn ngữ khác nhau giữa các tệp

Hãy dùng template chuẩn tại:

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### Nhánh của tôi đang bị tụt phía sau

```bash
git fetch origin
git pull --ff-only
```

### Tôi muốn thêm hướng dẫn runtime

Chỉ thêm hướng dẫn build/run sau khi có manifest cụ thể (ví dụ: `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`) và đã xác nhận đường dẫn trong kho mã này.

## 🗺️ Lộ trình

1. Tăng cường **sear creation tools** với template soạn README chuẩn hóa, cổng chất lượng theo từng mục và kiểm tra rõ hơn từ bằng chứng sang đầu ra.
2. Mở rộng **self-healing tools** với kiểm tra tự động cho khối trùng lặp, lệch locale, anchor nội bộ hỏng và tham chiếu run đã cũ.
3. Chuẩn hóa **chain of prompt tools** xuyên suốt các giai đoạn chạy để truy vết ngữ cảnh, sinh nội dung, dịch thuật và xác minh có thể tái lập.
4. Bổ sung luồng bảo trì tài liệu bằng một lệnh duy nhất khi kho mã có script.
5. Thêm kiểm tra CI cho chất lượng markdown, toàn vẹn liên kết và tính tương đương cấu trúc i18n.
6. Đưa vào các thành phần runtime cụ thể khi đã thêm manifest nguồn và entrypoint.
7. Chốt quyết định license ổn định và thêm tệp license độc lập.

### Lộ trình theo trọng tâm nguyên tắc

| Trọng tâm | Mục tiêu gần hạn |
| --- | --- |
| **Sear creation tools** | Cải thiện template soạn thảo và prompt mục dựa trên bằng chứng. |
| **Self-healing tools** | Tự động hóa phát hiện trùng lặp, kiểm tra anchor cũ và sửa lệch locale. |
| **Chain of prompt tools** | Chuẩn hóa hợp đồng artifact theo giai đoạn chạy để tạo đầu ra đa ngôn ngữ có thể tái lập. |

## 🤝 Đóng góp

Hoan nghênh đóng góp.

1. Mở issue mô tả thay đổi dự định.
2. Tạo nhánh gọn, tập trung.
3. Giữ chỉnh sửa tài liệu theo hướng tăng dần và đúng với kho mã.
4. Bảo toàn liên kết, lệnh và bối cảnh lịch sử quan trọng.
5. Mở pull request kèm ghi chú xác minh ngắn gọn.

### Luồng đề xuất

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/README.*.md
git add README.md i18n/README.*.md
git commit -m "docs: refine README content"
git push -u origin docs/your-update
```

## 📄 Giấy phép

TBD. Một tệp license độc lập đã được lên kế hoạch nhưng chưa có trong snapshot hiện tại.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

# Privacy Policy — Xu

**Effective: 2026-06-01 · Contact: luuhongson157@gmail.com**

> If there is a conflict between the Vietnamese and English versions, the Vietnamese version prevails (per Vietnamese law).

---

## English

### Summary
Xu is a **local-first** personal finance app: all your data (transactions, budgets, categories, notes) is stored **only on your device**, encrypted with AES-256 (SQLCipher). We do NOT collect, store, or sell your personal data.

### 1. Data Xu Collects
Xu does NOT collect any data about you. Specifically:
- NO accounts, NO login, NO email
- NO analytics, NO tracking, NO cookies
- NO location data, NO advertising identifiers
- NO access to contacts, photos, or other files unless you explicitly choose them

### 2. Data Stored on Your Device
- **SQLCipher database** (encrypted): transactions, categories, budgets, debts, goals, chat messages
- **Secure storage** (iOS Keychain / Android Keystore): PIN code (PBKDF2 hash), database key, Gemini API key (if you enter it yourself)
- **App preferences**: Dark/Light mode, language, auto-lock timeout

### 3. Third-Party Services (Optional — you choose to enable)

#### 3.1 Google Gemini AI (voluntary)
If you paste your own Gemini API key in Settings → AI, the app will send your Q&A text to the Google Gemini API. Google's policy: https://ai.google.dev/terms
- Xu does NOT see or store your key on any server (there is no Xu server)
- Questions are sent via TLS directly to Google
- You can disable AI at any time in Settings → AI → Off

#### 3.2 Google Drive (optional — backup)
If you enable "Google Drive backup", the app will upload an **encrypted** backup file to your personal Drive. Xu only requests `drive.appdata` permission (can only see files Xu creates, not your other files).

#### 3.3 Bank notification listener (Android — optional)
If enabled, the app reads bank notification content to suggest transactions. Processing is 100% **on-device** — nothing is sent anywhere.

#### 3.4 Receipt OCR (on-device)
Uses Google MLKit Text Recognition — runs completely offline on your device. Does NOT send images to any server.

### 4. Permissions
| Permission | Purpose | Optional |
|---|---|---|
| Camera | Capture receipts for OCR | Yes |
| Photo Library | Select receipt images | Yes |
| Microphone | Voice input for transactions | Yes |
| Speech Recognition | Convert voice to text | Yes |
| Face ID / Fingerprint | Unlock the app | Yes |
| Notifications | Daily reminders + budget alerts | Yes |
| Notification Listener (Android) | Read bank SMS notifications | Yes |

### 5. Your Rights
- **Access**: All data is on your device — view it anywhere in the app
- **Export**: Settings → Export CSV
- **Delete**: Settings → Delete all data (cannot be undone)
- **Portability**: Settings → Device backup

### 6. Children
Xu is not intended for users under 13. We do not collect data, so COPPA does not apply.

### 7. Policy Changes
When updated, the version and effective date at the top of this page will change. Previous versions are kept at: https://github.com/lhs157/Xu/tree/main/xu_app/docs/legal

### 8. Contact
luuhongson157@gmail.com

---

## Tiếng Việt

### Tóm tắt
Xu là ứng dụng tài chính cá nhân **local-first**: toàn bộ dữ liệu của bạn (giao dịch, ngân sách, danh mục, ghi chú) lưu trữ **chỉ trên thiết bị**, mã hoá AES-256 (SQLCipher). Chúng tôi KHÔNG thu thập, lưu trữ hoặc bán dữ liệu cá nhân của bạn.

### 1. Dữ liệu Xu thu thập
Xu KHÔNG thu thập bất kỳ dữ liệu nào về bạn. Cụ thể:
- KHÔNG có tài khoản, KHÔNG đăng nhập, KHÔNG email
- KHÔNG analytics, KHÔNG tracking, KHÔNG cookies
- KHÔNG thông tin định vị, KHÔNG identifier quảng cáo
- KHÔNG đọc danh bạ, ảnh, hoặc file khác ngoài những file bạn chủ động chọn

### 2. Dữ liệu lưu trên thiết bị
- **DB SQLCipher** (mã hoá): giao dịch, danh mục, ngân sách, nhắm nợ, mục tiêu, tin nhắn chat
- **Secure storage** (Keychain iOS / Keystore Android): mã PIN (PBKDF2 hash), khoá DB, Gemini API key (nếu bạn tự nhập)
- **App preferences**: chế độ Dark/Light, ngôn ngữ, timeout auto-lock

### 3. Dịch vụ bên thứ ba (Tuỳ chọn — bạn chọn bật)

#### 3.1 Google Gemini AI (tự nguyện)
Nếu bạn paste Gemini API key của mình vào Settings → AI, app sẽ gửi văn bản hỏi/đáp tới Google Gemini API. Chính sách của Google: https://ai.google.dev/terms
- Xu KHÔNG thấy, KHÔNG lưu key của bạn ở server (không có server Xu)
- Câu hỏi gửi qua TLS trực tiếp tới Google
- Bạn có thể tắt AI bất kỳ lúc nào ở Settings → AI → Tắt

#### 3.2 Google Drive (tuỳ chọn — backup)
Nếu bạn bật "Sao lưu Google Drive", app sẽ upload file backup **đã mã hoá** lên Drive cá nhân của bạn. Xu chỉ xin quyền `drive.appdata` (chỉ thấy file Xu tạo ra, không thấy file khác).

#### 3.3 Bank notification listener (Android — tuỳ chọn)
Nếu bạn bật, app đọc nội dung thông báo ngân hàng để gợi ý giao dịch. Xử lý 100% **trên thiết bị**, không gửi đi đâu.

#### 3.4 OCR hoá đơn (on-device)
Dùng Google MLKit Text Recognition — chạy hoàn toàn offline trên thiết bị. KHÔNG gửi ảnh lên server.

### 4. Quyền (Permissions)
| Quyền | Mục đích | Tuỳ chọn |
|---|---|---|
| Camera | Chụp hoá đơn để OCR | Có |
| Photo Library | Chọn ảnh hoá đơn | Có |
| Microphone | Voice input ghi giao dịch | Có |
| Speech Recognition | Chuyển voice → text | Có |
| Face ID / Fingerprint | Mở khoá app | Có |
| Notifications | Nhắc nhở hàng ngày + budget alert | Có |
| Notification Listener (Android) | Đọc SMS ngân hàng | Có |

### 5. Quyền của bạn
- **Truy cập**: Toàn bộ dữ liệu nằm trên thiết bị bạn, xem ở bất kỳ màn hình app
- **Xuất**: Settings → Xuất CSV
- **Xoá**: Settings → Xoá toàn bộ dữ liệu (không thể khôi phục)
- **Mang đi**: Settings → Sao lưu thiết bị

### 6. Trẻ em
Xu không nhắm tới user dưới 13 tuổi. Không thu thập dữ liệu nên không vi phạm COPPA.

### 7. Thay đổi chính sách
Khi cập nhật, version + ngày hiệu lực ở đầu trang sẽ thay đổi. Bản cũ giữ ở: https://github.com/lhs157/Xu/tree/main/xu_app/docs/legal

### 8. Liên hệ
luuhongson157@gmail.com

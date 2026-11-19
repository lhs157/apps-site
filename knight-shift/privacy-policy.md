# Privacy Policy — Knight Shift

**Last updated: 2026-11-19 · Contact: luuhongson157@gmail.com**

---

## English

Knight Shift ("the app") is a cartoon castle-defence game for iPhone, iPad and Android (`com.lhs157.knightshift`), made by Luu Hong Son, an independent developer ("we"). You play a knight who holds the castle gate through each night, shooting and dragging weapons into place. This policy explains what data the app and the services built into it handle, and why.

### 1. Optional sign-in
Version 2.0.0 has no Knight Shift account or in-game sign-in. In versions with **Settings → Account → Cloud account**, you can keep playing as a guest or sign in with Google, Facebook or Apple to sync progress. The app has no chat or user-generated content.

Google's Firebase Authentication verifies your sign-in and maintains your Knight Shift account. It processes a Firebase user ID, the sign-in provider and its user identifier, and profile details such as an email address if the provider shares them. Apple may share a private relay address. The provider handles your sign-in credentials. We use this account information to identify your save, link sign-in methods you choose and manage account access. Firebase also processes IP addresses and browser or app information to help secure authentication. See [Firebase privacy information](https://firebase.google.com/support/privacy).

### 2. Data kept on your device
Your game data stays in the app's storage on your device:

- progress: nights finished and stars earned;
- Gold and Gems, weapons, skins and charms, and achievements;
- settings: sound, vibration, language, frame rate and similar options;
- a random player ID shown in Settings, which is included in your save;
- a list of store transaction IDs that have already been credited (so a purchase is never credited twice).

We do not upload your game save to our configuration server. Uninstalling removes the app's local copy. Any cloud copy is handled separately as described in sections 3 and 11.

### 3. Cloud save (optional)
If you sign in to a Knight Shift account, your full game save is synced to Google Cloud Firestore in Singapore. It is stored under your Firebase user ID and includes your progress, inventory, settings, player ID, and in-game purchase records such as transaction IDs used to record grants and prevent duplicate credits. We use it to restore and sync your progress. The save contains no payment card details or sign-in credentials. Access by the app requires authentication as the owner of the save.

Legacy cloud save uses the platform's own service. In version 2.0.0, it is off until you turn it on in Settings:

- **iPhone and iPad:** your save is stored in your own **iCloud** account (iCloud key-value storage). Apple holds it under your Apple ID and Apple's privacy policy: https://www.apple.com/legal/privacy/.
- **Android:** your save is stored in **Google Play Games saved games**, in your own Google account, under Google's privacy policy: https://policies.google.com/privacy.

For these legacy platform saves, we do not receive a separate copy.

### 4. Leaderboards and achievements
The app uses **Game Center** (iOS) and **Google Play Games Services** (Android) for leaderboards and achievements. Your game nickname and scores are handled and shown to other players by Apple or Google, according to your own settings with them. Apple's privacy policy: https://www.apple.com/legal/privacy/. Google's: https://policies.google.com/privacy.

### 5. Ads (Google AdMob)
The app is free and shows ads from Google AdMob:

- **Rewarded ads**, only when you tap to watch one: to double your Gold, to call a Resupply, or to get a second spin.
- **Interstitial (full-screen) ads**, at natural breaks after a win, never before night 11. The default interval is 10 wins and 10 minutes; these intervals may be adjusted through remote configuration. The **Knight for Life** purchase turns interstitial ads off.

**Personalised ads.** Ads can be personalised. On iOS this happens only if you allow it in Apple's App Tracking Transparency prompt, which the app shows after night 3. If you do not allow it, the app does not use the advertising identifier (IDFA).

**What the Google Mobile Ads SDK may collect.** According to Google's own disclosures, when an ad is requested or shown the SDK may collect and send to Google: your IP address (which can be used to estimate your general location), device identifiers (on Android the advertising ID and app set ID; on iOS an app- or developer-scoped device identifier, and the IDFA if you allowed tracking), information about the ads you have seen, interactions such as app launches, taps and video views, and diagnostic data such as crash logs, app launch time, hang rate and energy use. Google uses this data to show and measure ads, prevent fraud and improve the SDK. All of it is encrypted in transit.

**Consent.** If you are in the European Economic Area, the United Kingdom, Switzerland or a US state whose law requires it, the app shows Google's consent form (User Messaging Platform) before ads are requested. You can change your choice at any time in **Settings → Manage ad consent**.

**Your controls.** On iOS you can change tracking permission in Settings → Privacy & Security → Tracking. On Android you can reset or delete your advertising ID in the system settings. You can manage Google's ad settings at https://myadcenter.google.com.

Google's policies: https://policies.google.com/privacy and https://policies.google.com/technologies/partner-sites.
Sources for the list above (checked 2026-10-19): https://developers.google.com/admob/ios/privacy/data-disclosure, https://developers.google.com/admob/android/privacy/play-data-disclosure, https://support.google.com/admob/answer/7676680.

### 6. In-app purchases
The app sells Gem packs (consumable), a Starter Pack, Knight for Life and a Season Pass. Each is a one-time purchase; there are no subscriptions. Payment goes through the App Store (Apple) or Google Play (Google) and is handled entirely by them; the app never sees your card, bank or account details. The app receives the product ID and a transaction ID so it can grant the item. You can restore non-consumable purchases in **Settings → Restore purchases**.

The app uses Unity In-App Purchasing, a library from Unity Technologies, to talk to the store. When you start or finish a purchase, this library sends Unity a purchase event: the product, the transaction ID, the store, the app version, your device model, operating system version and language, a random installation ID and session ID created by the library, and on Apple devices the identifier for vendor (IDFV). Unity uses this to run and report on its purchase service and to prevent fraud. The app does not send your advertising identifier to Unity. Unity's privacy policy: https://unity.com/legal/game-player-and-app-user-privacy-policy (source checked 2026-10-19: https://docs.unity.com/en-us/iap/privacy-and-consent/overview).

### 7. Analytics and configuration (Firebase)
The app uses **Firebase Analytics** from Google to understand how the game is played and balance it. It records gameplay events (night started, won or lost; weapons used; ads watched; purchases; screens opened) together with an app-instance ID, device model, OS and app version, language, and an approximate country estimated from the IP address. It does not receive your name or email. Advertising-related storage (such as ad_storage) is switched on only if you allow it through the App Tracking Transparency prompt or Google's consent form.

The app also uses **Firebase Remote Config** to download settings (for example turning an event on or off, or the pace of ads). Firebase processes installation identifiers and technical request information to provide this service.

Firebase privacy information: https://firebase.google.com/support/privacy. Google's policy: https://policies.google.com/privacy.

### 7a. Game configuration and news
The app downloads public game settings, descriptions, release news and update information from our Cloudflare-hosted service. These requests do not include your game save, purchase receipts or player ID. Cloudflare processes network information such as IP addresses, requested URLs and HTTP headers to deliver and protect the service. The configuration database stores game content, not player profiles. Some shared promotional content is hosted on GitHub Pages. Provider policies: https://www.cloudflare.com/privacypolicy/ and https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement.

### 8. Notifications
The app supports local reminders and remote notifications through Firebase Cloud Messaging (FCM) and, on Apple devices, Apple Push Notification service (APNs). These services process installation identifiers and push tokens to deliver messages. The app subscribes to notification topics based on its language and notification settings (daily reminders, events and pass updates). Notifications are displayed only with system permission where required. You can manage notification categories in the app and disable notifications in system settings. Firebase privacy information: https://firebase.google.com/support/privacy.

### 9. Feedback by email
The feedback button in the app opens your own Mail app with a pre-written message to luuhongson157@gmail.com. It includes the app version, your device model, OS version, language and current night. You can see and edit the message before sending. We use your email address only to reply.

### 10. Other data
The app uses vibration (haptics) and your language setting. It does not access your precise location, contacts, photos, camera or microphone. We do not sell your data.

### 11. Deleting your data
- **Knight Shift account:** We retain the account and its cloud save while the account exists. To delete both, open **Settings → Account → Cloud account → Delete account** and confirm with your sign-in provider. Deletion removes the active cloud save and the account's save on that device. Google documents its separate retention period for Firebase Authentication data. You can also request deletion by email. See [account deletion instructions](delete-data.md) and [Firebase retention information](https://firebase.google.com/support/privacy#data_processing_information).
- **On your device:** If you play as a guest, **Settings → Delete data** removes the local game save. Uninstalling removes the app's local copy.
- **iCloud:** open iOS Settings → your name → iCloud → Manage Account Storage (or Manage Storage) → Knight Shift → Delete Data.
- **Google Play Games:** open the Google Play Games app, go to Settings and use the option to delete your Play Games data for Knight Shift (or manage it at https://myaccount.google.com).
- Data held by Google for ads or analytics: https://myadcenter.google.com or Google's privacy tools. Purchase data held by Unity: unity-iap-contact@unity3d.com.

### 12. Children
The app is a general-audience game. It is not directed at children under 13 and is not in Apple's Kids category or Google Play's Families programme. It contains mild cartoon violence. We do not knowingly collect personal data from children. If you are a parent and think your child has shared data with us, email us and we will help.

### 13. Changes to this policy
If the app starts handling data in a new way (for example a new service), we will update this page before that version is released and change the date at the top.

### 14. Contact
Email: luuhongson157@gmail.com

---

## Tiếng Việt

Knight Shift ("ứng dụng") là game thủ thành hoạt hình trên iPhone, iPad và Android (`com.lhs157.knightshift`), do Luu Hong Son, một nhà phát triển độc lập ("chúng tôi"), làm ra. Bạn vào vai một hiệp sĩ giữ cổng lâu đài qua từng đêm, bắn và kéo-thả vũ khí vào vị trí. Trang này giải thích ứng dụng và các dịch vụ tích hợp trong đó xử lý dữ liệu nào, và vì sao.

### 1. Đăng nhập tùy chọn
Bản 2.0.0 không có tài khoản Knight Shift hoặc đăng nhập trong game. Trong các bản có mục **Cài đặt → Tài khoản → Tài khoản đám mây**, bạn có thể tiếp tục chơi với tư cách khách hoặc đăng nhập bằng Google, Facebook hay Apple để đồng bộ tiến độ. Ứng dụng không có chat hay nội dung do người dùng tạo.

Firebase Authentication của Google xác minh lượt đăng nhập và quản lý tài khoản Knight Shift. Dịch vụ xử lý mã người dùng Firebase, tên nhà cung cấp đăng nhập, mã người dùng tại nhà cung cấp đó và thông tin hồ sơ như email nếu nhà cung cấp chia sẻ. Apple có thể cung cấp địa chỉ email chuyển tiếp riêng tư. Nhà cung cấp đăng nhập xử lý thông tin xác thực của bạn. Chúng tôi dùng thông tin tài khoản để xác định bản lưu, liên kết phương thức đăng nhập bạn chọn và quản lý quyền truy cập. Firebase cũng xử lý địa chỉ IP và thông tin về trình duyệt hoặc ứng dụng để hỗ trợ bảo mật đăng nhập. Xem [thông tin quyền riêng tư của Firebase](https://firebase.google.com/support/privacy).

### 2. Dữ liệu lưu trên máy bạn
Dữ liệu chơi nằm trong bộ nhớ của ứng dụng trên máy bạn:

- tiến độ: các đêm đã qua và số sao đạt được;
- Vàng và Ngọc, vũ khí, skin và bùa, thành tựu;
- cài đặt: âm thanh, rung, ngôn ngữ, tốc độ khung hình và các tuỳ chọn tương tự;
- một ID người chơi ngẫu nhiên hiện trong Cài đặt và có trong bản lưu;
- danh sách mã giao dịch của store đã được cấp (để một giao dịch không bao giờ bị cộng hai lần).

Chúng tôi không tải bản lưu trò chơi của bạn lên máy chủ cấu hình của chúng tôi. Gỡ ứng dụng sẽ xóa bản lưu trên máy. Bản trên đám mây được xử lý riêng theo mục 3 và mục 11.

### 3. Lưu mây (tuỳ chọn)
Nếu bạn đăng nhập tài khoản Knight Shift, bản lưu đầy đủ được đồng bộ lên Google Cloud Firestore tại Singapore. Dữ liệu được lưu theo mã người dùng Firebase, gồm tiến độ, kho vật phẩm, cài đặt, mã người chơi và hồ sơ mua trong game, chẳng hạn mã giao dịch để ghi nhận vật phẩm đã cấp và tránh cấp trùng. Chúng tôi dùng dữ liệu này để khôi phục và đồng bộ tiến độ. Bản lưu không chứa thông tin thẻ thanh toán hoặc thông tin xác thực đăng nhập. Ứng dụng phải xác thực đúng chủ tài khoản để truy cập bản lưu.

Tính năng lưu mây cũ dùng dịch vụ của từng nền tảng. Trong bản 2.0.0, tính năng này tắt cho tới khi bạn tự bật trong Cài đặt:

- **iPhone và iPad:** bản save được lưu vào **iCloud** của chính bạn (iCloud key-value storage). Apple giữ dữ liệu này theo Apple ID của bạn và chính sách quyền riêng tư của Apple: https://www.apple.com/legal/privacy/.
- **Android:** bản save được lưu vào **Google Play Games saved games** trong tài khoản Google của bạn, theo chính sách của Google: https://policies.google.com/privacy.

Đối với bản lưu qua các dịch vụ nền tảng này, chúng tôi không nhận bản sao riêng.

### 4. Bảng xếp hạng và thành tựu
Ứng dụng dùng **Game Center** (iOS) và **Google Play Games Services** (Android) cho bảng xếp hạng và thành tựu. Biệt danh và điểm của bạn do Apple hoặc Google xử lý và hiển thị cho người chơi khác theo cài đặt của chính bạn với họ. Chính sách của Apple: https://www.apple.com/legal/privacy/. Của Google: https://policies.google.com/privacy.

### 5. Quảng cáo (Google AdMob)
Ứng dụng miễn phí và hiện quảng cáo từ Google AdMob:

- **Quảng cáo có thưởng**, chỉ khi bạn tự bấm xem: để nhân đôi Vàng, gọi Tiếp viện, hoặc có lượt quay thứ hai.
- **Quảng cáo toàn màn hình (interstitial)**, ở điểm nghỉ sau khi thắng, không trước đêm 11. Khoảng cách mặc định là 10 trận thắng và 10 phút; các khoảng cách này có thể được điều chỉnh qua cấu hình từ xa. Gói **Hiệp Sĩ Trọn Đời** tắt quảng cáo toàn màn hình.

**Quảng cáo cá nhân hoá.** Quảng cáo có thể được cá nhân hoá. Trên iOS, điều này chỉ xảy ra nếu bạn cho phép ở hộp thoại App Tracking Transparency của Apple; ứng dụng hiện hộp thoại này sau đêm 3. Nếu bạn không cho phép, ứng dụng không dùng mã định danh quảng cáo (IDFA).

**Google Mobile Ads SDK có thể thu thập gì.** Theo công bố của chính Google, khi một quảng cáo được yêu cầu hoặc hiện ra, SDK có thể thu thập và gửi cho Google: địa chỉ IP (có thể dùng để ước tính vị trí chung), mã định danh thiết bị (trên Android là mã quảng cáo và app set ID; trên iOS là mã định danh trong phạm vi ứng dụng hoặc nhà phát triển, và IDFA nếu bạn cho phép theo dõi), thông tin về các quảng cáo bạn đã xem, tương tác như mở ứng dụng, chạm, xem video, và dữ liệu chẩn đoán như nhật ký lỗi, thời gian mở ứng dụng, tỉ lệ treo, mức dùng pin. Google dùng dữ liệu này để hiển thị và đo quảng cáo, chống gian lận và cải thiện SDK. Mọi dữ liệu đều được mã hoá khi truyền đi.

**Đồng ý.** Nếu bạn ở Khu vực Kinh tế Châu Âu, Vương quốc Anh, Thụy Sĩ hoặc một bang của Mỹ có luật yêu cầu, ứng dụng hiện biểu mẫu đồng ý của Google (User Messaging Platform) trước khi yêu cầu quảng cáo. Bạn đổi lựa chọn bất cứ lúc nào ở **Cài đặt → Tùy chọn quảng cáo**.

**Bạn tự quản lý.** Trên iOS, bạn đổi quyền theo dõi ở Cài đặt → Quyền riêng tư & Bảo mật → Theo dõi. Trên Android, bạn đặt lại hoặc xoá mã quảng cáo trong cài đặt hệ thống. Cài đặt quảng cáo của Google quản lý tại https://myadcenter.google.com.

Chính sách của Google: https://policies.google.com/privacy và https://policies.google.com/technologies/partner-sites.
Nguồn cho danh sách trên (tra ngày 19/10/2026): https://developers.google.com/admob/ios/privacy/data-disclosure, https://developers.google.com/admob/android/privacy/play-data-disclosure, https://support.google.com/admob/answer/7676680.

### 6. Mua trong ứng dụng
Ứng dụng bán các gói Ngọc (hàng tiêu hao), Gói Khởi Đầu, Hiệp Sĩ Trọn Đời và Pass mùa. Mỗi món là mua một lần; không có gói đăng ký định kỳ. Việc thanh toán đi qua App Store (Apple) hoặc Google Play (Google) và do họ xử lý hoàn toàn; ứng dụng không bao giờ thấy thông tin thẻ, ngân hàng hay tài khoản của bạn. Ứng dụng chỉ nhận mã sản phẩm và mã giao dịch để cấp món đã mua. Bạn khôi phục các món mua không tiêu hao ở **Cài đặt → Khôi phục mua hàng**.

Ứng dụng dùng Unity In-App Purchasing, thư viện của Unity Technologies, để làm việc với store. Khi bạn bắt đầu hoặc hoàn tất một lần mua, thư viện này gửi cho Unity một sự kiện mua hàng: sản phẩm, mã giao dịch, store, phiên bản ứng dụng, đời máy, phiên bản hệ điều hành và ngôn ngữ, một mã cài đặt và mã phiên ngẫu nhiên do thư viện tạo, và trên máy Apple là mã định danh nhà cung cấp (IDFV). Unity dùng dữ liệu này để vận hành, báo cáo dịch vụ mua hàng và chống gian lận. Ứng dụng không gửi mã định danh quảng cáo của bạn cho Unity. Chính sách quyền riêng tư của Unity: https://unity.com/legal/game-player-and-app-user-privacy-policy (nguồn tra ngày 19/10/2026: https://docs.unity.com/en-us/iap/privacy-and-consent/overview).

### 7. Phân tích và cấu hình (Firebase)
Ứng dụng dùng **Firebase Analytics** của Google để hiểu cách game được chơi và cân bằng game. Dịch vụ ghi các sự kiện chơi (bắt đầu, thắng, thua đêm; vũ khí đã dùng; quảng cáo đã xem; giao dịch mua; màn hình đã mở) cùng mã app-instance, đời máy, phiên bản hệ điều hành và ứng dụng, ngôn ngữ, và quốc gia ước tính từ địa chỉ IP. Dịch vụ không nhận tên hay email của bạn. Phần lưu trữ liên quan quảng cáo (như ad_storage) chỉ bật khi bạn cho phép qua hộp thoại App Tracking Transparency hoặc biểu mẫu đồng ý của Google.

Ứng dụng cũng dùng **Firebase Remote Config** để tải cấu hình (ví dụ bật/tắt một sự kiện, hay nhịp hiện quảng cáo). Firebase xử lý mã định danh bản cài đặt và thông tin kỹ thuật của yêu cầu để cung cấp dịch vụ này.

Thông tin quyền riêng tư của Firebase: https://firebase.google.com/support/privacy. Chính sách của Google: https://policies.google.com/privacy.

### 7a. Cấu hình và tin tức trò chơi
Ứng dụng tải cấu hình công khai, mô tả, tin phiên bản và thông tin cập nhật từ dịch vụ của chúng tôi trên Cloudflare. Các yêu cầu này không chứa bản lưu trò chơi, biên nhận mua hàng hoặc mã người chơi. Cloudflare xử lý thông tin mạng như địa chỉ IP, URL được yêu cầu và HTTP header để chuyển dữ liệu và bảo vệ dịch vụ. Cơ sở dữ liệu cấu hình lưu nội dung trò chơi, không lưu hồ sơ người chơi. Một số nội dung quảng bá dùng chung được lưu trên GitHub Pages. Chính sách nhà cung cấp: https://www.cloudflare.com/privacypolicy/ và https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement.

### 8. Thông báo
Ứng dụng hỗ trợ lời nhắc cục bộ và thông báo đẩy qua Firebase Cloud Messaging (FCM), cùng Apple Push Notification service (APNs) trên thiết bị Apple. Các dịch vụ này xử lý mã định danh bản cài đặt và push token để chuyển thông báo. Ứng dụng đăng ký chủ đề dựa trên ngôn ngữ và cài đặt thông báo (lời nhắc hằng ngày, sự kiện và cập nhật Pass). Thông báo chỉ hiển thị khi được hệ thống cho phép tại nơi yêu cầu quyền. Bạn quản lý các nhóm thông báo trong ứng dụng hoặc tắt thông báo trong cài đặt hệ thống. Thông tin quyền riêng tư của Firebase: https://firebase.google.com/support/privacy.

### 9. Góp ý qua email
Nút góp ý trong ứng dụng mở app Mail của chính bạn với thư soạn sẵn gửi luuhongson157@gmail.com. Thư có phiên bản ứng dụng, đời máy, phiên bản hệ điều hành, ngôn ngữ và đêm hiện tại. Bạn xem và sửa được thư trước khi gửi. Chúng tôi chỉ dùng địa chỉ email của bạn để trả lời.

### 10. Dữ liệu khác
Ứng dụng dùng rung và cài đặt ngôn ngữ. Ứng dụng không truy cập vị trí chính xác, danh bạ, ảnh, camera hay micro. Chúng tôi không bán dữ liệu của bạn.

### 11. Xoá dữ liệu
- **Tài khoản Knight Shift:** Chúng tôi lưu tài khoản và bản lưu đám mây trong thời gian tài khoản còn tồn tại. Để xóa cả hai, mở **Cài đặt → Tài khoản → Tài khoản đám mây → Xóa tài khoản** và xác nhận với nhà cung cấp đăng nhập. Thao tác này xóa bản lưu đám mây đang sử dụng và bản lưu của tài khoản trên thiết bị đó. Google công bố thời hạn lưu riêng đối với dữ liệu Firebase Authentication. Bạn cũng có thể yêu cầu xóa qua email. Xem [hướng dẫn xóa tài khoản](delete-data.md) và [thông tin về thời hạn lưu dữ liệu của Firebase](https://firebase.google.com/support/privacy#data_processing_information).
- **Trên máy:** Nếu chơi với tư cách khách, **Cài đặt → Xóa dữ liệu** xóa bản lưu trên máy. Gỡ ứng dụng cũng xóa bản lưu này.
- **iCloud:** mở Cài đặt iOS → tên của bạn → iCloud → Quản lý dung lượng tài khoản (hoặc Quản lý dung lượng) → Knight Shift → Xoá dữ liệu.
- **Google Play Games:** mở app Google Play Games, vào Cài đặt và dùng tuỳ chọn xoá dữ liệu Play Games của Knight Shift (hoặc quản lý tại https://myaccount.google.com).
- Dữ liệu quảng cáo hoặc phân tích do Google giữ: https://myadcenter.google.com hoặc công cụ quyền riêng tư của Google. Dữ liệu mua hàng do Unity giữ: unity-iap-contact@unity3d.com.

### 12. Trẻ em
Đây là game cho mọi người. Ứng dụng không nhắm tới trẻ em dưới 13 tuổi, không thuộc mục Trẻ em (Kids) của Apple hay chương trình Gia đình (Families) của Google Play. Game có bạo lực hoạt hình nhẹ. Chúng tôi không cố ý thu thập dữ liệu cá nhân của trẻ em. Nếu bạn là phụ huynh và cho rằng con mình đã gửi dữ liệu cho chúng tôi, hãy gửi email để chúng tôi hỗ trợ.

### 13. Thay đổi chính sách
Nếu ứng dụng bắt đầu xử lý dữ liệu theo cách mới (ví dụ thêm một dịch vụ), chúng tôi cập nhật trang này trước khi bản đó phát hành và đổi ngày ở đầu trang.

### 14. Liên hệ
Email: luuhongson157@gmail.com

---

[← Home](../index.md) · [Support](support.md) · [Terms](terms.md)

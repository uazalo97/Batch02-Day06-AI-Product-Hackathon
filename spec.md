# AI Product Canvas — Chatbot Hỗ Trợ Đặt Lịch Khám Bệnh

---

## 1. Bằng chứng

### Nỗi đau đến từ đâu?

#### Trải nghiệm trực tiếp (quan sát nội bộ)

Nhóm thử nghiệm quy trình đặt lịch khám tại một số bệnh viện lớn (Bạch Mai, Việt Đức, Bệnh viện Đại học Y Hà Nội) theo cả hai kênh: đến trực tiếp và qua ứng dụng/hotline.

Những điểm vướng ghi nhận được:

- **Xếp hàng từ sáng sớm:** Để có số thứ tự khám trong ngày tại các bệnh viện tuyến trung ương, bệnh nhân thường phải có mặt trước 5–6 giờ sáng. Nhiều người đến lúc 7h đã không còn số.
- **Hotline thường bận hoặc không có người nghe:** Gọi thử đường dây đặt lịch của một số bệnh viện vào giờ hành chính, tỷ lệ kết nối được lần đầu thấp, phải gọi lại nhiều lần.
- **Ứng dụng hiện có thiếu thân thiện với người lớn tuổi:** Các app như MyVinmec, BookingCare yêu cầu đăng ký tài khoản, chọn chuyên khoa từ danh sách dài, điền nhiều trường thông tin — đây là rào cản lớn với người ít quen công nghệ.
- **Người dùng không biết nên khám chuyên khoa nào:** Khi có triệu chứng như "tê tay", "chóng mặt", "đau bụng âm ỉ", người bệnh không rõ nên đến Nội, Thần kinh, hay Tiêu hóa. App hiện tại không giải quyết bước này — người dùng phải tự chọn.

> ⚠️ **Lưu ý:** Các con số cụ thể (tỷ lệ cuộc gọi thành công, thời gian chờ trung bình) chưa được đo đạc chính thức — đây là **quan sát định tính đã được thành viên trong team trải nghiệm**, chưa phải dữ liệu định lượng có kiểm chứng.

---

#### Nguồn bên ngoài

**1. Đánh giá ứng dụng BookingCare trên Google Play (tham khảo công khai)**

Một số đánh giá người dùng đề cập đến khó khăn khi không biết chọn chuyên khoa nào phù hợp, hoặc phàn nàn giao diện nhiều bước khó thao tác trên điện thoại cũ.

**2. Báo cáo / bài báo về quá tải bệnh viện tuyến trên tại Việt Nam**

Theo các bài phóng sự trên VnExpress và Tuổi Trẻ, tình trạng bệnh nhân xếp hàng từ tờ mờ sáng tại các bệnh viện lớn ở Hà Nội và TP.HCM vẫn phổ biến, đặc biệt với người từ tỉnh lẻ lên khám chuyên sâu.

**3. Cách sản phẩm khác xử lý cùng vấn đề**

- **BookingCare / Medpro:** Cho phép đặt lịch theo bác sĩ hoặc chuyên khoa, nhưng không có bước tư vấn triệu chứng trước khi chọn khoa — người dùng vẫn phải tự quyết định.
- **Các chatbot bệnh viện hiện có (Vinmec, FV):** Chủ yếu cung cấp FAQ, không dẫn dắt hỏi triệu chứng rồi tự hoàn tất đặt lịch trong cùng một luồng hội thoại.

**Khoảng trống được xác nhận:** Chưa có sản phẩm nào kết hợp liền mạch: _hỏi triệu chứng → gợi ý chuyên khoa → đặt lịch ngay trong chat → phát phiếu xác nhận_, mà không cần người dùng rời khỏi hội thoại.

---

## 2. Lát cắt để build

> **Một bệnh nhân lớn tuổi mô tả triệu chứng bằng ngôn ngữ tự nhiên, AI hỏi thêm một vài câu làm rõ, gợi ý chuyên khoa phù hợp, và tạo ra phiếu đặt lịch để bệnh nhân xác nhận bằng một nút bấm duy nhất.**

Đây là luồng tối thiểu đủ để chứng minh giá trị cốt lõi:

- **Một người dùng:** Bệnh nhân low tech, ít quen công nghệ, dùng điện thoại Android phổ thông.
- **Một công việc:** Đặt được lịch khám mà không cần gọi điện hay tự chọn chuyên khoa.
- **Một quyết định AI đưa ra:** Gợi ý chuyên khoa dựa trên mô tả triệu chứng.
- **Một kết quả trả về:** Phiếu hẹn khám hiển thị trong chat, bệnh nhân bấm "Xác nhận" để hoàn tất.

---

## 3. AI Product Canvas

### Ô 1 — Giá trị (Value)

| Câu hỏi                                                  | Trả lời                                                                                                                                        |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dành cho ai?**                                         | Bệnh nhân phổ thông, đặc biệt người trung niên và cao tuổi (40+), ít quen dùng app, muốn đặt lịch mà không phải xếp hàng hay gọi hotline.      |
| **Họ đau ở đâu?**                                        | Không biết khám chuyên khoa nào; hotline bận; app hiện tại quá nhiều bước; phải đến sớm mới có số.                                             |
| **AI giải được điều gì mà cách hiện tại chưa làm được?** | Hỏi – hiểu – gợi ý – đặt lịch trong một luồng hội thoại tự nhiên, không cần người dùng biết tên chuyên khoa hay điều hướng giao diện phức tạp. |

---

### Ô 2 — Niềm tin (Trust)

| Tình huống                           | Cơ chế xử lý                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AI trả lời sai chuyên khoa**       | Hiện đề xuất dưới dạng "gợi ý" (không phải chẩn đoán), kèm lý do ngắn gọn. Bệnh nhân có thể chọn khoa khác từ danh sách hoặc yêu cầu giải thích lại.               |
| **Bệnh nhân không đồng ý với gợi ý** | Nút "Chọn chuyên khoa khác" luôn hiện sẵn. Không ép buộc.                                                                                                          |
| **Thông tin lịch hẹn sai**           | Phiếu xác nhận hiển thị đầy đủ: tên bệnh nhân, ngày giờ, chuyên khoa, bác sĩ (nếu có) — bệnh nhân đọc và bấm xác nhận mới chốt. Human-in-the-loop ở đúng điểm này. |
| **Chuyển sang người thật**           | Nếu triệu chứng phức tạp hoặc bệnh nhân yêu cầu, chatbot cung cấp số hotline trực tiếp của bộ phận đặt lịch bệnh viện.                                             |

**Tuyên bố minh bạch với người dùng:** Chatbot không phải bác sĩ, không đưa ra chẩn đoán, chỉ hỗ trợ định hướng và đặt lịch.

---

### Ô 3 — Tính khả thi (Feasibility)

| Yếu tố                   | Đánh giá                                                                                                                                                         |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Chi phí mỗi lượt gọi** | Sử dụng LLM API (GPT-4o / Claude Sonnet). Mỗi lượt hội thoại ~3–8 lượt gọi API. Chi phí ước tính $0.01–$0.05/lượt đặt lịch — chấp nhận được ở quy mô thử nghiệm. |
| **Độ trễ**               | Mục tiêu < 3 giây mỗi phản hồi. Dùng streaming để tăng cảm giác phản hồi nhanh.                                                                                  |
| **Dữ liệu cần có**       | Danh sách chuyên khoa, lịch trống của bác sĩ, thông tin cơ bản bệnh nhân (tên, SĐT, ngày sinh). Mock được cho MVP.                                               |
| **Rủi ro lớn nhất**      | AI gợi ý sai chuyên khoa dẫn đến bệnh nhân đặt nhầm → mất thời gian, giảm tin tưởng. Xử lý bằng bước xác nhận và cho phép hủy/đổi dễ dàng.                       |
| **Ngưỡng dừng**          | Nếu tỷ lệ bệnh nhân phải gọi lại hotline để sửa lịch sau khi dùng chatbot > 20%, cần xem xét lại luồng tư vấn.                                                   |

---

### Ô 4 — Tín hiệu học (Learning Signal)

| Sự kiện người dùng                               | Dữ liệu thu về                                                             | Cách dùng                                                |
| ------------------------------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| Bệnh nhân chọn chuyên khoa khác với gợi ý của AI | Cặp (triệu chứng → chuyên khoa AI gợi ý → chuyên khoa bệnh nhân thực chọn) | Cải thiện prompt / fine-tune bộ phân loại chuyên khoa    |
| Bệnh nhân hủy lịch ngay sau khi đặt              | Nội dung hội thoại dẫn đến quyết định hủy                                  | Phát hiện luồng tư vấn thiếu thông tin hoặc gây nhầm lẫn |
| Bệnh nhân sửa thông tin trên phiếu hẹn           | Trường nào bị sửa, sửa thành gì                                            | Phát hiện lỗi trích xuất thông tin từ hội thoại          |
| Bệnh nhân yêu cầu giải thích lại                 | Câu hỏi theo-up                                                            | Xác định điểm mà mô hình chưa giải thích đủ rõ           |

Tất cả tín hiệu được lưu vào log có cấu trúc, phục vụ đánh giá định kỳ (ví dụ: mỗi 2 tuần xem lại top 20 ca gợi ý sai).

---

## 4. Tăng năng lực hay Tự động hóa?

### Quyết định: **Tự động hóa có kiểm soát (Supervised Automation)**

Cụ thể hơn, đây là mô hình **"AI chuẩn bị, con người xác nhận"**:

| Bước                       | AI làm                         | Con người làm                 |
| -------------------------- | ------------------------------ | ----------------------------- |
| Hỏi triệu chứng & làm rõ   | ✅ Tự động                     | —                             |
| Gợi ý chuyên khoa          | ✅ Tự động                     | Có thể ghi đè                 |
| Điền thông tin phiếu hẹn   | ✅ Tự động                     | Có thể điền khi đặt hộ        |
| **Xác nhận đặt lịch**      | ❌ Không tự động               | ✅ **Bệnh nhân bấm xác nhận** |
| Gửi xác nhận cho bệnh viện | ✅ Tự động sau khi có xác nhận | —                             |

### Vì sao chọn mức này?

- **Hậu quả nếu sai:** Đặt nhầm lịch khám làm bệnh nhân mất thời gian, gây khó chịu và giảm tin tưởng — không nguy hiểm tính mạng nhưng đủ đau để cần human checkpoint.
- **Khả năng hoàn tác:** Dễ — bệnh nhân có thể hủy/đổi lịch ngay trong chat. Nhưng vẫn tốt hơn nếu không đặt sai ngay từ đầu.
- **Đúng với đối tượng low-tech:** Bệnh nhân lớn tuổi cảm thấy yên tâm hơn khi "được xem lại trước khi chốt", thay vì AI tự động làm hết mà họ không hiểu chuyện gì xảy ra.

---

## 5. Bốn đường đi của trải nghiệm

### Đường 1 — AI đúng và tự tin

> Bệnh nhân: "Tôi bị đau đầu, chóng mặt, tay tê mấy ngày nay."
> AI hỏi thêm: tuổi, huyết áp có cao không, có tiền sử tai biến không.
> AI gợi ý: Khoa Thần kinh. Tin tưởng cao.

**Người dùng thấy gì:**

- Tin nhắn rõ ràng: _"Dựa trên triệu chứng của bạn, tôi gợi ý khám tại **Khoa Thần kinh**. Bạn muốn đặt lịch không?"_
- Một nút xanh: **"Đặt lịch Khoa Thần kinh"**
- Phiếu hẹn hiện ra, bệnh nhân bấm **"Xác nhận"** — xong.
- Tổng thao tác: 2 lần chạm.

---

### Đường 2 — AI không chắc chắn

> Bệnh nhân: "Tôi hay mệt, ăn không ngon."
> Triệu chứng mơ hồ, nhiều khả năng: Nội tiết, Tiêu hóa, Tâm thần kinh.

**Cách xử lý:**

- AI không đưa ra một gợi ý duy nhất mà hỏi thêm: _"Bạn có sụt cân gần đây không? Giấc ngủ có ổn không?"_
- Nếu sau 2 lượt hỏi vẫn còn 2 khả năng, AI trình bày cả hai: _"Có thể phù hợp với Khoa Tiêu hóa hoặc Nội tổng hợp. Bạn muốn chọn khoa nào?"_
- Không tự ý chọn thay bệnh nhân khi độ tin cậy thấp.

---

### Đường 3 — AI sai

> AI gợi ý Khoa Cơ xương khớp, nhưng bệnh nhân biết mình đã có lịch hẹn với bác sĩ Tim mạch và triệu chứng liên quan tim.

**Cách người dùng gỡ ra:**

- Trên phiếu xác nhận luôn có nút **"Đổi chuyên khoa"** — bệnh nhân chọn lại từ danh sách.
- Hoặc gõ thẳng: _"Tôi muốn khám Tim mạch"_ — chatbot cập nhật ngay.
- Sau khi sửa, AI xác nhận lại: _"Đã cập nhật: Khoa Tim mạch. Bạn xác nhận chưa?"_
- Không bao giờ mất dữ liệu đã nhập; sửa một trường không reset toàn bộ phiếu.

---

### Đường 4 — Người dùng sửa

> Bệnh nhân nhận phiếu hẹn, thấy AI điền sai ngày sinh (1965 thay vì 1956).

**Dữ liệu đi về đâu:**

- Sự kiện sửa được log: `{field: "dob", original: "1965", corrected: "1956", session_id: "..."}`.
- Định kỳ, nhóm xem lại log để phát hiện pattern: AI hay nhầm năm sinh? Hay nhầm số điện thoại? → Cải thiện bước trích xuất thông tin từ hội thoại.
- Trong tương lai, dùng các ca sửa này làm tập test để đánh giá chất lượng trích xuất.

---

## 6. Những kiểu lỗi đáng lo nhất

### Lỗi 1 — Gợi ý sai chuyên khoa do triệu chứng mơ hồ hoặc chồng lấn

**Xuất hiện khi nào:**
Triệu chứng không đặc hiệu (mệt mỏi, chóng mặt, đau lưng) hoặc bệnh nhân dùng từ địa phương / không chuẩn xác về mặt y khoa.

**Ai chịu thiệt và nặng đến đâu:**
Bệnh nhân mất một buổi đến nhầm khoa, phải đổi lịch. Không nguy hiểm nhưng gây mất tin tưởng nghiêm trọng, đặc biệt với người lớn tuổi đi xe từ xa.

**Prototype xử lý thế nào:**

- Khi độ tự tin thấp (dưới ngưỡng nội bộ), AI hỏi thêm thay vì gợi ý ngay.
- Luôn trình bày gợi ý dưới dạng "có thể phù hợp", không dùng ngôn ngữ chắc chắn tuyệt đối.
- Cho phép đổi chuyên khoa dễ dàng trên phiếu xác nhận.
- Bước human-in-the-loop (bệnh nhân đọc và xác nhận phiếu) là lưới an toàn cuối cùng.

---

### Lỗi 2 — Bỏ qua triệu chứng khẩn cấp, tiếp tục luồng đặt lịch thông thường

**Xuất hiện khi nào:**
Bệnh nhân mô tả triệu chứng nguy hiểm nhưng dùng từ nhẹ nhàng hoặc bình thường hóa: _"tôi bị đau ngực hơi hơi mấy hôm nay"_, _"chân bị liệt một chút"_.

**Ai chịu thiệt và nặng đến đâu:**
Nghiêm trọng nhất trong danh sách. Nếu chatbot tiếp tục đặt lịch thay vì cảnh báo cấp cứu, có thể ảnh hưởng đến tính mạng bệnh nhân. Đây cũng là rủi ro pháp lý và uy tín lớn nhất của sản phẩm.

**Prototype xử lý thế nào:**

- Xây dựng danh sách từ khóa / pattern triệu chứng khẩn cấp (đau ngực, khó thở đột ngột, liệt nửa người, méo miệng, xuất huyết bất thường).
- Khi phát hiện, dừng toàn bộ luồng đặt lịch, hiện cảnh báo nổi bật: _"Triệu chứng bạn mô tả có thể cần xử lý khẩn cấp. Vui lòng gọi **115** hoặc đến cấp cứu gần nhất ngay."_
- Không đặt lịch, không gợi ý chuyên khoa — chỉ hướng đến cấp cứu.
- Đây là rule cứng (hard rule), không phụ thuộc vào phán đoán của LLM.

---

### Lỗi 3 — Trích xuất sai thông tin cá nhân vào phiếu hẹn

**Xuất hiện khi nào:**
Bệnh nhân cung cấp thông tin theo ngôn ngữ tự nhiên, không theo form: _"tôi tên Nguyễn Văn An, sinh năm sáu nhăm, số điện thoại 09... "_ — AI có thể nhầm năm sinh, thiếu số điện thoại, hoặc ghép sai tên.

**Ai chịu thiệt và nặng đến đâu:**
Phiếu hẹn sai thông tin → bệnh viện không tìm được hồ sơ → bệnh nhân bị từ chối hoặc phải làm lại thủ tục. Gây phiền toái, đặc biệt với người đi từ xa.

**Prototype xử lý thế nào:**

- Sau khi trích xuất, hiển thị từng trường thông tin rõ ràng để bệnh nhân đọc lại trước khi xác nhận.
- Cho phép chỉnh sửa từng trường riêng lẻ (không cần nhập lại toàn bộ).
- Log tất cả các lần sửa để cải thiện bước trích xuất trong các phiên bản sau.
- Đây chính là lý do phiếu xác nhận là bắt buộc, không bao giờ đặt lịch ngầm định.

## 8. Phân công thành viên

| MSSV        | Họ và tên          | Vai trò                  | Nhiệm vụ cụ thể                                                                                                                                                                |
| ----------- | ------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2A202600840 | Nguyễn Nam Thắng   | Backend — AI & Infra     | Xây dựng AI triage flow bằng LangGraph; thiết kế và duy trì API chat                                                                                                           |
| 2A202600934 | Trần Trúc Quỳnh    | Backend — Data & API     | Thiết kế database schema; xây dựng booking API và catalog API (danh sách chuyên khoa, lịch trống bác sĩ).                                                                      |
| 2A202600663 | Phạm Huy Cảnh      | Frontend — Core UI       | Xây dựng giao diện chat chính; form nhập thông tin bệnh nhân; luồng đặt lịch phía client (từ hội thoại đến phiếu hẹn); quản lý repository (repo owner, review PR, phân nhánh). |
| 2A202600855 | Nguyễn Tiến Huân   | Frontend — UX & Mobile   | Styling và tối ưu mobile UI; thiết kế quick replies (nút gợi ý nhanh); màn hình xác nhận lịch hẹn (confirmation screen).                                                       |
| 2A202600810 | Nguyễn Xuân Tới    | Spec & Prompt & Research | Viết và kiểm thử prompt cho triage flow; thu thập bằng chứng người dùng (quan sát, đánh giá app, phỏng vấn); đảm bảo spec phản ánh nhu cầu thực.                               |
| 2A202600575 | Phạm Thị Bích Ngọc | Spec & Prompt & Demo     | Lên ý tưởng và viết kịch bản demo; viết và kiểm thử prompt dưới dạng `.md`; đảm bảo luồng hội thoại tự nhiên và phù hợp đối tượng low-tech.                                    |

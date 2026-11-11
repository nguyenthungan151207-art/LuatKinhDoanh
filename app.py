
import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="LUẬT KINH DOANH | Study Studio", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
:root{--navy:#071b3a;--blue:#145da0;--cyan:#55c2e8;--ice:#eaf5ff;--ink:#14243a;}
html,body,[class*="css"]{font-family:'Poppins',sans-serif;}
.stApp{background:linear-gradient(135deg,#f4f9ff 0%,#eaf4ff 48%,#f8fbff 100%);color:var(--ink);}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#071b3a,#103d70);color:white;}
section[data-testid="stSidebar"] *{color:white!important;}
.hero{background:linear-gradient(120deg,#071b3a 0%,#145da0 62%,#218fc1 100%);padding:2.2rem 2.4rem;border-radius:24px;color:white;box-shadow:0 18px 45px rgba(9,50,95,.18);position:relative;overflow:hidden;animation:rise .7s ease-out;}
.hero:after{content:"";position:absolute;width:280px;height:280px;border:1px solid rgba(255,255,255,.18);border-radius:50%;right:-70px;top:-110px;box-shadow:0 0 0 35px rgba(255,255,255,.04),0 0 0 75px rgba(255,255,255,.03);}
.hero h1{font-size:2.1rem;line-height:1.25;margin:0 0 .5rem;font-weight:800;color:white;}
.hero p{color:#dceeff;margin:0;max-width:800px;}
.kicker{letter-spacing:2px;text-transform:uppercase;font-size:.72rem;font-weight:700;color:#9edfff;margin-bottom:.6rem;}
.panel{background:white;border:1px solid #dceafa;border-radius:18px;padding:1.15rem 1.25rem;box-shadow:0 8px 26px rgba(14,62,108,.06);margin:.5rem 0 1rem;animation:rise .45s ease-out;}
.panel h3{color:#0b3767;margin-top:0;}
.small{color:#5c718a;font-size:.88rem;}
.pill{display:inline-block;padding:.28rem .7rem;border-radius:999px;background:#e3f3ff;color:#145da0;font-weight:700;font-size:.75rem;margin:.15rem .2rem .15rem 0;}
.warn{background:#fff8e8;border-left:4px solid #e8a52b;padding:.9rem 1rem;border-radius:10px;color:#68480b;}
.good{background:#eaf8f3;border-left:4px solid #2b9b75;padding:.9rem 1rem;border-radius:10px;}
.question{background:white;border:1px solid #d9e8f8;border-radius:16px;padding:1rem 1.2rem;margin:.8rem 0;}
div.stButton>button{border-radius:12px;border:0;background:linear-gradient(100deg,#145da0,#218fc1);color:white;font-weight:600;padding:.55rem 1.1rem;transition:all .2s;}
div.stButton>button:hover{transform:translateY(-2px);box-shadow:0 8px 20px #145da044;color:white;}
hr{border-color:#d8e8f8;}
@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:700px){.hero{padding:1.5rem}.hero h1{font-size:1.55rem}}
</style>
""", unsafe_allow_html=True)

# ---------- SOURCE-GROUNDED CONTENT ----------
topics = {
"Chương 1 · Tổng quan": {
"tag":"Nền tảng · học nhanh",
"goal":"Hiểu Luật kinh doanh điều chỉnh quan hệ nào, dùng phương pháp nào và vì sao cần pháp luật trong kinh tế thị trường.",
"sections":[
("1. Luật kinh tế là gì?","Là hệ thống quy phạm pháp luật do Nhà nước ban hành, điều chỉnh các quan hệ phát sinh trong quá trình tổ chức, quản lý và hoạt động kinh doanh của các chủ thể kinh doanh, chủ yếu là doanh nghiệp."),
("2. Ba nhóm quan hệ được điều chỉnh","(1) Nội bộ chủ thể kinh doanh: chủ sở hữu, thành viên, cổ đông, cơ quan quản lý. (2) Giữa các chủ thể kinh doanh: sản xuất, mua bán, cung ứng dịch vụ. (3) Giữa chủ thể kinh doanh với cơ quan quản lý nhà nước: đăng ký, thanh tra, kiểm tra, xử lý vi phạm."),
("3. Phương pháp điều chỉnh","Nội bộ tổ chức: mệnh lệnh/thỏa thuận tùy quan hệ và cơ cấu. Giữa các chủ thể kinh doanh: bình đẳng, thỏa thuận. Giữa cơ quan quản lý nhà nước và chủ thể kinh doanh: mệnh lệnh."),
("4. Điều lệ công ty","Là bản thỏa thuận ràng buộc các chủ sở hữu/người sáng lập/người góp vốn về tạo lập, góp vốn, tổ chức, quản lý và hoạt động công ty. Lập trước khi đăng ký, nộp kèm hồ sơ và có thể sửa đổi, bổ sung."),
("5. Hợp đồng trong kinh doanh","Thỏa thuận giữa thương nhân với thương nhân hoặc thương nhân với bên không phải thương nhân để xác lập, thay đổi hoặc chấm dứt quyền và nghĩa vụ trong hoạt động kinh doanh. Hình thức có thể là lời nói, văn bản, hành vi cụ thể, trừ trường hợp luật yêu cầu khác."),
("6. Vai trò Luật kinh tế","Tạo môi trường bình đẳng, tự do cho quan hệ kinh tế; khắc phục tiêu cực thị trường, hài hòa tăng trưởng và công bằng xã hội; góp phần phát triển kinh tế thị trường định hướng XHCN.")
]},
"Chương 2 · Chủ thể kinh doanh": {
"tag":"Trọng tâm cao · Luật Doanh nghiệp",
"goal":"Phân biệt loại hình doanh nghiệp theo chủ sở hữu, trách nhiệm tài sản, tư cách pháp nhân, huy động vốn và quản trị.",
"sections":[
("Hộ kinh doanh","Theo tài liệu: do một cá nhân hoặc thành viên hộ gia đình đăng ký; chịu trách nhiệm bằng toàn bộ tài sản. Một cá nhân chỉ đăng ký một hộ kinh doanh trên toàn quốc; đăng ký tại cơ quan cấp xã nơi đặt trụ sở. Căn cứ tài liệu dẫn Điều 82, 90 Nghị định 168/2025/NĐ-CP."),
("Doanh nghiệp – khái niệm","Tổ chức có tên riêng, có tài sản, có trụ sở giao dịch, được thành lập/đăng ký theo pháp luật nhằm mục đích kinh doanh. Sáu yếu tố ghi trong slide: tổ chức kinh tế; tên riêng; trụ sở; tài sản; đăng ký; mục đích kinh doanh."),
("Doanh nghiệp tư nhân (DNTN)","Một cá nhân làm chủ; không có tư cách pháp nhân; chủ DNTN chịu trách nhiệm vô hạn; không được phát hành bất kỳ loại chứng khoán nào. Chủ DNTN quyết định bộ máy tổ chức, quản lý và là đại diện theo pháp luật. Tài liệu nhấn mạnh quyền quản lý, bán, cho thuê doanh nghiệp. Căn cứ: Điều 188, 190–192 LDN."),
("Công ty hợp danh","Ít nhất 02 thành viên hợp danh là cá nhân; có thể có thành viên góp vốn là cá nhân/tổ chức. Có tư cách pháp nhân. Thành viên hợp danh chịu trách nhiệm vô hạn; thành viên góp vốn chịu trách nhiệm hữu hạn. Không được phát hành chứng khoán. Căn cứ: Điều 177–187 LDN."),
("Công ty TNHH 2 thành viên trở lên","Có từ 2 đến 50 thành viên là cá nhân/tổ chức; có tư cách pháp nhân; thành viên chịu trách nhiệm hữu hạn; không phát hành cổ phần (trừ trường hợp chuyển đổi thành CTCP). Cơ cấu: HĐTV, Chủ tịch HĐTV, Giám đốc/TGĐ. HĐTV là cơ quan quyết định cao nhất. Căn cứ: Điều 47, 49–68 LDN."),
("Công ty TNHH 1 thành viên","Do 01 cá nhân hoặc tổ chức làm chủ; có tư cách pháp nhân; chủ sở hữu chịu trách nhiệm hữu hạn; không phát hành cổ phần. Cơ cấu tùy chủ sở hữu là cá nhân hay tổ chức. Căn cứ: Điều 74–87 LDN."),
("Công ty cổ phần (CTCP)","Ít nhất 03 cổ đông, không giới hạn tối đa; có tư cách pháp nhân; cổ đông chịu trách nhiệm hữu hạn; được phát hành cổ phần, trái phiếu và chứng khoán khác. Căn cứ: Điều 111–167 LDN."),
("ĐHĐCĐ và HĐQT","ĐHĐCĐ gồm tất cả cổ đông có quyền biểu quyết, là cơ quan quyết định cao nhất. HĐQT là cơ quan quản lý công ty. Đừng nhầm: ĐHĐCĐ quyết định những vấn đề thuộc thẩm quyền đại hội; HĐQT quản lý và thực hiện quyền, nghĩa vụ theo luật/điều lệ."),
("Tổ chức lại doanh nghiệp","Chia: công ty bị chia chấm dứt. Tách: công ty bị tách vẫn tồn tại. Hợp nhất: các công ty cũ chấm dứt, tạo công ty mới. Sáp nhập: công ty bị sáp nhập chấm dứt, chuyển toàn bộ sang công ty nhận sáp nhập."),
("Giải thể","Theo tài liệu ôn tập, các trường hợp gồm hết thời hạn hoạt động không gia hạn; quyết định của chủ thể có thẩm quyền; không đủ số lượng thành viên tối thiểu trong 06 tháng liên tục mà không chuyển đổi; bị thu hồi GCN đăng ký doanh nghiệp (trừ ngoại lệ luật định). Điều kiện quan trọng: thanh toán hết nợ/nghĩa vụ tài sản và không đang giải quyết tranh chấp tại Tòa án/Trọng tài."),
("HTX và liên hiệp HTX – học nhận diện","HTX: ít nhất 05 thành viên chính thức, có tư cách pháp nhân, tự nguyện hợp tác tương trợ, quản trị tự chủ, bình đẳng, dân chủ. Liên hiệp HTX: ít nhất 03 HTX thành viên chính thức. Tài liệu ghi căn cứ Luật HTX 2023.")
]},
"Chương 3 · Hợp đồng trong kinh doanh": {
"tag":"Trọng tâm cao · BLDS + LTM",
"goal":"Nắm quy trình giao kết, điều kiện hiệu lực, trường hợp vô hiệu và cách phân biệt phạt vi phạm với bồi thường thiệt hại.",
"sections":[
("Luật áp dụng","Hợp đồng dân sự: BLDS 2015. Hợp đồng thương mại: BLDS 2015, Luật Thương mại 2005 và luật chuyên ngành."),
("Ai có quyền ký?","Khi làm tình huống, kiểm tra năng lực chủ thể và thẩm quyền đại diện/ủy quyền. Cá nhân tự mình giao kết; pháp nhân thông qua người đại diện; người đứng tên đăng ký kinh doanh hoặc người được ủy quyền trong phạm vi thẩm quyền (theo tài liệu ôn tập)."),
("Đề nghị giao kết","Là việc thể hiện rõ ý định giao kết và chịu sự ràng buộc của bên đề nghị đối với bên đã xác định hoặc công chúng. Thời điểm có hiệu lực do bên đề nghị ấn định hoặc từ khi bên được đề nghị nhận được đề nghị. Căn cứ: khoản 1 Điều 386 BLDS."),
("Chấp nhận đề nghị & im lặng","Bên được đề nghị có thể chấp nhận, không chấp nhận hoặc đề xuất sửa đổi. Im lặng không mặc nhiên là chấp nhận, trừ khi có thỏa thuận hoặc thói quen đã xác lập theo quy định. Tham chiếu Điều 392–397 BLDS."),
("Nội dung hợp đồng cần có","Đối tượng; số lượng/chất lượng; giá và thanh toán; thời hạn/địa điểm; quyền và nghĩa vụ; thông tin cơ bản; phương thức giải quyết tranh chấp; trách nhiệm pháp lý; sửa đổi và chấm dứt."),
("Thực hiện hợp đồng","Các bên thực hiện hành vi để đáp ứng quyền dân sự tương ứng của bên kia. Nguyên tắc: thực hiện đúng; trung thực, hợp tác, tin cậy; không xâm phạm lợi ích Nhà nước, công cộng và quyền/lợi ích hợp pháp người thứ ba."),
("Sửa đổi và chấm dứt","Sửa đổi theo thỏa thuận, trừ trường hợp đặc biệt; có thể theo Điều 420 BLDS khi hoàn cảnh thay đổi cơ bản; hình thức sửa đổi theo hình thức hợp đồng ban đầu. Chấm dứt khi hoàn thành, theo thỏa thuận, hủy bỏ/đơn phương chấm dứt, đối tượng không còn hoặc trường hợp luật định."),
("Điều kiện có hiệu lực","Các bên có năng lực phù hợp; tự nguyện; mục đích/nội dung không vi phạm điều cấm, không trái đạo đức xã hội; hình thức phù hợp quy định. Thời điểm hiệu lực theo Điều 401 BLDS, trừ thỏa thuận hoặc luật khác."),
("Hợp đồng vô hiệu","Tài liệu liệt kê: vi phạm điều cấm/trái đạo đức; giả tạo; sai năng lực/thẩm quyền đại diện; nhầm lẫn; lừa dối/đe dọa; người xác lập không nhận thức/làm chủ hành vi; vi phạm hình thức; đối tượng không thể thực hiện."),
("Hậu quả vô hiệu","Theo Điều 131, 133 BLDS trong tài liệu: khôi phục tình trạng ban đầu, hoàn trả những gì đã nhận; không hoàn trả được bằng hiện vật thì quy ra tiền; bên có lỗi gây thiệt hại phải bồi thường; lưu ý quyền lợi người thứ ba ngay tình."),
("Sáu chế tài trong thương mại","Buộc thực hiện đúng hợp đồng; phạt vi phạm; bồi thường thiệt hại; tạm ngừng; đình chỉ; hủy bỏ hợp đồng."),
("Phạt vi phạm vs bồi thường","PHẠT: phải có hành vi vi phạm và có thỏa thuận phạt; mức tối đa tài liệu ghi là 8% giá trị phần nghĩa vụ bị vi phạm (trừ ngoại lệ luật định). BỒI THƯỜNG: cần vi phạm, thiệt hại thực tế và quan hệ nhân quả trực tiếp; gồm tổn thất thực tế, trực tiếp và khoản lợi trực tiếp đáng lẽ được hưởng. Hai chế tài có thể áp dụng đồng thời theo tài liệu."),
("Miễn trách nhiệm","Tài liệu nêu: các bên đã thỏa thuận; bất khả kháng; vi phạm hoàn toàn do lỗi bên kia; thực hiện quyết định cơ quan nhà nước có thẩm quyền mà các bên không thể biết khi giao kết. Bên vi phạm phải thông báo và chứng minh."),
("Mua bán hàng hóa","Theo Điều 24 Luật Thương mại 2005 trong tài liệu: lời nói, văn bản hoặc hành vi cụ thể, trừ khi pháp luật yêu cầu hình thức khác.")
]},
"Chương 4 · Phá sản & phục hồi": {
"tag":"Trọng tâm cao · đọc luật khi làm bài",
"goal":"Nhớ điều kiện mất khả năng thanh toán, người có quyền/nghĩa vụ nộp đơn, hội nghị chủ nợ, phục hồi và thứ tự phân chia tài sản.",
"sections":[
("Khái niệm phá sản","Theo phần cẩm nang dẫn khoản 2 Điều 4 Luật Phá sản: doanh nghiệp/HTX mất khả năng thanh toán và bị Tòa án nhân dân ra quyết định tuyên bố phá sản."),
("Mất khả năng thanh toán","Theo phần cẩm nang dẫn khoản 1 Điều 4 Luật Phá sản: không thực hiện nghĩa vụ thanh toán khoản nợ trong thời hạn 03 tháng kể từ ngày đến hạn thanh toán."),
("Trình tự tổng quát","Nộp đơn yêu cầu mở thủ tục → hòa giải/thụ lý → xem xét mở hoặc không mở thủ tục → chỉ định Quản tài viên/doanh nghiệp quản lý, thanh lý tài sản → hội nghị chủ nợ → phục hồi hoặc tuyên bố phá sản → thi hành và phân chia tài sản. Đây là sơ đồ khái quát theo slide/cẩm nang; khi làm bài phải mở đúng văn bản áp dụng."),
("Người nộp đơn","Tài liệu gợi ý phải học riêng nhóm chủ thể có quyền nộp đơn và nhóm có nghĩa vụ nộp đơn; slide dẫn khoản 1, 2, 5, 6 và khoản 3, 4 Điều 5 Luật Phá sản. Hãy dùng bản luật/phiếu điều luật giảng viên yêu cầu để xác định đúng từng chủ thể; app không tự điền danh sách khi tài liệu trích dẫn chưa thể hiện đầy đủ."),
("Hội nghị chủ nợ","Thành phần theo phần cẩm nang dẫn Điều 77: chủ nợ có tên trong danh sách; đại diện NLĐ/công đoàn; người bảo lãnh; chủ DN/HTX hoặc người đại diện; người nộp đơn. Điều kiện hợp lệ trong tài liệu: chủ nợ tham gia đại diện ít nhất 51% tổng số nợ không có bảo đảm."),
("Thông qua nghị quyết chủ nợ","Theo cẩm nang: ít nhất một nửa tổng số chủ nợ không có bảo đảm có mặt và đại diện từ 65% tổng số nợ không có bảo đảm trở lên biểu quyết tán thành. Ghi nhớ hai con số 51% và 65% nhưng phải phân biệt: điều kiện hợp lệ của hội nghị và điều kiện thông qua nghị quyết."),
("Phục hồi hoạt động","Sau nghị quyết hội nghị chủ nợ, doanh nghiệp/HTX xây dựng phương án chi tiết; tài liệu nhấn mốc 15 ngày và 30 ngày trong quy trình trình phương án. Nếu thực hiện xong và không còn mất khả năng thanh toán thì phục hồi; nếu không thực hiện được/hết hạn vẫn mất khả năng thanh toán/đình chỉ thì chuyển hướng tuyên bố phá sản."),
("Thứ tự phân chia tài sản – theo cẩm nang","(1) Chi phí phá sản. (2) Tiền lương, trợ cấp thôi việc, BHXH, BHYT và quyền lợi NLĐ. (3) Khoản nợ nhằm phục hồi hoạt động kinh doanh. (4) Nghĩa vụ tài chính với Nhà nước; nợ không bảo đảm; phần nợ có bảo đảm chưa được thanh toán. (5) Phần còn lại thuộc chủ sở hữu/thành viên/cổ đông theo loại hình."),
("Bài tập chia tài sản – cách làm","Bước 1: xác định khối tài sản được đem phân chia sau khi xử lý tài sản bảo đảm và tài sản không thuộc khối phá sản. Bước 2: lần lượt thanh toán theo thứ tự ưu tiên được luật áp dụng quy định. Bước 3: nếu một thứ tự không đủ tiền thì phân chia theo tỷ lệ trong cùng thứ tự (chỉ áp dụng khi điều luật tương ứng quy định). Bước 4: còn dư mới chuyển sang thứ tự sau. Đây là khung tư duy; phải đối chiếu đúng điều luật hiện hành trước khi tính."),
("Phá sản và giải thể","Giải thể: doanh nghiệp chấm dứt theo trường hợp luật định và điều kiện quan trọng là thanh toán hết nợ/nghĩa vụ tài sản. Phá sản: mất khả năng thanh toán và có quyết định tuyên bố phá sản của Tòa án. Đừng kết luận chỉ vì doanh nghiệp ngừng kinh doanh là đã phá sản.")
]},
"Chương 5 · Giải quyết tranh chấp": {
"tag":"Trọng tâm cao · Trọng tài & Tòa án",
"goal":"Phân biệt thương lượng, hòa giải, trọng tài, Tòa án; hiểu thỏa thuận trọng tài, phán quyết chung thẩm và căn cứ hủy.",
"sections":[
("Bốn phương thức","Thương lượng; hòa giải; trọng tài; Tòa án. Tiêu chí lựa chọn theo tài liệu: nhanh, thuận lợi, duy trì hợp tác, giữ bí mật/uy tín và ít tốn kém."),
("Trọng tài thương mại","Các bên tự nguyện lựa chọn bên thứ ba trung lập là trọng tài viên để giải quyết tranh chấp; quyết định có tính bắt buộc đối với các bên."),
("Trọng tài vụ việc (Ad hoc)","Thành lập khi phát sinh tranh chấp và chấm dứt khi giải quyết xong; không có trụ sở/bộ máy/danh sách trọng tài viên riêng, không có quy tắc tố tụng riêng như trung tâm."),
("Trọng tài thường trực/quy chế","Tổ chức theo trung tâm, có danh sách trọng tài viên, bộ máy gọn nhẹ và quy tắc tố tụng của trung tâm."),
("Bốn nguyên tắc trọng tài","Tôn trọng thỏa thuận hợp pháp; trọng tài viên độc lập, khách quan, vô tư; các bên bình đẳng; không công khai trừ khi các bên thỏa thuận khác."),
("Thẩm quyền trọng tài","Tranh chấp phát sinh từ hoạt động thương mại; tranh chấp có ít nhất một bên hoạt động thương mại; tranh chấp khác mà pháp luật quy định được giải quyết bằng trọng tài."),
("Quy trình trọng tài","Khởi kiện → thành lập HĐTT → chuẩn bị phiên họp → phiên họp giải quyết → phán quyết → thi hành hoặc yêu cầu hủy."),
("Phán quyết trọng tài","Theo tài liệu: quyết định theo nguyên tắc đa số; nếu không đạt đa số thì theo ý kiến Chủ tịch HĐTT; có giá trị chung thẩm. Thi hành được khuyến khích tự nguyện; có thể yêu cầu cơ quan thi hành án dân sự."),
("Hủy phán quyết","Tài liệu yêu cầu học kỹ căn cứ Điều 68, quyền yêu cầu Điều 69 và Tòa án xét đơn Điều 71 Luật Trọng tài thương mại. Không được hiểu Tòa án là cấp phúc thẩm xét lại nội dung phán quyết."),
("Tòa án","Cơ quan xét xử nhân danh quyền lực Nhà nước; bản án/quyết định có cơ chế cưỡng chế thi hành. Nguyên tắc được tài liệu nhấn: quyền tự định đoạt; nghĩa vụ cung cấp/chứng minh chứng cứ; hòa giải."),
("Thẩm quyền Tòa án","Cần phân biệt thẩm quyền theo vụ việc, cấp xét xử và lãnh thổ. Cẩm nang lưu ý cơ cấu TAND khu vực/cấp tỉnh và các mốc tố tụng phải đối chiếu văn bản hiện hành trước kỳ thi.")
]}
}

flashcards = [
("Luật kinh tế điều chỉnh mấy nhóm quan hệ?","3 nhóm: nội bộ chủ thể; giữa các chủ thể kinh doanh; giữa chủ thể kinh doanh với cơ quan quản lý nhà nước."),
("Phương pháp giữa các chủ thể kinh doanh?","Bình đẳng, thỏa thuận."),
("DNTN có tư cách pháp nhân không?","Không. Một cá nhân làm chủ và chủ chịu trách nhiệm vô hạn."),
("CTCP tối thiểu bao nhiêu cổ đông?","Ít nhất 03, không giới hạn tối đa."),
("TNHH 2 thành viên trở lên có tối đa bao nhiêu thành viên?","50 thành viên."),
("Thành viên hợp danh chịu trách nhiệm gì?","Vô hạn; thành viên góp vốn chịu trách nhiệm hữu hạn."),
("ĐHĐCĐ là gì trong CTCP?","Gồm tất cả cổ đông có quyền biểu quyết, là cơ quan quyết định cao nhất."),
("HĐQT là gì?","Cơ quan quản lý công ty cổ phần."),
("Chia và tách khác nhau điểm mấu chốt nào?","Chia: công ty bị chia chấm dứt. Tách: công ty bị tách vẫn tồn tại."),
("Hợp nhất và sáp nhập khác nhau?","Hợp nhất tạo công ty mới; sáp nhập chuyển vào công ty nhận sáp nhập."),
("Im lặng có phải chấp nhận đề nghị?","Không mặc nhiên; trừ thỏa thuận hoặc thói quen đã xác lập theo quy định."),
("Phạt vi phạm cần điều kiện gì?","Có hành vi vi phạm và có thỏa thuận phạt."),
("Bồi thường thiệt hại cần gì?","Có vi phạm, thiệt hại thực tế và quan hệ nhân quả trực tiếp."),
("Hai chế tài phạt và bồi thường có đi cùng?","Theo tài liệu ôn tập: có thể áp dụng đồng thời."),
("Mất khả năng thanh toán được tài liệu định nghĩa theo mốc nào?","Không thanh toán khoản nợ trong 03 tháng kể từ ngày đến hạn (cẩm nang dẫn Luật Phá sản)."),
("Điều kiện hợp lệ Hội nghị chủ nợ theo cẩm nang?","Chủ nợ tham gia đại diện ít nhất 51% tổng số nợ không có bảo đảm."),
("Tỷ lệ thông qua nghị quyết Hội nghị chủ nợ theo cẩm nang?","Ít nhất 1/2 số chủ nợ không bảo đảm có mặt và đại diện từ 65% tổng nợ không bảo đảm trở lên tán thành."),
("Phán quyết trọng tài có tính chất gì?","Có giá trị chung thẩm theo tài liệu ôn tập."),
("Phiên họp trọng tài công khai không?","Không công khai, trừ khi các bên có thỏa thuận khác."),
("Giải thể và phá sản khác nhau?","Giải thể cần bảo đảm thanh toán hết nợ; phá sản gắn với mất khả năng thanh toán và quyết định tuyên bố phá sản của Tòa án.")
]

quiz = [
("Một công ty có quan hệ giữa cổ đông với HĐQT. Đây thuộc nhóm quan hệ nào?",["Giữa các chủ thể kinh doanh","Nội bộ chủ thể kinh doanh","Giữa Nhà nước và doanh nghiệp","Quan hệ lao động"],1,"Đây là quan hệ phát sinh bên trong tổ chức kinh tế."),
("Phương pháp điều chỉnh quan hệ giữa hai chủ thể kinh doanh thông thường là gì?",["Mệnh lệnh","Bình đẳng, thỏa thuận","Cưỡng chế hình sự","Phục tùng hành chính"],1,"Cẩm nang chương 1 ghi phương pháp bình đẳng, thỏa thuận."),
("Phát biểu nào đúng về DNTN?",["Có tư cách pháp nhân","Có ít nhất 2 chủ sở hữu","Chủ DNTN chịu trách nhiệm vô hạn","Được phát hành cổ phiếu"],2,"DNTN do một cá nhân làm chủ, không có tư cách pháp nhân, chủ chịu trách nhiệm vô hạn."),
("Công ty hợp danh phải có tối thiểu bao nhiêu thành viên hợp danh?",["1","2","3","5"],1,"Ít nhất 02 thành viên hợp danh là cá nhân."),
("Công ty TNHH hai thành viên trở lên có số thành viên tối đa theo tài liệu là bao nhiêu?",["20","30","50","Không giới hạn"],2,"Từ 2 đến 50 thành viên."),
("Đặc điểm nào đúng về CTCP?",["Tối thiểu 2 cổ đông","Không được phát hành cổ phần","Ít nhất 3 cổ đông, không giới hạn tối đa","Cổ đông chịu trách nhiệm vô hạn"],2,"Theo Điều 111 LDN được dẫn trong cẩm nang."),
("Cơ quan quyết định cao nhất của CTCP là?",["HĐQT","Giám đốc","ĐHĐCĐ","Ban kiểm soát"],2,"ĐHĐCĐ gồm tất cả cổ đông có quyền biểu quyết."),
("Khi chia doanh nghiệp, công ty bị chia thế nào?",["Vẫn tồn tại","Chấm dứt tồn tại","Chuyển thành hộ kinh doanh","Tự động thành công ty hợp danh"],1,"Đây là điểm phân biệt chia với tách."),
("Khi tách doanh nghiệp, công ty bị tách?",["Chấm dứt ngay","Vẫn tiếp tục tồn tại","Bắt buộc giải thể","Mất tư cách pháp nhân ngay"],1,"Tách là chuyển một phần tài sản/quyền/nghĩa vụ để lập công ty mới; công ty bị tách vẫn tồn tại."),
("Im lặng của bên được đề nghị giao kết hợp đồng?",["Luôn là chấp nhận","Luôn là từ chối","Không mặc nhiên là chấp nhận","Làm hợp đồng vô hiệu"],2,"Trừ thỏa thuận hoặc thói quen đã xác lập theo quy định."),
("Điều kiện nào là điều kiện của phạt vi phạm?",["Phải có thiệt hại thực tế","Phải có thỏa thuận phạt","Phải có lỗi cố ý","Phải có bản án"],1,"Phạt vi phạm cần có hành vi vi phạm và thỏa thuận phạt."),
("Điều kiện nào thuộc bồi thường thiệt hại?",["Chỉ cần có thỏa thuận phạt","Không cần thiệt hại","Thiệt hại thực tế và quan hệ nhân quả trực tiếp","Chỉ cần bên kia không hài lòng"],2,"Tài liệu yêu cầu thiệt hại thực tế, trực tiếp và hành vi vi phạm là nguyên nhân trực tiếp."),
("Phạt vi phạm và bồi thường thiệt hại có thể áp dụng đồng thời không?",["Không bao giờ","Có thể theo tài liệu ôn tập","Chỉ khi Tòa án cho phép","Chỉ trong hợp đồng dân sự"],1,"Slide/cẩm nang ghi hai chế tài có thể áp dụng đồng thời."),
("Theo cẩm nang, mất khả năng thanh toán là không thanh toán khoản nợ trong thời hạn nào kể từ ngày đến hạn?",["15 ngày","30 ngày","2 tháng","3 tháng"],3,"Cẩm nang dẫn khoản 1 Điều 4 Luật Phá sản: 03 tháng."),
("Theo cẩm nang, điều kiện hợp lệ của Hội nghị chủ nợ là chủ nợ tham gia đại diện ít nhất bao nhiêu % tổng nợ không bảo đảm?",["30%","51%","65%","75%"],1,"51% là điều kiện hợp lệ; đừng nhầm với tỷ lệ 65% để thông qua nghị quyết."),
("Tỷ lệ đại diện tổng nợ không bảo đảm để thông qua nghị quyết theo cẩm nang là?",["51%","60%","65%","75%"],2,"Đại diện từ 65% trở lên và ít nhất một nửa số chủ nợ không bảo đảm có mặt tán thành."),
("Nguyên tắc nào đúng về trọng tài thương mại?",["Luôn công khai","Trọng tài viên phải độc lập, khách quan, vô tư","Tòa án xét xử lại toàn bộ như phúc thẩm","Không cần thỏa thuận của các bên"],1,"Nguyên tắc độc lập, khách quan, vô tư được nêu trong slide."),
("Phán quyết trọng tài có giá trị?",["Sơ thẩm","Phúc thẩm","Chung thẩm","Chỉ là khuyến nghị"],2,"Theo tài liệu ôn tập, phán quyết có giá trị chung thẩm."),
("Trọng tài vụ việc Ad hoc được thành lập khi nào?",["Luôn tồn tại như trung tâm","Khi phát sinh tranh chấp","Do Tòa án lập","Chỉ khi có doanh nghiệp nhà nước"],1,"Được thành lập khi phát sinh tranh chấp và chấm dứt khi giải quyết xong."),
("Phương thức nào giải quyết tranh chấp nhân danh quyền lực Nhà nước?",["Thương lượng","Hòa giải","Trọng tài","Tòa án"],3,"Tòa án là cơ quan xét xử nhân danh quyền lực Nhà nước.")
]

case_prompts = [
("Tình huống 1 · Nhầm phạt với bồi thường","Bên A giao hàng trễ. Hợp đồng có điều khoản phạt 5%. Bên B không chứng minh được thiệt hại. Bên B có thể yêu cầu gì?","Có thể yêu cầu phạt vi phạm vì có hành vi vi phạm và có thỏa thuận phạt. Yêu cầu bồi thường cần chứng minh thiệt hại thực tế và quan hệ nhân quả trực tiếp; dữ kiện hiện tại chưa đủ."),
("Tình huống 2 · Chia hay tách?","Công ty X chuyển một phần tài sản, quyền và nghĩa vụ sang lập công ty Y, còn X tiếp tục hoạt động. Đây là hình thức nào?","Tách doanh nghiệp. Dấu hiệu quyết định: công ty bị tách vẫn tồn tại."),
("Tình huống 3 · DNTN hay TNHH MTV?","Một cá nhân sở hữu toàn bộ doanh nghiệp. Chủ sở hữu phải chịu trách nhiệm bằng toàn bộ tài sản và doanh nghiệp không có tư cách pháp nhân. Loại hình nào?","Doanh nghiệp tư nhân. Một chủ sở hữu không đủ để kết luận TNHH MTV; phải xét tư cách pháp nhân và chế độ trách nhiệm."),
("Tình huống 4 · Im lặng","Bên bán gửi đề nghị, bên mua đã nhận nhưng không trả lời. Bên bán cho rằng hợp đồng đã hình thành. Nhận định này đúng không?","Không mặc nhiên đúng. Im lặng không phải chấp nhận, trừ trường hợp có thỏa thuận hoặc thói quen đã xác lập theo quy định."),
("Tình huống 5 · Phá sản hay giải thể?","Doanh nghiệp không trả được khoản nợ đã đến hạn trong thời gian theo luật và Tòa án ra quyết định tuyên bố phá sản. Đây là gì?","Phá sản. Phải có tình trạng mất khả năng thanh toán và quyết định tuyên bố phá sản của Tòa án."),
("Tình huống 6 · Trọng tài","Hợp đồng có thỏa thuận trọng tài hợp lệ. Một bên muốn yêu cầu Tòa án xét xử lại nội dung phán quyết trọng tài vì không đồng ý kết quả. Có thể coi Tòa án là cấp phúc thẩm không?","Không. Tài liệu nhấn mạnh phán quyết trọng tài có giá trị chung thẩm; việc yêu cầu hủy chỉ xem xét theo căn cứ và thủ tục luật định, không phải xét xử phúc thẩm lại nội dung.")
]

# ---------- STATE ----------
if "done_cards" not in st.session_state: st.session_state.done_cards = set()
if "answers" not in st.session_state: st.session_state.answers = {}
if "submitted" not in st.session_state: st.session_state.submitted = False
if "flash_index" not in st.session_state: st.session_state.flash_index = 0

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## ⚖️ LAW STUDY STUDIO")
    st.caption("LUẬT KINH DOANH · FINAL EXAM")
    page = st.radio("KHU VỰC HỌC TẬP",["Tổng quan","Lộ trình 10 ngày","Học từ mất gốc","Flashcards","Trắc nghiệm","Bài tập tình huống","Bản đồ điều luật","Chiến thuật phòng thi"],label_visibility="visible")
    st.divider()
    st.markdown("**Mốc thi**")
    st.markdown("### 21 / 11 / 2026")
    st.caption("Còn 10 ngày tính từ 11/11/2026.")
    st.progress(len(st.session_state.done_cards)/len(flashcards))
    st.caption(f"Flashcards đã tự đánh dấu: {len(st.session_state.done_cards)}/{len(flashcards)}")

def hero(title, subtitle, kicker="YOUR PERSONAL LAW EXAM COACH"):
    st.markdown(f'<div class="hero"><div class="kicker">{kicker}</div><h1>{title}</h1><p>{subtitle}</p></div>',unsafe_allow_html=True)

def panel(title, body):
    st.markdown(f'<div class="panel"><h3>{title}</h3>{body}</div>',unsafe_allow_html=True)

def source_note():
    st.markdown('<div class="warn"><b>Lưu ý về căn cứ:</b> Nội dung học được biên soạn từ slide Luật kinh doanh 2025, file “Ôn tập LKD” và file “Top các bộ luật cần mang theo đi thi” bạn tải lên. Một số phần trong tài liệu có dẫn chiếu văn bản/điều luật ở các thời điểm khác nhau. Khi làm bài, hãy đối chiếu bản luật giảng viên yêu cầu mang vào phòng thi; ứng dụng không tự thay thế văn bản luật gốc.</div>',unsafe_allow_html=True)

if page=="Tổng quan":
    hero("Từ mất gốc đến phòng thi tự tin","Không học vẹt tràn lan. Học theo thứ tự: hiểu khái niệm → phân biệt cặp dễ nhầm → nhớ điều luật → làm tình huống.","BLUE EDITION · STUDY SMARTER")
    st.write("")
    a,b,c=st.columns(3)
    a.metric("10 ngày","lộ trình ôn","11/11 → 20/11")
    b.metric("5 chương","khung kiến thức","bám theo tài liệu")
    c.metric("20 câu","bài test nhanh","có giải thích")
    panel("Bắt đầu đúng cách","<span class='pill'>Bước 1</span> Học phần “Học từ mất gốc” mỗi ngày 2–3 chủ đề.<br><span class='pill'>Bước 2</span> Ôn flashcards để nhớ định nghĩa, tỷ lệ và điểm phân biệt.<br><span class='pill'>Bước 3</span> Làm trắc nghiệm, đọc giải thích cả câu đúng lẫn câu sai.<br><span class='pill'>Bước 4</span> Tập trình bày tình huống theo 6 bước và mở đúng luật.")
    st.subheader("Thứ tự ưu tiên theo ghi chú ôn thi bạn gửi")
    priorities=[
        ("01","Luật Doanh nghiệp","DNTN, hợp danh, TNHH 2TV, CTCP; Điều 17; quyền chủ DNTN; ĐHĐCĐ và HĐQT; vốn điều lệ/phiếu biểu quyết."),
        ("02","Hợp đồng","BLDS về giao kết, thời điểm hiệu lực, người ký; LTM về phạt vi phạm và bồi thường."),
        ("03","Phục hồi & phá sản","Chủ thể có quyền/nghĩa vụ nộp đơn; phục hồi; thứ tự phân chia tài sản; bài tập chia tài sản."),
        ("04","Trọng tài & Tòa án","Trọng tài viên, thỏa thuận trọng tài, phán quyết chung thẩm, hủy phán quyết; thẩm quyền Tòa án."),
        ("05","Hộ kinh doanh & HTX","Học khái niệm, đặc điểm nhận diện theo ghi chú ôn tập.")
    ]
    for n,t,d in priorities:
        st.markdown(f'<div class="panel"><span class="pill">ƯU TIÊN {n}</span><b>{t}</b><div class="small">{d}</div></div>',unsafe_allow_html=True)
    source_note()

elif page=="Lộ trình 10 ngày":
    hero("Lộ trình 10 ngày","Mỗi ngày có mục tiêu rõ ràng. Đừng cố đọc hết luật một lượt; hãy học chủ đề rồi luyện tra điều.")
    plan=[
    ("11/11 · Ngày 1","Nền tảng + loại hình doanh nghiệp","Chương 1; DNTN; hợp danh; TNHH MTV; TNHH 2TV. Vẽ bảng so sánh trách nhiệm và pháp nhân."),
    ("12/11 · Ngày 2","Công ty cổ phần","Cổ phần/cổ phiếu; vốn điều lệ; ĐHĐCĐ; HĐQT; quyền cổ đông; phiếu biểu quyết."),
    ("13/11 · Ngày 3","Thành lập & tổ chức lại","Điều 17; điều kiện thành lập; chia/tách/hợp nhất/sáp nhập; giải thể."),
    ("14/11 · Ngày 4","Giao kết hợp đồng","Chủ thể ký; đại diện/ủy quyền; đề nghị; chấp nhận; im lặng; thời điểm hiệu lực."),
    ("15/11 · Ngày 5","Vô hiệu & chế tài","Điều kiện hiệu lực; các trường hợp vô hiệu; hậu quả; phạt vs bồi thường; miễn trách nhiệm."),
    ("16/11 · Ngày 6","Phá sản – thủ tục & chủ thể","Mất khả năng thanh toán; quyền/nghĩa vụ nộp đơn; quy trình; hội nghị chủ nợ."),
    ("17/11 · Ngày 7","Phục hồi & chia tài sản","Phương án phục hồi; thứ tự phân chia; làm ít nhất 2 bài tính."),
    ("18/11 · Ngày 8","Trọng tài thương mại","Ad hoc vs quy chế; trọng tài viên; nguyên tắc; thỏa thuận; phán quyết; hủy."),
    ("19/11 · Ngày 9","Tòa án & tổng ôn","Thẩm quyền vụ việc/cấp/lãnh thổ; so sánh trọng tài–Tòa án; luyện tình huống."),
    ("20/11 · Ngày 10","Thi thử & chốt điều luật","Làm 1 đề tổng hợp có bấm giờ; chữa lỗi; đánh dấu điều luật cần mở; ngủ đủ."),
    ]
    for day,topic,task in plan:
        with st.expander(f"{day}  ·  {topic}",expanded=day.startswith("11/11")):
            st.write(task)
            st.checkbox("Hoàn thành ngày này",key="plan_"+day)
    panel("Công thức học mỗi buổi 90 phút","25 phút hiểu bài → 20 phút tự kể lại không nhìn tài liệu → 25 phút làm câu hỏi/tình huống → 20 phút tra điều luật và ghi lỗi sai.")
    source_note()

elif page=="Học từ mất gốc":
    hero("Học từ mất gốc","Chọn chương, đọc phần giải thích ngắn, sau đó tự nói lại bằng lời của mình.")
    selected=st.selectbox("Chọn chương",list(topics.keys()))
    item=topics[selected]
    st.markdown(f"<span class='pill'>{item['tag']}</span>",unsafe_allow_html=True)
    panel("Sau khi học xong, bạn phải làm được",item["goal"])
    for title,body in item["sections"]:
        with st.expander(title):
            st.write(body)
            st.caption("Tự kiểm tra: Hãy thử giải thích lại ý này trong 20–30 giây mà không nhìn màn hình.")
    source_note()

elif page=="Flashcards":
    hero("Flashcards · Nhớ nhanh","Mỗi thẻ là một câu hỏi ngắn. Hãy tự trả lời trước khi bấm hiện đáp án.")
    idx=st.session_state.flash_index % len(flashcards)
    q,a=flashcards[idx]
    st.markdown(f'<div class="panel"><div class="kicker">CARD {idx+1:02d} / {len(flashcards)}</div><h3 style="font-size:1.25rem">{q}</h3></div>',unsafe_allow_html=True)
    with st.expander("Hiện đáp án"):
        st.success(a)
    x,y,z=st.columns(3)
    if x.button("← Thẻ trước"): st.session_state.flash_index=(idx-1)%len(flashcards); st.rerun()
    if y.button("Đã nhớ ✓"): st.session_state.done_cards.add(idx); st.session_state.flash_index=(idx+1)%len(flashcards); st.rerun()
    if z.button("Thẻ tiếp →"): st.session_state.flash_index=(idx+1)%len(flashcards); st.rerun()
    st.caption(f"Đã đánh dấu nhớ: {len(st.session_state.done_cards)}/{len(flashcards)} thẻ. Tiến độ lưu trong phiên trình duyệt hiện tại.")

elif page=="Trắc nghiệm":
    hero("Kiểm tra kiến thức","20 câu trọng tâm theo nội dung tài liệu. Chọn đáp án rồi nộp bài để xem điểm và giải thích.")
    if st.button("Làm lại bài / xóa lựa chọn"):
        st.session_state.answers={}; st.session_state.submitted=False; st.rerun()
    with st.form("quiz_form"):
        for i,(q,opts,correct,why) in enumerate(quiz):
            st.markdown(f'<div class="question"><b>Câu {i+1}. {q}</b></div>',unsafe_allow_html=True)
            choice=st.radio("Chọn một đáp án",opts,index=None,key=f"q_{i}",label_visibility="collapsed")
            st.session_state.answers[i]=opts.index(choice) if choice in opts else None
        submitted=st.form_submit_button("Nộp bài và chấm điểm")
    if submitted:
        st.session_state.submitted=True
    if st.session_state.submitted:
        score=0
        for i,(q,opts,correct,why) in enumerate(quiz):
            ans=st.session_state.answers.get(i)
            if ans==correct: score+=1
        st.metric("Kết quả",f"{score}/{len(quiz)}",f"{score/len(quiz)*100:.0f}%")
        if score>=16: st.success("Rất tốt. Hãy chuyển sang làm tình huống và tra luật.")
        elif score>=11: st.info("Bạn đã có nền. Ôn lại các câu sai và làm lại sau vài giờ.")
        else: st.warning("Đừng nản. Quay lại phần Học từ mất gốc, học từng chương rồi làm lại.")
        for i,(q,opts,correct,why) in enumerate(quiz):
            ans=st.session_state.answers.get(i)
            ok=ans==correct
            with st.expander(f"Câu {i+1} · {'Đúng' if ok else 'Sai / chưa chọn'}"):
                st.write(q)
                st.write("**Đáp án đúng:**",opts[correct])
                if ans is not None: st.write("**Bạn chọn:**",opts[ans])
                st.caption(why)

elif page=="Bài tập tình huống":
    hero("Luyện tư duy pháp lý","Không chỉ chọn đúng/sai: phải chỉ ra quan hệ pháp luật, điều luật, điều kiện và kết luận.")
    st.markdown("**Khung 6 bước làm bài tình huống**")
    steps=["Xác định quan hệ pháp luật: doanh nghiệp, hợp đồng, phá sản hay tranh chấp.","Xác định chủ thể: ai là cá nhân, thương nhân, công ty, cổ đông, chủ nợ, đại diện?","Xác định sự kiện và mốc thời gian: giao kết, đến hạn, vi phạm, nhận thông báo.","Chọn luật chuyên ngành trước; nếu thiếu mới dùng luật chung.","Đối chiếu từng điều kiện với dữ kiện; không bỏ qua dữ kiện bất lợi.","Kết luận ai có quyền/nghĩa vụ gì và hậu quả pháp lý."]
    for i,s in enumerate(steps,1): st.markdown(f"**{i}.** {s}")
    for title,question,answer in case_prompts:
        with st.expander(title):
            st.write(question)
            st.text_area("Tự viết câu trả lời trước",key="case_"+title,height=100,placeholder="Căn cứ điều luật… Trong tình huống… Vì vậy…")
            with st.expander("Gợi ý đáp án"):
                st.success(answer)
    panel("Mẫu trình bày gọn","“Căn cứ Điều … [văn bản], điều kiện để … là … Trong tình huống, … nên … Vì vậy, … có/không có quyền … và hậu quả pháp lý là …”")

elif page=="Bản đồ điều luật":
    hero("Bản đồ tra cứu điều luật","Dùng để biết mở luật nào và tra cụm điều nào. Đây là chỉ mục học tập theo tài liệu bạn gửi, không phải bản thay thế luật gốc.")
    refs=[
    ("Luật Doanh nghiệp 2020","Điều 4, 6, 7, 10, 17, 26, 29, 32, 35–44, 74–87, 88–90, 111–167, 177–205","Khái niệm, quyền thành lập, đăng ký, DNTN, TNHH, CTCP, hợp danh, tổ chức lại."),
    ("Bộ luật Dân sự 2015","Điều 123–133; 386–401; 420","Giao kết, hiệu lực, vô hiệu, hậu quả vô hiệu, hoàn cảnh thay đổi cơ bản."),
    ("Luật Thương mại 2005","Điều 24; nhóm điều về chế tài (đặc biệt phạt, bồi thường, miễn trách nhiệm)","Hình thức mua bán hàng hóa; chế tài trong thương mại."),
    ("Luật Phá sản / văn bản phục hồi phá sản theo yêu cầu môn học","Tài liệu cẩm nang dẫn Điều 4, 5, 8, 47–49, 52–58, 77, 130; tài liệu khác nhắc Điều 43","Chủ thể nộp đơn, mất khả năng thanh toán, hội nghị chủ nợ, phục hồi, phân chia tài sản. Phải xác nhận văn bản và số điều đang được giảng viên yêu cầu."),
    ("Luật Trọng tài thương mại","Điều 30–38; Điều 62–63; Điều 68–71","Khởi kiện, thành lập HĐTT, phán quyết, thi hành, yêu cầu hủy."),
    ("Bộ luật Tố tụng dân sự","Nhóm điều về thẩm quyền theo vụ việc/cấp/lãnh thổ và trình tự xét xử","Dùng khi câu hỏi yêu cầu xác định Tòa án có thẩm quyền; đối chiếu bản hiện hành.")
    ]
    for law,articles,usage in refs:
        with st.expander(law):
            st.write("**Cụm điều:**",articles)
            st.write("**Dùng khi:**",usage)
    st.markdown('<div class="warn"><b>Cảnh báo cần kiểm tra trước khi học thuộc:</b> Tài liệu “Top các bộ luật…” ghi “Luật phục hồi phá sản 2025” và nhắc Điều 43; trong khi slide/cẩm nang có nhiều dẫn chiếu Luật Phá sản và Điều 54 về phân chia tài sản. Không tự ghép hai hệ thống điều khoản. Hãy xác nhận với giảng viên/bản luật mang thi xem văn bản mới nào áp dụng và số điều tương ứng.</div>',unsafe_allow_html=True)
    source_note()

elif page=="Chiến thuật phòng thi":
    hero("Chiến thuật làm bài để lấy điểm","Đi thi luật: không cần viết dài, cần đúng vấn đề – đúng căn cứ – đúng điều kiện – đúng kết luận.")
    panel("Nếu đề hỏi nhận định đúng/sai","1. Chốt đúng/sai ngay câu đầu.<br>2. Ghi căn cứ pháp lý (điều, khoản, tên văn bản).<br>3. Giải thích điều kiện luật định.<br>4. Đối chiếu dữ kiện trong nhận định.<br>5. Kết luận lại ngắn gọn.")
    panel("Nếu đề cho tình huống","Xác định loại quan hệ → chủ thể → hành vi/sự kiện → luật áp dụng → điều kiện → kết luận. Đừng nhảy thẳng vào kết luận khi chưa xác định ai có quyền ký, ai vi phạm và thời điểm nào.")
    panel("Ba bẫy dễ mất điểm","• Có vi phạm hợp đồng không đồng nghĩa tự động có phạt: phạt cần thỏa thuận.<br>• Có một chủ sở hữu không đồng nghĩa DNTN: phải phân biệt với TNHH MTV.<br>• Không đồng ý phán quyết trọng tài không đồng nghĩa được kháng cáo như bản án.")
    panel("Tối 20/11","Chỉ ôn bảng so sánh, flashcards sai, điều luật đã đánh dấu và một bài tập chia tài sản. Không học chương mới quá khuya.")
    source_note()

st.markdown("<hr><div class='small' style='text-align:center'>LUẬT KINH DOANH · BLUE STUDY STUDIO · Nội dung học tập tổng hợp từ tài liệu người học cung cấp.</div>",unsafe_allow_html=True)

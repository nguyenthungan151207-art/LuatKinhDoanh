import streamlit as st
from datetime import date

st.set_page_config(page_title="Luật Kinh Doanh | Ôn thi giữa kỳ", page_icon="💗", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
:root { --pink:#f6d9e9; --pink2:#fcecf4; --lav:#e8e0fb; --lav2:#f5f1ff; --ink:#55445f; --muted:#887a91; --line:#eadff0; }
html, body, [class*="css"], [data-testid="stAppViewContainer"] {font-family:'Poppins',sans-serif;}
.stApp {background:radial-gradient(circle at 8% 4%,#fff2f8 0,transparent 28%),radial-gradient(circle at 92% 12%,#f0eaff 0,transparent 30%),linear-gradient(135deg,#fffafd 0%,#faf7ff 52%,#fff8fc 100%);color:var(--ink);}
[data-testid="stSidebar"] {display:none;}
.block-container {max-width:1180px;padding-top:1.5rem;padding-bottom:3rem;}
header[data-testid="stHeader"] {background:rgba(255,250,253,.7);}
.nav-wrap {background:rgba(255,255,255,.78);border:1px solid #eee3f2;border-radius:24px;padding:10px 14px;box-shadow:0 10px 30px #8b6d9910;backdrop-filter:blur(12px);margin:2px 0 24px;}
div[role="radiogroup"] {gap:8px;justify-content:center;flex-wrap:wrap;}
div[role="radiogroup"] label {background:#fff;border:1px solid #eadff0;border-radius:999px;padding:8px 16px!important;transition:all .25s ease;box-shadow:0 3px 10px #a98db012;}
div[role="radiogroup"] label:hover {transform:translateY(-2px);border-color:#d8b7df;background:#fff7fc;}
div[role="radiogroup"] label:has(input:checked) {background:linear-gradient(100deg,#f8dce9,#e9e1fb);border-color:#d8b8df;color:#5b4269;box-shadow:0 6px 18px #b18bb51c;}
div[role="radiogroup"] label p {font-weight:600;font-size:.88rem;}
.hero {position:relative;overflow:hidden;padding:34px 38px;border-radius:30px;background:linear-gradient(115deg,#f6dce9 0%,#e9e1fb 58%,#f9e8f2 100%);color:#594666;margin:10px 0 22px;box-shadow:0 16px 40px #a786b51c;animation:fadeUp .65s ease both;}
.hero:before,.hero:after {content:"";position:absolute;border:1px solid #fff9;border-radius:50%;pointer-events:none;}
.hero:before {width:260px;height:260px;right:-65px;top:-145px;box-shadow:0 0 0 24px #fff2,0 0 0 52px #fff1;}
.hero:after {width:110px;height:110px;right:20%;bottom:-80px;}
.hero h1 {font-size:2rem;line-height:1.3;margin:0 0 8px;font-weight:800;position:relative;z-index:1;}
.hero p {font-size:.98rem;margin:0;max-width:800px;position:relative;z-index:1;color:#705c7b;}
.hero .eyebrow {display:inline-block;background:#ffffffa8;border:1px solid #fff;border-radius:99px;padding:5px 12px;font-size:.74rem;letter-spacing:.08em;font-weight:700;margin-bottom:13px;}
.panel {background:#ffffffd9;border:1px solid var(--line);border-radius:20px;padding:18px 20px;margin:10px 0;box-shadow:0 8px 24px #8d6c9b0c;animation:fadeUp .45s ease both;}
.soft {background:#fff4fa;border:1px solid #f2dce9;padding:13px 16px;border-radius:14px;margin:10px 0;}
.lav {background:#f5f1ff;border:1px solid #e5ddf6;padding:13px 16px;border-radius:14px;margin:10px 0;}
.smallmuted {color:var(--muted);font-size:.86rem;}
div.stButton>button,div.stFormSubmitButton>button {border-radius:14px;border:1px solid #e2cde7;background:linear-gradient(100deg,#f8e2ed,#eee8fc);color:#5d466c;font-weight:600;transition:all .2s ease;}
div.stButton>button:hover,div.stFormSubmitButton>button:hover {transform:translateY(-2px);border-color:#cda7d5;box-shadow:0 7px 18px #a98ab51f;color:#493356;}
[data-testid="stMetric"] {background:#fff;border:1px solid var(--line);padding:14px;border-radius:17px;box-shadow:0 6px 18px #a98ab50c;}
.stProgress>div>div>div>div {background:linear-gradient(90deg,#e7aeca,#b8a8e9);}
div[data-testid="stExpander"] {border:1px solid #eadff0;border-radius:16px;background:#ffffffa8;overflow:hidden;}
div[data-testid="stExpander"] summary:hover {color:#8b669c;}
hr {border-color:#eee4f2;}
@keyframes fadeUp {from {opacity:0;transform:translateY(12px)} to {opacity:1;transform:translateY(0)}}
@keyframes floatSoft {0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
.float-soft {animation:floatSoft 4s ease-in-out infinite;}
@media (prefers-reduced-motion:reduce) { *,*:before,*:after {animation:none!important;transition:none!important;scroll-behavior:auto!important;} }
</style>
""", unsafe_allow_html=True)

CHAPTERS = {
"Chương 1 · Nền tảng & chủ thể kinh doanh": {
"tag":"Nắm khái niệm trước, học luật sau", "time":"45–60 phút", "goal":"Hiểu Luật kinh doanh điều chỉnh quan hệ nào; phân biệt các chủ thể; nhận diện loại hình doanh nghiệp và cơ quan quản lý.",
"lessons":[
("1. Luật kinh doanh là gì?", "Hiểu đơn giản: đây là nhóm quy tắc pháp luật điều chỉnh việc thành lập, tổ chức, quản lý và hoạt động kinh doanh. Đề hỏi khái niệm thì đừng chỉ viết ‘luật về kinh doanh’; cần nêu chủ thể, quan hệ và mục đích điều chỉnh.", ["Quan hệ nội bộ: giữa thành viên, cổ đông, chủ sở hữu và bộ máy quản lý.","Quan hệ bên ngoài: giữa các chủ thể kinh doanh với nhau khi mua bán, cung ứng dịch vụ.","Quan hệ quản lý nhà nước: đăng ký, thanh tra, kiểm tra và xử lý vi phạm."]),
("2. Doanh nghiệp và chủ thể không phải doanh nghiệp", "Doanh nghiệp là tổ chức có tên riêng, tài sản, trụ sở giao dịch, được thành lập/đăng ký theo luật để kinh doanh. Hộ kinh doanh và hợp tác xã là các chủ thể kinh doanh nhưng không đồng nhất với các loại hình doanh nghiệp theo Luật Doanh nghiệp.", ["Bốn loại hình doanh nghiệp: DNTN, công ty hợp danh, công ty TNHH, công ty cổ phần.","Hộ kinh doanh: cá nhân hoặc thành viên hộ gia đình đăng ký; lưu ý chế độ trách nhiệm tài sản theo quy định hiện hành.","Hợp tác xã: tổ chức kinh tế tập thể, thành viên tự nguyện thành lập và hợp tác tương trợ; tra Luật HTX 2023 và văn bản hướng dẫn."]),
("3. Điều kiện thành lập và đăng ký doanh nghiệp", "Khi xử lý tình huống, kiểm tra lần lượt: người thành lập có bị cấm không; vốn góp có hợp pháp không; ngành nghề có bị cấm/kinh doanh có điều kiện không; tên và trụ sở có hợp lệ không; hồ sơ và cơ quan đăng ký có đúng không.", ["Điều 17 Luật Doanh nghiệp: nhóm chủ thể có quyền và nhóm bị cấm thành lập, quản lý doanh nghiệp.","Tài sản góp vốn và chuyển quyền sở hữu: đối chiếu Điều 34–36 LDN.","Hồ sơ đăng ký thành lập theo loại hình; thời hạn giải quyết, công bố nội dung và mã số doanh nghiệp cần tra văn bản hiện hành."]),
("4. Nhận diện 4 loại hình doanh nghiệp", "Mấu chốt để phân biệt: ai là chủ; có tư cách pháp nhân không; chịu trách nhiệm hữu hạn hay vô hạn; có được phát hành cổ phần/chứng khoán không; cơ quan quản lý nào.", ["DNTN: một cá nhân làm chủ; chủ chịu trách nhiệm bằng toàn bộ tài sản; doanh nghiệp không có tư cách pháp nhân.","Hợp danh: ít nhất 2 thành viên hợp danh là cá nhân; thành viên hợp danh chịu trách nhiệm vô hạn, thành viên góp vốn chịu trách nhiệm hữu hạn; có tư cách pháp nhân.","TNHH: 1 hoặc 2–50 thành viên tùy loại; chủ sở hữu/thành viên chịu trách nhiệm hữu hạn; có tư cách pháp nhân; không phát hành cổ phần (trừ trường hợp luật quy định khi chuyển đổi).","CTCP: ít nhất 3 cổ đông, không giới hạn tối đa; cổ đông chịu trách nhiệm hữu hạn; có tư cách pháp nhân; được phát hành cổ phần và các loại chứng khoán theo luật."]),
("5. Cơ cấu quản trị cần thuộc", "Đừng nhầm cơ quan quyết định cao nhất với cơ quan quản lý. Ở công ty cổ phần, ĐHĐCĐ là cơ quan quyết định cao nhất; HĐQT là cơ quan quản lý công ty.", ["TNHH 2 thành viên trở lên: Hội đồng thành viên là cơ quan quyết định cao nhất; có Chủ tịch HĐTV và Giám đốc/Tổng giám đốc.","CTCP: ĐHĐCĐ gồm tất cả cổ đông có quyền biểu quyết; HĐQT quản lý công ty; Giám đốc/Tổng giám đốc điều hành.","DNTN: chủ DNTN có quyền quyết định tổ chức, quản lý và là người đại diện theo pháp luật theo quy định."]),
("6. Tổ chức lại và giải thể", "Học bằng cặp đối chiếu: chia/tách; hợp nhất/sáp nhập. Câu hỏi thường kiểm tra công ty cũ còn tồn tại hay không.", ["Chia: công ty bị chia chấm dứt; hình thành các công ty mới.","Tách: công ty bị tách vẫn tồn tại, đồng thời có công ty mới.","Hợp nhất: các công ty bị hợp nhất chấm dứt để tạo công ty mới.","Sáp nhập: công ty bị sáp nhập chấm dứt, chuyển toàn bộ sang công ty nhận sáp nhập.","Giải thể: phải đáp ứng điều kiện thanh toán hết nợ/nghĩa vụ tài sản và các điều kiện luật định."])
],
"quiz":[
{"q":"Công ty cổ phần phải có tối thiểu bao nhiêu cổ đông?","opts":["1","2","3","Không giới hạn tối thiểu"],"a":2,"why":"Điều 111 Luật Doanh nghiệp 2020 quy định CTCP có ít nhất 03 cổ đông và không hạn chế số lượng tối đa."},
{"q":"Cơ quan quyết định cao nhất của công ty cổ phần là?","opts":["Hội đồng quản trị","Đại hội đồng cổ đông","Giám đốc","Ban kiểm soát"],"a":1,"why":"ĐHĐCĐ gồm tất cả cổ đông có quyền biểu quyết và là cơ quan quyết định cao nhất."},
{"q":"Điểm phân biệt cốt lõi giữa chia và tách doanh nghiệp là gì?","opts":["Số lượng cổ đông","Công ty bị chia/tách có còn tồn tại không","Tên doanh nghiệp","Địa chỉ trụ sở"],"a":1,"why":"Chia làm công ty bị chia chấm dứt; tách thì công ty bị tách tiếp tục tồn tại."},
{"q":"Chủ doanh nghiệp tư nhân chịu trách nhiệm về nghĩa vụ của doanh nghiệp bằng?","opts":["Chỉ vốn điều lệ","Phần vốn đã góp","Toàn bộ tài sản của mình","Không phải chịu trách nhiệm"],"a":2,"why":"DNTN không có tư cách pháp nhân; chủ DNTN chịu trách nhiệm vô hạn bằng toàn bộ tài sản."},
{"q":"Thành viên hợp danh trong công ty hợp danh phải là?","opts":["Cá nhân","Tổ chức","Cá nhân hoặc tổ chức","Chỉ cơ quan nhà nước"],"a":0,"why":"Thành viên hợp danh phải là cá nhân; công ty có ít nhất hai thành viên hợp danh."}
],
"essay":["Phân tích và so sánh doanh nghiệp tư nhân với công ty TNHH một thành viên.","Phân biệt Đại hội đồng cổ đông và Hội đồng quản trị trong công ty cổ phần.","Một công ty bị tách thành hai công ty mới. Công ty ban đầu có chấm dứt tồn tại không? Phân tích.","Trình bày các điều kiện cơ bản để một cá nhân được quyền thành lập doanh nghiệp."]
},
"Chương 2 · Hợp đồng trong kinh doanh": {
"tag":"Nắm quy trình giao kết và hiệu lực", "time":"50–65 phút", "goal":"Phân tích được chủ thể, đề nghị, chấp nhận, thời điểm giao kết, hiệu lực, vô hiệu và chấm dứt hợp đồng.",
"lessons":[
("1. Hợp đồng là gì?", "Hợp đồng là sự thỏa thuận giữa các bên nhằm xác lập, thay đổi hoặc chấm dứt quyền, nghĩa vụ dân sự. Trong kinh doanh, hợp đồng thường gắn với hoạt động sinh lợi và có thể chịu sự điều chỉnh đồng thời của BLDS và luật chuyên ngành như Luật Thương mại.", ["Luật chung: Bộ luật Dân sự 2015.","Luật chuyên ngành: Luật Thương mại 2005 và các luật liên quan.","Nguyên tắc: tự do, tự nguyện cam kết, thỏa thuận nhưng không vi phạm điều cấm, không trái đạo đức xã hội."]),
("2. Ai có quyền ký hợp đồng?", "Không phải cứ là nhân viên hoặc người có mặt tại công ty thì được quyền ký. Cần xác định người ký là người đại diện theo pháp luật hay đại diện theo ủy quyền; phạm vi đại diện có bao trùm giao dịch không.", ["Cá nhân: phải có năng lực pháp luật và năng lực hành vi phù hợp với giao dịch.","Tổ chức: giao dịch thông qua người đại diện theo pháp luật hoặc người đại diện theo ủy quyền.","Nếu ký vượt quá phạm vi đại diện hoặc không có quyền đại diện, hậu quả pháp lý cần xem Điều 142–143 BLDS và tình tiết bên thứ ba có biết hay không."]),
("3. Giao kết hợp đồng diễn ra thế nào?", "Giao kết thường gồm đề nghị giao kết và chấp nhận đề nghị. Chấp nhận phải thể hiện sự đồng ý với toàn bộ nội dung đề nghị; trả lời có sửa đổi, bổ sung có thể được xem là đề nghị mới tùy trường hợp.", ["Đề nghị giao kết: thể hiện rõ ý định giao kết và chịu sự ràng buộc đối với bên được đề nghị.","Chấp nhận: đồng ý toàn bộ nội dung; lưu ý thời hạn trả lời và trường hợp im lặng.","Hợp đồng có thể giao kết bằng lời nói, văn bản hoặc hành vi cụ thể, trừ trường hợp luật yêu cầu hình thức nhất định."]),
("4. Thời điểm, địa điểm giao kết và hiệu lực", "Đây là phần dễ ra tự luận vì ảnh hưởng đến việc xác định hợp đồng đã hình thành chưa, luật áp dụng, thời hạn thực hiện và trách nhiệm khi vi phạm.", ["Thời điểm giao kết xác định theo Điều 400 BLDS; cần phân biệt hợp đồng bằng lời nói, văn bản, phương tiện điện tử và trường hợp phải công chứng/chứng thực/đăng ký.","Địa điểm giao kết theo Điều 399 BLDS: do các bên thỏa thuận; nếu không có thỏa thuận thì áp dụng quy tắc luật định.","Hiệu lực hợp đồng: xem Điều 401 BLDS; nguyên tắc có hiệu lực từ thời điểm giao kết, trừ thỏa thuận hoặc luật có quy định khác."]),
("5. Điều kiện có hiệu lực và hợp đồng vô hiệu", "Khi đề hỏi hợp đồng có hiệu lực không, kiểm tra đủ 4 nhóm: chủ thể; tự nguyện; mục đích/nội dung; hình thức nếu luật bắt buộc.", ["Điều 117 BLDS: chủ thể có năng lực phù hợp; tự nguyện; mục đích và nội dung không vi phạm điều cấm, không trái đạo đức xã hội.","Hình thức là điều kiện có hiệu lực khi luật có quy định.","Hợp đồng vô hiệu: xem các Điều 123–133 BLDS; hậu quả cơ bản là khôi phục tình trạng ban đầu, hoàn trả những gì đã nhận, xử lý lỗi và hoa lợi/lợi tức theo luật."]),
("6. Sửa đổi, thực hiện và chấm dứt", "Khi làm tình huống, xác định nghĩa vụ nào đến hạn, bên nào thực hiện/không thực hiện và hợp đồng có căn cứ sửa đổi, tạm ngừng, đình chỉ hay hủy bỏ không.", ["Thực hiện đúng đối tượng, chất lượng, số lượng, thời hạn, địa điểm và phương thức đã thỏa thuận.","Hoàn cảnh thay đổi cơ bản: Điều 420 BLDS, phải đáp ứng các điều kiện luật định.","Chấm dứt hợp đồng theo thỏa thuận, hoàn thành, đơn phương chấm dứt/hủy bỏ hoặc căn cứ khác theo luật."])
],
"quiz":[
{"q":"Điều kiện nào sau đây KHÔNG phải điều kiện chung để giao dịch dân sự có hiệu lực?","opts":["Chủ thể có năng lực phù hợp","Các bên hoàn toàn tự nguyện","Mọi hợp đồng đều phải công chứng","Mục đích, nội dung không vi phạm điều cấm"],"a":2,"why":"Không phải mọi hợp đồng đều phải công chứng; chỉ khi luật quy định hoặc các bên thỏa thuận."},
{"q":"Một người ký hợp đồng nhân danh công ty. Việc đầu tiên cần kiểm tra là gì?","opts":["Chữ ký có đẹp không","Tư cách đại diện và phạm vi đại diện","Công ty có nhiều nhân viên không","Người ký có chức danh cao nhất không"],"a":1,"why":"Phải xác định người ký có quyền đại diện và giao dịch nằm trong phạm vi đại diện."},
{"q":"Chấp nhận đề nghị giao kết hợp đồng về nguyên tắc phải thể hiện điều gì?","opts":["Đồng ý toàn bộ nội dung đề nghị","Chỉ đồng ý giá","Im lặng trong mọi trường hợp","Tự ý thay đổi điều khoản"],"a":0,"why":"Chấp nhận phải là sự đồng ý với toàn bộ nội dung đề nghị, có lưu ý các trường hợp luật định."},
{"q":"Điều 117 BLDS 2015 quy định nhóm điều kiện nào?","opts":["Điều kiện phá sản","Điều kiện có hiệu lực của giao dịch dân sự","Thẩm quyền trọng tài","Điều kiện giải thể"],"a":1,"why":"Điều 117 là điều kiện có hiệu lực của giao dịch dân sự."}
],
"essay":["Trình bày quá trình giao kết hợp đồng và xác định thời điểm giao kết trong các hình thức khác nhau.","Một trưởng phòng ký hợp đồng thay công ty nhưng không có giấy ủy quyền. Phân tích những vấn đề pháp lý cần kiểm tra và hậu quả có thể phát sinh.","Phân tích các điều kiện có hiệu lực của hợp đồng theo Điều 117 BLDS 2015.","Phân biệt hợp đồng vô hiệu với hợp đồng bị đơn phương chấm dứt thực hiện."]
},
"Chương 3 · Vi phạm hợp đồng & chế tài thương mại": {
"tag":"Học bằng điều kiện áp dụng", "time":"45–55 phút", "goal":"Phân biệt các chế tài và biết khi nào được phạt vi phạm, bồi thường thiệt hại, miễn trách nhiệm.",
"lessons":[
("1. Vi phạm hợp đồng là gì?", "Là việc một bên không thực hiện, thực hiện không đầy đủ hoặc không đúng nghĩa vụ theo thỏa thuận hoặc theo luật. Trước khi chọn chế tài, phải chỉ ra nghĩa vụ nào bị vi phạm.", ["Xác định hợp đồng và nghĩa vụ hợp pháp.","Xác định hành vi vi phạm, thời điểm vi phạm và chứng cứ.","Kiểm tra điều kiện áp dụng chế tài theo Luật Thương mại và thỏa thuận."]),
("2. Các chế tài trong thương mại", "Luật Thương mại 2005 quy định nhiều chế tài. Không được mặc định cứ vi phạm là tự động áp dụng tất cả chế tài.", ["Buộc thực hiện đúng hợp đồng.","Phạt vi phạm.","Bồi thường thiệt hại.","Tạm ngừng, đình chỉ, hủy bỏ hợp đồng.","Các biện pháp khác theo Điều 292 và quy định liên quan."]),
("3. Phạt vi phạm", "Phạt vi phạm là khoản tiền bên vi phạm phải trả nếu hợp đồng có thỏa thuận phạt và có hành vi vi phạm thuộc phạm vi thỏa thuận. Đây là điểm mấu chốt: phạt không tự động phát sinh chỉ vì có vi phạm.", ["Điều 300 LTM: phải có thỏa thuận phạt vi phạm.","Điều 301 LTM: mức phạt tối đa thông thường không quá 8% giá trị phần nghĩa vụ hợp đồng bị vi phạm; cần kiểm tra trường hợp luật chuyên ngành có quy định khác.","Đừng nhầm giá trị toàn bộ hợp đồng với giá trị phần nghĩa vụ bị vi phạm."]),
("4. Bồi thường thiệt hại", "Bồi thường nhằm bù đắp tổn thất thực tế, trực tiếp do hành vi vi phạm gây ra và khoản lợi trực tiếp đáng lẽ được hưởng nếu không có vi phạm, theo điều kiện luật định.", ["Điều 302 LTM: bồi thường tổn thất thực tế, trực tiếp và khoản lợi trực tiếp đáng lẽ được hưởng.","Điều 303: căn cứ phát sinh trách nhiệm bồi thường gồm có hành vi vi phạm, thiệt hại thực tế và quan hệ nhân quả trực tiếp.","Điều 304: bên yêu cầu bồi thường có nghĩa vụ chứng minh tổn thất.","Điều 305: nghĩa vụ hạn chế tổn thất."]),
("5. Phạt và bồi thường có thể cùng áp dụng không?", "Có thể cùng áp dụng nếu có đủ căn cứ. Phạt cần thỏa thuận; bồi thường cần chứng minh các điều kiện phát sinh. Nếu không có thỏa thuận phạt thì không thể chỉ dựa vào việc vi phạm để đòi tiền phạt.", ["Phạt: căn cứ chính là thỏa thuận phạt + vi phạm.","Bồi thường: căn cứ chính là vi phạm + thiệt hại + quan hệ nhân quả + chứng minh.","Đọc Điều 307 LTM để xử lý mối quan hệ giữa phạt và bồi thường."]),
("6. Miễn trách nhiệm", "Bên vi phạm có thể được miễn trách nhiệm trong các trường hợp luật quy định, nhưng phải chứng minh điều kiện và thực hiện nghĩa vụ thông báo/chứng minh theo luật.", ["Điều 294 LTM: các trường hợp miễn trách nhiệm.","Điều 295 LTM: thông báo và xác nhận trường hợp miễn trách nhiệm.","Điều 296: kéo dài thời hạn, từ chối thực hiện hợp đồng trong trường hợp bất khả kháng theo điều kiện luật định."])
],
"quiz":[
{"q":"Phạt vi phạm trong hợp đồng thương mại có tự động phát sinh khi một bên vi phạm không?","opts":["Có, luôn luôn","Không, phải có thỏa thuận phạt","Chỉ cần có thiệt hại","Chỉ cần bên bị vi phạm yêu cầu"],"a":1,"why":"Điều 300 LTM yêu cầu có thỏa thuận phạt vi phạm."},
{"q":"Mức phạt vi phạm thông thường theo Điều 301 LTM tối đa là bao nhiêu?","opts":["5% giá trị toàn bộ hợp đồng","8% giá trị phần nghĩa vụ bị vi phạm","10% giá trị toàn bộ hợp đồng","Không giới hạn"],"a":1,"why":"Mức phạt thông thường không quá 8% giá trị phần nghĩa vụ hợp đồng bị vi phạm, trừ trường hợp luật có quy định khác."},
{"q":"Yếu tố nào là căn cứ phát sinh trách nhiệm bồi thường thiệt hại theo LTM?","opts":["Chỉ cần có vi phạm","Vi phạm, thiệt hại thực tế và quan hệ nhân quả trực tiếp","Chỉ cần có điều khoản phạt","Chỉ cần bên bị vi phạm không hài lòng"],"a":1,"why":"Điều 303 LTM quy định ba căn cứ cơ bản."},
{"q":"Bên yêu cầu bồi thường cần làm gì?","opts":["Không cần chứng minh","Chứng minh tổn thất theo luật","Chỉ gửi tin nhắn","Tự ấn định thiệt hại"],"a":1,"why":"Điều 304 LTM quy định nghĩa vụ chứng minh tổn thất thuộc bên yêu cầu bồi thường."}
],
"essay":["Phân biệt phạt vi phạm và bồi thường thiệt hại trong hợp đồng thương mại.","Hợp đồng không có điều khoản phạt. Bên mua giao hàng trễ và bên bán yêu cầu phạt 8%. Yêu cầu này có căn cứ không? Giải thích.","Phân tích điều kiện áp dụng chế tài bồi thường thiệt hại.","Trình bày các trường hợp miễn trách nhiệm do vi phạm hợp đồng theo Luật Thương mại."]
},
"Chương 4 · Phục hồi & phá sản": {
"tag":"Chú ý luật mới và bài tập chia tài sản", "time":"45–60 phút", "goal":"Phân biệt mất khả năng thanh toán với phá sản; xác định người có quyền/nghĩa vụ nộp đơn và thứ tự phân chia tài sản.",
"lessons":[
("1. Khái niệm cốt lõi", "Mất khả năng thanh toán và phá sản không phải một. Mất khả năng thanh toán là tình trạng không thực hiện nghĩa vụ trả khoản nợ trong thời hạn luật định kể từ ngày đến hạn; phá sản là tình trạng được Tòa án tuyên bố theo thủ tục luật định.", ["Không được kết luận doanh nghiệp phá sản chỉ vì đang nợ nhiều.","Cần kiểm tra khoản nợ đến hạn, thời gian không thanh toán và các điều kiện luật định.","Phục hồi là cơ hội tái cơ cấu/tiếp tục hoạt động; phá sản là thủ tục tư pháp có thể dẫn đến thanh lý và phân chia tài sản."]),
("2. Ai có quyền hoặc nghĩa vụ nộp đơn?", "Đề thi hay hỏi theo vai trò: chủ nợ, người lao động, người đại diện, chủ doanh nghiệp, thành viên/cổ đông, người quản lý. Phải mở đúng điều khoản của Luật Phục hồi, phá sản 2025 mà giảng viên yêu cầu.", ["Lập bảng 3 cột: chủ thể – quyền hay nghĩa vụ – điều kiện/thời điểm.","Không đánh đồng quyền yêu cầu mở thủ tục với quyền đề xuất/ tham gia phương án phục hồi.","Khi làm bài phải trích đúng điều, khoản theo bản luật 2025 đang được áp dụng trong học phần."]),
("3. Khung quy trình cần hiểu", "Nhớ logic hơn là học vẹt từng bước: nộp đơn → Tòa án xem xét/thụ lý → mở hoặc không mở thủ tục → quản lý tài sản và xác minh nghĩa vụ → hội nghị chủ nợ/ phương án phục hồi → công nhận phục hồi hoặc tuyên bố phá sản và xử lý tài sản.", ["Kiểm tra điều kiện và chủ thể nộp đơn.","Xác định hậu quả của việc thụ lý/mở thủ tục đối với việc đòi nợ và xử lý tài sản.","Theo dõi phương án phục hồi, biểu quyết và hậu quả nếu phục hồi không thành."]),
("4. Phân chia tài sản", "Đây là dạng bài phải làm theo dữ kiện, không được tự chia theo cảm tính. Trước hết xác định tài sản thuộc khối tài sản phá sản, chi phí thủ tục, khoản nợ có bảo đảm và không có bảo đảm; sau đó áp dụng đúng thứ tự ưu tiên của điều luật hiện hành.", ["Tách riêng tài sản bảo đảm và nghĩa vụ được bảo đảm.","Tính giá trị tài sản bảo đảm; nếu thiếu thì phần thiếu được xử lý theo quy định về nợ không có bảo đảm.","Xác định thứ tự ưu tiên thanh toán theo đúng Điều 43 của Luật Phục hồi, phá sản 2025 được nhắc trong review.","Nếu tài sản không đủ cho cùng một thứ tự ưu tiên, phân chia theo tỷ lệ theo luật."]),
("5. Phân biệt giải thể và phá sản", "Giải thể là chấm dứt doanh nghiệp theo các trường hợp luật định; về nguyên tắc phải bảo đảm thanh toán hết nợ và nghĩa vụ tài sản. Phá sản gắn với mất khả năng thanh toán và quyết định của Tòa án theo thủ tục phá sản.", ["Giải thể: thủ tục hành chính/doanh nghiệp theo Luật Doanh nghiệp; phải thanh toán hết nghĩa vụ.","Phá sản: thủ tục tư pháp; có thể không đủ tài sản thanh toán toàn bộ nợ.","Hậu quả đối với chủ doanh nghiệp/người quản lý có thể khác nhau; đối chiếu điều luật hiện hành."])
],
"quiz":[
{"q":"Mất khả năng thanh toán có đồng nghĩa doanh nghiệp đã bị tuyên bố phá sản không?","opts":["Có","Không, phải theo thủ tục và có quyết định của Tòa án","Có nếu nợ lớn","Có nếu chủ nợ yêu cầu"],"a":1,"why":"Mất khả năng thanh toán là điều kiện/tình trạng pháp lý; phá sản gắn với quyết định tuyên bố của Tòa án."},
{"q":"Khi giải bài phân chia tài sản, bước đầu tiên nên làm gì?","opts":["Chia đều cho tất cả chủ nợ","Xác định khối tài sản và phân loại nợ, tài sản bảo đảm","Trả cổ đông trước","Bỏ qua chi phí thủ tục"],"a":1,"why":"Phải xác định tài sản, nghĩa vụ có bảo đảm và các khoản nợ trước khi áp dụng thứ tự ưu tiên."},
{"q":"Giải thể và phá sản khác nhau căn bản ở điểm nào?","opts":["Tên gọi","Căn cứ, điều kiện, thủ tục và hậu quả pháp lý","Đều do chủ nợ quyết định","Không có điểm khác"],"a":1,"why":"Giải thể và phá sản có căn cứ, điều kiện, cơ quan/thủ tục và cách xử lý nghĩa vụ khác nhau."}
],
"essay":["Phân biệt mất khả năng thanh toán và phá sản.","Ai có quyền và ai có nghĩa vụ nộp đơn yêu cầu mở thủ tục theo Luật Phục hồi, phá sản 2025? Hãy phân tích theo từng nhóm chủ thể.","Trình bày nguyên tắc và thứ tự phân chia tài sản theo Điều 43 Luật Phục hồi, phá sản 2025.","Phân biệt giải thể doanh nghiệp với phá sản doanh nghiệp."]
},
"Chương 5 · Giải quyết tranh chấp kinh doanh": {
"tag":"Trọng tài và Tòa án: phân biệt đúng", "time":"50–60 phút", "goal":"Chọn được phương thức giải quyết tranh chấp, xác định thẩm quyền, hiệu lực và căn cứ hủy phán quyết trọng tài.",
"lessons":[
("1. Bốn phương thức giải quyết", "Có bốn phương thức thường học: thương lượng, hòa giải, trọng tài và Tòa án. Chọn phương thức tùy mục tiêu: giữ quan hệ, bảo mật, chi phí, tính cưỡng chế và khả năng thi hành.", ["Thương lượng: các bên tự trao đổi, không có bên thứ ba quyết định.","Hòa giải: có bên thứ ba hỗ trợ; kết quả dựa trên sự tự nguyện/thỏa thuận.","Trọng tài: dựa trên thỏa thuận trọng tài hợp lệ; phán quyết có tính chung thẩm.","Tòa án: cơ quan xét xử nhà nước, giải quyết theo thủ tục tố tụng; bản án có cơ chế cưỡng chế thi hành."]),
("2. Trọng tài vụ việc và trọng tài quy chế", "Trọng tài vụ việc (Ad hoc) được thành lập cho vụ tranh chấp cụ thể và kết thúc khi giải quyết xong. Trọng tài quy chế hoạt động tại trung tâm, có danh sách trọng tài viên và quy tắc tố tụng riêng.", ["Ad hoc: linh hoạt, các bên phải chủ động nhiều hơn.","Quy chế: có tổ chức/trung tâm hỗ trợ và quy tắc tố tụng.","Không nhầm trung tâm trọng tài với Tòa án; trọng tài không phải cơ quan xét xử nhà nước."]),
("3. Điều kiện và nguyên tắc trọng tài", "Trọng tài không tự có thẩm quyền chỉ vì tranh chấp là thương mại. Cần kiểm tra thỏa thuận trọng tài bằng văn bản và phạm vi tranh chấp có thuộc thẩm quyền theo luật không.", ["Điều 5–6 Luật TTTM: nguyên tắc giải quyết và hiệu lực của thỏa thuận trọng tài; lưu ý trường hợp thỏa thuận vô hiệu/không thể thực hiện.","Trọng tài viên độc lập, khách quan, vô tư; các bên bình đẳng; phiên họp không công khai trừ khi có thỏa thuận khác.","Trọng tài viên phải đáp ứng tiêu chuẩn, điều kiện theo Điều 20 và các trường hợp không được làm trọng tài viên theo luật."]),
("4. Phán quyết trọng tài và hủy phán quyết", "Phán quyết trọng tài có tính chung thẩm; Tòa án không xét xử phúc thẩm nội dung như với bản án sơ thẩm. Tuy nhiên, luật cho phép yêu cầu hủy trong các căn cứ giới hạn.", ["Đọc Điều 68 Luật TTTM về căn cứ hủy phán quyết.","Đọc Điều 69 về quyền yêu cầu hủy và thời hạn; Điều 71 về thủ tục Tòa án xét đơn.","Hủy phán quyết không đồng nghĩa Tòa án xử lại toàn bộ nội dung tranh chấp."]),
("5. Tòa án giải quyết tranh chấp", "Khi đề hỏi Tòa nào có thẩm quyền, phân tích theo 3 lớp: thẩm quyền theo vụ việc, theo cấp Tòa án và theo lãnh thổ. Phải dùng cơ cấu Tòa án và BLTTDS đã được sửa đổi, bổ sung đang có hiệu lực tại thời điểm thi.", ["Theo vụ việc: xác định có phải tranh chấp kinh doanh, thương mại thuộc phạm vi luật định không.","Theo cấp: kiểm tra quy định tổ chức TAND hiện hành, không chép máy móc sơ đồ cũ trong slide.","Theo lãnh thổ: nguyên tắc thường là Tòa nơi bị đơn cư trú/làm việc/đặt trụ sở, trừ trường hợp ngoại lệ hoặc thỏa thuận hợp pháp."]),
("6. Công thức làm bài tình huống", "Dùng công thức 6 bước: xác định quan hệ pháp luật → chủ thể → sự kiện và mốc thời gian → chọn luật → đối chiếu điều kiện → kết luận quyền/nghĩa vụ và hậu quả.", ["Mở đầu: ‘Vấn đề pháp lý cần giải quyết là…’.","Căn cứ: ghi tên văn bản, điều, khoản.","Phân tích: nêu điều kiện luật định rồi đối chiếu từng dữ kiện.","Kết luận: trả lời thẳng ai có quyền, ai vi phạm, chế tài/phương thức nào được áp dụng."])
],
"quiz":[
{"q":"Trọng tài thương mại có thẩm quyền giải quyết tranh chấp dựa trên cơ sở quan trọng nào?","opts":["Chỉ cần một bên yêu cầu","Thỏa thuận trọng tài hợp lệ và tranh chấp thuộc thẩm quyền","Có đơn gửi công an","Có sự đồng ý của Tòa án trước khi tranh chấp"],"a":1,"why":"Trọng tài dựa trên sự tự nguyện/thỏa thuận trọng tài hợp lệ và phạm vi thẩm quyền theo luật."},
{"q":"Phán quyết trọng tài về nguyên tắc có tính chất gì?","opts":["Sơ thẩm","Phúc thẩm","Chung thẩm","Chỉ là khuyến nghị"],"a":2,"why":"Phán quyết trọng tài là chung thẩm theo Luật Trọng tài thương mại."},
{"q":"Điều nào của Luật Trọng tài thương mại quy định căn cứ hủy phán quyết?","opts":["Điều 20","Điều 30","Điều 68","Điều 100"],"a":2,"why":"Điều 68 quy định căn cứ hủy phán quyết trọng tài."},
{"q":"Khi xác định thẩm quyền Tòa án, nên phân tích theo những lớp nào?","opts":["Chỉ theo địa chỉ nguyên đơn","Vụ việc, cấp Tòa và lãnh thổ","Chỉ theo giá trị tranh chấp","Chỉ theo nơi ký hợp đồng"],"a":1,"why":"Cần xác định đủ thẩm quyền theo vụ việc, theo cấp và theo lãnh thổ."}
],
"essay":["So sánh giải quyết tranh chấp bằng trọng tài thương mại và Tòa án.","Phân biệt trọng tài vụ việc và trọng tài quy chế.","Trình bày các căn cứ hủy phán quyết trọng tài theo Điều 68 Luật Trọng tài thương mại.","Một hợp đồng có điều khoản trọng tài. Một bên vẫn khởi kiện tại Tòa án. Hãy phân tích hướng xử lý và các ngoại lệ cần kiểm tra."]
}
}

LAW_LIST = [
("Hiến pháp 2013 và Nghị quyết 203/2025/QH15", "Khung hiến định; lưu ý nội dung sửa đổi, bổ sung năm 2025."),
("Luật Ban hành văn bản quy phạm pháp luật 2025", "Luật số 87/2025/QH15 và văn bản sửa đổi, bổ sung liên quan."),
("Bộ luật Dân sự 2015", "Trọng tâm hợp đồng: Điều 117, 123–133, 386–401, 420 và đại diện."),
("Bộ luật Tố tụng dân sự 2015 (đã sửa đổi, bổ sung)", "Thẩm quyền Tòa án, khởi kiện, sơ thẩm, phúc thẩm và thủ tục liên quan; kiểm tra mô hình Tòa án hiện hành."),
("Luật Doanh nghiệp 2020 (đã sửa đổi, bổ sung năm 2025)", "Điều 17; các loại hình; quản trị CTCP/TNHH; đăng ký và tổ chức lại."),
("Nghị định 168/2025/NĐ-CP", "Đăng ký doanh nghiệp và hộ kinh doanh; dùng bản đang có hiệu lực."),
("Luật Hợp tác xã 2023 và Nghị định 113/2024/NĐ-CP", "Khái niệm, tổ chức, thành viên và hướng dẫn thi hành."),
("Luật Phục hồi, phá sản 2025", "Nguồn trọng tâm theo hình ảnh/review; đặc biệt chủ thể nộp đơn và Điều 43 về phân chia tài sản."),
("Luật Thương mại 2005", "Chế tài: Điều 292–316; phạt vi phạm Điều 300–301; bồi thường Điều 302–305."),
("Luật Trọng tài thương mại 2010", "Thỏa thuận trọng tài, trọng tài viên, phán quyết và hủy phán quyết; chú ý Điều 68–71."),
("Các văn bản hướng dẫn, sửa đổi và quy định liên quan", "Luôn đối chiếu văn bản hợp nhất/văn bản sửa đổi có hiệu lực tại ngày thi.")
]


# Tạo đủ 20 câu hỏi riêng cho TỪNG chương. Các câu bổ sung được rút trực tiếp từ
# các ý gạch đầu dòng trong phần bài học, không tự thêm số điều luật.
import random

def build_chapter_quiz(chapter_data, seed):
    questions = list(chapter_data["quiz"])
    facts = []
    for lesson_title, explanation, bullets in chapter_data["lessons"]:
        for bullet in bullets:
            fact = bullet.strip()
            if fact and fact not in facts:
                facts.append(fact)
    rng = random.Random(seed)
    rng.shuffle(facts)
    all_facts = list(facts)
    idx = 0
    while len(questions) < 20 and facts:
        correct_fact = facts[idx % len(facts)]
        distractors = [x for x in all_facts if x != correct_fact]
        rng.shuffle(distractors)
        opts = [correct_fact] + distractors[:3]
        rng.shuffle(opts)
        questions.append({
            "q": "Phát biểu nào sau đây phù hợp với nội dung đã học trong chương?",
            "opts": opts,
            "a": opts.index(correct_fact),
            "why": f"Đây là ý cần nhớ trong phần bài học: {correct_fact}",
            "topic": "Ôn lại ý chính trong bài"
        })
        idx += 1
    # Nếu một chương có ít hơn 20 gạch đầu dòng độc lập, bổ sung câu hỏi ôn ý
    # bằng cách thay đổi góc hỏi, vẫn giữ nguyên dữ kiện kiến thức gốc.
    while len(questions) < 20 and all_facts:
        fact = all_facts[(len(questions) * 3) % len(all_facts)]
        distractors = [x for x in all_facts if x != fact]
        rng.shuffle(distractors)
        opts = [fact] + distractors[:3]
        rng.shuffle(opts)
        questions.append({
            "q": "Khi ôn chương này, nội dung nào dưới đây cần được ghi nhớ?",
            "opts": opts,
            "a": opts.index(fact),
            "why": f"Đối chiếu với phần bài học: {fact}",
            "topic": "Củng cố kiến thức nền"
        })
    return questions[:20]

CHAPTER_QUIZZES = {
    name: build_chapter_quiz(chapter, i + 31)
    for i, (name, chapter) in enumerate(CHAPTERS.items())
}

PAGES = ["Tổng quan", "Học theo chương", "Luyện tự luận", "Kết quả ôn tập", "Sổ tay luật"]
if "current_page" not in st.session_state:
    st.session_state.current_page = "Tổng quan"
if "done" not in st.session_state:
    st.session_state.done = set()
if "chapter_results" not in st.session_state:
    st.session_state.chapter_results = {}
if "essay_drafts" not in st.session_state:
    st.session_state.essay_drafts = {}

st.markdown("<div class='nav-wrap'>", unsafe_allow_html=True)
page = st.radio("Khu vực học tập", PAGES, horizontal=True,
                index=PAGES.index(st.session_state.current_page),
                label_visibility="collapsed", key="main_navigation")
st.session_state.current_page = page
st.markdown("</div>", unsafe_allow_html=True)

if page == "Tổng quan":
    st.markdown("""
    <div class='hero'>
      <span class='eyebrow'>LAW STUDY STUDIO</span>
      <h1>Luật Kinh doanh · Góc học tập</h1>
      <p>Học theo từng chương, luyện câu hỏi riêng cho từng phần và theo dõi những kiến thức cần ôn lại.</p>
    </div>""", unsafe_allow_html=True)
    total_q = sum(len(v) for v in CHAPTER_QUIZZES.values())
    done_count = len(st.session_state.done)
    tested_count = len(st.session_state.chapter_results)
    c1,c2,c3 = st.columns(3)
    c1.metric("Chương học", f"{len(CHAPTERS)}")
    c2.metric("Ngân hàng câu hỏi", f"{total_q} câu", "20 câu / chương")
    c3.metric("Chương đã kiểm tra", f"{tested_count}/{len(CHAPTERS)}")
    st.markdown("### Chọn chương để bắt đầu")
    for i,(name,ch) in enumerate(CHAPTERS.items(),1):
        result = st.session_state.chapter_results.get(name)
        score_text = f" · Lần gần nhất: {result['score']}/{result['total']}" if result else ""
        status = "Đã hoàn thành" if name in st.session_state.done else "Chưa hoàn thành"
        with st.container(border=True):
            a,b = st.columns([5,1])
            a.markdown(f"**{i}. {name}**")
            a.caption(ch["goal"])
            a.caption(f"{status}{score_text}")
            if b.button("Học ngay →", key=f"overview_go_{i}"):
                st.session_state.target_ch = name
                st.session_state.current_page = "Học theo chương"
                st.rerun()
    st.markdown("<div class='soft'><b>Mẹo học:</b> Đọc từng mục lý thuyết → làm đủ 20 câu của chương → xem phần sai trong Kết quả ôn tập → quay lại học đúng mục còn yếu → luyện tự luận.</div>", unsafe_allow_html=True)

elif page == "Học theo chương":
    st.markdown("""
    <div class='hero'>
      <span class='eyebrow'>LEARN · PRACTICE · REVIEW</span>
      <h1>Học theo chương</h1>
      <p>Mỗi chương có phần giải thích, câu hỏi tự luận và bài trắc nghiệm 20 câu riêng để kiểm tra mức độ hiểu bài.</p>
    </div>""", unsafe_allow_html=True)
    names = list(CHAPTERS.keys())
    default = names.index(st.session_state.get("target_ch", names[0])) if st.session_state.get("target_ch") in names else 0
    chosen = st.selectbox("Chọn chương muốn học", names, index=default)
    c = CHAPTERS[chosen]
    st.markdown(f"<div class='lav'><b>Mục tiêu chương:</b> {c['goal']}</div>", unsafe_allow_html=True)
    st.markdown("### 1. Nội dung bài học")
    for title, explain, bullets in c["lessons"]:
        with st.expander(title):
            st.write(explain)
            for bullet in bullets:
                st.markdown(f"- {bullet}")
    st.markdown("### 2. Câu hỏi tự luận cuối chương")
    for i,q in enumerate(c["essay"],1):
        with st.expander(f"Câu tự luận {i}: {q}"):
            st.markdown("**Khung triển khai:** xác định vấn đề → nêu căn cứ pháp lý → giải thích quy định → áp dụng/so sánh → kết luận.")
            draft_key = f"{chosen}_{i}"
            st.text_area("Bài làm thử", key=f"chapter_essay_{draft_key}", height=125,
                         placeholder="Viết câu trả lời của bạn tại đây…")
    st.markdown("### 3. Bài trắc nghiệm chương")
    st.caption("20 câu cho riêng chương này. Chọn đáp án cho từng câu rồi nộp bài để xem điểm và các phần cần ôn lại.")
    quiz = CHAPTER_QUIZZES[chosen]
    with st.form(f"quiz_form_{names.index(chosen)}"):
        answers = []
        for i,q in enumerate(quiz,1):
            st.markdown(f"**Câu {i}/20. {q['q']}**")
            answers.append(st.radio("Chọn một đáp án", q["opts"], key=f"answer_{names.index(chosen)}_{i}", index=None))
            if i < len(quiz):
                st.divider()
        submitted = st.form_submit_button("Nộp bài · Xem kết quả", use_container_width=True)
    if submitted:
        correct = 0
        wrong_topics = []
        wrong_items = []
        for i,(q,ans) in enumerate(zip(quiz,answers),1):
            is_correct = ans is not None and q["opts"].index(ans) == q["a"]
            if is_correct:
                correct += 1
            else:
                topic = q.get("topic", "Kiến thức chương")
                if topic not in wrong_topics:
                    wrong_topics.append(topic)
                wrong_items.append({"number":i,"question":q["q"],"correct":q["opts"][q["a"]],"why":q["why"],"topic":topic})
        st.session_state.chapter_results[chosen] = {
            "score":correct, "total":len(quiz), "wrong_topics":wrong_topics,
            "wrong_items":wrong_items, "answered":sum(a is not None for a in answers)
        }
        st.rerun()
    latest = st.session_state.chapter_results.get(chosen)
    if latest:
        st.markdown("#### Kết quả lần làm gần nhất")
        score_col, percent_col = st.columns(2)
        score_col.metric("Số câu đúng", f"{latest['score']}/{latest['total']}")
        percent_col.metric("Tỷ lệ", f"{latest['score']/latest['total']*100:.0f}%")
        if latest["wrong_items"]:
            st.warning("Bạn nên ôn lại các câu sai bên dưới.")
            for item in latest["wrong_items"]:
                with st.expander(f"Câu {item['number']}: {item['question']}"):
                    st.markdown(f"**Đáp án đúng:** {item['correct']}")
                    st.write(item["why"])
        else:
            st.success("Rất tốt! Bạn đã trả lời đúng toàn bộ câu hỏi của chương này.")
    if st.button("Đánh dấu đã học xong chương", key=f"done_{names.index(chosen)}"):
        st.session_state.done.add(chosen)
        st.success("Đã ghi nhận chương hoàn thành.")

elif page == "Luyện tự luận":
    st.markdown("""
    <div class='hero'>
      <span class='eyebrow'>ESSAY PRACTICE</span>
      <h1>Phòng luyện thi tự luận</h1>
      <p>Luyện cách lập luận và trình bày bài làm theo từng chủ đề trong chương.</p>
    </div>""", unsafe_allow_html=True)
    allq = [(chapter,q) for chapter,ch in CHAPTERS.items() for q in ch["essay"]]
    cat = st.selectbox("Lọc câu hỏi theo chương", ["Tất cả"] + list(CHAPTERS.keys()))
    subset = [(chapter,q) for chapter,q in allq if cat == "Tất cả" or chapter == cat]
    for i,(chapter,q) in enumerate(subset,1):
        with st.expander(f"{i}. {q}"):
            st.caption(chapter)
            st.markdown("1. Xác định vấn đề pháp lý.\n2. Chọn đúng văn bản và điều khoản.\n3. Nêu quy định, điều kiện pháp lý.\n4. Đối chiếu từng dữ kiện hoặc tiêu chí so sánh.\n5. Kết luận rõ ràng.")
            st.text_area("Bài làm của bạn", key=f"essay_room_{i}_{chapter}", height=160)
    st.markdown("<div class='soft'><b>Khung viết tình huống:</b><br>Vấn đề pháp lý → Căn cứ pháp lý → Quy định pháp luật → Đối chiếu tình huống → Kết luận.</div>", unsafe_allow_html=True)

elif page == "Kết quả ôn tập":
    st.markdown("""
    <div class='hero'>
      <span class='eyebrow'>YOUR STUDY PROGRESS</span>
      <h1>Kết quả ôn tập</h1>
      <p>Theo dõi chương đã học, điểm từng chương và những phần kiến thức bạn cần quay lại.</p>
    </div>""", unsafe_allow_html=True)
    completed = len(st.session_state.done)
    tested = len(st.session_state.chapter_results)
    a,b,c = st.columns(3)
    a.metric("Đã đánh dấu hoàn thành", f"{completed}/{len(CHAPTERS)}")
    b.metric("Đã làm bài kiểm tra", f"{tested}/{len(CHAPTERS)}")
    avg = (sum(v["score"]/v["total"]*10 for v in st.session_state.chapter_results.values()) / tested) if tested else 0
    c.metric("Điểm trung bình", f"{avg:.1f}/10" if tested else "Chưa có")
    st.markdown("### Tiến độ theo chương")
    for name,ch in CHAPTERS.items():
        result = st.session_state.chapter_results.get(name)
        if result:
            pct = result["score"]/result["total"]
            st.markdown(f"**{name}**")
            st.progress(pct, text=f"{result['score']}/{result['total']} câu đúng · {pct*100:.0f}%")
            if result["wrong_items"]:
                st.markdown("**Cần ôn lại:**")
                for topic in result["wrong_topics"]:
                    st.markdown(f"- {topic}")
                with st.expander("Xem câu sai và đáp án"):
                    for item in result["wrong_items"]:
                        st.markdown(f"**Câu {item['number']}. {item['question']}**")
                        st.markdown(f"Đáp án: {item['correct']}")
                        st.caption(item["why"])
            else:
                st.success("Chưa ghi nhận câu sai ở lần làm gần nhất.")
        else:
            st.markdown(f"**{name}**")
            st.progress(0, text="Chưa làm bài kiểm tra chương này")
        st.divider()
    if not tested:
        st.info("Sau khi làm bài 20 câu ở từng chương, điểm số và kiến thức cần ôn lại sẽ tự động xuất hiện tại đây.")
    st.caption("Lưu ý: kết quả hiện được lưu trong phiên làm việc Streamlit. Nếu tải lại ứng dụng hoặc mở bằng phiên mới, dữ liệu phiên có thể được làm mới.")

elif page == "Sổ tay luật":
    st.markdown("""
    <div class='hero'>
      <span class='eyebrow'>LEGAL QUICK REFERENCE</span>
      <h1>Sổ tay tra cứu văn bản</h1>
      <p>Danh mục văn bản theo tài liệu và hai hình ảnh bạn đã cung cấp.</p>
    </div>""", unsafe_allow_html=True)
    for law,focus in LAW_LIST:
        with st.expander(law):
            st.write(focus)
    st.markdown("### Các nhóm điều khoản cần tra")
    refs = {
        "Doanh nghiệp":"Điều 17; 34–36; các quy định về loại hình và quản trị công ty trong Luật Doanh nghiệp (đối chiếu bản sửa đổi).",
        "Hợp đồng":"Điều 117; 123–133; 386–401 Bộ luật Dân sự 2015 và quy định về đại diện.",
        "Chế tài thương mại":"Điều 292; 294–296; 300–305; 307; 308–316 Luật Thương mại 2005.",
        "Phục hồi, phá sản":"Luật Phục hồi, phá sản 2025 theo tài liệu giảng viên; tra cứu đúng bản luật được yêu cầu.",
        "Trọng tài":"Điều 5–6; 18–20; 30–39; 45–53; 62–71 Luật Trọng tài thương mại 2010.",
        "Tòa án":"Bộ luật Tố tụng dân sự và văn bản sửa đổi, bổ sung có hiệu lực tại thời điểm áp dụng."
    }
    for k,v in refs.items():
        st.markdown(f"- **{k}:** {v}")


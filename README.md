# Luật Kinh Doanh – Study Studio

Ứng dụng Streamlit ôn thi giữa kỳ môn Luật Kinh doanh.

## Chạy local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy bằng GitHub + Streamlit Community Cloud
1. Đưa toàn bộ thư mục này lên một GitHub repository.
2. Vào https://share.streamlit.io/ và đăng nhập bằng GitHub.
3. Chọn repository, branch và file `app.py`.
4. Deploy.

## Các khu vực
- Tổng quan
- Học theo chương
- Luyện tự luận
- Kết quả ôn tập
- Sổ tay luật

Mỗi chương có 20 câu hỏi trắc nghiệm riêng. Kết quả và phần cần ôn lại được tổng hợp trong mục Kết quả ôn tập. Dữ liệu tiến độ hiện lưu trong phiên Streamlit; khi cần lưu bền vững giữa các phiên, có thể bổ sung SQLite hoặc cơ sở dữ liệu ngoài.

Giao diện sử dụng Poppins, nền hồng pastel và tím lavender, thanh điều hướng ngang, cùng hiệu ứng chuyển động nhẹ.

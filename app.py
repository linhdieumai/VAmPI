from config import vuln_app
import os

'''
 Decide if you want to server a vulnerable version or not!
 DO NOTE: some functionalities will still be vulnerable even if the value is set to 0
          as it is a matter of bad practice. Such an example is the debug endpoint.
'''
vuln = int(os.getenv('vulnerable', 1))
# vuln=1
# token alive for how many seconds?
alive = int(os.getenv('tokentimetolive', 60))

@app.after_request
def add_security_headers(response):
    # Chống trình duyệt tự đoán kiểu dữ liệu
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Ghi đè tên Server để giấu thông tin thật
    response.headers['Server'] = 'VAmPI-Secure-Server'
    # Chống gọi tài nguyên chéo từ trang lạ
    response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'
    # Ngăn trình duyệt lưu cache dữ liệu nhạy cảm
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

# start the app with port 5000 and debug on!
if __name__ == '__main__':
    vuln_app.run(host='0.0.0.0', port=5000, debug=True)

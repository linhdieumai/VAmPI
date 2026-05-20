from config import vuln_app
import os

'''
 Decide if you want to server a vulnerable version or not!
 DO NOTE: some functionalities will still be vulnerable even if the value is set to 0
          as it is a matter of bad practice. Such an example is the debug endpoint.
'''
vuln = int(os.getenv('vulnerable', 1))
# vuln=1
alive = int(os.getenv('tokentimetolive', 60))

# --- BẮT ĐẦU ĐOẠN CODE SỬA LỖI ZAP ---
# Lấy đối tượng lõi Flask từ Connexion app
app = vuln_app.app

@app.after_request
def add_security_headers(response):
    # 1. Khắc phục lỗi X-Content-Type-Options Header Missing [10021]
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # 2. Khắc phục lỗi Cross-Origin-Resource-Policy Header Missing or Invalid [90004]
    response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'
    
    return response
# --- KẾT THÚC ĐOẠN CODE SỬA LỖI ZAP ---

# start the app with port 5000 and debug on!
if __name__ == '__main__':
    vuln_app.run(host='0.0.0.0', port=5000, debug=True)

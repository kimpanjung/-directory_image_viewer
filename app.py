from flask import Flask, render_template, send_file, request, send_file, session
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# 이미지 폴더 경로
# image_folder_path = '/Users/kaflix_wanya/Desktop/add_test/2024/01/02'
base_image_folder_path = '/Users/kaflix_wanya/Desktop/add_test'

@app.route('/')
def index():
     # URL 파라미터에서 'parameter' 값을 읽어옴
    parameter = request.args.get('parameter', default='')

    # URL 파라미터를 기반으로 이미지 폴더 경로 설정
    image_folder_path = os.path.join(base_image_folder_path, parameter)

    
    # 이미지 폴더 내의 파일 목록 가져오기
    image_list = []
    for root, dirs, files in os.walk(image_folder_path):
        for file in files:
            # 이미지 파일의 확장자를 확인하여 이미지 파일인 경우에만 추가
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_list.append(file)

    session['image_folder_path'] = image_folder_path

    return render_template('index.html', image_list=image_list)


@app.route('/image/<filename>')
def serve_image(filename):
    # 이미지 파일의 전체 경로
    # image_path = os.path.join(base_image_folder_path, filename)
    image_path = os.path.join(session['image_folder_path'], filename)

    # 해당 이미지 파일 서빙
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port=8103)

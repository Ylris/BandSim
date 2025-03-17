from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# 配置上传文件存储路径
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 配置允许的文件类型
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # 生成安全的文件名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{file.filename}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        # 保存文件
        file.save(filepath)
        
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'filepath': filepath
        }), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/api/health', methods=['GET'])
def get_health_data():
    # 模拟健康数据
    health_data = {
        'heart_rate': 75,
        'steps': 8000,
        'calories': 500,
        'sleep_hours': 7.5
    }
    return jsonify(health_data)

@app.route('/api/sports', methods=['GET'])
def get_sports_data():
    # 模拟运动数据
    sports_data = {
        'running_distance': 5.2,
        'cycling_distance': 15.0,
        'swimming_distance': 1.0,
        'workout_duration': 45
    }
    return jsonify(sports_data)

@app.route('/api/settings', methods=['GET', 'POST'])
def handle_settings():
    if request.method == 'GET':
        # 模拟设置数据
        settings_data = {
            'notifications': True,
            'dark_mode': False,
            'language': 'en',
            'units': 'metric'
        }
        return jsonify(settings_data)
    
    elif request.method == 'POST':
        data = request.get_json()
        # 这里可以添加设置保存逻辑
        return jsonify({'message': 'Settings updated successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
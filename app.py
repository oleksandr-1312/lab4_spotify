from flask import Flask
from app.controller.user_controller import user_bp

app = Flask(__name__)

# Реєструємо наші маршрути
app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == '__main__':
    # Запускаємо сервер на стандартному порту 5000
    app.run(debug=True)
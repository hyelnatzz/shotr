from app import create_app
from app.config import Config

app = create_app(Config)

app.run(debug=True, host='0.0.0.0')
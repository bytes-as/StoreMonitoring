from app import create_app
import config

app = create_app(config.Config())

if __name__ == '__main__':
    app.run(port=7777, debug = True)
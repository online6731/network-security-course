from api import app
from sniffer import Sniffer

if __name__ == '__main__':
    Sniffer().run()
    app.run(debug=True, host='0.0.0.0')

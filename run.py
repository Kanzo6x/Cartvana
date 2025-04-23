from cartvana.app import createApp

flaskApp = createApp()

if __name__ == '__main__':
    flaskApp.run(debug=True)
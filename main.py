# Flask is lightwight, django is production level

from website import create_app

app = create_app()

if __name__ == '__main__': #this makes so that only if you run this file does the server start, otherwise it starts whenever it is imported
    app.run(debug=True) #run the server, debug true makes it so the app reruns for every change


from website import create_app

app = create_app()
print('hello')
if __name__ == "__main__":
    app.run(debug=True)
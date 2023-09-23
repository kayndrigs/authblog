from website import create_app


if __name__ == "__main__":
    app = create_app()
    # every single change will rerun the flask server
    app.run(debug=True)


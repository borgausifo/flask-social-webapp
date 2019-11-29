from app import app


# Only run the code inside the if statement if we've execute this file.
# We don't want to run our app if we have imported this file, as running the app
# would block and prevent importing this file, since it runs until the app is shut down.
if __name__ == '__main__':
    # Run the app.
    # The debug=True flag is just here for development purposes.
    # It gives us more information if an error happens.
    app.run(debug=True)



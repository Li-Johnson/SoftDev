from flask import Flask, request, render_template, /
                redirect, url_for, session, flash

app = Flask(__name__)


if __name__ == "__main__":
    app.debug = True
    app.run()
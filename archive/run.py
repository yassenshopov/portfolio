from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def current_template():
   return render_template('current/index.html')

if __name__ == '__main__':
   app.run()
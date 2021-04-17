from app import app

# dyno runs app itself
# and don't execute next code
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

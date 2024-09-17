from flask import Flask

app = Flask(__name__)

# Manually set the ENV configuration
app.config["ENV"] = "development"  # or "production" depending on your environment

# Rest of your initialization code
if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views


# Manually set the ENV configuration
app.config["ENV"] = "development"  # or "production" depending on your environment

# Rest of your initialization code

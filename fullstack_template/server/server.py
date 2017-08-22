# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/21 18:59:27 by scollet           #+#    #+#              #
#    Updated: 2017/08/21 18:59:29 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, render_template

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "ey"

if __name__ == "__main__":
    app.run

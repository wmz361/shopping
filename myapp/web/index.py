from flask import Blueprint, render_template

indexBP=Blueprint('indexBP',__name__)

@indexBP.route('/')
def index():
    return render_template('indexUnLogined.html')
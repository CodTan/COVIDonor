from flask import Flask, render_template, Markup

app = Flask(__name__, template_folder = 'templates')

headings = ("one","two",)

# tweet = Markup('<blockquote class=\"twitter-tweet\"><p lang=\"en\" dir=\"ltr\">Sir my father the veteran journalist Saeed Naqvi is in desperate need of a hospital bed with Oxygen. His levels are dipping <a href=\"https://twitter.com/drharshvardhan?ref_src=twsrc%%5Etfw\">@drharshvardhan</a> <a href=\"https://twitter.com/ArvindKejriwal?ref_src=twsrc%%5Etfw\">@ArvindKejriwal</a> <a href=\"https://twitter.com/msisodia?ref_src=twsrc%%5Etfw\">@msisodia</a> <a href=\"https://twitter.com/SatyendarJain?ref_src=twsrc%%5Etfw\">@SatyendarJain</a>.</p>&mdash; Saba Naqvi (@_sabanaqvi) <a href=\"https://twitter.com/_sabanaqvi/status/1385611561515962375?ref_src=twsrc%%5Etfw\">April 23, 2021</a></blockquote> <script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script> ')
tweet = Markup('<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Just to clarify, I did not recover from COVID nor did I get infected. <br>But I got a check for antibodies and it showed antibody positive. So was wondering if I can donate plasma to those in need.</p>&mdash; Sunil Rao (@RaoManjanbail) <a href="https://twitter.com/RaoManjanbail/status/1385814792036765699?ref_src=twsrc%%5Etfw">April 24, 2021</a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>')

data = (
    (tweet,tweet),
    (tweet,tweet)
)


@app.route('/')
def home():
    return 'Welcome!'
    # return render_template("home.html",headings=headings, data=data)
    # return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True) 
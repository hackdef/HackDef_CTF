from flask import Flask, render_template_string

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["PRODUCTION"] = True

@app.route("/")
def index():
  return "yo Sé que Sí enconTrarás mI falla"

@app.route("/<path:template>")
def template(template):
  if len(template) > 500:
    return "Mucho texto!"
  return render_template_string(template)

if __name__ == '__main__':
  app.run()

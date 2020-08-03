@@ -24,11 +24,6 @@ def scrape():
   # return render_template("index.html", mars=mars)
   return render_template("return.html", mars=mars)

@app.route("/hemisphere")
def hemisphere():
    scraping.get_mars_hemisphere()
    return "Hemisphere Scraping Successful!"

if __name__ == "__main__":
   app.run()

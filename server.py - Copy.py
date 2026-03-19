from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        name = request.form.get("name")

        score = 0
        for i in range(1,11):
            if request.form.get(f"q{i}") == "yes":
                score += 1

        if score >= 8:
            stress = "High Stress"
        elif score >= 5:
            stress = "Medium Stress"
        else:
            stress = "Low Stress"

        with open("data.txt", "a") as f:
            f.write(f"{name},{score},{stress}\n")

        return render_template("result.html", name=name, score=score, stress=stress)

    return render_template("index.html")


@app.route("/admin")
def admin():
    students = []

    try:
        with open("data.txt", "r") as f:
            for line in f:
                name, score, stress = line.strip().split(",")
                students.append((name, score, stress))
    except:
        pass

    return render_template("admin.html", students=students)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
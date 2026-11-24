from flask import Flask, render_template, request

app = Flask(__name__)


def parse_grade(value, field_name):
    try:
        grade = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} debe ser un número entre 10 y 70.")
    if not 10 <= grade <= 70:
        raise ValueError(f"{field_name} debe estar entre 10 y 70.")
    return grade


@app.get("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    datos = {"nota1": "", "nota2": "", "nota3": "", "asistencia": ""}
    error = None

    if request.method == "POST":
        datos = {key: request.form.get(key, "").strip() for key in datos}
        try:
            notas = [parse_grade(datos[f"nota{i}"], f"La nota {i}") for i in range(1, 4)]
            asistencia = float(datos["asistencia"])
            if not 0 <= asistencia <= 100:
                raise ValueError("La asistencia debe estar entre 0 y 100%.")
            promedio = sum(notas) / len(notas)
            aprobado = promedio >= 40 and asistencia >= 75
            resultado = {"promedio": promedio, "aprobado": aprobado}
        except ValueError as exc:
            error = str(exc)

    return render_template("ejercicio1.html", datos=datos, resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombres = [request.form.get(f"nombre{i}", "").strip() for i in range(1, 4)] if request.method == "POST" else ["", "", ""]
    ganador = None
    error = None

    if request.method == "POST":
        if any(not nombre for nombre in nombres):
            error = "Completa los tres nombres para continuar."
        else:
            ganador = max(nombres, key=len)

    return render_template("ejercicio2.html", nombres=nombres, ganador=ganador, error=error)


if __name__ == "__main__":
    app.run(debug=True)



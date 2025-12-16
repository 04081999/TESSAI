from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        data = {
            # Variables catégorielles
            "etat_civil": request.form.get("etat_civil"),
            "sexe": request.form.get("sexe"),
            "region": request.form.get("region"),
            "ville": request.form.get("ville"),
            "niveau_etude": request.form.get("niveau_etude"),
            "profession": request.form.get("profession"),
            "chome": request.form.get("chome"),
            "type_logement": request.form.get("type_logement"),
            "situation_familiale": request.form.get("situation_familiale"),
            "assurance": request.form.get("assurance"),
            "acces_internet": request.form.get("acces_internet"),
            "moyen_transport": request.form.get("moyen_transport"),

            # Variables numériques
            "age": request.form.get("age"),
            "revenu_mensuel": request.form.get("revenu_mensuel"),
            "depense_mensuelle": request.form.get("depense_mensuelle"),
            "nombre_enfants": request.form.get("nombre_enfants"),
            "anciennete_emploi": request.form.get("anciennete_emploi"),
            "heures_travail": request.form.get("heures_travail"),
            "distance_travail": request.form.get("distance_travail"),
            "taille_menage": request.form.get("taille_menage"),
        }

        return render_template("result.html", data=data)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
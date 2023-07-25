import os
import psycopg2
from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv('/.env')

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_port = os.getenv('DB_PORT')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
    database= db_name,
    user= db_user,
    host= db_host,
    password= db_password,
    port= db_port)

@app.route("/get-topn/<topn>") 
def get_topn_documents(topn):
    try:
        # connecte à la base de données
        connection = connect_db()
        cursor = connection.cursor()

        # Exécute la requête pour obtenir topn documents avec les scores les plus élevés
        query = """SELECT s.score, c.*
            FROM louis_v004.crawl c
            INNER JOIN louis_v004.score s ON c.id = s.entity_id
            ORDER BY s.score DESC
            LIMIT %s;
            """
        if int(topn) <= 100 and int(topn) > 0: 
            cursor.execute(query,(topn,))  # Passe la valeur de topn dans la requête
        else:
            return "Valeur topn invalide, vérifiez que celle-ci est située entre 1 et 100"
        
        top_documents = cursor.fetchall()
       
        parsed_results = []
        for row in top_documents:

            first_column_value = row[0]
            second_column_value = row[1]
            third_column_value = row[2]
            fourth_column_value = row[3]

            # crée une liste avec les valeurs des colonnes
            parsed_results.append({
                'score': first_column_value,
                'id': second_column_value,
                'url': third_column_value,
                'title': fourth_column_value
                })

        cursor.close()

        #print(parsed_results)

        # Retourne le résultat au format JSON
        return jsonify(parsed_results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(debug=True)
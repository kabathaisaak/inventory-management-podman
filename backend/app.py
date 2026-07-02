from flask import Flask, jsonify, request
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )


@app.route("/products/<int:id>")
def get_product(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id,name,price FROM products WHERE id=%s",
        (id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return jsonify({"message":"Product not found"}),404

    return jsonify({
        "id":row[0],
        "name":row[1],
        "price":float(row[2])
    })



@app.route("/products", methods=["POST"])
def create_product():

    data=request.get_json()

    conn=get_connection()
    cur=conn.cursor()

    cur.execute(
        """
        INSERT INTO products(name,price)
        VALUES(%s,%s)
        RETURNING id
        """,
        (
            data["name"],
            data["price"]
        )
    )

    new_id=cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message":"Product created",
        "id":new_id
    }),201



@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):

    data=request.get_json()

    conn=get_connection()
    cur=conn.cursor()

    cur.execute(
        """
        UPDATE products
        SET name=%s,
            price=%s
        WHERE id=%s
        """,
        (
            data["name"],
            data["price"],
            id
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message":"Product updated"
    })  



@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):

    conn=get_connection()
    cur=conn.cursor()

    cur.execute(
        "DELETE FROM products WHERE id=%s",
        (id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message":"Product deleted"
    })     

@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API",
        "status": "Running"
    })

@app.route("/products")
def get_products():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, price FROM products ORDER BY id")

    rows = cur.fetchall()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": float(row[2])
        })

    cur.close()
    conn.close()

    return jsonify(products)

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
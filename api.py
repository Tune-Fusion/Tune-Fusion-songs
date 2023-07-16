from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL configurations
mysql_config = {
    'host': 'mysql',
    'database': 'tune_fusion_db',
    'user': 'root',
    'password': 'mysql@123'
}


def create_connection():
    try:
        conn = mysql.connector.connect(**mysql_config)
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print('Error:', e)
        return None

@app.route('/songs', methods=['GET'])
def get_songs():
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM song')
            songs = cursor.fetchall()
            cursor.close()
            conn.close()
            return jsonify(songs)
        else:
            return jsonify({'error': 'Unable to connect to the database'}), 500
    except Error as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to fetch songs'}), 500

@app.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM song WHERE song_id=%s', (song_id,))
            song = cursor.fetchone()
            cursor.close()
            conn.close()
            if song:
                return jsonify(song)
            else:
                return jsonify({'error': 'Song not found'}), 404
        else:
            return jsonify({'error': 'Unable to connect to the database'}), 500
    except Error as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to fetch song'}), 500

@app.route('/songs', methods=['POST'])
def create_song():
    try:
        data = request.get_json()
        song_name = data['song_name']
        link = data['link']
        artist_id = data['artist_id']
        user_id = data['user_id']
        upload_date = data['upload_date']
        print("hehe")
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO song (song_name, link, artist_id, user_id, upload_date) VALUES (%s, %s, %s, %s, %s)',
                           (song_name, link, artist_id, user_id, upload_date))
            conn.commit()
            new_song_id = cursor.lastrowid
            cursor.close()
            conn.close()
            return jsonify({'message': 'Song created successfully', 'song_id': new_song_id}), 201
        else:
            return jsonify({'error': 'Unable to connect to the database'}), 500
    except Error as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to create song'}), 500

@app.route('/songs/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    try:
        data = request.get_json()
        song_name = data['song_name']
        link = data['link']
        artist_id = data['artist_id']
        user_id = data['user_id']
        upload_date = data['upload_date']

        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE song SET song_name=%s, link=%s, artist_id=%s, user_id=%s, upload_date=%s WHERE song_id=%s',
                           (song_name, link, artist_id, user_id, upload_date, song_id))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'message': 'Song updated successfully'}), 200
        else:
            return jsonify({'error': 'Unable to connect to the database'}), 500
    except Error as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to update song'}), 500

@app.route('/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM song WHERE song_id=%s', (song_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'message': 'Song deleted successfully'}), 200
        else:
            return jsonify({'error': 'Unable to connect to the database'}), 500
    except Error as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to delete song'}), 500


def initialise_db():
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            with open('schema.sql') as f:
                sql_statements = f.read()
                # Split the SQL statements at semicolon to separate them
                sql_commands = sql_statements.split(';')
                for command in sql_commands:
                    if command.strip():
                        cursor.execute(command)
            conn.commit()
            cursor.close()
            conn.close()
            print('Database initialised successfully')
        else:
            print('Unable to connect to the database')
    except Error as e:
        print('Error:', e)
        print('Failed to initialise database')


if __name__ == '__main__':
    initialise_db()
    app.run(debug=True, host='0.0.0.0', port=8080)


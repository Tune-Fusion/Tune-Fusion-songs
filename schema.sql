-- Create the Artists table
CREATE TABLE artists (
  artist_id INT AUTO_INCREMENT PRIMARY KEY,
  artist_name VARCHAR(100) NOT NULL
);

-- Create the User table
CREATE TABLE User (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(100) NOT NULL,
  username VARCHAR(50) NOT NULL,
  dob DATE NOT NULL,
  location VARCHAR(200) NOT NULL
);

-- Create the Song table
CREATE TABLE song (
  song_id INT AUTO_INCREMENT PRIMARY KEY,
  song_name VARCHAR(200) NOT NULL,
  link VARCHAR(500) NOT NULL,
  artist_id INT NOT NULL,
  user_id INT NOT NULL,
  upload_date DATE NOT NULL,
  FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
  FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Change the AUTO_INCREMENT value for the song table to 1000
ALTER TABLE song AUTO_INCREMENT = 1000;
ALTER TABLE artists AUTO_INCREMENT = 1000;
ALTER TABLE User AUTO_INCREMENT = 1000;

-- Populate the Artists table with fake entries
INSERT INTO artists (artist_name) VALUES
  ('John Doe'),
  ('Jane Smith'),
  ('Mike Johnson'),
  ('Emily Adams'),
  ('David Lee');

-- Populate the User table with fake entries
INSERT INTO User (Name, username, dob, location) VALUES
  ('Alice Johnson', 'alice.j', '1990-05-15', 'New York'),
  ('Bob Williams', 'bob.w', '1985-10-20', 'Los Angeles'),
  ('Charlie Brown', 'charlie.b', '1992-03-08', 'Chicago'),
  ('Eva Martinez', 'eva.m', '1988-12-12', 'Miami'),
  ('Frank Wilson', 'frank.w', '1995-07-02', 'Houston');

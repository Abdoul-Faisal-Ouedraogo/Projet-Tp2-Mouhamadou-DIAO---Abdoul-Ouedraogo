CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);

INSERT INTO tasks (content) VALUES ('Finir le TP Docker'), ('Pousser sur GitHub');
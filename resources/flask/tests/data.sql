INSERT INTO user (name, username, password)
VALUES
    ('user', 'username', 'pbkdf2:sha256:5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8'),
    ('John Doe', 'other', 'pbkdf2:sha256:5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8');

INSERT INTO task (user_id, body)
VALUES
    ('test title', 1);

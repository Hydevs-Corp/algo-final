CREATE TABLE IF NOT EXISTS tweets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT NOT NULL,
    positive TINYINT(1) DEFAULT 0,
    negative TINYINT(1) DEFAULT 0
);

-- Insert some dummy data for initial training
INSERT INTO tweets (text, positive, negative) VALUES
    ("J'adore ce nouveau produit, il est fantastique !", 1, 0),
    ("C'est la pire expérience de ma vie, je déteste.", 0, 1),
    ("Vraiment génial, je recommande fortement.", 1, 0),
    ("Très décevant, ne l'achetez pas.", 0, 1),
    ("Superbe interface utilisateur, très fluide.", 1, 0),
    ("Le service client est horrible.", 0, 1),
    ("Une qualité exceptionnelle, je suis ravi.", 1, 0),
    ("C'est nul, ça ne marche pas du tout.", 0, 1);

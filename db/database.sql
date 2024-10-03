

CREATE DATABASE IF NOT EXISTS `DATABASE`    


DROP TABLE IF EXISTS `Filmes`
CREATE TABLE Filmes(
    `id` mediumint(8) unsigned NOT NULL auto_increment,
    `titulo` varchar(255) NOT NULL,
    `genero` varchar(50) NOT NULL,
    `ano` mediumint(8) NOT NULL,
     PRIMARY KEY (`id`)
)auto_increment = 1;



INSERT INTO `Filmes` (titulo,genero,ano)
VALUES (
    'O Poderoso Chefão', 'Drama/Crime', '1972'
    'Star Wars: Uma Nova Esperança', 'Ficção Científica/Aventura', '1977'
    'Matrix', 'Ficção Científica/Ação', '1999'
    'Clube da Luta', 'Drama/Suspense', '1999'
    'O Senhor dos Anéis: A Sociedade do Anel', 'Fantasia/Aventura', '2001'
    'Forrest Gump: O Contador de Histórias', 'Drama/Romance', '1994'
    'Pulp Fiction: Tempo de Violência', 'Drama/Crime', '1994'
    'A Origem', 'Ficção Científica/Suspense', '2010'
    'Interstellar', 'Ficção Científica/Aventura', '2014'
    'Vingadores: Ultimato', 'Ação/Aventura', '2019'
    'Coringa', 'Drama/Suspense', '2019'
    'Os Sete Samurais', 'Ação/Drama', '1954'
    'Parasita', 'Drama/Suspense', '2019'
    'Mad Max: Estrada da Fúria', 'Ação/Ficção Científica', '2015'
    'O Grande Truque', 'Drama/Suspense', '2006'
    'Cidade de Deus', 'Drama/Crime', '2002'
    'O Silêncio dos Inocentes', 'Suspense/Terror', '1991'
    'Gladiador', 'Drama/Ação', '2000'
    'Jurassic Park: O Parque dos Dinossauros', 'Ficção Científica/Aventura', '1993'
    'O Lobo de Wall Street', 'Comédia/Drama', '2013'
    'A Lista de Schindler', 'Drama/Histórico', '1993'
    'Harry Potter e a Pedra Filosofal', 'Fantasia/Aventura', '2001'
    'Indiana Jones e os Caçadores da Arca Perdida', 'Ação/Aventura', '1981'
    'De Volta para o Futuro', 'Ficção Científica/Aventura', '1985'
    'Batman: O Cavaleiro das Trevas', 'Ação/Crime', '2008'
    'E.T.: O Extraterrestre', 'Ficção Científica/Família', '1982'
    'O Exorcista', 'Terror', '1973'
    'Tubarão', 'Suspense/Terror', '1975'
    'La La Land: Cantando Estações', 'Musical/Romance', '2016'
    'O Pianista', 'Drama/Histórico', '2002'
    'O Resgate do Soldado Ryan', 'Drama/Guerra', '1998'
    'Django Livre', 'Ação/Western', '2012'
    'Scarface', 'Crime/Drama', '1983'
    'O Iluminado', 'Terror/Suspense', '1980'
    'Titanic', 'Romance/Drama', '1997'
    'Coração Valente', 'Ação/Drama', '1995'
    'A Vida é Bela', 'Drama/Comédia', '1997'
    'Corra!', 'Suspense/Terror', '2017'
    'O Quinto Elemento', 'Ficção Científica/Ação', '1997'
    'Homem de Ferro', 'Ação/Ficção Científica', '2008'
    'Blade Runner: O Caçador de Androides', 'Ficção Científica/Suspense', '1982'
    'Monty Python e o Cálice Sagrado', 'Comédia/Fantasia', '1975'
    'Os Infiltrados', 'Suspense/Crime', '2006'
    'Whiplash: Em Busca da Perfeição', 'Drama/Música', '2014'
    'Toy Story', 'Animação/Família', '1995'
    'O Labirinto do Fauno', 'Fantasia/Drama', '2006'
    'Her', 'Ficção Científica/Drama', '2013'
    'Oldboy', 'Suspense/Ação', '2003'
    'O Artista', 'Comédia/Drama', '2011'
    'O Rei Leão', 'Animação/Família', '1994');







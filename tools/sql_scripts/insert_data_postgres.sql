-- ------- command with command line ----------
-- psql -U postgres -h localhost -d vocal_trainer -f insert_data_postgres.sql


INSERT INTO "phoneme_type"
(
    "id","type_name"
)
VALUES
(1,'Consonnes'),
(2,'Voyelles');


INSERT INTO "sub_phoneme_type"
(
"id","sub_type_name", "phoneme_type_id"
)
VALUES
(1,'Occlusives', 1),
(2,'Fricatives', 1),
(3,'Combinaisons', 1),
(4,'Nasales', 1),
(5,'Spirantes', 1),
(6,'Pré-fermées', 2),
(7,'Fermées', 2),
(8,'Semi-ouvertes', 2),
(9,'Ouvertes', 2),
(10,'Moyennes', 2),
(11,'Diphtongues', 2);



INSERT INTO "phoneme_information"
(
"id","label", "sound_file_name", "sub_phoneme_type_id"
) 
VALUES 
(1, 'p', 'p.mp3', 1),
(2, 'b', 'b.mp3', 1),
(3, 't', 't.mp3', 1),
(4, 'd',  'd.mp3', 1),
(5, 'k',  'k.mp3', 1),
(6, 'g',  'g.mp3', 1),
(7, 'f',  'f.mp3', 2),
(8, 'v',  'v.mp3', 2),
(9, 'θ',  'θ.mp3', 2),
(10, 'ð',  'ð.mp3', 2),
(11, 's',  's.mp3', 2),
(12, 'z',  'z.mp3', 2),
(13, 'ʃ',  'ʃ.mp3', 2),
(14, 'ʒ',  'ʒ.mp3', 2),
(15, 'h',  'h.mp3', 2),
(16, 't̠ʃ', 't̠ʃ.mp3', 3),
(17, 'd̠ʒ',  'd̠ʒ.mp3', 3),
(18, 'm',  'm.mp3', 4),
(19, 'n',  'n.mp3', 4),
(20, 'ŋ',  'ŋ.mp3', 4),
(21, 'l',  'l.mp3', 5),
(22, 'ɹ',  'ɹ.mp3', 5),
(23, 'j',  'j.mp3', 5),
(24, 'w',  'w.mp3', 5 ),
(25, 'ɪ',  'ɪ.mp3', 6),
(26, 'ʊ',  'ʊ.mp3', 6),
(27, 'i', 'i.mp3', 7),
(28, 'u', 'u.mp3', 7),
(29, 'ɛ', 'ɛ.mp3', 8),
(30, 'ɜ', 'ɜ.mp3', 8),
(31, 'ʌ', 'ʌ.mp3', 8),
(32, 'ɔ', 'ɔ.mp3', 8),
(33, 'ə', 'ə.mp3', 10),
(34, 'æ', 'æ.mp3', 9),
(35, 'ɑ', 'ɑ.mp3', 9),
(36, 'eɪ', 'eɪ.mp3', 11),
(37, 'aɪ', 'aɪ.mp3', 11),
(38, 'oʊ', 'oʊ.mp3', 11),
(39, 'aʊ', 'aʊ.mp3', 11),
(40, 'ɔɪ', 'ɔɪ.mp3', 11);



INSERT INTO "example_word" 
(
"id","label", "phoneme_id"
) 
VALUES 
(1,'Pigeon', 1),
(2,'Burn', 2),
(3,'Turtle', 3),
(4,'Dream', 4),
(5,'Key', 5),
(6,'Game', 6),
(7,'Fish', 7),
(8,'Video', 8),
(9,'Thing', 9),
(10,'This', 10),
(11,'Snake', 11),
(12,'Zebra', 12),
(13,'Shoe', 13),
(14,'Pleasure', 14),
(15,'Hat', 15),
(16,'Choice', 16),
(17,'Gym', 17),
(18,'Marmot', 18),
(19,'Noodle', 19),
(20,'King', 20),
(21,'Loop', 21),
(22,'Round', 22),
(23,'Yeast', 23),
(24,'Wife', 24),
(25,'Pick', 25),
(26,'Book', 26),
(27,'Sleep', 27),
(28,'Blue', 28),
(29,'Red', 29),
(30,'Purple', 30),
(31,'Fun', 31),
(32,'North', 32),
(33,'Pilot', 33),
(34,'Carrot', 33),
(35,'Sat', 34),
(36,'Hat', 34),
(37,'Art', 35),
(38,'Start', 35),
(39,'Late', 36),
(40,'Train', 36),
(41,'Light', 37),
(42,'Rice', 37),
(43,'Phone', 38),
(44,'Note', 38),
(45,'About', 39),
(46,'House', 39),
(47,'Down', 39),
(48,'Boy', 40),
(49,'Noise', 40);




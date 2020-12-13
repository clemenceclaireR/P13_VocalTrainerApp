-- ---------- command for command line ------------
-- mysql -u <user> -p < insert_data_mysql.sql  --


USE vocal_trainer;


INSERT INTO phoneme_type
(
    id, type_name
)
VALUES
(1,'Consonnes'),
(2,'Voyelles - Diphtongues'),
(3,'Voyelles - Simples');

INSERT INTO sub_phoneme_type
(
    id, sub_type_name, phoneme_type_id
) 
VALUES 
(1,'Occlusives', 1),
(2,'Fricatives', 1),
(3,'Combinaisons', 1),
(4,'Nasales', 1),
(5,'Spirantes', 1);



INSERT INTO phoneme_information
(
    id, label, phoneme_ipa_name, sound_file_name, sub_phoneme_type_id
) 
VALUES 
(1, 'p', 'p', 'p.mp3', 1),
(2, 'b', 'b', 'b.mp3', 1),
(3, 't', 't', 't.mp3', 1),
(4, 'd', 'd', 'd.mp3', 1);



INSERT INTO example_word
(
    id, label, phoneme_id
) 
VALUES 
(1,'Pigeon', 1),
(2,'Burn', 2);

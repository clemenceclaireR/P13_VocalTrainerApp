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
"id","subtype_name", "phoneme_type_id", "order"
)
VALUES
(1,'Occlusives', 1, 1),
(2,'Fricatives', 1, 2),
(3,'Combinaisons', 1, 3),
(4,'Nasales', 1, 4),
(5,'Spirantes', 1, 5),
(6,'Pré-fermées', 2, null),
(7,'Fermées', 2, null),
(8,'Semi-ouvertes', 2, null),
(9,'Ouvertes', 2, null),
(10,'Moyennes', 2, null),
(11,'Diphtongues', 2, null);



INSERT INTO "phoneme_information"
(
"id","label", "sound_file_path", "sub_phoneme_type_id"
) 
VALUES 
(1, 'p', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509597/phonemes/p.mp3', 1),
(2, 'b', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613508988/phonemes/b.mp3', 1),
(3, 't', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509708/phonemes/t.mp3', 1),
(4, 'd',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509081/phonemes/d.mp3', 1),
(5, 'k',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509404/phonemes/k.mp3', 1),
(6, 'g',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509304/phonemes/g.mp3', 1),
(7, 'f',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509288/phonemes/f.mp3', 2),
(8, 'v',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509802/phonemes/v.mp3', 2),
(9, 'θ',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509907/phonemes/%CE%B8.mp3', 2),
(10, 'ð',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509134/phonemes/%C3%B0.mp3', 2),
(11, 's',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509637/phonemes/s.mp3', 2),
(12, 'z',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509854/phonemes/z.mp3', 2),
(13, 'ʃ',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509674/phonemes/%CA%83.mp3', 2),
(14, 'ʒ',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509890/phonemes/%CA%92.mp3', 2),
(15, 'h',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509325/phonemes/h.mp3', 2),
(16, 't̠ʃ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509729/phonemes/t%CC%A0%CA%83.mp3', 3),
(17, 'd̠ʒ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509175/phonemes/d%CC%A0%CA%92.mp3', 3),
(18, 'm',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509444/phonemes/m.mp3', 4),
(19, 'n',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509462/phonemes/n.mp3', 4),
(20, 'ŋ',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509499/phonemes/%C5%8B.mp3', 4),
(21, 'l',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509424/phonemes/l.mp3', 5),
(22, 'ɹ',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509615/phonemes/%C9%B9.mp3', 5),
(23, 'j',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509383/phonemes/j.mp3', 5),
(24, 'w',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509839/phonemes/w.mp3', 5),
(25, 'ɪ',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509365/phonemes/%C9%AA.mp3', 6),
(26, 'ʊ',  'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509776/phonemes/%CA%8A.mp3', 6),
(27, 'i', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509347/phonemes/i.mp3', 7),
(28, 'u', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509747/phonemes/u.mp3', 7),
(29, 'ɛ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509249/phonemes/%C9%9B.mp3', 8),
(30, 'ɜ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509268/phonemes/%C9%9C.mp3', 8),
(31, 'ʌ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509821/phonemes/%CA%8C.mp3', 8),
(32, 'ɔ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509012/phonemes/%C9%94.mp3', 8),
(33, 'ə', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509203/phonemes/%C9%99.mp3', 10),
(34, 'æ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613500684/phonemes/%C3%A6.mp3', 9),
(35, 'ɑ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613500314/phonemes/%C9%91.mp3', 9),
(36, 'eɪ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509231/phonemes/e%C9%AA.mp3', 11),
(37, 'aɪ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613508888/phonemes/a%C9%AA.mp3', 11),
(38, 'oʊ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509573/phonemes/o%CA%8A.mp3', 11),
(39, 'aʊ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613508957/phonemes/a%CA%8A.mp3', 11),
(40, 'ɔɪ', 'https://res.cloudinary.com/crvocaltrainer/video/upload/v1613509047/phonemes/%C9%94%C9%AA.mp3', 11);

INSERT INTO "minimal_pair_category"
(
  "id", "phoneme_id", "associated_phoneme_id", "sub_phoneme_type_id"
)
VALUES
(1, 9, 11, 2),
(2, 10, 12, 2),
(3, 15, null, 2),
(4, 13, 16, 2),
(5, 22, null, 5),
(6, 19, 20, 4),
(7, 29, 36, 11),
(8, 32, 38, 11),
(9, 25, 27, 6),
(10, 25, 29, 6),
(11, 34, 29, 9),
(12, 34, 31, 9),
(13, 26, 28, 6),
(14, 35, 1, 9);



INSERT INTO "minimal_pair_information"
(
  "id", "label", "ipa_label", "associated_word_id", "category_id"
)
VALUES
(1, 'thick',  '/θɪk/', 2, 1),
(2, 'sick',  '/sɪk/', 1, 1),
(3, 'think',  '/θɪŋk/', 4, 1),
(4, 'sink', '/siɲk/', 3, 1),
(5, 'thumb', '/θʌm/', 6, 1),
(6, 'some', '/sʌm/', 5, 1),
(7, 'theme', '/θiːm/', 8, 1),
(8, 'seem', '/siːm/', 7, 1),
(9, 'faith', '/feɪθ/', 10, 1),
(10, 'face', '/feɪs/', 9, 1),
(11, 'path', '/pæθ/', 12, 1),
(12, 'pass', '/pæs/', 11, 1),
(13, 'fourth', '/fɔɹθ/', 14, 1),
(14, 'force', '/fɔɹs/', 13, 1),
(15, 'worth', '/wɝθ/', 16, 1),
(16, 'worse', '/wɝs/', 15, 1),
(17, 'then', '/ðɛn/', 18, 2),
(18, 'zen', '/zɛn/', 17, 2),
(19, 'lithe', '/laɪð/', 20, 2),
(20, 'lies', '/laɪz/', 19, 2),
(21, 'with', '/wɪð/', 22, 2),
(22, 'wizz', '/wɪz/', 21, 2),
(23, 'breathe', '/bɹið/', 24, 2),
(24, 'breeze', '/bɹiːz/', 23, 2),
(25, 'seethe', '/siːð/', 26, 2),
(26, 'sees', '/siːz/', 25, 2),
(27, 'loathe', '/ˈloʊð/', 28, 2),
(28, 'lows', '/loʊz/', 27, 2 ),
(29, 'clothing', '/kloʊðɪŋ/', 30, 2),
(30, 'closing', '/kloʊzɪŋ/', 29, 2),
(31, 'teething', '/tiðɪŋ/', 32, 2),
(32, 'teasing', '/tiːzɪŋ/', 31, 2),
(33, 'his', '/hɪz/', 34, 3),
(34, 'is', '/ɪz/', 33, 3),
(35, 'ham', '/hæm/', 36, 3),
(36, 'am', '/æm/', 35, 3),
(37, 'hate', '/heɪt/', 38, 3),
(38, 'ate', '/eɪt/', 37, 3),
(39, 'heart', '/hɑɹt/', 40, 3),
(40, 'art', '/ɑɹt/', 39, 3),
(41, 'hold', '/hoʊld/', 42, 3),
(42, 'old', '/oʊld/', 41, 3),
(43, 'hair', '/hɛr/', 44, 3),
(44, 'air', '/ɛɹ/', 43, 3),
(45, 'hand', '/hænd/', 46, 3),
(46, 'and', '/ænd/', 45, 3),
(47, 'harm', '/hɑɹm/', 48, 3),
(48, 'arm', '/ɑɹm/', 47, 3),
(49, 'shoes', '/ʃuːz/', 50, 4),
(50, 'choose', '/tʃuːz/', 49, 4),
(51, 'ship', '/ʃɪp/', 52, 4),
(52, 'chip', '/tʃɪp/', 51, 4),
(53, 'shore', '/ʃɔɹ/', 54, 4),
(54, 'chore', '/tʃɔɹ/', 53, 4),
(55, 'chic', '/ʃiːk/', 56, 4),
(56, 'cheek', '/tʃiːk/', 55, 4),
(57, 'bash', '/bæʃ/', 58, 4),
(58, 'batch', '/bætʃ/', 57, 4),
(59, 'marsh', '/mɑɹʃ/', 60, 4),
(60, 'march', '/mɑɹtʃ/', 59, 4),
(61, 'wish', '/wɪʃ/', 62, 4),
(62, 'which', '/wɪtʃ/', 61, 4),
(63, 'crush', '/kɹʌʃ/', 64, 4),
(64, 'crutch', '/kɹʌtʃ/', 63, 4),
(65, 'hear', '/hɪɹ/', 66, 5),
(66, 'he', '/hi/', 65, 5),
(67, 'source', '/sɔɹs/', 68, 5),
(68, 'sauce', '/sɔs/', 67, 5),
(69, 'orphan', '/ɔɹfən/', 70, 5),
(70, 'often', '/ɔfən/', 69, 5),
(71, 'beard', '/bɪɹd/', 72, 5),
(72, 'bid', '/bɪd/', 71, 5),
(73, 'kin', '/kɪn/', 74, 6),
(74, 'king', '/kɪŋ/', 73, 6),
(75, 'thin', '/θɪn/', 76, 6),
(76, 'thing', '/θɪŋ/', 75, 6),
(77, 'ran', '/ɹæn/', 78, 6),
(78, 'rang', '/ɹæŋ/', 77, 6),
(79, 'stun', '/stʌn/', 80, 6),
(80, 'stung', '/stʌŋ/', 79, 6),
(81, 'ton', '/tʌn/', 82, 6),
(82, 'tongue', '/tʌŋ/', 81, 6),
(83, 'ban', '/bæn/', 84, 6),
(84, 'bang', '/bæŋ/', 83, 6),
(85, 'hand', '/hænd/', 86, 6),
(86, 'hanged', '/hæŋd/', 85, 6),
(87, 'wind', '/wɪnd/', 88, 6),
(88, 'winged', '/wɪŋd/', 87, 6),
(89, 'let', '/lɛt/', 90, 7),
(90, 'late', '/leɪt/', 89, 7),
(91, 'pepper', '/pɛpɚ/', 92, 7),
(92, 'paper', '/peɪpɚ/', 91, 7),
(93, 'chess', '/tʃɛs/', 94, 7),
(94, 'chase', '/tʃeɪs/', 93, 7),
(95, 'test', '/tɛst/', 96, 7),
(96, 'taste', '/teɪst/', 95, 7),
(97, 'men', '/mɛn/', 98, 7),
(98, 'main', '/meɪn/', 97, 7),
(99, 'less', '/lɛs/', 100, 7),
(100, 'lace', '/leɪs/', 99, 7),
(101, 'west', '/wɛst/', 102, 7),
(102, 'waste', '/weɪst/', 101, 7),
(103, 'sell', '/sɛl/', 104, 7),
(104, 'sale', '/seɪl/', 103, 7),
(105, 'on', '/ɔn/', 106, 8),
(106, 'own', '/oʊn/', 105, 8),
(107, 'ball', '/bɔl', 108, 8),
(108, 'bowl', '/boʊl/', 107, 8),
(109, 'cost', '/kɔst/', 110, 8),
(110, 'coast', '/koʊst/', 109, 8),
(111, 'caught', '/kɔt/', 112, 8),
(112, 'coat', '/koʊt/', 111, 8),
(113, 'law', '/lɔ/', 114, 8),
(114, 'low', '/loʊ/', 113, 8),
(115, 'hall', '/hɔl/', 116, 8),
(116, 'hole', '/hoʊl/', 115, 8),
(117, 'gall', '/gɔl/', 118, 8),
(118, 'goal', '/goʊl/', 117, 8),
(119, 'walk', '/wɔk/', 120, 8),
(120, 'woke', '/woʊk/', 119, 8),
(121, 'bit', '/bɪt/', 122, 9),
(122, 'beet', '/biːt/', 121, 9),
(123, 'fit', '/fɪt/', 124, 9),
(124, 'feet', '/fiːt/', 123, 9),
(125, 'sit', '/sɪt/', 126, 9),
(126, 'seat', '/siːt/', 125, 9),
(127, 'ship', '/ʃɪp/', 128, 9),
(128, 'sheep', '/ʃiːp/', 127, 9),
(129, 'lip', '/lɪp/', 130, 9),
(130, 'leap', '/liːp/', 129, 9),
(131, 'chip', '/tʃɪp/', 132, 9),
(132, 'cheap', '/tʃip/', 131, 9),
(133, 'fill', '/fɪl/', 134 ,9),
(134, 'feel', '/fiːl/', 133, 9),
(135, 'hill', '/hɪl/', 136, 9),
(136, 'heal', '/hiːl/', 135, 9),
(137, 'bid', '/bɪd/', 138, 10),
(138, 'bed', '/bɛd/', 137, 10),
(139, 'since', '/sɪns/', 140, 10),
(140, 'sense', '/sɛns/', 139, 10),
(141, 'deer', '/dɪɹ/', 142, 10),
(142, 'dare', '/dɛɹ/', 141, 10),
(143, 'win', '/wɪn/', 144, 10),
(144, 'when', '/wɛn/', 143, 10),
(145, 'bill', '/bɪl/', 146, 10),
(146, 'bell', '/bɛl/', 145, 10),
(147, 'steer', '/stɪr/', 148, 10),
(148, 'stair', '/stɛr/', 147, 10),
(149, 'hill', '/hɪl/', 150, 10),
(150, 'hell', '/hɛl/', 149, 10),
(151, 'beer', '/bɪɹ/', 152, 10),
(152, 'bear', '/bɛr/', 151, 10),
(153, 'tan', '/tæn/', 154, 11),
(154, 'ten', '/tɛn/', 153, 11),
(155, 'man', '/mæn/', 156, 11),
(156, 'men', '/mɛn/', 155, 11),
(157, 'pan', '/pæn/', 158, 11),
(158, 'pen', '/pɛn/', 157, 11),
(159, 'bat', '/bæt/', 160, 11),
(160, 'bet', '/bɛt/', 159, 11),
(161, 'sad', '/sæd/', 162, 11),
(162, 'said', '/sɛd/', 161, 11),
(163, 'bad', '/bæd/', 164, 11),
(164, 'bed', '/bɛd/', 163, 11),
(165, 'and', '/ænd/', 166, 11),
(166, 'end', '/ɛnd/', 165, 11),
(167, 'jam', '/dʒæm/', 168, 11),
(168, 'gem', '/dʒɛm/', 167, 11),
(169, 'cat', '/kæt/', 170, 12),
(170, 'cut', '/kʌt/', 169, 12),
(171, 'ran', '/ɹæn/', 172, 12),
(172, 'run', '/ɹʌn/', 171, 12),
(173, 'hat', '/hæt/', 174, 12),
(174, 'hut', '/hʌt/', 173, 12),
(175, 'massed', '/mæst/', 176, 12),
(176, 'must', '/mʌst/', 175, 12),
(177, 'hag', '/hæɡ/', 178, 12),
(178, 'hug', '/hʌɡ/', 177, 12),
(179, 'sang', '/sæŋ/', 180, 12),
(180, 'sung', '/sʌŋ/', 179, 12),
(181, 'began', '/bɪˈɡæn/', 182, 12),
(182, 'begun', '/bɪˈɡʌn/', 181, 12),
(183, 'ankle', '/ˈæŋ.kəl/', 184, 12),
(184, 'uncle', '/ˈʌŋ.kəl/', 183, 12),
(185, 'pull', '/pʊl/', 186, 13),
(186, 'pool', '/pul/', 185, 13),
(187, 'soot', '/sʊt/', 188, 13),
(188, 'suit', '/sut/', 187, 13),
(189, 'full', '/fʊl/', 190, 13),
(190, 'fool', '/ful/', 189, 13),
(191, 'look', '/lʊk/', 192, 13),
(192, 'Luke', '/luk/', 191, 13),
(193, 'should', '/ʃʊd/', 194, 13),
(194, 'shoed', '/ʃud/', 193, 13),
(195, 'cookie', '/ˈkʊki/', 196, 13),
(196, 'kookie', '/ˈkuki/', 195, 13),
(197, 'stood', '/stʊd/', 198, 13),
(198, 'stewed', '/stud/', 197, 13),
(199, 'could', '/kʊd/', 200, 13),
(200, 'cooed', '/kud/', 199, 13),
(201, 'hot', '/hɑt/', 202, 14),
(202, 'hut', '/hʌt/', 201, 14),
(203, 'dog', '/dɑg/', 204, 14),
(204, 'dug', '/dʌg/', 203, 14),
(205, 'cop', '/kɑp/', 206, 14),
(206, 'cup', '/kʌp/', 205, 14),
(207, 'cot', '/kɑt/', 208, 14),
(208, 'cut', '/kʌt/', 207, 14),
(209, 'pop', '/pɑp/', 210, 14),
(210, 'pup', '/pʌp/', 209, 14),
(211, 'shot', '/ʃɑt/', 212, 14),
(212, 'shut', '/ʃʌt/', 211, 14),
(213, 'lock', '/lɑk/', 214, 14),
(214, 'luck', '/lʌk/', 213, 14),
(215, 'not', '/nɑt/', 216, 14),
(216, 'nut', '/nʌt/', 215, 14);



INSERT INTO "minimal_pair_word_phoneme_letters"
(
    "minimal_pair_id", "letters", "ipa_letters"
)
VALUES
(1, 'th', 'θ'),
(2, 's', 's'),
(3, 'th', 'θ'),
(4, 's', 's'),
(5, 'th', 'θ'),
(6, 's', 's'),
(7, 'th', 'θ'),
(8, 's', 's'),
(9, 'th', 'θ'),
(10, 'c', 's'),
(11, 'th', 'θ'),
(12, 'ss', 's'),
(13, 'th', 'θ'),
(14, 'c', 's'),
(15, 'th', 'θ'),
(16, 's', 's'),
(17, 'th', 'ð'),
(18, 'z', 'z'),
(19, 'th', 'ð'),
(20, 's', 'z'),
(21, 'th', 'ð'),
(22, 'zz', 'z'),
(23, 'th', 'ð'),
(24, 'z', 'z'),
(25, 'th', 'ð'),
(26, 's', 'z'),
(27, 'th', 'ð'),
(28, 's', 'z'),
(29, 'th',  'ð'),
(30, 's', 'z'),
(31, 'th', 'ð'),
(32, 's', 'z'),
(33, 'h', 'h'),
(34, '', ''),
(35, 'h', 'h'),
(36, '', ''),
(37, 'h', 'h'),
(38, '', ''),
(39, 'h', 'h'),
(40, '', ''),
(41, 'h', 'h'),
(42, '', ''),
(43, 'h', 'h'),
(44, '', ''),
(45, 'h', 'h'),
(46, '', ''),
(47, 'h', 'h'),
(48, '', ''),
(49, 'sh', 'ʃ'),
(50, 'ch', 'tʃ'),
(51, 'sh', 'ʃ'),
(52, 'ch', 'tʃ'),
(53, 'sh', 'ʃ'),
(54, 'ch', 'tʃ'),
(55, 'ch', 'ʃ'),
(56, 'ch', 'tʃ'),
(57, 'sh', 'ʃ'),
(58, 'tch', 'tʃ'),
(59, 'sh', 'ʃ'),
(60, 'ch', 'tʃ'),
(61, 'sh', 'ʃ'),
(62, 'ch', 'tʃ'),
(63, 'sh', 'ʃ'),
(64, 'tch', 'tʃ'),
(65, 'r', 'ɹ'),
(66, '', ''),
(67, 'r', 'ɹ'),
(68, '', ''),
(69, 'r', 'ɹ'),
(70, '', ''),
(71, 'r', 'ɹ'),
(72, '', ''),
(73, 'n', 'n'),
(74, 'ng', 'ŋ'),
(75, 'n', 'n'),
(76, 'ng', 'ŋ'),
(77, 'n', 'n'),
(78, 'ng', 'ŋ'),
(79, 'n', 'n'),
(80, 'ng', 'ŋ'),
(81, 'n', 'n'),
(82, 'ng', 'ŋ'),
(83, 'n', 'n'),
(84, 'ng', 'ŋ'),
(85, 'n', 'n'),
(86, 'ng', 'ŋ'),
(87, 'n', 'n'),
(88, 'ng', 'ŋ'),
(89, 'e', 'ɛ'),
(90, 'a', 'eɪ'),
(91, 'e', 'ɛ'),
(92, 'a', 'eɪ'),
(93, 'e', 'ɛ'),
(94, 'a', 'eɪ'),
(95, 'e', 'ɛ'),
(96, 'a', 'eɪ'),
(97, 'e', 'ɛ'),
(98, 'ai', 'eɪ'),
(99,  'e', 'ɛ'),
(100, 'a', 'eɪ'),
(101, 'e', 'ɛ'),
(102, 'a', 'eɪ'),
(103, 'e', 'ɛ'),
(104, 'a', 'eɪ'),
(105, 'o', 'ɔ'),
(106, 'ow', 'oʊ'),
(107, 'a', 'ɔ'),
(108, 'ow', 'oʊ'),
(109, 'o', 'ɔ'),
(110, 'oa', 'oʊ'),
(111, 'au', 'ɔ'),
(112, 'oa', 'oʊ'),
(113,  'a', 'ɔ'),
(114, 'ow', 'oʊ'),
(115, 'a', 'ɔ'),
(116, 'o', 'oʊ'),
(117, 'a', 'ɔ'),
(118, 'oa', 'oʊ'),
(119, 'a', 'ɔ'),
(120, 'o', 'oʊ'),
(121, 'i', 'ɪ'),
(122, 'ee', 'iː'),
(123, 'i', 'ɪ'),
(124, 'ee', 'iː'),
(125, 'i', 'ɪ'),
(126, 'ea', 'iː'),
(127, 'i', 'ɪ'),
(128, 'ee', 'iː'),
(129, 'i', 'ɪ'),
(130, 'ea', 'iː'),
(131, 'i', 'ɪ'),
(132, 'ea', 'iː'),
(133, 'i', 'ɪ'),
(134, 'ee', 'iː'),
(135, 'i', 'ɪ'),
(136, 'ea', 'iː'),
(137, 'i', 'ɪ'),
(138, 'e', 'ɛ'),
(139, 'i', 'ɪ'),
(140, 'e', 'ɛ'),
(141, 'ee',  'ɪ'),
(142, 'a', 'ɛ'),
(143, 'i', 'ɪ'),
(144, 'e', 'ɛ'),
(145, 'i', 'ɪ'),
(146, 'e', 'ɛ'),
(147, 'ee',  'ɪ'),
(148, 'ai', 'ɛ'),
(149, 'i', 'ɪ'),
(150, 'e', 'ɛ'),
(151, 'ee',  'ɪ'),
(152, 'ea', 'ɛ'),
(153, 'a', 'æ'),
(154, 'e', 'ɛ'),
(155, 'a', 'æ'),
(156, 'e', 'ɛ'),
(157, 'a', 'æ'),
(158, 'e', 'ɛ'),
(159, 'a', 'æ'),
(160, 'e', 'ɛ'),
(161, 'a', 'æ'),
(162, 'ai', 'ɛ'),
(163, 'a', 'æ'),
(164, 'e', 'ɛ'),
(165, 'a', 'æ'),
(166, 'e', 'ɛ'),
(167, 'a', 'æ'),
(168,  'e', 'ɛ'),
(169, 'a', 'æ'),
(170, 'u', 'ʌ'),
(171, 'a', 'æ'),
(172, 'u', 'ʌ'),
(173, 'a', 'æ'),
(174, 'u', 'ʌ'),
(175, 'a', 'æ'),
(176, 'u', 'ʌ'),
(177, 'a', 'æ'),
(178, 'u', 'ʌ'),
(179, 'a', 'æ'),
(180, 'u', 'ʌ'),
(181, 'a', 'æ'),
(182, 'u', 'ʌ'),
(183, 'a', 'æ'),
(184, 'u', 'ʌ'),
(185, 'u', 'ʊ'),
(186, 'oo', 'ul'),
(187, 'oo', 'ʊ'),
(188, 'ui', 'u'),
(189, 'u', 'ʊ'),
(190, 'oo', 'u'),
(191, 'oo', 'ʊ'),
(192, 'u', 'u'),
(193, 'ou', 'ʊ'),
(194, 'oe', 'u'),
(195, 'oo', 'ʊ'),
(196, 'oo', 'u'),
(197, 'oo',  'ʊ'),
(198, 'ewe', 'u'),
(199, 'oul', 'ʊ'),
(200, 'ooe', 'u'),
(201, 'o', 'ɑ'),
(202, 'u', 'ʌ'),
(203, 'o', 'ɑ'),
(204, 'u', 'ʌ'),
(205, 'o', 'ɑ'),
(206, 'u', 'ʌ'),
(207, 'o', 'ɑ'),
(208, 'u', 'ʌ'),
(209, 'o', 'ɑ'),
(210, 'u', 'ʌ'),
(211, 'o', 'ɑ'),
(212, 'u', 'ʌ'),
(213, 'o', 'ɑ'),
(214, 'u', 'ʌ'),
(215, 'o', 'ɑ'),
(216, 'u', 'ʌ');




INSERT INTO "example_word" 
(
"id","label", "ipa_label", "phoneme_id"
) 
VALUES 
(1,'pigeon','/ˈpɪ.dʒən/', 1),
(2,'burn', '/bɝn/', 2),
(3,'turtle', '/ˈtɝtəl/', 3),
(4,'dream', '/dɹim/', 4),
(5,'key', '/ki/', 5),
(6,'game', '/ɡeɪm/', 6),
(7,'fish', '/fɪʃ/', 7),
(8,'video', '/ˈvɪd.iˌoʊ/', 8),
(9,'thing', '/θɪŋ/', 9),
(10,'this', '/ðɪs/', 10),
(11,'snake', '/ˈsneɪk/', 11),
(12,'zebra', '/ˈzɛbɹə/', 12),
(13,'shoe', '/ʃuː/', 13),
(14,'pleasure', '/ˈplɛʒə/', 14),
(15,'hat', '/hæt/', 15),
(16,'choice', '/tʃɔɪs/', 16),
(17,'gym', '/dʒɪm/', 17),
(18,'marmot', '/ˈmɑɹ.mət/', 18),
(19,'noodle', '/nuːdl̩/', 19),
(20,'king', '/kɪŋ/', 20),
(21,'loop', '/lup/', 21),
(22,'round', '/raʊnd/', 22),
(23,'yeast', '/jist/', 23),
(24,'wife', '/waɪf/', 24),
(25,'pick', '/pɪk/', 25),
(26,'book', '/bʊk/', 26),
(27,'sleep', '/slip/', 27),
(28,'blue', '/blu/', 28),
(29,'red', '/rɛd/', 29),
(30,'purple', '/ˈpɝpəl/', 30),
(31,'fun', '/fʌn/', 31),
(32,'north', '/nɔrθ/', 32),
(33,'pilot', '/ˈpaɪlət/', 33),
(34,'carrot', '/ˈkærət/', 33),
(35,'sat', '/''sæt/', 34),
(36,'hat', '/hæt/', 34),
(37,'art', '/ɑrt/', 35),
(38,'start', '/stɑrt/', 35),
(39,'late', '/leɪt/', 36),
(40,'train', '/treɪn/', 36),
(41,'light', '/laɪt/', 37),
(42,'rice', '/raɪs/', 37),
(43,'phone', '/foʊn/', 38),
(44,'note', '/noʊt/', 38),
(45,'about', '/əˈbaʊt/', 39),
(46,'house', '/ˈhaʊs/', 39),
(47,'down', '/daʊn/', 39),
(48,'boy', '/bɔɪ/', 40),
(49,'noise', '/nɔɪz/', 40);




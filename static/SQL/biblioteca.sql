-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-10-2022 a las 08:21:40
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anime`
--

CREATE TABLE `anime` (
  `id_anime` int(11) NOT NULL,
  `nombre` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_cap` int(5) NOT NULL,
  `cantidad_temp` int(5) NOT NULL,
  `tipo` varchar(300) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anime`
--

INSERT INTO `anime` (`id_anime`, `nombre`, `cantidad_cap`, `cantidad_temp`, `tipo`) VALUES
(1, 'sakura card captor', 70, 2, 'Japones'),
(2, 'inuyasha', 182, 2, 'Japones'),
(3, 'ben-to', 12, 1, 'Japones'),
(4, 'Blood+', 50, 1, 'Japones'),
(5, 'Blood-c', 12, 1, 'Japones'),
(6, 'Noucome', 12, 1, 'Japones'),
(7, 'Sousei no Onmyouji', 50, 1, 'Japones'),
(8, 'Sankarea', 12, 1, 'Japones'),
(9, 'hajimete kamisama', 24, 2, 'Japones'),
(10, 'Shakugan no Shana', 72, 3, 'Japones'),
(11, 'Bokutachi wa benkyou ga dekinay', 24, 2, 'Japones'),
(12, 'Noucome', 10, 1, 'Japones'),
(13, 'Nisekoi', 32, 2, 'Japones'),
(14, 'Sword Art Online', 80, 4, 'Japones'),
(15, 'ore wo suki nano wa omae dake ka yo', 12, 1, 'Japones'),
(16, 'Danmachi', 25, 2, 'Japones'),
(17, 'Kaguya-sama wa Kokurasetai: Tensai-tachi no Ren\'ai Zun?sen', 25, 2, 'Japones'),
(18, 'Domenstic na Kanojo', 12, 1, 'Japones'),
(19, 'go toubun no hanayome', 12, 1, 'Japones'),
(20, 'Tate no Yuusha no Nariagari', 24, 1, 'Japones'),
(21, '3D Kanojo: Real Girl', 24, 2, 'Japones'),
(22, 'ore ga suki nano wa im?to dakedo im?to ja nai', 12, 1, 'Japones'),
(23, 'kishuku gakkou no juliet', 12, 1, 'Japones'),
(24, 'seishun buta yarou wa bunny girl senpai no yume wo minai', 12, 1, 'Japones'),
(25, '1', 24, 2, 'Japones'),
(26, 'wotaku ni koi wa muzukashii', 12, 1, 'Japones'),
(27, 'Devils Line', 12, 1, 'Japones'),
(28, 'tada kun wa koi wa shinai', 13, 1, 'Japones'),
(29, 'Citrus', 12, 1, 'Japones'),
(30, 'Gamers!', 12, 1, 'Japones'),
(31, 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e (TV)', 12, 1, 'Japones'),
(32, 'Hamimete no Gal', 11, 1, 'Japones'),
(33, 'isekai wa smartphone to tomo ni', 12, 1, 'Japones'),
(34, 'Funkumenkei noise', 12, 1, 'Japones'),
(35, 'Eromanga-sense', 14, 1, 'Japones'),
(36, 'Tsuki ga Kirei', 12, 1, 'Japones'),
(37, 'Fuuka', 12, 1, 'Japones'),
(38, 'Masamune-kun no Revenge', 13, 1, 'Japones'),
(39, 'Tokyo Ghoul', 48, 4, 'Japones'),
(40, 'isuca', 10, 1, 'Japones'),
(41, 'seiken tsukai no world break', 12, 1, 'Japones'),
(42, 'saenai heronie no sodatekata', 24, 2, 'Japones'),
(43, 'ansatsu kyoushitsu', 24, 2, 'Japones'),
(44, 'juuou mujin no fanrir', 12, 1, 'Japones'),
(45, 'shinmai no testatemt', 24, 2, 'Japones'),
(46, 'kamisama hamimemashita', 36, 3, 'Japones'),
(47, 'absolute duo', 12, 1, 'Japones'),
(48, 'Ore, Twintails ni Narimasu', 12, 1, 'Japones'),
(49, 'shigatsu wa kimi no uso', 24, 1, 'Japones'),
(50, 'Trinity seven', 12, 1, 'Japones'),
(51, 'Aoharu x Kikanjuu', 12, 1, 'Japones'),
(52, 'Denpa Kyoushi', 24, 1, 'Japones'),
(53, 'shingeki no bahamut: genesis', 12, 1, 'Japones'),
(54, 'log horizon', 50, 2, 'Japones'),
(55, 'Madan no Ou to Vanadis', 12, 1, 'Japones'),
(56, 'Seirei Tsukai no Blade Dance', 18, 1, 'Japones'),
(57, 'ao haru ride', 13, 1, 'Japones'),
(58, 'akame ga kill', 24, 1, 'Japones'),
(59, 'date a live', 36, 3, 'Japones'),
(60, 'hitsugi no chaika', 24, 2, 'Japones'),
(61, 'no game no life', 12, 1, 'Japones'),
(62, 'black bullet', 13, 1, 'Japones'),
(63, '1', 26, 1, 'Japones'),
(64, 'kamigami no asobi', 12, 1, 'Japones'),
(65, 'Soredemo Sekai wa Utsukushii', 12, 1, 'Japones'),
(66, 'seikoku no dragonar', 12, 1, 'Japones'),
(67, 'akuma no riddle', 13, 1, 'Japones'),
(68, 'Bokura wa Minna Kawaisou', 12, 1, 'Japones'),
(69, 'sakura trick', 12, 1, 'Japones'),
(70, 'Inari Konkon Koi Iroha', 11, 1, 'Japones'),
(71, 'noragami', 24, 2, 'Japones'),
(72, 'wicht craft works', 12, 1, 'Japones'),
(73, 'tokyo raven', 24, 1, 'Japones'),
(74, 'Machine-Doll wa Kizutsukanai', 12, 1, 'Japones'),
(75, 'Walkure Romanze', 12, 1, 'Japones'),
(76, 'yuushibu', 13, 1, 'Japones'),
(77, 'strike the blood', 34, 1, 'Japones'),
(78, 'kill la kill', 26, 1, 'Japones'),
(79, 'golden time', 24, 1, 'Japones'),
(80, 'kyoukai no katana', 12, 1, 'Japones'),
(81, 'nagi no asukara', 26, 1, 'Japones'),
(82, 'kami nomi zo shiru sekai', 36, 3, 'Japones'),
(83, 'arata kangatari', 12, 1, 'Japones'),
(84, 'oreimo', 32, 2, 'Japones'),
(85, 'Shingeki no Kyojin', 59, 4, 'Japones'),
(86, 'Yahari Ore no Seishun Love Come wa Machigatteiru', 26, 2, 'Japones'),
(87, 'Hataraku Maou-sama!', 13, 1, 'Japones'),
(88, 'Mondaiji-tachi ga Isekai kara Kuru Sou Desu yo?', 11, 1, 'Japones'),
(89, 'Kotoura-san', 13, 1, 'Japones'),
(90, 'Boku wa Tomodachi ga Sukunai', 25, 2, 'Japones'),
(91, 'sakurasou no pet kanojo', 24, 1, 'Japones'),
(92, 'kokoro connect', 13, 1, 'Japones'),
(93, 'sukitte linayo', 14, 1, 'Japones'),
(94, 'code:breaker', 13, 1, 'Japones'),
(95, 'btooom!', 12, 1, 'Japones'),
(96, 'Tonari no Kaibutsu-kun', 14, 1, 'Japones'),
(97, 'Campione!', 13, 1, 'Japones'),
(98, 'Oda Nobuna no Yabou', 12, 1, 'Japones'),
(99, 'Hagure Yuusha no Estetica', 12, 1, 'Japones'),
(100, 'Dakara Boku wa, H ga Dekinai', 12, 1, 'Japones'),
(101, 'La Storia Della Arcana Famiglia', 13, 1, 'Japones'),
(102, 'Haiyoru! Nyaruko-san', 25, 2, 'Japones'),
(103, 'Tasogare Otome x Amnesia', 13, 1, 'Japones'),
(104, 'accel world', 26, 1, 'Japones'),
(105, 'Papa no Iu Koto wo Kikinasai!', 15, 1, 'Japones'),
(106, 'zero no tsukaima', 49, 4, 'Japones'),
(107, 'Guilty Crown', 22, 1, 'Japones'),
(108, 'mirai nikki', 27, 1, 'Japones'),
(109, 'chihayafuru', 75, 3, 'Japones'),
(110, 'tsugumomo', 24, 2, 'Japones'),
(111, 'Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...', 12, 1, 'Japones'),
(112, 'Kakushigoto', 12, 1, 'Japones'),
(113, 'Kyokou Suiri', 12, 1, 'Japones'),
(114, 'Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.', 12, 1, 'Japones'),
(115, 'ID:Invaded', 13, 1, 'Japones'),
(116, 'shokugeki no souma', 74, 5, 'Japones'),
(117, 'Assasins Pride', 12, 1, 'Japones'),
(118, 'Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!', 13, 1, 'Japones'),
(119, 'Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!', 12, 1, 'Japones'),
(120, 'Hataage! Kemono Michi', 12, 1, 'Japones'),
(121, 'isekai cheat magician', 12, 1, 'Japones'),
(122, 'Arifureta Shokugyou de Sekai Saikyou', 13, 1, 'Japones'),
(123, 'Dr. Stone', 24, 1, 'Japones'),
(124, 'Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai.', 12, 1, 'Japones'),
(125, 'Maou-sama, Retry!', 12, 1, 'Japones'),
(126, 'Kimetsu no Yaiba', 26, 1, 'Japones'),
(127, 'Ulysses: Jehanne Darc to Renkin no Kishi', 12, 1, 'Japones'),
(128, 'Goblin Slayer', 12, 1, 'Japones'),
(129, 'Tonari no Kyuuketsuki-san', 12, 1, 'Japones'),
(130, 'Yagate Kimi ni Naru', 13, 1, 'Japones'),
(131, 'Tensei shitara Slime Datta Ken', 25, 1, 'Japones'),
(132, 'Overlord', 39, 3, 'Japones'),
(133, 'Isekai Maou to Shoukan Shoujo no Dorei Majutsu', 12, 1, 'Japones'),
(134, 'Death March kara Hajimaru Isekai Kyousoukyoku', 12, 1, 'Japones'),
(135, 'Grancrest Senki', 24, 1, 'Japones'),
(136, 'Net-juu no Susume', 12, 1, 'Japones'),
(137, 'Blend S', 12, 1, 'Japones'),
(138, 'UQ Holder!: Mahou Sensei Negima! 2', 15, 1, 'Japones'),
(139, 'Hajimete no Gal', 11, 1, 'Japones'),
(140, 'Isekai Shokudou', 12, 1, 'Japones'),
(141, 'Knight\'s & Magic', 13, 1, 'Japones'),
(142, 'Saenai Heroine no Sodatekata', 23, 2, 'Japones'),
(143, 'Fukumenkei Noise', 12, 1, 'Japones'),
(144, 'Re:Creators', 22, 1, 'Japones'),
(145, 'Clockwork Planet', 12, 1, 'Japones'),
(146, 'Rokudenashi Majutsu Koushi to Akashic Records', 12, 1, 'Japones'),
(147, 'rewrite', 24, 2, 'Japones'),
(148, 'Kobayashi-san Chi no Maid Dragon', 14, 1, 'Japones'),
(149, 'Kono Subarashii Sekai ni Shukufuku wo!', 22, 2, 'Japones'),
(150, 'Gabriel DropOut', 14, 1, 'Japones'),
(151, 'Demi-chan wa Kataritai', 13, 1, 'Japones'),
(152, 'Okusama ga Seito Kaichou!', 25, 2, 'Japones'),
(153, 'WWW.Working!!', 13, 1, 'Japones'),
(154, 'Nejimaki Seirei Senki: Tenkyou no Alderamin', 13, 1, 'Japones'),
(155, 'Kiznaiver', 12, 1, 'Japones'),
(156, 'Netoge no Yome wa Onnanoko ja Nai to Omotta?', 12, 1, 'Japones'),
(157, 'Hundred', 12, 1, 'Japones'),
(158, 'Gakusen Toshi Asterisk', 24, 2, 'Japones'),
(159, 'Akagami no Shirayuki-hime', 24, 2, 'Japones'),
(160, 'Gate: Jieitai Kanochi nite, Kaku Tatakaeri', 24, 2, 'Japones'),
(161, 'Dimension W', 13, 1, 'Japones'),
(162, 'Saijaku Muhai no Bahamut', 12, 1, 'Japones'),
(163, 'Boku dake ga Inai Machi (Erased)', 12, 1, 'Japones'),
(164, 'Ansatsu Kyoushitsu (TV)', 47, 2, 'Japones'),
(165, 'Owari no Seraph', 24, 2, 'Japones'),
(166, 'gakuen', 12, 1, 'Japones'),
(167, 'Shinmai Maou no Testament', 23, 2, 'Japones'),
(168, 'Ore ga Ojousama Gakkou ni Shomin Sample Toshite Gets?Sareta Ken', 12, 1, 'Japones'),
(169, 'Hidan no Aria', 13, 1, 'Japones'),
(170, 'Noragami', 25, 2, 'Japones'),
(171, 'Rakudai Kishi no Cavalry ', 12, 1, 'Japones'),
(172, 'Kuusen Madoushi Kouhosei no Kyoukan', 13, 1, 'Japones'),
(173, 'Jitsu wa Watashi wa', 13, 1, 'Japones'),
(174, 'Charlotte', 14, 1, 'Japones'),
(175, 'Aoharu x Kikanjuu', 12, 1, 'Japones'),
(176, 'Yamada-kun to 7-nin no Majo (TV)', 12, 1, 'Japones'),
(177, 'Juuou Mujin no Fafnir', 12, 1, 'Japones'),
(178, 'Hitsugi no Chaika', 23, 1, 'Japones'),
(179, 'Inou-Battle wa Nichijou-kei no Naka de', 12, 1, 'Japones'),
(180, 'Amagi Brilliant Park', 13, 1, 'Japones'),
(181, 'Himegoto', 13, 1, 'Japones'),
(182, 'Soredemo Sekai wa Utsukushii', 12, 1, 'Japones'),
(183, '.Seikoku no Dragonar', 12, 1, 'Japones'),
(184, 'Mikakunin de Shinkoukei', 12, 1, 'Japones'),
(185, 'Ore No Imouto Ga Konnani Kawaii Wake Ga Nai', 25, 2, 'Japones'),
(186, 'Boku wa Tomodachi ga Sukunai', 25, 2, 'Japones'),
(187, 'Ore no Kanojo to Osananajimi ga Shuraba Sugiru', 13, 1, 'Japones'),
(188, 'Kuma Kuma Kuma Bear', 12, 1, 'Japones'),
(189, 'Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen', 12, 1, 'Japones'),
(190, 'Tsuujou Kougeki ga Zentai Kougeki de Ni-kai Kougeki no Okaasan wa Suki Desu ka', 13, 1, 'Japones'),
(191, 'Maou Gakuin no Futekigousha', 13, 1, 'Japones'),
(192, 'Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen', 36, 3, 'Japones'),
(193, 'Hachi-nan tte, Sore wa Nai deshou!', 12, 1, 'Japones'),
(194, 'Infinite Dendrogram', 12, 1, 'Japones'),
(195, 'Houkago Saikoro Club', 12, 1, 'Japones'),
(196, 'Youjo Senki', 12, 1, 'Japones'),
(197, 'Kenja No Mago', 12, 1, 'Japones'),
(198, 'Irozuku Sekai no Ashita kara', 13, 1, 'Japones'),
(199, 'Hyakuren no Haou to Seiyaku no Valkyria', 12, 1, 'Japones'),
(200, 'Amaama to Inazuma', 12, 1, 'Japones'),
(201, 'gakuen babysistters', 12, 1, 'Japones'),
(202, 'Inuyashiki', 11, 1, 'Japones'),
(203, 'Boku no Kanojo ga Majimesugiru Sho-bitch na Ken', 11, 1, 'Japones'),
(204, 'Netsuzou TRap', 12, 1, 'Japones'),
(205, 'koi to uso', 13, 1, 'Japones'),
(206, 'Tsurezure Children', 12, 1, 'Japones'),
(207, 'kakegurui', 24, 2, 'Japones'),
(208, 'Sin: Nanatsu no Taizai', 12, 1, 'Japones'),
(209, 'Kyoukai no Rinne (TV)', 75, 3, 'Japones'),
(210, 'Renai Boukun', 12, 1, 'Japones'),
(211, 'Busou Shoujo Machiavellianism', 13, 1, 'Japones'),
(212, 'watashi ga motete dousunda', 12, 1, 'Japones'),
(213, 'Masou Gakuen HxH', 12, 1, 'Japones'),
(214, 'Ajin', 26, 2, 'Japones'),
(215, 'musaigen no phantom workd', 14, 1, 'Japones'),
(216, 'Taimadou Gakuen 35 Shiken Shoutai', 12, 1, 'Japones'),
(217, 'Himouto! Umaru-chan', 26, 2, 'Japones'),
(218, 'Plastic Memories', 13, 1, 'Japones'),
(219, 'Isshuukan Friends.', 12, 1, 'Japones'),
(220, 'Mahou Sensou', 12, 1, 'Japones'),
(221, 'Toaru Hikushi e no Koiuta', 13, 1, 'Japones'),
(222, 'Infinite Stratos', 24, 2, 'Japones'),
(223, 'Outbreak Company', 12, 1, 'Japones'),
(224, 'Hentai Ouji to Warawanai Neko', 12, 1, 'Japones'),
(225, 'Ore no Kanojo to Osananajimi ga Shuraba Sugiru', 13, 1, 'Japones'),
(226, 'Binbougami ga!', 13, 1, 'Japones'),
(227, 'Kore wa Zombie Desu ka?', 24, 2, 'Japones'),
(228, 'Inu x Boku SS', 13, 1, 'Japones'),
(229, 'Maken-Ki!', 22, 2, 'Japones'),
(230, 'Maji de Watashi ni Koi Shinasai!!', 12, 1, 'Japones'),
(231, 'Mayo Chiki!', 13, 1, 'Japones'),
(232, 'Seikon no Qwaser', 36, 2, 'Japones'),
(233, 'Yosuga no Sora', 14, 1, 'Japones'),
(234, 'Sora no Otoshimono', 26, 2, 'Japones'),
(235, 'Highschool of hte Dead ', 12, 1, 'Japones'),
(236, 'Okami-san to Shichinin no Nakama-tachi', 12, 1, 'Japones'),
(237, 'Kaichou wa maid sama!', 26, 1, 'Japones'),
(238, 'Seiken no Blacksmith', 12, 1, 'Japones'),
(239, 'Kampfer', 13, 1, 'Japones'),
(240, 'Princess Lover!', 12, 1, 'Japones'),
(241, 'Toradora', 25, 1, 'Japones'),
(242, 'Akane Iro ni Somaru Saka', 12, 1, 'Japones'),
(243, 'Special A', 24, 1, 'Japones'),
(244, 'Itazura na Kiss', 25, 1, 'Japones'),
(245, 'Clannad', 48, 2, 'Japones'),
(246, 'Myself Yourself', 13, 1, 'Japones'),
(247, 'Kaze no Stigma', 24, 1, 'Japones'),
(248, 'Princess Resurrection', 26, 1, 'Japones'),
(249, '.Shinkyoku Soukai Polyphonica', 24, 2, 'Japones'),
(250, 'Otome wa Boku ni Koishiteru', 24, 2, 'Japones'),
(251, 'Kanon 2006', 24, 1, 'Japones'),
(252, '.Kamisama Kazoku', 13, 1, 'Japones'),
(253, 'Usagi Drop', 11, 1, 'Japones'),
(254, 'Tsubasa Chronicle', 52, 1, 'Japones'),
(255, 'Elfen Lied', 13, 1, 'Japones'),
(256, 'Aishiteruze Baby', 26, 1, 'Japones'),
(257, 'Koi Kaze', 13, 1, 'Japones'),
(258, 'High Score Girl', 24, 2, 'Japones'),
(259, 'Hadi girl', 10, 1, 'Japones'),
(260, 'Maken-Ki!', 22, 2, 'Japones'),
(261, 'urasekai picnic', 12, 1, 'Japones'),
(262, 'Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari', 12, 1, 'Japones'),
(263, 'Mushoku Tensei: Isekai Ittara Honki Dasu', 11, 1, 'Japones'),
(264, 'Ore dake Haireru Kakushi Dungeon', 12, 1, 'Japones'),
(265, 'Horimiya', 13, 1, 'Japones'),
(266, 'Jaku-Chara Tomozaki-kun', 12, 1, 'Japones'),
(267, 'Sword Art Online: Progressive Movie - Hoshi Naki Yoru no Aria', 1, 1, 'Japones'),
(268, 'Spy x Family', 12, 1, 'Japones'),
(269, 'Komi-san wa, Comyushou desu.', 24, 2, 'Japones'),
(270, 'Yuusha-Yamemasu', 13, 1, 'Japones'),
(271, 'Tensai Ouji no Akaji Kokka Saisei Jutsu', 12, 1, 'Japones'),
(272, 'Kenja no Deshi wo Nanoru Kenja', 12, 1, 'Japones'),
(273, 'Fantasy Bishoujo Juniku Ojisan to', 12, 1, 'Japones'),
(274, 'Sono Bisque Doll wa Koi wo Suru', 12, 1, 'Japones'),
(275, 'Leadale no Daichi nite', 12, 1, 'Japones'),
(276, 'Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shima', 12, 1, 'Japones'),
(277, '86 - Eighty Six', 24, 2, 'Japones'),
(278, 'Seirei Gensouki', 12, 1, 'Japones'),
(279, 'Genjitsu Shugi Yuusha no Oukoku Saikenki', 26, 1, 'Japones'),
(280, 'Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita', 12, 1, 'Japones'),
(281, 'Ijiranaide, Nagatoro-san', 12, 1, 'Japones'),
(282, 'Mushoku Tensei: Isekai Ittara Honki Dasu', 11, 1, 'Japones'),
(283, 'Kumo Desu ga, Nani ka?', 24, 1, 'Japones'),
(284, 'Uzaki-chan wa Asobitai!', 12, 1, 'Japones'),
(285, 'Shironeko Project: Zero Chronicle', 12, 1, 'Japones'),


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comic`
--

CREATE TABLE `comic` (
  `id_comic` int(11) NOT NULL,
  `nombre` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_cap` int(5) NOT NULL,
  `autor` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `tipo` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `comic`
--

INSERT INTO `comic` (`id_comic`, `nombre`, `cantidad_cap`, `autor`, `tipo`) VALUES
(1, 'Solo Leveling', 179, 'Chu-Gong', 'Coreano'),
(2, 'Komi-san wa, Komyushou Desu.', 377, 'Tomohito Oda', 'Japones');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id_genero` int(11) NOT NULL,
  `genero` varchar(300) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id_genero`, `genero`) VALUES
(4, 'Accion'),
(5, 'Artes Marciales'),
(6, 'Aventuras'),
(2, 'Comedia'),
(7, 'Demonios'),
(8, 'Fantasia'),
(3, 'Magia'),
(1, 'Romance'),
(9, 'Sobrenatural');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generoanime`
--

CREATE TABLE `generoanime` (
  `id_anime` int(11) NOT NULL,
  `id_genero` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generocomic`
--

CREATE TABLE `generocomic` (
  `id_comic` int(11) NOT NULL,
  `id_genero` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generonovela`
--

CREATE TABLE `generonovela` (
  `id_novela` int(11) NOT NULL,
  `id_genero` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `novela`
--

CREATE TABLE `novela` (
  `id_novela` int(11) NOT NULL,
  `nombre` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_cap` int(5) NOT NULL,
  `autor` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `tipo` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `novela`
--

INSERT INTO `novela` (`id_novela`, `nombre`, `cantidad_cap`, `autor`, `tipo`) VALUES
(1, 'Two As One Princess', 108, 'Himezaki Shiu', 'Japones');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anime`
--
ALTER TABLE `anime`
  ADD PRIMARY KEY (`id_anime`);

--
-- Indices de la tabla `comic`
--
ALTER TABLE `comic`
  ADD PRIMARY KEY (`id_comic`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id_genero`),
  ADD UNIQUE KEY `genero` (`genero`);

--
-- Indices de la tabla `generoanime`
--
ALTER TABLE `generoanime`
  ADD PRIMARY KEY (`id_anime`,`id_genero`),
  ADD KEY `id_categoria` (`id_genero`);

--
-- Indices de la tabla `generocomic`
--
ALTER TABLE `generocomic`
  ADD PRIMARY KEY (`id_comic`,`id_genero`);

--
-- Indices de la tabla `generonovela`
--
ALTER TABLE `generonovela`
  ADD PRIMARY KEY (`id_novela`,`id_genero`);

--
-- Indices de la tabla `novela`
--
ALTER TABLE `novela`
  ADD PRIMARY KEY (`id_novela`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anime`
--
ALTER TABLE `anime`
  MODIFY `id_anime` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;

--
-- AUTO_INCREMENT de la tabla `comic`
--
ALTER TABLE `comic`
  MODIFY `id_comic` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id_genero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `novela`
--
ALTER TABLE `novela`
  MODIFY `id_novela` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `generoanime`
--
ALTER TABLE `generoanime`
  ADD CONSTRAINT `generoanime_ibfk_1` FOREIGN KEY (`id_anime`) REFERENCES `anime` (`id_anime`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `generoanime_ibfk_2` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

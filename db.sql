# File name: E:/MIT_CS50/MIT_CS50/me50/neteng0911/db.sql
# Creation date: 08/08/2023
# Created by SQLite to MySQL 2.3 [Demo]
# --------------------------------------------------
# More conversion tools at http://www.convert-in.com

SET NAMES utf8;

#
# Table structure for table 'auth_group'
#

DROP TABLE IF EXISTS `auth_group` CASCADE;
CREATE TABLE `auth_group` (
  `id` INT NOT NULL,
  `name` VARCHAR(150) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE `sqlite_autoindex_auth_group_1` (`name`)
) ENGINE=InnoDB;

#
# Dumping data for table 'auth_group'
#

LOCK TABLES `auth_group` WRITE;
UNLOCK TABLES;

#
# Table structure for table 'auth_group_permissions'
#

DROP TABLE IF EXISTS `auth_group_permissions` CASCADE;
CREATE TABLE `auth_group_permissions` (
  `id` INT NOT NULL,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `auth_group_permissions_permission_id_84c5c92e` (`permission_id`),
  INDEX `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  UNIQUE `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`, `permission_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'auth_group_permissions'
#

LOCK TABLES `auth_group_permissions` WRITE;
UNLOCK TABLES;

#
# Table structure for table 'auth_permission'
#

DROP TABLE IF EXISTS `auth_permission` CASCADE;
CREATE TABLE `auth_permission` (
  `id` INT NOT NULL,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) CHARACTER SET utf8 NOT NULL,
  `name` VARCHAR(255) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `auth_permission_content_type_id_2f476e4b` (`content_type_id`),
  UNIQUE `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`, `codename`)
) ENGINE=InnoDB;

#
# Dumping data for table 'auth_permission'
#

LOCK TABLES `auth_permission` WRITE;
INSERT IGNORE INTO `auth_permission`(`id`, `content_type_id`, `codename`, `name`) VALUES(1, 1, 'add_user', 'Can add user'), (2, 1, 'change_user', 'Can change user'), (3, 1, 'delete_user', 'Can delete user'), (4, 1, 'view_user', 'Can view user'), (5, 2, 'add_route', 'Can add route'), (6, 2, 'change_route', 'Can change route'), (7, 2, 'delete_route', 'Can delete route'), (8, 2, 'view_route', 'Can view route'), (9, 3, 'add_logentry', 'Can add log entry'), (10, 3, 'change_logentry', 'Can change log entry'), (11, 3, 'delete_logentry', 'Can delete log entry'), (12, 3, 'view_logentry', 'Can view log entry'), (13, 4, 'add_permission', 'Can add permission'), (14, 4, 'change_permission', 'Can change permission'), (15, 4, 'delete_permission', 'Can delete permission'), (16, 4, 'view_permission', 'Can view permission'), (17, 5, 'add_group', 'Can add group'), (18, 5, 'change_group', 'Can change group'), (19, 5, 'delete_group', 'Can delete group'), (20, 5, 'view_group', 'Can view group'), (21, 6, 'add_contenttype', 'Can add content type'), (22, 6, 'change_contenttype', 'Can change content type'), (23, 6, 'delete_contenttype', 'Can delete content type'), (24, 6, 'view_contenttype', 'Can view content type'), (25, 7, 'add_session', 'Can add session'), (26, 7, 'change_session', 'Can change session'), (27, 7, 'delete_session', 'Can delete session'), (28, 7, 'view_session', 'Can view session'), (29, 8, 'add_reply', 'Can add reply'), (30, 8, 'change_reply', 'Can change reply'), (31, 8, 'delete_reply', 'Can delete reply'), (32, 8, 'view_reply', 'Can view reply'), (33, 9, 'add_comment', 'Can add comment'), (34, 9, 'change_comment', 'Can change comment'), (35, 9, 'delete_comment', 'Can delete comment'), (36, 9, 'view_comment', 'Can view comment'), (37, 10, 'add_message', 'Can add message'), (38, 10, 'change_message', 'Can change message'), (39, 10, 'delete_message', 'Can delete message'), (40, 10, 'view_message', 'Can view message'), (41, 11, 'add_qrcode', 'Can add qrcode'), (42, 11, 'change_qrcode', 'Can change qrcode'), (43, 11, 'delete_qrcode', 'Can delete qrcode'), (44, 11, 'view_qrcode', 'Can view qrcode'), (45, 12, 'add_cookie', 'Can add Cookie'), (46, 12, 'change_cookie', 'Can change Cookie'), (47, 12, 'delete_cookie', 'Can delete Cookie'), (48, 12, 'view_cookie', 'Can view Cookie'), (49, 13, 'add_cookiegroup', 'Can add Cookie Group'), (50, 13, 'change_cookiegroup', 'Can change Cookie Group');
UNLOCK TABLES;

#
# Table structure for table 'Capstone_comment'
#

DROP TABLE IF EXISTS `Capstone_comment` CASCADE;
CREATE TABLE `Capstone_comment` (
  `id` INT NOT NULL,
  `comm_txt` VARCHAR(150) CHARACTER SET utf8 NOT NULL,
  `created_date` DATETIME NOT NULL,
  `owner_id` INT,
  `route_comm_id` INT,
  PRIMARY KEY (`id`),
  INDEX `Capstone_comment_route_comm_id_4ba6b433` (`route_comm_id`),
  INDEX `Capstone_comment_owner_id_d9b3b3fc` (`owner_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_comment'
#

LOCK TABLES `Capstone_comment` WRITE;
INSERT IGNORE INTO `Capstone_comment`(`id`, `comm_txt`, `created_date`, `owner_id`, `route_comm_id`) VALUES(68, 'hi', '2022-06-12 19:18:11.329729', 2, 104), (69, 'ss', '2022-06-18 18:16:07.568958', 4, 119), (70, 'test comm no61', '2022-06-19 20:08:54.581574', 8, 120), (71, '', '2022-07-24 14:43:50.283095', 4, 113), (72, '', '2022-07-24 14:44:08.754669', 4, 113), (73, '', '2022-07-24 14:44:42.803456', 4, 113), (74, '', '2022-07-24 14:45:01.182207', 4, 113), (75, '', '2022-07-24 14:48:55.558105', 4, 113), (76, '', '2022-07-24 14:50:21.680029', 4, 113), (77, 'test', '2022-07-24 14:52:45.738188', 4, 122), (78, 'test', '2022-07-24 14:59:31.133393', 4, 122), (79, 'xwxw', '2022-07-24 14:59:42.941877', 4, 121), (80, '', '2022-07-24 18:38:34.320110', 4, 113), (81, '', '2022-07-24 18:39:17.091700', 4, 113), (82, '', '2022-07-24 18:39:43.046486', 4, 113), (83, '', '2022-07-24 18:39:53.484521', 4, 113), (84, '', '2022-07-24 18:40:12.730788', 4, 113), (85, '', '2022-07-24 18:40:31.694762', 4, 113), (86, '', '2022-07-24 18:41:21.947513', 4, 113), (87, '', '2022-07-24 18:41:59.773548', 4, 113), (88, '', '2022-07-24 18:42:43.610805', 4, 113), (89, 'hey', '2022-07-24 18:43:02.809620', 4, 122), (90, '', '2022-07-24 18:43:24.618144', 4, 113), (91, '', '2022-07-24 18:44:46.520331', 4, 113), (92, '', '2022-07-24 18:46:34.309535', 4, 113), (93, 'hgg', '2022-07-24 18:47:35.353533', 4, 122), (94, '', '2022-07-24 19:00:27.173702', 4, 113), (95, '', '2022-07-24 19:05:24.780239', 4, 113), (96, '', '2022-07-24 19:10:05.477204', 4, 113), (97, 'rrrr', '2022-07-24 19:11:44.963492', 4, 113), (98, '', '2022-07-24 19:14:45.817112', 4, 113), (99, '', '2022-07-24 19:15:41.285949', 4, 113), (100, '', '2022-07-24 19:15:58.880323', 4, 113), (101, '', '2022-07-24 19:19:31.024189', 4, 113), (102, '', '2022-07-24 19:21:46.114614', 4, 113), (103, '', '2022-07-24 19:22:10.547709', 4, 113), (104, '', '2022-07-24 19:24:15.523550', 4, 113), (105, '', '2022-07-24 19:25:43.892138', 4, 113), (106, '', '2022-07-24 19:26:09.296799', 4, 113), (107, '', '2022-07-24 19:26:27.612733', 4, 113), (108, 'tr', '2022-07-24 19:40:14.976809', 4, 122), (109, 'nonon', '2022-07-24 19:40:34.974286', 4, 118), (110, 'nonon', '2022-07-24 19:42:58.023606', 4, 118), (111, 'hey', '2022-07-24 19:43:40.277250', 4, 122), (112, 'trip', '2022-08-05 16:18:55.014781', 4, 122), (113, 'test comm', '2022-09-29 07:06:50.036204', 4, 122), (114, 'test comm no61', '2022-10-09 09:22:15.866161', 4, 122), (115, 'test comm no61', '2022-10-09 09:22:24.055844', 4, 122), (116, 'test comm no61', '2022-10-09 09:24:14.404068', 4, 122), (117, 'test comm no61', '2022-10-09 09:24:16.791197', 4, 122);
UNLOCK TABLES;

#
# Table structure for table 'Capstone_comment_lists'
#

DROP TABLE IF EXISTS `Capstone_comment_lists` CASCADE;
CREATE TABLE `Capstone_comment_lists` (
  `id` INT NOT NULL,
  `comment_id` INT NOT NULL,
  `route_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Capstone_comment_lists_route_id_191a7df6` (`route_id`),
  INDEX `Capstone_comment_lists_comment_id_f016f7d5` (`comment_id`),
  UNIQUE `Capstone_comment_lists_comment_id_route_id_b6308b55_uniq` (`comment_id`, `route_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_comment_lists'
#

LOCK TABLES `Capstone_comment_lists` WRITE;
INSERT IGNORE INTO `Capstone_comment_lists`(`id`, `comment_id`, `route_id`) VALUES(68, 68, 104), (69, 69, 119), (70, 70, 120), (71, 71, 113), (72, 72, 113), (73, 73, 113), (74, 74, 113), (75, 75, 113), (76, 76, 113), (77, 77, 122), (78, 78, 122), (79, 79, 121), (80, 80, 113), (81, 81, 113), (82, 82, 113), (83, 83, 113), (84, 84, 113), (85, 85, 113), (86, 86, 113), (87, 87, 113), (88, 88, 113), (89, 89, 122), (90, 90, 113), (91, 91, 113), (92, 92, 113), (93, 93, 122), (94, 94, 113), (95, 95, 113), (96, 96, 113), (97, 97, 113), (98, 98, 113), (99, 99, 113), (100, 100, 113), (101, 101, 113), (102, 102, 113), (103, 103, 113), (104, 104, 113), (105, 105, 113), (106, 106, 113), (107, 107, 113), (108, 108, 122), (109, 109, 118), (110, 110, 118), (111, 111, 122), (112, 112, 122), (113, 113, 122), (114, 114, 122), (115, 115, 122), (116, 116, 122), (117, 117, 122);
UNLOCK TABLES;

#
# Table structure for table 'Capstone_message'
#

DROP TABLE IF EXISTS `Capstone_message` CASCADE;
CREATE TABLE `Capstone_message` (
  `id` INT NOT NULL,
  `content` VARCHAR(150) CHARACTER SET utf8 NOT NULL,
  `created_date` DATETIME NOT NULL,
  `route_id` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_message'
#

LOCK TABLES `Capstone_message` WRITE;
INSERT IGNORE INTO `Capstone_message`(`id`, `content`, `created_date`, `route_id`) VALUES(1, 'You have been removed from route', '2022-04-10 07:19:34.146300', 75), (2, 'You have been removed from route', '2022-04-10 07:24:31.588217', 75), (3, 'You have been removed from route', '2022-04-10 08:41:20.983696', 75), (4, 'You have been removed from route', '2022-04-11 17:29:37.253613', 75), (5, 'You have been removed from route', '2022-04-11 17:32:52.219411', 75), (6, 'You have been removed from route', '2022-04-11 17:32:58.639346', 75), (7, 'You have been removed from route', '2022-04-12 14:04:11.800929', 77), (8, 'You have been removed from route', '2022-04-12 17:35:48.786229', 77), (9, 'You have been removed from route', '2022-04-12 17:35:52.409087', 77), (10, 'Driver just cancelled the trip', '2022-04-14 05:16:08.509482', 67), (11, 'Attention! Driver just edited the trip', '2022-04-14 05:23:26.947384', 79), (12, 'Attention! Driver just edited the trip', '2022-04-14 05:23:26.961889', 79), (13, 'test for deleting', '2022-02-14 05:42:13.836824', 1), (14, 'Attention! Driver just edited the trip', '2022-04-19 12:31:57.114559', 81), (15, 'Attention! Driver just edited the trip', '2022-04-19 12:31:57.135779', 81), (16, 'Attention! You have been removed from trip', '2022-04-19 12:33:00.278467', 81), (17, 'Attention! You have been removed from trip', '2022-04-19 12:43:34.707893', 82), (18, 'Attention! You have been removed from trip', '2022-04-19 12:46:54.351884', 83), (19, 'Attention! Driver just edited the trip', '2022-04-19 12:47:30.204595', 83), (20, 'Attention! Driver just edited the trip', '2022-04-19 14:07:47.359466', 85), (21, 'Attention! You have been removed from trip', '2022-04-19 14:09:38.880574', 85), (22, 'Attention! Driver just edited the trip', '2022-04-23 16:00:59.689273', 85), (23, 'Attention! You have been removed from trip', '2022-04-28 19:01:09.956396', 86), (24, 'Attention! You have been removed from trip', '2022-04-28 19:10:29.734276', 86), (25, 'Attention! You have been removed from trip', '2022-04-28 19:14:02.383232', 86), (26, 'Attention! You have been removed from trip', '2022-04-28 19:17:17.141577', 86), (27, 'Attention! You have been removed from trip', '2022-06-18 16:26:12.030351', 119), (28, 'Attention! You have been removed from trip', '2022-06-18 16:32:38.720805', 119), (29, 'Attention! You have been removed from trip', '2022-06-18 16:40:01.745617', 119), (30, 'Attention! You have been removed from trip', '2022-06-18 16:41:51.156089', 119), (31, 'Attention! You have been removed from trip', '2022-06-18 17:01:58.065940', 119), (32, 'Attention! Trip finalised', '2022-06-18 19:30:24.533689', 119), (33, 'Attention! Trip finalised', '2022-06-18 19:32:22.186638', 119), (34, 'Attention! You have been removed from trip', '2022-06-18 19:34:13.756969', 119), (35, 'Attention! Trip finalised', '2022-06-18 19:34:55.681211', 119), (36, 'Attention! Trip finalised', '2022-06-18 19:38:32.944087', 120), (37, 'Attention! Driver just edited the trip', '2022-08-03 17:01:36.750576', 121), (38, 'Attention! Driver just edited the trip', '2022-08-03 17:01:36.765625', 121), (39, 'Attention! Driver just edited the trip', '2022-08-13 15:24:24.352754', 122), (40, 'Attention! You have been removed from trip', '2022-08-13 15:25:03.447031', 122), (41, 'Attention! You have been removed from trip', '2022-10-18 05:51:57.144262', 122), (42, 'Attention! You have been removed from trip', '2022-10-22 10:30:50.446153', 126), (43, 'Attention! Driver just edited the trip', '2022-11-01 20:22:01.106694', 127);
UNLOCK TABLES;

#
# Table structure for table 'Capstone_message_recipient'
#

DROP TABLE IF EXISTS `Capstone_message_recipient` CASCADE;
CREATE TABLE `Capstone_message_recipient` (
  `id` INT NOT NULL,
  `message_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Capstone_message_recipient_user_id_16c8542f` (`user_id`),
  INDEX `Capstone_message_recipient_message_id_74133201` (`message_id`),
  UNIQUE `Capstone_message_recipient_message_id_user_id_3871e8cf_uniq` (`message_id`, `user_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_message_recipient'
#

LOCK TABLES `Capstone_message_recipient` WRITE;
INSERT IGNORE INTO `Capstone_message_recipient`(`id`, `message_id`, `user_id`) VALUES(1, 2, 2), (2, 3, 4), (3, 4, 4), (4, 5, 4), (5, 6, 2), (6, 7, 2), (7, 8, 2), (8, 9, 4), (9, 10, 2), (10, 11, 1), (11, 12, 4), (12, 13, 1), (13, 14, 2), (14, 15, 4), (15, 16, 4), (16, 17, 4), (17, 18, 4), (18, 19, 2), (19, 20, 2), (20, 21, 2), (21, 22, 4), (22, 23, 1), (23, 24, 1), (24, 25, 1), (25, 26, 1), (26, 27, 5), (27, 28, 2), (28, 29, 21), (29, 30, 18), (30, 31, 8), (31, 33, 1), (32, 33, 2), (33, 34, 1), (34, 35, 2), (35, 35, 8), (36, 36, 4), (37, 36, 8), (38, 37, 5), (39, 38, 49), (40, 39, 48), (41, 40, 48), (42, 41, 4), (43, 42, 49), (44, 43, 48);
UNLOCK TABLES;

#
# Table structure for table 'Capstone_qrcode'
#

DROP TABLE IF EXISTS `Capstone_qrcode` CASCADE;
CREATE TABLE `Capstone_qrcode` (
  `id` INT NOT NULL,
  `code` VARCHAR(12) CHARACTER SET utf8 NOT NULL,
  `passenger_id` INT,
  PRIMARY KEY (`id`),
  INDEX `Capstone_qrcode_passenger_id_8d581bdc` (`passenger_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_qrcode'
#

LOCK TABLES `Capstone_qrcode` WRITE;
INSERT IGNORE INTO `Capstone_qrcode`(`id`, `code`, `passenger_id`) VALUES(149, '18229', 48), (150, '58962', 48), (151, '84695', 48), (152, '98386', 48), (156, '48706', 48), (159, '46605', 48), (173, '28691', 58), (175, '58989', 2), (177, '94428', 8), (178, '56768', 4), (181, '99359', 49), (182, '92193', 5), (184, '41060', 5), (185, '22266', 5), (186, '61335', 5), (187, '59754', 5), (188, '50081', 5), (189, '30398', 5), (190, '35738', 5), (191, '72414', 5), (192, '26724', 5), (193, '20619', 5), (194, '11475', 5), (195, '23076', 5), (196, '88556', 5), (197, '12860', 5), (198, '93399', 5), (199, '62842', 5), (200, '77006', 5), (201, '17684', 5), (202, '28566', 4), (203, '42023', 4), (204, '21007', 4), (205, '54957', 4), (206, '64451', 4), (207, '35683', 4), (208, '48270', 4), (209, '21722', 5), (210, '70557', 5), (211, '28690', 5), (212, '14302', 5), (213, '87757', 5), (214, '52604', 5), (215, '16455', 5), (216, '39693', 5), (217, '83956', 5), (218, '66555', 5), (219, '99111', 5), (220, '59775', 5), (221, '89912', 5);
UNLOCK TABLES;

#
# Table structure for table 'Capstone_qrcode_trip'
#

DROP TABLE IF EXISTS `Capstone_qrcode_trip` CASCADE;
CREATE TABLE `Capstone_qrcode_trip` (
  `id` INT NOT NULL,
  `qrcode_id` INT NOT NULL,
  `route_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Capstone_qrcode_trip_route_id_f2f1d439` (`route_id`),
  INDEX `Capstone_qrcode_trip_qrcode_id_ab2ecab6` (`qrcode_id`),
  UNIQUE `Capstone_qrcode_trip_qrcode_id_route_id_243c00bc_uniq` (`qrcode_id`, `route_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_qrcode_trip'
#

LOCK TABLES `Capstone_qrcode_trip` WRITE;
INSERT IGNORE INTO `Capstone_qrcode_trip`(`id`, `qrcode_id`, `route_id`) VALUES(139, 149, 115), (140, 150, 115), (141, 151, 115), (142, 152, 115), (146, 156, 115), (149, 159, 117), (163, 173, 119), (165, 175, 119), (167, 177, 119), (168, 178, 120), (171, 181, 121), (172, 182, 121), (199, 209, 122), (200, 210, 122), (201, 211, 122), (202, 212, 122), (203, 213, 122), (204, 214, 122), (205, 215, 122), (206, 216, 122), (207, 217, 122), (208, 218, 122), (209, 219, 122), (210, 220, 122), (211, 221, 122), (212, 222, 122), (213, 223, 122), (214, 224, 122), (215, 225, 122), (216, 226, 122), (219, 229, 125), (220, 230, 125), (221, 231, 125), (222, 232, 125), (223, 233, 125), (228, 238, 125), (236, 246, 125), (237, 247, 125), (238, 248, 125), (240, 250, 122), (241, 251, 122), (244, 254, 126), (252, 262, 127), (259, 269, 127);
UNLOCK TABLES;

#
# Table structure for table 'Capstone_route'
#

DROP TABLE IF EXISTS `Capstone_route` CASCADE;
CREATE TABLE `Capstone_route` (
  `id` INT NOT NULL,
  `destination` VARCHAR(64) CHARACTER SET utf8 NOT NULL,
  `date_orig` DATE NOT NULL,
  `time_orig` TIME NOT NULL,
  `time_dep` TIME NOT NULL,
  `no_pass` INT NOT NULL,
  `cost` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `map_pic` VARCHAR(256) CHARACTER SET utf8,
  `created_date` DATETIME NOT NULL,
  `thedriver_id` INT,
  `departure` VARCHAR(64) CHARACTER SET utf8 NOT NULL,
  `fin_set` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `keynum` VARCHAR(12) CHARACTER SET utf8 NOT NULL,
  `dist` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `d_a` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `date_ret` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Capstone_route_thedriver_id_af104316` (`thedriver_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_route'
#

LOCK TABLES `Capstone_route` WRITE;
INSERT IGNORE INTO `Capstone_route`(`id`, `destination`, `date_orig`, `time_orig`, `time_dep`, `no_pass`, `cost`, `map_pic`, `created_date`, `thedriver_id`, `departure`, `fin_set`, `keynum`, `dist`, `d_a`, `date_ret`) VALUES(102, 'valtou 29  athens', '2022-06-19', '23:16:00', '23:22:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 18:17:12.974457', 2, 'kazantzaki 8 alimos athens  greece', 0, '16469', 1.0558000000000000e+01, 1, '2022-06-13'), (103, 'skoufou 10 athens greece', '2022-06-19', '21:20:00', '21:25:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=skoufou 10 athens greece2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 18:19:22.891547', 2, 'kazantzaki 8 alimos athens  greece', 0, '48021', 9.8219999999999992e+00, 1, '2022-06-13'), (104, 'Skoufa athens', '2022-06-19', '22:19:00', '22:21:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 19:17:48.653483', 2, 'kazantzaki 8 alimos athens  greece', 0, '37978', 1.0250000000000000e+01, 0, '2022-06-13'), (105, 'ymhttou 72 athens', '2022-06-13', '22:59:00', '23:09:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=valtou 29 athens1&wp.1=ymhttou 72 athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 19:59:16.773756', 2, 'valtou 29 athens', 0, '51702', 3.8650000000000002e+00, 1, '2022-06-13'), (106, 'Skoufa athens', '2022-06-12', '23:08:00', '23:11:00', 1, 0.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0= kazantzaki athens greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 20:07:05.456964', 2, ' kazantzaki athens greece', 0, '34177', 4.8200000000000003e+00, 1, '2022-06-13'), (107, 'skoufou 10 athens greece', '2022-06-12', '23:11:00', '23:14:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 athens greece1&wp.1=skoufou 10 athens greece2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 20:09:35.261521', 2, 'kazantzaki 8 athens greece', 0, '73637', 4.5019999999999998e+00, 1, '2022-06-13'), (108, 'valtou 29  athens', '2022-06-12', '23:13:00', '23:15:00', 1, 0.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 20:10:03.190829', 2, 'kazantzaki 8 alimos athens  greece', 0, '29358', 1.0558000000000000e+01, 1, '2022-06-13'), (109, 'Skoufa athens', '2022-06-23', '01:15:00', '03:16:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0= kazantzaki athens greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 20:13:54.546203', 2, ' kazantzaki athens greece', 0, '33931', 4.8200000000000003e+00, 1, '2022-06-13'), (110, 'ymhttou 72 athens', '2022-06-12', '23:16:00', '23:18:00', 1, 0.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=valtou 29 athens1&wp.1=ymhttou 72 athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-12 20:14:37.810990', 2, 'valtou 29 athens', 0, '72630', 3.8650000000000002e+00, 1, '2022-06-13'), (111, 'valtou 29  athens', '2022-06-15', '01:06:00', '03:11:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=ymhttou athens1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 08:06:18.976027', 2, 'ymhttou athens', 0, '69495', 2.9249999999999998e+00, 1, '2022-06-13'), (112, 'Skoufa athens', '2022-06-13', '14:59:00', '15:05:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 08:59:43.566415', 58, 'kazantzaki 8 alimos athens  greece', 0, '85092', 1.0250000000000000e+01, 1, '2022-06-13'), (113, 'valtou 29  athens', '2022-06-13', '22:05:00', '23:07:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 18:05:21.556005', 4, 'kazantzaki 8 alimos athens  greece', 0, '69950', 1.0558000000000000e+01, 1, '2022-06-07'), (114, 'valtou 29  athens', '2022-06-13', '22:11:00', '18:09:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 18:09:30.820714', 4, 'kazantzaki 8 alimos athens  greece', 0, '66636', 1.0558000000000000e+01, 1, '2022-06-15'), (115, 'Skoufa athens', '2022-06-14', '23:10:00', '12:10:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0= kazantzaki athens greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 18:10:38.319756', 4, ' kazantzaki athens greece', 0, '76184', 4.8200000000000003e+00, 1, '2022-06-21'), (116, 'Skoufa athens', '2022-06-14', '21:12:00', '21:14:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 athens greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 18:10:58.842215', 4, 'kazantzaki 8 athens greece', 0, '84396', 4.5609999999999999e+00, 1, '2022-06-28'), (117, 'valtou 29  athens', '2022-06-14', '22:11:00', '21:16:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=valtou 29 athens1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 18:11:50.143960', 4, 'valtou 29 athens', 0, '90148', 0.0000000000000000e+00, 1, '2022-07-05'), (118, 'Skoufa athens', '2022-06-14', '21:15:00', '21:16:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 18:13:57.187340', 4, 'kazantzaki 8 alimos athens  greece', 0, '75204', 1.0250000000000000e+01, 1, '2022-06-29'), (119, 'Skoufa athens', '2022-06-20', '21:15:00', '21:17:00', 3, 2.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 athens greece1&wp.1=Skoufa athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-13 18:14:35.596340', 4, 'kazantzaki 8 athens greece', 1, '95804', 4.5609999999999999e+00, 0, '2022-06-30'), (120, 'valtou 29  athens', '2022-06-24', '22:39:00', '22:40:00', 3, 3.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-06-18 19:37:53.303316', 2, 'kazantzaki 8 alimos athens  greece', 1, '95828', 1.0558000000000000e+01, 1, '2022-06-25'), (121, 'valtou 29  athens', '2022-08-10', '20:45:00', '17:45:00', 2, 2.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-07-07 14:46:00.149500', 4, 'kazantzaki 8 alimos athens  greece', 0, '94775', 1.0558000000000000e+01, 0, '2022-08-14'), (122, 'valtou 29  athens', '2022-10-22', '20:44:00', '18:47:00', 2, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0= kazantzaki athens greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-07-21 15:45:02.053037', 4, 'kazantzaki athens greece', 1, '36508', 6.7649999999999997e+00, 0, '2022-11-18'), (125, 'valtou 29  athens', '2022-10-19', '09:29:00', '08:31:00', 4, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0= kazantzaki athens greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-10-18 05:29:55.879326', 49, ' kazantzaki athens greece', 0, '21665', 1.1654999999999999e+01, 0, '2022-10-27'), (126, 'valtou 29  athens', '2022-10-29', '19:42:00', '23:46:00', 2, 2.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-10-20 14:43:05.970403', 4, 'kazantzaki 8 alimos athens  greece', 1, '79913', 1.0558000000000000e+01, 0, '2022-10-30'), (127, 'valtou 29  athens', '2022-11-08', '23:26:00', '22:31:00', 2, 2.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=kazantzaki 8 alimos athens  greece1&wp.1=valtou 29  athens2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2022-10-26 16:27:09.452526', 4, 'kazantzaki 8 alimos athens  greece', 0, '60829', 1.0558000000000000e+01, 0, '2022-11-15'), (128, 'χαριλάου τρικούπη 4 αθήνα', '2023-01-22', '14:16:00', '01:09:00', 1, 1.0000000000000000e+00, 'https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=λεωφόρος κηφισίας 35 αθήνα1&wp.1=χαριλάου τρικούπη 4 αθήνα2&o=json&key=Ak1lcrrpdMdej2d1w_shmItLOBhpEmeQpVz6g6FsRwa7CkamEDl4sgkw00XlEPbF', '2023-01-22 09:10:55.052252', 5, 'λεωφόρος κηφισίας 35 αθήνα', 0, '31005', 9.7040000000000006e+00, 0, '2023-01-24');
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'Capstone_route_thepassenger'
#

DROP TABLE IF EXISTS `Capstone_route_thepassenger` CASCADE;
CREATE TABLE `Capstone_route_thepassenger` (
  `id` INT NOT NULL,
  `route_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Capstone_route_thepassenger_user_id_e95505c8` (`user_id`),
  INDEX `Capstone_route_thepassenger_route_id_add5a60e` (`route_id`),
  UNIQUE `Capstone_route_thepassenger_route_id_user_id_03cba0d6_uniq` (`route_id`, `user_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_route_thepassenger'
#

LOCK TABLES `Capstone_route_thepassenger` WRITE;
INSERT IGNORE INTO `Capstone_route_thepassenger`(`id`, `route_id`, `user_id`) VALUES(1686, 115, 48), (1689, 117, 48), (1708, 119, 2), (1711, 119, 8), (1712, 120, 4), (1715, 121, 49), (1716, 121, 5), (1768, 125, 5), (1774, 125, 4), (1786, 122, 5), (1787, 122, 48), (1790, 126, 5), (1798, 127, 48), (1805, 127, 5);
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'Capstone_user'
#

DROP TABLE IF EXISTS `Capstone_user` CASCADE;
CREATE TABLE `Capstone_user` (
  `id` INT NOT NULL,
  `password` VARCHAR(128) CHARACTER SET utf8 NOT NULL,
  `last_login` DATETIME,
  `is_superuser` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `username` VARCHAR(150) CHARACTER SET utf8 NOT NULL,
  `first_name` VARCHAR(150) CHARACTER SET utf8 NOT NULL,
  `last_name` VARCHAR(150) CHARACTER SET utf8 NOT NULL,
  `is_staff` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `is_active` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `email` VARCHAR(254) CHARACTER SET utf8 NOT NULL,
  `date_joined` DATETIME NOT NULL,
  `name` VARCHAR(64) CHARACTER SET utf8 NOT NULL,
  `surname` VARCHAR(64) CHARACTER SET utf8 NOT NULL,
  `profile_pic` VARCHAR(100) CHARACTER SET utf8 NOT NULL,
  `about` VARCHAR(64) CHARACTER SET utf8,
  `dob` DATE NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE `sqlite_autoindex_Capstone_user_1` (`username`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_user'
#

LOCK TABLES `Capstone_user` WRITE;
INSERT IGNORE INTO `Capstone_user`(`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `email`, `date_joined`, `name`, `surname`, `profile_pic`, `about`, `dob`) VALUES(1, '1234', '2022-05-21 19:45:47', 0, 'Evan', '', '', 0, 1, 'e.mgos@gml.com', '2022-02-20 18:30:39', 'xxxx', 'xxxx', 'vag.jpg', NULL, '2022-06-05'), (2, 'pbkdf2_sha256$216000$T36mwHIB02o5$4IvUX2DcXmql+2kmoRH8REG3cu2WxHYE/AERx0FlBSw=', '2022-06-19 19:31:17.392518', 0, 'Faid', '', '', 0, 1, 'info@neng.gr', '2022-03-06 20:45:59.441604', 'xxxx', 'xxxx', '/default_user.jpg', NULL, '2022-06-05'), (3, 'pbkdf2_sha256$216000$eucu1cZbc2X2$uvVUBsqcqwZTuwU2f64B32cKFVm77y8n/dDgPZJ2XyI=', '2022-03-27 07:33:11.906710', 0, 'myr', '', '', 0, 1, 'myr@se.g', '2022-03-06 20:46:50.628817', 'xxxx', 'xxxx', '/default_user.jpg', NULL, '2022-06-05'), (4, 'pbkdf2_sha256$216000$tMc0TtWq7iDG$biql2CQi1dag/uu0V/ctrx2Gg5GhCtBZuv8jj1iUK7g=', '2023-08-06 16:32:22.534786', 0, 'Myr', '', '', 0, 1, 'wer@dfr.jh', '2022-03-22 17:52:45', 'xxxx', 'xxxx', 'vag_hj86j6b.jpg', 'The best', '2022-06-05'), (5, 'pbkdf2_sha256$216000$MHMEjm8vTyGk$DFPMMyedki+DhqSGb4kV/abNKdBg909XIz6wPL1CWG0=', '2023-08-06 16:31:48.787683', 1, 'admin', '', '', 1, 1, 'admin@sde.df', '2022-03-27 16:48:13.496270', 'xxxx', 'xxxx', '/default_user.jpg', NULL, '2022-06-05'), (6, 'pbkdf2_sha256$216000$CVxi1WX8dSY9$Fn1uQovXLFiKqsdK32cBTdHfUcRaIudbAb+TNcsxibw=', '2022-03-27 18:05:32.539131', 0, 'Retr', '', '', 0, 1, 'ert@sde.cv', '2022-03-27 18:05:31.583495', 'xxxx', 'xxxx', '/default_user.jpg', NULL, '2022-06-05'), (7, 'pbkdf2_sha256$216000$pkdDOXZ17FXZ$U68LGK8BmwGpZL/plkeW/GfY1ThxbikD9nH+dvbzB5c=', '2022-03-27 18:08:42.283588', 0, 'drttt', '', '', 0, 1, 'xmd@ld.cd', '2022-03-27 18:08:41.726182', 'xxxx', 'xxxx', '/default_user.jpg', NULL, '2022-06-05'), (8, 'pbkdf2_sha256$216000$TjJ8tNs5auSF$5XqpnxDNE69tFf6saAkHVPCxepM8wtuw0IOL34IB4gI=', '2022-07-31 10:01:14.104274', 0, 'Wert', '', '', 0, 1, 'asd@kdj.cdf', '2022-03-27 18:25:41.529955', 'Evang', 'Matr', '/default_user.jpg', NULL, '2022-06-05'), (9, 'pbkdf2_sha256$216000$TgwJiiltmvo8$dF1KkF1zsxoHLov6oKUPyRvULUL7zSpNHjq9uE1VrC0=', '2022-05-01 10:21:09.274561', 0, 'der', '', '', 0, 1, 'wer@dfr', '2022-05-01 10:21:08.381809', 'mar', 'der', '/default_user.jpg', NULL, '2022-06-05'), (18, 'pbkdf2_sha256$216000$JNaXPaCagwHq$SalyDJ1wayXcwJ8/Or1yeWByMmX2B6s0+A4JU3XPtQQ=', '2022-06-03 18:12:40.924951', 0, 'evanmat', '', '', 0, 1, 'e.matragos@gmail.com', '2022-05-22 18:38:32.702214', 'evan', 'matr', '/default_user.jpg', NULL, '2022-06-05'), (19, 'pbkdf2_sha256$216000$b4rbhTildVM2$c5jhVFcLz7TTyac9VlhLHoY+0c80r+GWwcY5Zk52ZU8=', NULL, 0, 'wqe', '', '', 0, 0, 'ert@fdr.co', '2022-05-22 18:53:49.620335', 'wrr', 'sbb', '/default_user.jpg', NULL, '2022-06-05'), (20, 'pbkdf2_sha256$216000$ftKbO8PQoy9i$Ao0NJCiwMtiI11TXs/+K/HOxxo27EAvLsFh1dm+uIyM=', NULL, 0, 'wed', '', '', 0, 0, 'xhdh@kdk.v', '2022-05-22 18:56:34.086944', 'qw', 'xd', '/default_user.jpg', NULL, '2022-06-05'), (21, 'pbkdf2_sha256$216000$MqYgqbxwLI3T$FgKmRu3RqyfrdmMTpW7lviTDokmp1dsXMKo/v6s69cw=', NULL, 0, 'xwx', '', '', 0, 0, 'ckmw@nh.j', '2022-05-22 19:00:29.380310', 'wec', 'sefr', '/default_user.jpg', NULL, '2022-06-05'), (22, 'pbkdf2_sha256$216000$xagSeuv8ogIp$a9yeDox5HB9TnqI4tRgd6FkLle7U8IrZ546DWFtEMCU=', NULL, 0, 'dfrr', '', '', 0, 0, 'ndhdh@dd.c', '2022-05-22 19:07:25.661307', 'jjj', 'qw', '/default_user.jpg', NULL, '2022-06-05'), (26, '1234', NULL, 0, 'rtty', '', '', 0, 1, 'SDF@dff.ki', '2022-06-05 11:09:47', 'WFW', 'EF', '/default_user.jpg', NULL, '2022-06-05'), (27, 'pbkdf2_sha256$216000$53PnuoztbIky$iJt7T9MvTraL7b18UkyTjA/82UJNqX2UR2UPBLyoRo0=', NULL, 0, 'Myrbgdb', '', '', 0, 0, 'dg@ddr.gt', '2022-06-05 16:27:31.496052', 'wer', 'brre', '/default_user.jpg', NULL, '2022-06-05'), (28, 'pbkdf2_sha256$216000$suFH5OyOzvrx$7OaZuMgu7lX1TfXxIPbY8RBnUjkYTJR0pjWo5ZHCV4M=', NULL, 0, 'Myrgae', '', '', 0, 0, 'eae@feew.u', '2022-06-05 16:32:28.297375', 'SEE', 'rgr', '/default_user.jpg', NULL, '2022-06-05'), (29, 'pbkdf2_sha256$216000$CVb6POFQLJ6L$871QnSW7FiwVHRUDX9BkzZyxlT5CqenNJXBLHRhtqb4=', NULL, 0, 'adwqdqew', '', '', 0, 0, 'zcc@sssw.efe', '2022-06-11 15:27:05.915087', 'asq', 'wcw', '/default_user.jpg', NULL, '2022-06-11'), (30, 'pbkdf2_sha256$216000$FSL6GAa1sL5j$hTwryHd3rDHnwU6YuHxpOXIaMm8MDgl93hlZgI2ozlw=', NULL, 0, 'sdwaaa', '', '', 0, 0, 'hdhdh@jjf.cjj', '2022-06-11 15:31:54.519540', 'hg', 'hh', '/default_user.jpg', NULL, '2022-06-11'), (31, 'pbkdf2_sha256$216000$B0jNKCek0WXr$rCHL8LzRnMq+3vsk4XrRL2a/5N/6b6qR1fVZXl0H/Lg=', NULL, 0, 'sxqwxq', '', '', 0, 0, 'aas@dv.v', '2022-06-11 15:33:24.865831', 'q', 'sd', '/default_user.jpg', NULL, '2022-06-11'), (32, 'pbkdf2_sha256$216000$p4qsyB6zTDnZ$9NuKgMElOEHW6gaVHMR9kL/ufRnyLFSiq6pGbjeV0T0=', NULL, 0, 'Myrqq', '', '', 0, 0, 'axqsx@xcc.ck', '2022-06-11 15:34:22.995078', 's', 'wqd', '/default_user.jpg', NULL, '2022-06-11'), (33, 'pbkdf2_sha256$216000$f4YjYPcqaaxi$9SLG0K5rn4fiUZCUnUpgo1R4CBjAd8veqEHtfBiEkp8=', NULL, 0, 'Myrcas', '', '', 0, 0, 'ehdg@ndd.fjf', '2022-06-11 16:29:30.522255', 'sjs', 'jds', '/default_user.jpg', NULL, '2022-06-11'), (34, 'pbkdf2_sha256$216000$kvi0DLfaxi2o$T4pEtfyuTfyWjZHJp+V3qeovhfwz0tONHi1dOqdZoWE=', NULL, 0, 'Myraaa', '', '', 0, 0, 'emd@mdm.d', '2022-06-11 16:45:22.921252', 'aa', 'e', '/default_user.jpg', NULL, '2022-06-11'), (35, 'pbkdf2_sha256$216000$PKOyG01FUCYa$3s64JghjBpylkIw7oTYI03PG8DIHwahDJQ9EceEDH4E=', NULL, 0, 'Myraaaaa', '', '', 0, 0, 'nshs@bsb.jj', '2022-06-11 16:47:10.673245', 'ss', 'qq', '/default_user.jpg', NULL, '2022-06-11'), (37, 'pbkdf2_sha256$216000$9UrwVCgfMHzT$ywdHgkZe1pwoo2VqOs6l4EtXnLmtfddkvGtQ3p+/7vY=', NULL, 0, 'Myrww', '', '', 0, 0, 'jjsjs@jsj.hh', '2022-06-11 18:52:29.704567', 'gsgs', 'sgsg', '/default_user.jpg', NULL, '2022-06-11'), (46, 'pbkdf2_sha256$216000$vNUMin9nTwjf$oLSgpjtfxuhKdnV3lm9wArsgd1+04R5xOKGqRI/jjIM=', NULL, 0, 'Faidsqws', '', '', 0, 0, 'vfqcqvlmwldsjmxopq@nthrw.com', '2022-06-11 19:52:32.112924', 'qs', 'ws', '/default_user.jpg', NULL, '2022-06-11'), (47, 'pbkdf2_sha256$216000$QUM8xM9gOWlq$2BfHJxER5cePGEI+8VNpr+PqFxP549Jnil5LpQce0yM=', '2022-06-11 19:55:27.470502', 0, 'Faid123', '', '', 0, 1, 'aakohjglnrfntfikey@kvhrs.com', '2022-06-11 19:53:57.271853', 'zws', 'WD', '/default_user.jpg', NULL, '2022-06-11'), (48, 'pbkdf2_sha256$216000$18GhQ8jV3fSx$JaNeuecseWD9jEnJTMaAdr9Ts3aG+jL+5gY45k4bvy0=', '2022-11-01 20:22:21.743413', 0, 'Myrvjh', '', '', 0, 1, 'vwejuobkyxxnjtjyfm@nthrw.com', '2022-06-12 10:29:28.827226', 'jbkb', 'jhb', '/default_user.jpg', NULL, '2022-06-12'), (49, 'pbkdf2_sha256$216000$KVzZ3KVbOgrY$tUcKbeyeZvaclji2ILHx6bbAgMOcGPx20U9U3qc33n4=', '2022-10-30 12:11:17.821869', 0, 'Myrvjhds', '', '', 0, 1, 'sdahxmonfpzzxltdgm@bvhrk.com', '2022-06-12 10:36:31.604676', 'xed', 'eef3', '/default_user.jpg', NULL, '2022-06-12'), (50, 'pbkdf2_sha256$216000$gakFe2CYmCHw$DFkhMg8ER0UffmU8hWyXQY3nZ2eXMbUBWIJmPS6iW0k=', NULL, 0, 'Ret', '', '', 0, 0, 'oxwllnysosaogmswvj@bvhrs.com', '2022-06-13 08:16:57.198254', 'RT', 'GGH', '/default_user.jpg', NULL, '2022-06-13'), (51, 'pbkdf2_sha256$216000$yni7wJyjpMXc$0oX32vC6AonOli5SC5UwJ+bV/v+1acbongozL7G+GCU=', NULL, 0, 'Faidfrrr', '', '', 0, 0, 'isjteimkpldorxrzzy@bvhrs.com', '2022-06-13 08:25:44.670789', 'hjjh', 'bb', '/default_user.jpg', NULL, '2022-06-13'), (52, 'pbkdf2_sha256$216000$FiggFcC4uTum$eD5jx5PKg60lM5PRLVEz150yz18Iiw9abL5z0GdjWVE=', NULL, 0, 'qww', '', '', 0, 0, 'dww59411@xcoxc.com', '2022-06-13 08:29:41.859404', 'A', 'we', '/default_user.jpg', NULL, '2022-06-13'), (53, 'pbkdf2_sha256$216000$jm9IsueeQc3w$YmYlFs/SZPASXUcEIVeSHY+jtPDe1fpPaZBTZk1CTSY=', NULL, 0, 'fgseeg', '', '', 0, 0, 'tcc63488@xcoxc.com', '2022-06-13 08:31:42.936231', 'shd', 'jsjs', '/default_user.jpg', NULL, '2022-06-13'), (54, 'pbkdf2_sha256$216000$7JsPPc3DEdF5$jZUxqI/kN9LK8gWyQc3g0/q+ux/a54pdRI5qe36MINw=', NULL, 0, 'fgseegq', '', '', 0, 0, 'tcc6348@xcoxc.com', '2022-06-13 08:34:06.319342', 'shd', 'jsjs', '/default_user.jpg', NULL, '2022-06-13'), (55, 'pbkdf2_sha256$216000$aGYrKYVJzfVq$39VxkGyLHlt8uvKaye8Tvk47IsKruwTzitMBzFPebbU=', NULL, 0, 'fgseegq1', '', '', 0, 0, 'tcc634@xcoxc.com', '2022-06-13 08:37:52.586899', 'shd', 'jsjs', '/default_user.jpg', NULL, '2022-06-13'), (56, 'pbkdf2_sha256$216000$pn52tIhAskw9$wAn0QzxcV8DgEwmxF8qLQThjSrjWf3rSngbCCpiqH9E=', NULL, 0, 'fgseegq12', '', '', 0, 0, 'tcc634@xco2xc.com', '2022-06-13 08:39:04.234250', 'shd', 'jsjs', '/default_user.jpg', NULL, '2022-06-13'), (57, 'pbkdf2_sha256$216000$XVhmHoD3rrsx$sv6SR2ppTTYQ9zLczXbYOi4tqQTbV6ElRnqSU0qA0o8=', NULL, 0, 'fgseegq125', '', '', 0, 0, 'tcc6354@xco2xc.com', '2022-06-13 08:40:35.013808', 'shd', 'jsjs', '/default_user.jpg', NULL, '2022-06-13'), (58, 'pbkdf2_sha256$216000$LHSOgARY10WD$kJANQaiaWMqjcfKSAR7qDSPAXcBVPGyEMD3oOLsJ/k8=', '2022-06-18 19:35:30.572808', 0, 'fvf', '', '', 0, 1, 'hdt32406@xcoxc.com', '2022-06-13 08:50:02.648982', 'qw', 'ewf', '/default_user.jpg', NULL, '2022-06-13'), (59, 'pbkdf2_sha256$216000$vbdBxTHruQTP$vUNLkzgVAmxeIikweJo5AaJQK+RWX7Mhy9vsJQK5D38=', NULL, 0, 'fvffge', '', '', 0, 0, 'rabege@efw.r', '2022-06-13 08:52:27.320942', 'wdw', 'qerf', '/default_user.jpg', NULL, '2022-06-13'), (60, 'pbkdf2_sha256$216000$61Bi44E9LIf9$ZbQBMf88nlqC7gkk+KRvdjD8Wkx5xxPHPVLuFFf/M8Q=', NULL, 0, 'fvfgsb', '', '', 0, 0, 'vehpoodql@gmail.com', '2022-06-13 08:54:38.948655', 'egq', 'dfer', '/default_user.jpg', NULL, '2022-06-13'), (61, 'pbkdf2_sha256$216000$m7eFoehG9FOV$Gv0QMsWnBMVsSCSGM+gO2S6qlP8JxONjjVw/YlOyPfE=', NULL, 0, 'fvfv s', '', '', 0, 0, 'vehpooreel@gmail.com', '2022-06-13 08:55:53.009678', 'fb', 'ewefgwerr', '/default_user.jpg', NULL, '2022-06-13'), (62, 'pbkdf2_sha256$216000$kKt4eA1PyJOQ$oHSIXfR0onG2ZB7YfbBGRquCcCd4NNCu7UvGIAA7AMA=', NULL, 0, 'fvffgewew', '', '', 0, 0, 'rabefge@efw.r', '2022-06-13 08:58:20.966003', 'wdw', 'qerf', '/default_user.jpg', NULL, '2022-06-13'), (63, 'pbkdf2_sha256$216000$tMc0TtWq7iDG$biql2CQi1dag/uu0V/ctrx2Gg5GhCtBZuv8jj1iUK7g=', '2022-06-13 09:41:25.030661', 0, 'qwe', '', '', 0, 1, 'dafw@daf.ur', '2022-06-13 09:37:31', 'qwe', 'asd', '/default_user.jpg', NULL, '2000-06-13'), (64, 'pbkdf2_sha256$216000$J3o0iLLYgFks$5VgG+jEdD4/7D7fr7qM1k72VxS0qZ+W+gZ7liueMWiI=', NULL, 0, 'Myrgaerf', '', '', 0, 1, 'wfq@ghg', '2022-06-13 09:53:35.228432', 'fg', 'rg', '/default_user.jpg', NULL, '2022-06-13'), (65, 'pbkdf2_sha256$216000$QPUr4D8UZ7qo$TyJq0cKFUIIZpaUgBbhMvIOR+hGI0pPQmp37A6YHZm0=', NULL, 0, 'grege', '', '', 0, 1, 'regew@egaraer.fd', '2022-06-13 09:55:01.672376', 'qq', 'ss', '/default_user.jpg', NULL, '2022-06-13'), (66, 'pbkdf2_sha256$216000$okGh0HXMqWYM$tpeA1zosuYwC9WR7fWw8X2xdcCfUH1PRmH9aYFxJGaU=', NULL, 0, 'vasa', '', '', 0, 0, 'vzbff@sfb.dgfh', '2022-06-13 09:56:40.853968', 'cfFw', 'faga', '/default_user.jpg', NULL, '2022-06-13'), (67, 'pbkdf2_sha256$216000$DyivPQpq8xim$ohXM0G3vpw5EuYWsdSD5nmOtFzv1n4/GRmsR4FYpgW4=', '2023-08-06 16:59:48.381348', 0, 'Mwe', '', '', 0, 1, 'via49845@omeie.com', '2023-08-06 16:58:51.048542', 'vf', 'eg', '/default_user.jpg', NULL, '2023-08-06');
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'Capstone_user_groups'
#

DROP TABLE IF EXISTS `Capstone_user_groups` CASCADE;
CREATE TABLE `Capstone_user_groups` (
  `id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Capstone_user_groups_group_id_f6634b5c` (`group_id`),
  INDEX `Capstone_user_groups_user_id_1a904e11` (`user_id`),
  UNIQUE `Capstone_user_groups_user_id_group_id_31451292_uniq` (`user_id`, `group_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_user_groups'
#

LOCK TABLES `Capstone_user_groups` WRITE;
UNLOCK TABLES;

#
# Table structure for table 'Capstone_user_user_permissions'
#

DROP TABLE IF EXISTS `Capstone_user_user_permissions` CASCADE;
CREATE TABLE `Capstone_user_user_permissions` (
  `id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Capstone_user_user_permissions_permission_id_e48a230b` (`permission_id`),
  INDEX `Capstone_user_user_permissions_user_id_1a4262e2` (`user_id`),
  UNIQUE `Capstone_user_user_permissions_user_id_permission_id_cb314e7d_u` (`user_id`, `permission_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'Capstone_user_user_permissions'
#

LOCK TABLES `Capstone_user_user_permissions` WRITE;
UNLOCK TABLES;

#
# Table structure for table 'cookie_consent_cookie'
#

DROP TABLE IF EXISTS `cookie_consent_cookie` CASCADE;
CREATE TABLE `cookie_consent_cookie` (
  `id` INT NOT NULL,
  `name` VARCHAR(250) CHARACTER SET utf8 NOT NULL,
  `description` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `path` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `domain` VARCHAR(250) CHARACTER SET utf8 NOT NULL,
  `created` DATETIME NOT NULL,
  `cookiegroup_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `cookie_consent_cookie_cookiegroup_id_96c0ab4b` (`cookiegroup_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'cookie_consent_cookie'
#

LOCK TABLES `cookie_consent_cookie` WRITE;
INSERT IGNORE INTO `cookie_consent_cookie`(`id`, `name`, `description`, `path`, `domain`, `created`, `cookiegroup_id`) VALUES(2, '*', 'This cookies are used by Facebook to allow sharing content.', '/', '.google.com', '2022-05-17 15:08:14.869518', 2), (3, 'csrftoken', '', '/', '', '2022-05-17 15:09:20.548671', 3), (4, 'sessionid', '', '/', '', '2022-05-17 15:09:51.121657', 3), (5, 'Optional cookies', '', '/', '/', '2022-05-17 16:18:25.061790', 1);
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'cookie_consent_cookiegroup'
#

DROP TABLE IF EXISTS `cookie_consent_cookiegroup` CASCADE;
CREATE TABLE `cookie_consent_cookiegroup` (
  `id` INT NOT NULL,
  `varname` VARCHAR(32) CHARACTER SET utf8 NOT NULL,
  `name` VARCHAR(100) CHARACTER SET utf8 NOT NULL,
  `description` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `is_required` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `is_deletable` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `ordering` INT NOT NULL,
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'cookie_consent_cookiegroup'
#

LOCK TABLES `cookie_consent_cookiegroup` WRITE;
INSERT IGNORE INTO `cookie_consent_cookiegroup`(`id`, `varname`, `name`, `description`, `is_required`, `is_deletable`, `ordering`, `created`) VALUES(1, 'optional', 'optional', '', 0, 1, 0, '2022-05-16 16:56:27.094659'), (2, 'social', 'social media', 'Google Plus need to know who you are to work properly.', 0, 1, 0, '2022-05-17 15:05:58.059786'), (3, 'required', 'Required cookies', 'This cookies are required for website.', 1, 0, 0, '2022-05-17 15:06:46.921880');
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'cookie_consent_logitem'
#

DROP TABLE IF EXISTS `cookie_consent_logitem` CASCADE;
CREATE TABLE `cookie_consent_logitem` (
  `id` INT NOT NULL,
  `action` INT NOT NULL,
  `version` VARCHAR(32) CHARACTER SET utf8 NOT NULL,
  `created` DATETIME NOT NULL,
  `cookiegroup_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `cookie_consent_logitem_cookiegroup_id_3bfbe953` (`cookiegroup_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'cookie_consent_logitem'
#

LOCK TABLES `cookie_consent_logitem` WRITE;
INSERT IGNORE INTO `cookie_consent_logitem`(`id`, `action`, `version`, `created`, `cookiegroup_id`) VALUES(1, 1, '2022-05-16T16:57:31.205339+00:00', '2022-05-16 17:04:37.978228', 1), (2, 1, '2022-05-16T16:57:31.205339+00:00', '2022-05-16 17:05:50.505681', 1), (3, 1, '2022-05-16T16:57:31.205339+00:00', '2022-05-16 17:08:57.814568', 1), (4, 1, '2022-05-16T16:57:31.205339+00:00', '2022-05-17 15:28:16.760744', 1), (5, 1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 15:28:31.844538', 2), (6, -1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 15:28:33.517492', 2), (7, 1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 15:28:36.242168', 2), (8, -1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 15:28:37.739094', 2), (9, -1, '', '2022-05-17 16:16:16.104719', 1), (10, 1, '', '2022-05-17 16:16:18.180001', 1), (11, 1, '', '2022-05-17 16:16:19.444961', 1), (12, 1, '', '2022-05-17 16:16:19.969560', 1), (13, -1, '', '2022-05-17 16:16:21.559159', 1), (14, 1, '', '2022-05-17 16:16:23.374086', 1), (15, 1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 16:16:26.644907', 2), (16, 1, '', '2022-05-17 16:16:28.679781', 1), (17, 1, '', '2022-05-17 16:16:32.277146', 1), (18, -1, '', '2022-05-17 16:16:35.027501', 1), (19, 1, '', '2022-05-17 16:16:36.566113', 1), (20, 1, '2022-05-17T16:18:25.061790+00:00', '2022-05-17 16:19:03.107729', 1), (21, -1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 17:05:31.247527', 2), (22, 1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 17:05:33.086413', 2), (23, -1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 17:11:35.285848', 2), (24, 1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 17:11:37.034877', 2), (25, -1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 17:13:44.146850', 2), (26, 1, '2022-05-17T15:08:14.869518+00:00', '2022-05-17 17:13:46.113309', 2);
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'django_admin_log'
#

DROP TABLE IF EXISTS `django_admin_log` CASCADE;
CREATE TABLE `django_admin_log` (
  `id` INT NOT NULL,
  `action_time` DATETIME NOT NULL,
  `object_id` LONGTEXT CHARACTER SET utf8,
  `object_repr` VARCHAR(200) CHARACTER SET utf8 NOT NULL,
  `change_message` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `content_type_id` INT,
  `user_id` INT NOT NULL,
  `action_flag` LONGTEXT CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_user_id_c564eba6` (`user_id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'django_admin_log'
#

LOCK TABLES `django_admin_log` WRITE;
INSERT IGNORE INTO `django_admin_log`(`id`, `action_time`, `object_id`, `object_repr`, `change_message`, `content_type_id`, `user_id`, `action_flag`) VALUES(1, '2022-04-12 17:43:05.031656', '77', '77: kazantzaki 8 alimos athens  greece to valtou 29  athens with 2 at 3.0 per passenger', '', 2, 5, 3), (2, '2022-04-14 05:42:13.841811', '13', 'Message object (13)', '[{"added": {}}]', 10, 5, 1), (3, '2022-05-16 16:56:27.100612', '1', 'gbdr', '[{"added": {}}]', 13, 5, 1), (4, '2022-05-16 16:57:31.210318', '1', 'cookie test /', '[{"added": {}}]', 12, 5, 1), (5, '2022-05-16 17:05:41.841809', '1', 'cookie test /index', '[{"changed": {"fields": ["Path"]}}]', 12, 5, 2), (6, '2022-05-16 17:08:44.590365', '1', 'cookie test /index/index', '[{"changed": {"fields": ["Domain"]}}]', 12, 5, 2), (7, '2022-05-17 15:04:58.035806', '1', 'optional', '[{"changed": {"fields": ["Variable name", "Name"]}}]', 13, 5, 2), (8, '2022-05-17 15:05:58.064183', '2', 'social media', '[{"added": {}}]', 13, 5, 1), (9, '2022-05-17 15:06:46.927909', '3', 'Required cookies', '[{"added": {}}]', 13, 5, 1), (10, '2022-05-17 15:08:14.875604', '2', '* .google.com/', '[{"added": {}}]', 12, 5, 1), (11, '2022-05-17 15:09:20.553818', '3', 'csrftoken /', '[{"added": {}}]', 12, 5, 1), (12, '2022-05-17 15:09:51.134151', '4', 'sessionid /', '[{"added": {}}]', 12, 5, 1), (13, '2022-05-17 16:14:15.994885', '1', 'cookie test /index/index', '', 12, 5, 3), (14, '2022-05-17 16:18:25.068777', '5', 'Optional cookies /', '[{"added": {}}]', 12, 5, 1), (15, '2022-05-17 17:13:00.124351', '5', 'Optional cookies //', '[{"changed": {"fields": ["Domain"]}}]', 12, 5, 2), (16, '2022-05-22 18:35:39.826154', '1', 'Evan', '[{"changed": {"fields": ["Password"]}}]', 1, 5, 2), (17, '2022-05-22 18:37:52.023960', '17', 'Evanwer', '', 1, 5, 3), (18, '2022-06-05 07:49:23.109238', '1', 'Evan', '[{"changed": {"fields": ["Profile pic"]}}]', 1, 5, 2), (19, '2022-06-05 07:53:19.999633', '1', 'Evan', '[{"changed": {"fields": ["Profile pic"]}}]', 1, 5, 2), (20, '2022-06-05 07:53:28.582814', '1', 'Evan', '[{"changed": {"fields": ["Profile pic"]}}]', 1, 5, 2), (21, '2022-06-05 10:54:06.692640', '23', 'George', '', 1, 5, 3), (22, '2022-06-05 10:54:41.756180', '24', 'jhhyy', '[{"added": {}}]', 1, 5, 1), (23, '2022-06-05 11:02:36.832436', '1', 'Evan', '[{"changed": {"fields": ["Profile pic"]}}]', 1, 5, 2), (24, '2022-06-05 11:02:46.177056', '1', 'Evan', '[{"changed": {"fields": ["Profile pic"]}}]', 1, 5, 2), (25, '2022-06-05 11:08:17.209448', '24', 'jhhyy', '', 1, 5, 3), (26, '2022-06-05 11:08:55.209833', '25', 'xh', '[{"added": {}}]', 1, 5, 1), (27, '2022-06-05 11:09:45.531315', '25', 'xh', '', 1, 5, 3), (28, '2022-06-05 11:10:11.174378', '26', 'rtty', '[{"added": {}}]', 1, 5, 1), (29, '2022-06-05 13:35:14.898368', '4', 'Myr', '[{"changed": {"fields": ["Email"]}}]', 1, 5, 2), (30, '2022-06-13 09:38:11.577058', '63', 'qwe', '[{"added": {}}]', 1, 5, 1), (31, '2022-06-13 09:40:27.000017', '63', 'qwe', '[{"changed": {"fields": ["Password"]}}]', 1, 5, 2), (32, '2022-06-13 09:41:15.622344', '63', 'qwe', '[{"changed": {"fields": ["Password"]}}]', 1, 5, 2), (33, '2022-06-15 11:02:53.500858', '119', '119: kazantzaki 8 athens greece to Skoufa athens with 2 at 2.0 per passenger', '[{"changed": {"fields": ["Date orig", "No pass", "Cost"]}}]', 2, 5, 2), (34, '2022-06-18 14:12:24.806383', '119', '119: kazantzaki 8 athens greece to Skoufa athens with 2 at 2.0 per passenger', '[{"changed": {"fields": ["Date orig", "Date ret"]}}]', 2, 5, 2), (35, '2022-06-18 15:57:12.711499', '119', '119: kazantzaki 8 athens greece to Skoufa athens with 2 at 3.0 per passenger', '[{"changed": {"fields": ["Cost"]}}]', 2, 5, 2), (36, '2022-06-18 15:58:10.140846', '119', '119: kazantzaki 8 athens greece to Skoufa athens with 3 at 2.0 per passenger', '[{"changed": {"fields": ["No pass", "Cost", "Thepassenger"]}}]', 2, 5, 2), (37, '2022-06-18 16:40:40.861383', '119', '119: kazantzaki 8 athens greece to Skoufa athens with 3 at 2.0 per passenger', '[{"changed": {"fields": ["Thepassenger"]}}]', 2, 5, 2), (38, '2022-06-18 16:41:19.103137', '119', '119: kazantzaki 8 athens greece to Skoufa athens with 3 at 2.0 per passenger', '[{"changed": {"fields": ["Thepassenger"]}}]', 2, 5, 2), (39, '2022-10-18 04:15:45.516643', '123', '123: kazantzaki 8 alimos athens  greece to valtou 29  athens with 3 at 1.0 per passenger', '[{"changed": {"fields": ["Thepassenger"]}}]', 2, 5, 2), (40, '2022-10-18 04:39:36.608452', '123', '123: kazantzaki 8 alimos athens  greece to valtou 29  athens with 3 at 1.0 per passenger', '', 2, 5, 3), (41, '2022-10-18 04:41:40.070873', '124', '124: kazantzaki 8 alimos athens  greece to valtou 29  athens with 3 at 2.0 per passenger', '[{"added": {}}]', 2, 5, 1), (42, '2022-10-18 04:42:22.202604', '124', '124: kazantzaki 8 alimos athens  greece to valtou 29  athens with 3 at 2.0 per passenger', '[{"changed": {"fields": ["Date orig", "Time orig"]}}]', 2, 5, 2), (43, '2022-10-18 04:46:26.539837', '124', '124: kazantzaki 8 alimos athens  greece to valtou 29  athens with 3 at 2.0 per passenger', '', 2, 5, 3), (44, '2022-10-18 04:47:02.231595', '122', '122: kazantzaki athens greece to valtou 29  athens with 3 at 1.0 per passenger', '[{"changed": {"fields": ["Date orig", "Date ret", "No pass"]}}]', 2, 5, 2), (45, '2022-10-18 05:10:03.751793', '122', '122: kazantzaki athens greece to valtou 29  athens with 3 at 1.0 per passenger', '[{"changed": {"fields": ["Thepassenger"]}}]', 2, 5, 2), (46, '2022-10-18 05:54:05.183275', '122', '122: kazantzaki athens greece to valtou 29  athens with 2 at 1.0 per passenger', '[{"changed": {"fields": ["No pass"]}}]', 2, 5, 2);
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'django_content_type'
#

DROP TABLE IF EXISTS `django_content_type` CASCADE;
CREATE TABLE `django_content_type` (
  `id` INT NOT NULL,
  `app_label` VARCHAR(100) CHARACTER SET utf8 NOT NULL,
  `model` VARCHAR(100) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`, `model`)
) ENGINE=InnoDB;

#
# Dumping data for table 'django_content_type'
#

LOCK TABLES `django_content_type` WRITE;
INSERT IGNORE INTO `django_content_type`(`id`, `app_label`, `model`) VALUES(1, 'Capstone', 'user'), (2, 'Capstone', 'route'), (3, 'admin', 'logentry'), (4, 'auth', 'permission'), (5, 'auth', 'group'), (6, 'contenttypes', 'contenttype'), (7, 'sessions', 'session'), (8, 'Capstone', 'reply'), (9, 'Capstone', 'comment'), (10, 'Capstone', 'message'), (11, 'Capstone', 'qrcode'), (12, 'cookie_consent', 'cookie'), (13, 'cookie_consent', 'cookiegroup'), (14, 'cookie_consent', 'logitem');
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'django_migrations'
#

DROP TABLE IF EXISTS `django_migrations` CASCADE;
CREATE TABLE `django_migrations` (
  `id` INT NOT NULL,
  `app` VARCHAR(255) CHARACTER SET utf8 NOT NULL,
  `name` VARCHAR(255) CHARACTER SET utf8 NOT NULL,
  `applied` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

#
# Dumping data for table 'django_migrations'
#

LOCK TABLES `django_migrations` WRITE;
INSERT IGNORE INTO `django_migrations`(`id`, `app`, `name`, `applied`) VALUES(1, 'contenttypes', '0001_initial', '2022-02-20 18:29:51.260016'), (2, 'contenttypes', '0002_remove_content_type_name', '2022-02-20 18:29:51.296965'), (3, 'auth', '0001_initial', '2022-02-20 18:29:51.311534'), (4, 'auth', '0002_alter_permission_name_max_length', '2022-02-20 18:29:51.325322'), (5, 'auth', '0003_alter_user_email_max_length', '2022-02-20 18:29:51.342929'), (6, 'auth', '0004_alter_user_username_opts', '2022-02-20 18:29:51.355407'), (7, 'auth', '0005_alter_user_last_login_null', '2022-02-20 18:29:51.365820'), (8, 'auth', '0006_require_contenttypes_0002', '2022-02-20 18:29:51.371990'), (9, 'auth', '0007_alter_validators_add_error_messages', '2022-02-20 18:29:51.391090'), (10, 'auth', '0008_alter_user_username_max_length', '2022-02-20 18:29:51.403762'), (11, 'auth', '0009_alter_user_last_name_max_length', '2022-02-20 18:29:51.424841'), (12, 'auth', '0010_alter_group_name_max_length', '2022-02-20 18:29:51.444694'), (13, 'auth', '0011_update_proxy_permissions', '2022-02-20 18:29:51.456916'), (14, 'auth', '0012_alter_user_first_name_max_length', '2022-02-20 18:29:51.467554'), (15, 'Capstone', '0001_initial', '2022-02-20 18:29:51.499360'), (16, 'Capstone', '0002_auto_20220213_1801', '2022-02-20 18:29:51.516592'), (17, 'Capstone', '0003_remove_route_passenger', '2022-02-20 18:29:51.531912'), (18, 'Capstone', '0004_route_passenger', '2022-02-20 18:29:51.556205'), (19, 'Capstone', '0005_auto_20220220_1834', '2022-02-20 18:29:51.572473'), (20, 'Capstone', '0006_auto_20220220_1904', '2022-02-20 18:29:51.606382'), (21, 'Capstone', '0007_auto_20220220_1927', '2022-02-20 18:29:51.637497'), (22, 'Capstone', '0008_remove_route_thepassenger', '2022-02-20 18:29:51.650685'), (23, 'admin', '0001_initial', '2022-02-20 18:29:51.665646'), (24, 'admin', '0002_logentry_remove_auto_add', '2022-02-20 18:29:51.681755'), (25, 'admin', '0003_logentry_add_action_flag_choices', '2022-02-20 18:29:51.712097'), (26, 'sessions', '0001_initial', '2022-02-20 18:29:51.721680'), (27, 'Capstone', '0009_auto_20220220_2045', '2022-02-20 18:45:45.908482'), (28, 'Capstone', '0010_auto_20220306_1410', '2022-03-06 12:11:04.996583'), (29, 'Capstone', '0011_auto_20220306_1643', '2022-03-06 14:43:19.341818'), (30, 'Capstone', '0012_auto_20220306_1713', '2022-03-06 15:13:44.943932'), (31, 'Capstone', '0013_auto_20220306_2009', '2022-03-06 18:09:12.679727'), (32, 'Capstone', '0014_auto_20220306_2106', '2022-03-06 19:06:31.435600'), (33, 'Capstone', '0015_auto_20220306_2111', '2022-03-06 19:11:25.721871'), (34, 'Capstone', '0016_auto_20220306_2239', '2022-03-06 20:39:23.831568'), (35, 'Capstone', '0017_auto_20220306_2242', '2022-03-06 20:42:39.640361'), (36, 'Capstone', '0002_auto_20220307_1201', '2022-03-07 10:01:24.084057'), (37, 'Capstone', '0003_auto_20220307_1416', '2022-03-07 12:16:47.358509'), (38, 'Capstone', '0004_auto_20220307_1532', '2022-03-07 13:32:17.903012'), (39, 'Capstone', '0005_auto_20220307_1536', '2022-03-07 13:36:56.144714'), (40, 'Capstone', '0006_auto_20220307_1859', '2022-03-07 17:00:04.310410'), (41, 'Capstone', '0007_auto_20220310_2143', '2022-03-13 14:20:17.351547'), (42, 'Capstone', '0008_auto_20220313_1620', '2022-03-13 14:20:17.400505'), (43, 'Capstone', '0009_auto_20220313_2100', '2022-03-13 19:00:18.028458'), (44, 'Capstone', '0010_auto_20220322_1614', '2022-03-22 14:14:53.608705'), (45, 'Capstone', '0011_auto_20220322_1814', '2022-03-22 16:14:46.181535'), (46, 'Capstone', '0012_auto_20220322_1904', '2022-03-22 17:04:54.259655'), (47, 'Capstone', '0013_auto_20220322_1918', '2022-03-22 17:18:18.866422'), (48, 'Capstone', '0014_auto_20220326_0925', '2022-03-26 07:25:30.732984'), (49, 'Capstone', '0015_auto_20220327_1943', '2022-03-27 16:43:44.433986'), (50, 'Capstone', '0016_auto_20220327_2118', '2022-03-27 18:19:10.093687');
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'django_session'
#

DROP TABLE IF EXISTS `django_session` CASCADE;
CREATE TABLE `django_session` (
  `session_key` VARCHAR(40) CHARACTER SET utf8 NOT NULL,
  `session_data` LONGTEXT CHARACTER SET utf8 NOT NULL,
  `expire_date` DATETIME NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date`),
  UNIQUE `sqlite_autoindex_django_session_1` (`session_key`)
) ENGINE=InnoDB;

#
# Dumping data for table 'django_session'
#

LOCK TABLES `django_session` WRITE;
INSERT IGNORE INTO `django_session`(`session_key`, `session_data`, `expire_date`) VALUES('km9zqo06io8f798f8iacg49xju5zp8cf', '.eJxVjL0OwyAQg9-FuUKBhL-O3fMM6DiOkrYCKSRT1XcvkTK0i2X5s_1mHvYt-73R6pfIrkywy28WAJ9UDhAfUO6VYy3bugR-VPhJG59rpNft7P4dZGi5rweb9CAsEihJxsogjCDsosmaiaSyjtJIzgQk5fSopZ0AuwdMkQSyzxfW6zhH:1nLqyl:iWlSoyDcBBgsR_BinFjMFhy72eT8h9K9Mm3YFABGNZo', '2022-03-06 18:30:39.701921'), ('uohaksb2hnacl180j2sty37s8w8bvlwi', '.eJxVjMsOwiAQRf-FtSFlKI9x6b7fQIYyStVAUtqV8d-VpAvd3nPueYlA-5bD3ngNSxJnocXpd4s0P7h0kO5UblXOtWzrEmVX5EGbnGri5-Vw_wKZWu5ZpUE59sjaUIqkGJARcDCAqMG6YaQrKAMj6BE8W1LRMLjvy1twJN4freA2HA:1nQxmF:1IIbUga3V8Uz8mhGWJk_nLw3zpGCvSmQpB884Cvz0S8', '2022-03-20 20:46:51.311617'), ('8dri9vpx1dbcz44j4q3bem1ohor925me', '.eJxVjL0OwyAQg9-FuUKBhL-O3fMM6DiOkrYCKSRT1XcvkTK0i2X5s_1mHvYt-73R6pfIrkywy28WAJ9UDhAfUO6VYy3bugR-VPhJG59rpNft7P4dZGi5rweb9CAsEihJxsogjCDsosmaiaSyjtJIzgQk5fSopZ0AuwdMkQSyzxfW6zhH:1nQxuk:1WW6cZFua-e8CvpTTK-q-jvD96lAH8KRu7c16DeDoq8', '2022-03-20 20:55:38.163291'), ('936irmg6en3f4bgjona8s2i7y7encf3w', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1nRIPv:xpo7jJ-L-hcvR9HqAyhLBED8VrJkto3cciZy61BmIuw', '2022-03-21 18:49:11.886438'), ('rv77pxs8itp3qsqcxrr5cw5gz9fspt1x', '.eJxVjDsPgjAUhf8KuTNpaHkVR3c3NyBNaS8vsRguDMb43y0JJrqcnJzH9wKlt7VXG-GiBgsn4BD-Zo02N3R7YUftupmZ2a3L0LB9wo6W2GW2OJ2P7R-g19T7dyTbLOLSoE4F5lI0POdovGQo8wRFKgtsYyzyxmBaZHEmZKKN99q0FrnZoXck0h2Sx5VlBUqNNLtvWkEYhSINK7guwyNAO6xoA9o8g9ptmp4V1DW8P3bTUCs:1nVyV4:6qjmuNnH4R2jHh8B7ndWC7BFyOCvxODg0YKzICMcbHU', '2022-04-03 16:33:50.894237'), ('kpfd3ovm8nhbjswa12znm7lfe7d4r8aq', '.eJxVjL0OwyAQg9-FuUKBhL-O3fMM6DiOkrYCKSRT1XcvkTK0i2X5s_1mHvYt-73R6pfIrkywy28WAJ9UDhAfUO6VYy3bugR-VPhJG59rpNft7P4dZGi5rweb9CAsEihJxsogjCDsosmaiaSyjtJIzgQk5fSopZ0AuwdMkQSyzxfW6zhH:1nWe8w:UrqBT9zZEpHxTVYwvC8N4Rt74zHtL9yythUYnCcmEqw', '2022-04-05 13:01:46.068680'), ('lo1nprbpkcz1ch7ur35g55wntyr1gcbj', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1nWigX:uFAx9hZNK4z7OMffHdCcRtquSL5GjvVT4LIoyAtggks', '2022-04-05 17:52:45.502304'), ('o33yj3onip5oqzxhyfv8z9h3d9iyw7m9', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1nY0vf:5XeDxV5N1abKlEnNzXVldFwFNcx0UigvFONevgaK9tk', '2022-04-09 07:33:43.471099'), ('sr07cr6juh9iyjjabuyvbudttj62welx', '.eJxVjMsOwiAQRf-FtSFlKI9x6b7fQIYyStVAUtqV8d-VpAvd3nPueYlA-5bD3ngNSxJnocXpd4s0P7h0kO5UblXOtWzrEmVX5EGbnGri5-Vw_wKZWu5ZpUE59sjaUIqkGJARcDCAqMG6YaQrKAMj6BE8W1LRMLjvy1twJN4freA2HA:1nYC3w:1MDvj15JMqU0EwXZAtuzS8CY_7uRGyJufndB2WkBMQA', '2022-04-09 19:27:00.566842'), ('kzxt2qtvnmd60vgiilkf3n30vo6imx2u', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1nYMsA:rieVuSwCwmY4pIBQjsYZL_TQMFMAOicaMHCT02XoaVc', '2022-04-10 06:59:34.601342'), ('aevfmmyr5w0o0wwhk7zebor3h8zqb8r2', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1nYNKA:-WPheJ4rn4kWhU-Iuj6ceFIaQDuIOgm81tUwt1BPPXQ', '2022-04-10 07:28:30.657997'), ('1nusxu4sy4paxf0qh97t3jsiortt8t64', '.eJxVjEEOwiAQRe_C2hBgylBcuvcMZBhQqgaS0q6MdzckXej2v_f-WwTatxL2ntewJHEWKE6_WyR-5jpAelC9N8mtbusS5VDkQbu8tpRfl8P9OyjUy6hJM4BG5eNtTjYqiGZOjJOF7Ix2Fo32SjMBMhnjFDBkn2kyFm20KD5fz9Y2_g:1nYXGe:oAuAMeZeAbCOXz5MczWFj_6x-dNkfpmup_k5vckXCqw', '2022-04-10 18:05:32.548826'), ('0gh12x0zn2tgjzi1rwdwsp5io2or18sj', '.eJxVjLsOwjAMAP8lM4pat-TByN5viOzYIQXUSE07If4dInWA9e50LxVw33LYq6xhZnVRTp1-GWF8yNIE33G5FR3Lsq0z6Zbow1Y9FZbn9Wj_BhlrbtuuB2vAjwnQMAg4S-giWTbkUQRkdMhmIEl0ZjFmgN6J9XbsvjB59f4A6O44Hw:1nYXaA:m5CnU5leEB_mS-cSFjf2zOaFX4BLOOtbYd3KBhe3dWw', '2022-04-10 18:25:42.087603'), ('30ue0kpz813ma4f3q3r732xq7k9be8mn', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1nd9lA:ymXhSgejEheIhlXQ7Po96uhIfeSngKky3QMv9Y1h9qQ', '2022-04-23 12:00:08.585044'), ('vwp0484fvnl53z00dz1vzpv2asglwi6l', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1ndRqH:HUIBAvpAIffXt_LoD8ekyb9tEuA8DC6PVYfwzcLYGJ0', '2022-04-24 07:18:37.871255'), ('ajcatv82hvjofjfwrys9v7g2o1m9l2oy', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1ndbMF:hAAgGOuyL1HYIF1Z09jrpIQkgaok4hALw98iTqHpkBk', '2022-04-24 17:28:15.569648'), ('uijz1yuhcfzir28a7thgjze3fq21htxs', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1ndmVe:QVVt18oPjcWh7K4Jsn8yekLE6si-ZFvr1DJ5TstPqAs', '2022-04-25 05:22:42.762488'), ('mgmi67di6ee23q3zoa8v27y1jrqi58f9', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1ndyVK:1XA5apaUJmlsNJIZBT4EallB9Rde8lOPnKgmNnIsUsY', '2022-04-25 18:11:10.528573'), ('r6p2pbphpvhhc8vcfn05tnxc5o174a5s', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1ne9qu:rdqriEGiHNoOPubH6oUUM-dqI20IKKSbCfqosxaBLhk', '2022-04-26 06:18:12.412764'), ('fojxtcz9fkan28g78hmkxkjpczl9m7jx', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1neH8T:clkqR96FXMpBaWcPXNCl13eDH83T2NSEpWxiUkKLa9w', '2022-04-26 14:04:49.395608'), ('ive9xs6as5yhy4j3xdqu3f7dufhbjgka', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1neKdL:_zEo_0zSaI-yQlWOV89kAS1MwIhRsAbMNEWHb5UnVY4', '2022-04-26 17:48:55.646659'), ('ijudj7ytqm9lne7arz4dtar6ff0hv5v4', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1necus:7DmE3gSeg4Ddfuiu0UFiK0FdZ2rf4vLLNEpks6CfCIQ', '2022-04-27 13:20:14.738692'), ('4fslmabe8toghvodk4iie9gjgkzmu4a3', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1neriF:tJibW07mdHDa8_NW0CtsfXlJgSY0l5f3yBPESlXVvOE', '2022-04-28 05:08:11.120041'), ('hy5bvafs33lvo5rlw8n4ma61ylsywelb', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1ngnGk:EkpUcuphprA-1etEW2Tb64c6W4ct4h1lQl8Y2ift-G8', '2022-05-03 12:47:46.316362'), ('4wgwxvek3gb7c2oeeh1xwyzmvzucmw45', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1nk9Nm:mRMPVyIpOwUGZFvIcyFtRtNeF3oYFda0CfqW_4BV7CQ', '2022-05-12 19:00:54.643664'), ('elwu7u8wpz0hb9oinpci29o8b11znd9f', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1nl35b:HHt3--xdocbfgMRwBLXDTjC_VDfaAfq07hMDcHDFeXs', '2022-05-15 06:29:51.720211'), ('6iclcu1f6anz014euwmjsyg831c6to7u', '.eJxVjDsOwyAQBe9CHSG-BqdM7zOgXRaCkwgkY1dR7h5bcpG0b2bemwXY1hK2npYwE7syxS6_G0J8pnoAekC9Nx5bXZcZ-aHwk3Y-NUqv2-n-HRToZa-lsAq0z5iN0YNVRls0jhxKK31OgxQOgdQooyZjBcYxeWVIR4q7LTX7fAHB7Tcv:1nl3yJ:-r9MLz-JIQHmZrNhLiL3zm0V5q6QpPXWvesFh-ILbaE', '2022-05-15 07:26:23.419272'), ('t0vrj7ynbdy5moeutqk5ml1x3aqfyd74', '.eJxVjDtuwzAQRO_COhb4WVKUy_Q5A7HLXUWKDTEgJaQwfPdQgBtPOfPmPVT6xdb-SuVUpcme9nKTTV0VQV05XhgxRAIIPaOdfZg4ijakUWcfSNSHSnjsSzqa1LRyf9r3jjB34znwD27fZchl2-tKw4kMr7UNX4Xl_vli3wQLtqW_jfYWXZxpBnDBW3CeYOSRjDdxlmD0SMh2MtkxeE15kmiBXebcaePU8x-jpUvu:1nlRY4:K7dNkawyI3NUAwW26Xh4h-VR2sGfuPSMVYcWF9VwNOQ', '2022-05-16 08:36:52.133616'), ('8psff29pf2c8n4faekqpj78vkfhewdch', 'eyJfcGFzc3dvcmRfcmVzZXRfdG9rZW4iOiJiNHQ0ODEtMDg5YTFkNDQ4MmM3ZTcyYjY5NDA4N2U0NjAxYTY0NWYifQ:1nlWw8:yaTXNcTPBiRzdwvREyGRUvRZ59nQfQJ8d5NrloUOta4', '2022-05-16 14:22:04.331725'), ('dqo8arvcli3a3n6ecl9qie4n7n6gqb3f', '.eJxVjDsOwjAQRO_iGln-xD9K-pzBWnvXOIAcKU4qxN1JpBTQjea9mTeLsK01bp2WOCG7MsMuv12C_KR2AHxAu888z21dpsQPhZ-083FGet1O9--gQq_7WgMGTRgkoUqesrBe7gmplFBIKl0gWQNkvXFCDEIK0jYo6_TgfLGSfb4I0Dfd:1nqdyt:n9Z-6tYINRYAYgkuJ5C-rz9l14bOFfkmX2to8ass6ME', '2022-05-30 16:54:03.090135'), ('azakr7mfohzvv532q338mz0h27c3h7la', '.eJxVjDsOwjAQRO_iGln-xD9K-pzBWnvXOIAcKU4qxN1JpBTQjea9mTeLsK01bp2WOCG7MsMuv12C_KR2AHxAu888z21dpsQPhZ-083FGet1O9--gQq_7WgMGTRgkoUqesrBe7gmplFBIKl0gWQNkvXFCDEIK0jYo6_TgfLGSfb4I0Dfd:1nqyiG:oOVHhPfIRsB6OncvNVsA4xn1adLaBSGbOS7mT-pQbXc', '2022-05-31 15:02:16.270624'), ('zzjgkykhbh8cv58xmqjqqag9iqbkznmz', '.eJxVjDsOwjAQRO_iGln-xD9K-pzBWnvXOIAcKU4qxN1JpBTQjea9mTeLsK01bp2WOCG7MsMuv12C_KR2AHxAu888z21dpsQPhZ-083FGet1O9--gQq_7WgMGTRgkoUqesrBe7gmplFBIKl0gWQNkvXFCDEIK0jYo6_TgfLGSfb4I0Dfd:1nqykS:xMUfgiRxQgzJQ41CESYkcQYeNoeoAZ-KIQOWsK7z0g0', '2022-05-31 15:04:32.782985'), ('12z6xf9wrqi31j8a5ax7k7ow5dei1iqg', '.eJxVjEEOwiAQRe_C2pDSDlBcuvcMzcwwSNVAUtqV8e7apAvd_vfef6kJtzVPW5NlmqM6KzOq0-9IyA8pO4l3LLequZZ1mUnvij5o09ca5Xk53L-DjC1_awDgwJa9JIuWI0iI3BlOAi7h6Ggg1wmjAeM9JQ6I1AcQtENvAzr1_gA5Tzkp:1nuGif:W734DGdBaPyJnUN_ec_LhbMhnbwTEUHnTgPsEJ6TMaA', '2022-06-09 16:52:17.978896'), ('es4q4h3pn7v83azorooij2nupwb9mz0h', '.eJxVjDsOwjAQBe_iGlnxd21K-pzB2s0aHEC2FCcV4u4QKQW0b2beSyTc1pK2npc0szgLK06_G-H0yHUHfMd6a3JqdV1mkrsiD9rl2Dg_L4f7d1Cwl2-NOTiOmtEblckb4yBEsjoQsDXR-iErQADviDjQcFVAOtoYjXfB2yDeH9MxNto:1nxBnN:U0MrkmhLUWCvqTYo2iB2BPkeWNZEAxX22rNq-kGOPt0', '2022-06-17 18:13:13.495190'), ('piei0wbngrtong9m1k76s21hxoljuvpl', '.eJxVjDsOwjAQBe_iGlnxd21K-pzB2s0aHEC2FCcV4u4QKQW0b2beSyTc1pK2npc0szgLK06_G-H0yHUHfMd6a3JqdV1mkrsiD9rl2Dg_L4f7d1Cwl2-NOTiOmtEblckb4yBEsjoQsDXR-iErQADviDjQcFVAOtoYjXfB2yDeH9MxNto:1nxBoN:E3FbKBU1wtNwA6CsQPvs-U6Ay-4-0A47gMPRzqEwe9k', '2022-06-17 18:14:15.778775'), ('mv7tdd1vjwfzchg7fzi2yupdjzn7idvd', '.eJxVjDsOwjAQBe_iGln-xd5Q0nMGy95d4wBypDipEHeHSCmgfTPzXiKmba1x67zEicRZOBCn3zEnfHDbCd1Tu80S57YuU5a7Ig_a5XUmfl4O9--gpl6_NRMAsXPFBiRjPClFbL11QIm9CxBAIY4mh1w0WK-1HR2WAYYclE0k3h8TCDfs:1o1AtN:9WhWgsOSm4Efu427967gAqlk2Hv4oPxPo1CVsY210Q4', '2022-06-28 18:03:53.236680'), ('29nf22vzaoa88lisj5dti80ji08smwxx', '.eJxVjLsOwjAMAP8lM4pat-TByN5viOzYIQXUSE07If4dInWA9e50LxVw33LYq6xhZnVRTp1-GWF8yNIE33G5FR3Lsq0z6Zbow1Y9FZbn9Wj_BhlrbtuuB2vAjwnQMAg4S-giWTbkUQRkdMhmIEl0ZjFmgN6J9XbsvjB59f4A6O44Hw:1o30iF:T9c6NUjpfUqEcGGtn4tH4SCK1qq4TzCAWuyYRz3crDc', '2022-07-03 19:35:59.491714'), ('ssbz9m1505w9ldo4n6o4psbn15o3shv0', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1o9Sma:fDqbjQ9B03uJKtvMfd4FLZCOIl53yOZNOOS9ijNE8N8', '2022-07-21 14:47:08.768437'), ('iqbp7ncjdrb63ydb51wj4emlv9uosto5', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1oFfLP:0_XKTALhm78Wc7635tRKkWVCv0dB8XInctSUULDVCLo', '2022-08-07 17:24:43.793999'), ('zlo7dw1wvxn33weddk5r57fey9h5me0c', '.eJxVjLsOwjAMAP8lM4pat-TByN5viOzYIQXUSE07If4dInWA9e50LxVw33LYq6xhZnVRTp1-GWF8yNIE33G5FR3Lsq0z6Zbow1Y9FZbn9Wj_BhlrbtuuB2vAjwnQMAg4S-giWTbkUQRkdMhmIEl0ZjFmgN6J9XbsvjB59f4A6O44Hw:1oI5l4:rtcEUqRCfa4V08eLNjwYfXRcogy61kKIkdsbJd8OKjg', '2022-08-14 10:01:14.118279'), ('3n492hbxe6m1vm54cdnmoi3gnroa7f3z', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1oMNa3:daGZ3Kmhl9He5sce-l2toyR3hXu95tRJY9cT4zfaYPI', '2022-08-26 05:51:35.472366'), ('z2esmeh6cvdb12stetca14k2hj8fg8c5', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1odmoC:ud5QHNtFpFkh1_at-TOMG-hRGN8CslKNXEW-u9bWRyE', '2022-10-13 06:14:08.937499'), ('4lt0238emzheqkb7eq1ibtejsdlq0fif', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1of272:iJAZ5UiF2tGL94IhRSzt7oPgKrvApHTdTu7l-Vua7Hc', '2022-10-16 16:46:44.186453'), ('yh9l77qhdhjnlp7fxdeurbgy6lgyw21k', '.eJxVjMsOwiAQRf-FtSFTyqO4dO83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mz0OL0u0VMD647oDvWW5Op1XWZo9wVedAur434eTncv4OCvXzrYfTOQfReKQcJKGkYNBvQFply1AaznTwCWzLkM2CmUYHLGQ2liax4fwDQLzg0:1of2Bt:8EeEoGx87oX_DP_EmHE2iMh9YPYeBLIW9iaPNdcwdXk', '2022-10-16 16:51:45.754128'), ('q3f5qujkb9tlvtizre7hbtoguq8zh466', '.eJxVjDsOwjAQBe_iGlk2G_8o6TmDtWuvcQA5UpxUiLuTSCmgfTPz3iLiutS4dp7jmMVFGHH63QjTk9sO8gPbfZJpass8ktwVedAub1Pm1_Vw_w4q9rrVZbABs3VI50C2oFI5aR4IQFlOZWPFGO_BAVhPgBo1O8UKfSgqkBOfL_wjODY:1ojjI9:z4XOrMfsL77Z1Y-oMf7M_qW74XPM053Gp88ZQJCfwSg', '2022-10-29 15:41:37.499283'), ('9wht17y67xgb5phrbmqe3bs8plfcxy3a', '.eJxVjEEOwiAQAP_C2RBgy7Z49N43NMsulaqhSWlPxr8bkh70OjOZt5ro2PN01LRNi6ir6oK6_MJI_EylGXlQua-a17JvS9Qt0aetelwlvW5n-zfIVHP7mm4eGCOTNY4G8TgHxoAEzN6j71OKBrAD8SROaKBIaMBaCGB6cerzBRNMN_o:1ok6EH:vgB-LEjCuODNFUjVCVrtallRM8zGv-X_j6GCNQd-xlA', '2022-10-30 16:11:09.012441'), ('db0whlycwiyje2svvq836z0bzisqn2vq', '.eJxVjDsOwjAQBe_iGlk2G_8o6TmDtWuvcQA5UpxUiLuTSCmgfTPz3iLiutS4dp7jmMVFGHH63QjTk9sO8gPbfZJpass8ktwVedAub1Pm1_Vw_w4q9rrVZbABs3VI50C2oFI5aR4IQFlOZWPFGO_BAVhPgBo1O8UKfSgqkBOfL_wjODY:1oqTPS:zBFS6_FS7xq1nfGCUx0yCUO6iJPWQX0Jnf_Nll34_6M', '2022-11-17 06:09:02.790735'), ('sq7fadjly3uh4oztva6q5tba218wiqz4', '.eJxVjDsOwjAQBe_iGlk2G_8o6TmDtWuvcQA5UpxUiLuTSCmgfTPz3iLiutS4dp7jmMVFGHH63QjTk9sO8gPbfZJpass8ktwVedAub1Pm1_Vw_w4q9rrVZbABs3VI50C2oFI5aR4IQFlOZWPFGO_BAVhPgBo1O8UKfSgqkBOfL_wjODY:1pJXGS:6vrsVonS0gy7AwP8XyBfkHBdg4AAeUmxM3BY5Pl4xL0', '2023-02-05 10:07:52.652430'), ('64mcchynbg6bppsq2amyvzurro2qxpj1', '.eJxVjEEOwiAQRe_C2hCg7Qy4dN8zEJgZpWpoUtqV8e7apAvd_vfef6mYtrXErckSJ1ZnBahOv2NO9JC6E76neps1zXVdpqx3RR-06XFmeV4O9--gpFa-tRPnyRvGMLBYz72xnSfXw9UQIDnHQ0YRFGMBRCgAGEy5CyFRIEL1_gABZTgg:1qSh6a:oO7g25bkv3K1I0Dzirz8lPzwKYLBrj3zhtB-HaXKQzk', '2023-08-20 16:59:48.422722');
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

#
# Table structure for table 'sqlite_sequence'
#

DROP TABLE IF EXISTS `sqlite_sequence` CASCADE;
CREATE TABLE `sqlite_sequence` (
  `name` LONGTEXT CHARACTER SET utf8,
  `seq` LONGTEXT CHARACTER SET utf8
) ENGINE=InnoDB;

#
# Dumping data for table 'sqlite_sequence'
#

LOCK TABLES `sqlite_sequence` WRITE;
INSERT IGNORE INTO `sqlite_sequence`(`name`, `seq`) VALUES('django_migrations', 90), ('django_content_type', 14), ('auth_permission', 56), ('auth_group', 0), ('django_admin_log', 46), ('Capstone_route_thepassenger', 1816), ('Capstone_comment_lists', 155), ('Capstone_comment', 155), ('Capstone_message', 43), ('Capstone_message_recipient', 44), ('Capstone_qrcode_trip', 270), ('Capstone_qrcode', 280), ('cookie_consent_cookie', 5), ('cookie_consent_cookiegroup', 3), ('cookie_consent_logitem', 26), ('Capstone_route', 128), ('Capstone_user', 67);
ALTER TABLE `Capstone_route` MODIFY `date_orig` DATE NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_orig` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `time_dep` TIME NOT NULL;
ALTER TABLE `Capstone_route` MODIFY `date_ret` DATE NOT NULL;
ALTER TABLE `Capstone_user` MODIFY `dob` DATE NOT NULL;
UNLOCK TABLES;

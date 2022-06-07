/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50096
 Source Host           : localhost:3306
 Source Schema         : keyfallblog

 Target Server Type    : MySQL
 Target Server Version : 50096
 File Encoding         : 65001

 Date: 07/06/2022 08:37:12
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article_tag
-- ----------------------------
DROP TABLE IF EXISTS `article_tag`;
CREATE TABLE `article_tag`  (
  `blog_id` int(11) NOT NULL,
  `tag.id` int(11) NOT NULL,
  PRIMARY KEY USING BTREE (`blog_id`, `tag.id`),
  INDEX `tag.id` USING BTREE(`tag.id`),
  CONSTRAINT `article_tag_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `article_tag_ibfk_2` FOREIGN KEY (`tag.id`) REFERENCES `tag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'InnoDB free: 11264 kB; (`blog_id`) REFER `keyfallblog/blog`(`id`); (`tag.id`) RE' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of article_tag
-- ----------------------------
INSERT INTO `article_tag` VALUES (1, 1);
INSERT INTO `article_tag` VALUES (3, 1);
INSERT INTO `article_tag` VALUES (5, 1);
INSERT INTO `article_tag` VALUES (1, 2);
INSERT INTO `article_tag` VALUES (4, 2);

-- ----------------------------
-- Table structure for blog
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blogname` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` varchar(5000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` date NOT NULL,
  `update_time` date NOT NULL,
  `image_url` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `stars` int(11) NOT NULL,
  `sort_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`),
  INDEX `sort_id` USING BTREE(`sort_id`),
  CONSTRAINT `blog_ibfk_1` FOREIGN KEY (`sort_id`) REFERENCES `sort` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'InnoDB free: 11264 kB; (`sort_id`) REFER `keyfallblog/sort`(`id`)' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of blog
-- ----------------------------
INSERT INTO `blog` VALUES (1, '第一篇', '早上都发你无法', '2022-05-23', '2022-05-23', NULL, 10, 1);
INSERT INTO `blog` VALUES (2, '第二篇', '序偶培训拿出来烧烤店覅', '2022-05-23', '2022-05-23', NULL, 20, 2);
INSERT INTO `blog` VALUES (3, '第三篇', '早上都发你无法', '2022-05-23', '2022-05-23', NULL, 10, 1);
INSERT INTO `blog` VALUES (4, '第四篇', '早上都发你无法', '2022-05-23', '2022-05-23', NULL, 10, 1);
INSERT INTO `blog` VALUES (5, '第五篇', '早上都发你无法', '2022-05-23', '2022-05-23', NULL, 10, 2);
INSERT INTO `blog` VALUES (6, '第六篇', '早上都发你无法', '2022-05-23', '2022-05-23', NULL, 10, 2);
INSERT INTO `blog` VALUES (7, '第七篇', '早上都发你无法', '2022-05-23', '2022-05-23', NULL, 10, NULL);

-- ----------------------------
-- Table structure for sort
-- ----------------------------
DROP TABLE IF EXISTS `sort`;
CREATE TABLE `sort`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sort
-- ----------------------------
INSERT INTO `sort` VALUES (1, 'java');
INSERT INTO `sort` VALUES (2, 'python');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES (1, 'java');
INSERT INTO `tag` VALUES (2, 'pyahon');

SET FOREIGN_KEY_CHECKS = 1;

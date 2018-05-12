-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2018 at 12:09 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `erp`
--
CREATE DATABASE IF NOT EXISTS `erp` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `erp`;

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('9342c8481a6d20acbfeec5b5bb84c4f87a8dd95d', '2018-05-07 06:21:27.749883', 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add Token', 7, 'add_token'),
(20, 'Can change Token', 7, 'change_token'),
(21, 'Can delete Token', 7, 'delete_token'),
(22, 'Can add state', 8, 'add_state'),
(23, 'Can change state', 8, 'change_state'),
(24, 'Can delete state', 8, 'delete_state'),
(25, 'Can add state', 9, 'add_state'),
(26, 'Can change state', 9, 'change_state'),
(27, 'Can delete state', 9, 'delete_state'),
(28, 'Can add company', 10, 'add_company'),
(29, 'Can change company', 10, 'change_company'),
(30, 'Can delete company', 10, 'delete_company'),
(31, 'Can add company branch', 11, 'add_companybranch'),
(32, 'Can change company branch', 11, 'change_companybranch'),
(33, 'Can delete company branch', 11, 'delete_companybranch'),
(34, 'Can add storage location', 12, 'add_storagelocation'),
(35, 'Can change storage location', 12, 'change_storagelocation'),
(36, 'Can delete storage location', 12, 'delete_storagelocation'),
(37, 'Can add uom', 13, 'add_uom'),
(38, 'Can change uom', 13, 'change_uom'),
(39, 'Can delete uom', 13, 'delete_uom'),
(40, 'Can add storage bin', 14, 'add_storagebin'),
(41, 'Can change storage bin', 14, 'change_storagebin'),
(42, 'Can delete storage bin', 14, 'delete_storagebin'),
(43, 'Can add purchase org', 15, 'add_purchaseorg'),
(44, 'Can change purchase org', 15, 'change_purchaseorg'),
(45, 'Can delete purchase org', 15, 'delete_purchaseorg'),
(46, 'Can add purchase group', 16, 'add_purchasegroup'),
(47, 'Can change purchase group', 16, 'change_purchasegroup'),
(48, 'Can delete purchase group', 16, 'delete_purchasegroup'),
(49, 'Can add purchase org mapping', 17, 'add_purchaseorgmapping'),
(50, 'Can change purchase org mapping', 17, 'change_purchaseorgmapping'),
(51, 'Can delete purchase org mapping', 17, 'delete_purchaseorgmapping'),
(52, 'Can add sales org', 18, 'add_salesorg'),
(53, 'Can change sales org', 18, 'change_salesorg'),
(54, 'Can delete sales org', 18, 'delete_salesorg'),
(55, 'Can add sales group', 19, 'add_salesgroup'),
(56, 'Can change sales group', 19, 'change_salesgroup'),
(57, 'Can delete sales group', 19, 'delete_salesgroup'),
(58, 'Can add material type', 20, 'add_materialtype'),
(59, 'Can change material type', 20, 'change_materialtype'),
(60, 'Can delete material type', 20, 'delete_materialtype'),
(61, 'Can add material', 21, 'add_material'),
(62, 'Can change material', 21, 'change_material'),
(63, 'Can delete material', 21, 'delete_material'),
(64, 'Can add material_uom', 22, 'add_material_uom'),
(65, 'Can change material_uom', 22, 'change_material_uom'),
(66, 'Can delete material_uom', 22, 'delete_material_uom'),
(67, 'Can add material_ tax', 23, 'add_material_tax'),
(68, 'Can change material_ tax', 23, 'change_material_tax'),
(69, 'Can delete material_ tax', 23, 'delete_material_tax'),
(70, 'Can add material purchase group', 24, 'add_materialpurchasegroup'),
(71, 'Can change material purchase group', 24, 'change_materialpurchasegroup'),
(72, 'Can delete material purchase group', 24, 'delete_materialpurchasegroup'),
(73, 'Can add material purchase org', 25, 'add_materialpurchaseorg'),
(74, 'Can change material purchase org', 25, 'change_materialpurchaseorg'),
(75, 'Can delete material purchase org', 25, 'delete_materialpurchaseorg'),
(76, 'Can add material type', 26, 'add_materialtype'),
(77, 'Can change material type', 26, 'change_materialtype'),
(78, 'Can delete material type', 26, 'delete_materialtype'),
(79, 'Can add material', 27, 'add_material'),
(80, 'Can change material', 27, 'change_material'),
(81, 'Can delete material', 27, 'delete_material'),
(82, 'Can add material purchase org', 28, 'add_materialpurchaseorg'),
(83, 'Can change material purchase org', 28, 'change_materialpurchaseorg'),
(84, 'Can delete material purchase org', 28, 'delete_materialpurchaseorg'),
(85, 'Can add material purchase group', 29, 'add_materialpurchasegroup'),
(86, 'Can change material purchase group', 29, 'change_materialpurchasegroup'),
(87, 'Can delete material purchase group', 29, 'delete_materialpurchasegroup'),
(88, 'Can add material_ tax', 30, 'add_material_tax'),
(89, 'Can change material_ tax', 30, 'change_material_tax'),
(90, 'Can delete material_ tax', 30, 'delete_material_tax'),
(91, 'Can add material_uom', 31, 'add_material_uom'),
(92, 'Can change material_uom', 31, 'change_material_uom'),
(93, 'Can delete material_uom', 31, 'delete_material_uom');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$Fl6VEi8tjRSg$ogKAZQz6E30gV8vfc3KgtxKxx50nVhSWaCqGZaPMYaM=', '2018-05-10 09:13:54.216094', 1, 'suraj', 'Suraj', 'Mondal', 'surajmondal1003@gmail.com', 1, 1, '2018-05-07 06:17:19.000000'),
(2, 'pbkdf2_sha256$100000$dr3E2mYUARMQ$wZK5AqDg5BDnR6ZUPrP59cAReynJFeXifJVO/wFTFck=', NULL, 1, 'tonmoy', 'Tonmoy', 'Sardar', 'tonmoy@gmail.com', 1, 1, '2018-05-11 07:26:48.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `company_branch_companybranch`
--

DROP TABLE IF EXISTS `company_branch_companybranch`;
CREATE TABLE `company_branch_companybranch` (
  `id` int(11) NOT NULL,
  `branch_name` varchar(100) NOT NULL,
  `branch_address` varchar(100) NOT NULL,
  `branch_city` varchar(100) NOT NULL,
  `branch_pincode` varchar(50) NOT NULL,
  `branch_contact_no` bigint(20) NOT NULL,
  `branch_email` varchar(50) NOT NULL,
  `branch_gstin` varchar(50) NOT NULL,
  `branch_pan` varchar(50) NOT NULL,
  `branch_cin` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `branch_state_id` int(11) DEFAULT NULL,
  `company_id` int(11) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company_branch_companybranch`
--

INSERT INTO `company_branch_companybranch` (`id`, `branch_name`, `branch_address`, `branch_city`, `branch_pincode`, `branch_contact_no`, `branch_email`, `branch_gstin`, `branch_pan`, `branch_cin`, `status`, `created_at`, `branch_state_id`, `company_id`, `created_by_id`) VALUES
(1, 'MATLA BDS BRIDGE 22', 'EN 32, Salt lake, Sector V, Kolkata', 'Kolkata1', '741258', 9874854710, 'unit001@gmail.com', 'gstin000in1123', 'aedk8546', 'cin456852', 1, '2018-05-07 13:32:01.927332', 1, 6, 1),
(2, 'sd2', 'Kolkata', 'Kolakta', '700091', 1234567, 'as@sadas.com', 'casdf', 'asdas', 'asdas', 1, '2018-05-09 06:31:03.011008', 1, 6, 1),
(3, 'abc', 'aasdasd', 'asdas', 'sad', 345634534, 'sds@ASa.com', 'asdsa', 'asd', 'asd', 1, '2018-05-09 07:49:15.029785', 2, 6, 1),
(4, 'ASD', 'zdxczx', 'dsf', 'sdf', 21312312, 'sd@sdwd.com', 'sdf', 'sdfsd', 'sdfs', 1, '2018-05-09 09:19:19.577577', 1, 1, 1),
(5, 'Test', 'lorem ipsum', 'kolkata', '700091', 3333333, 'test@gmail.com', '355', '35535', '6666', 1, '2018-05-11 11:44:35.867532', 1, 9, 1),
(6, 'Test45', 'Lorem ipsum', 'kolkata', '700091', 333333, 'test@gmail.com', '222222', 'g4654', 'fdgt34346', 1, '2018-05-11 12:52:31.143278', 1, 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `company_branch_storagebin`
--

DROP TABLE IF EXISTS `company_branch_storagebin`;
CREATE TABLE `company_branch_storagebin` (
  `id` int(11) NOT NULL,
  `bin_no` varchar(100) NOT NULL,
  `bin_volume` decimal(10,2) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `branch_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `storage_id` int(11) NOT NULL,
  `uom_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company_branch_storagebin`
--

INSERT INTO `company_branch_storagebin` (`id`, `bin_no`, `bin_volume`, `status`, `created_at`, `branch_id`, `company_id`, `created_by_id`, `storage_id`, `uom_id`) VALUES
(1, 'B001', '100.00', 1, '2018-05-08 09:20:59.730492', 1, 1, 1, 1, 1),
(2, 'B001', '250.00', 1, '2018-05-08 09:22:45.303971', 1, 6, 1, 1, 2),
(3, 'B002', '312.00', 1, '2018-05-09 10:13:20.637822', 4, 1, 1, 2, 1),
(4, 'B003', '121.00', 1, '2018-05-09 10:17:59.357343', 4, 1, 1, 1, 1),
(5, 'B004', '312.00', 1, '2018-05-09 10:32:46.479061', 4, 1, 1, 3, 3),
(6, 'B005', '312.00', 1, '2018-05-09 10:32:55.951014', 4, 1, 1, 3, 3),
(7, 'B006', '1212.00', 1, '2018-05-09 10:33:43.095941', 4, 1, 1, 1, 2),
(8, '111', '222233.00', 1, '2018-05-11 13:09:17.429466', 6, 8, 1, 4, 1),
(9, '11111111', '3333.00', 1, '2018-05-12 07:24:13.909431', 6, 8, 1, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `company_branch_storagelocation`
--

DROP TABLE IF EXISTS `company_branch_storagelocation`;
CREATE TABLE `company_branch_storagelocation` (
  `id` int(11) NOT NULL,
  `storage_address` varchar(100) NOT NULL,
  `storage_city` varchar(50) NOT NULL,
  `storage_pincode` varchar(50) NOT NULL,
  `storage_contact_no` bigint(20) NOT NULL,
  `storage_email` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `branch_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `storage_state_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company_branch_storagelocation`
--

INSERT INTO `company_branch_storagelocation` (`id`, `storage_address`, `storage_city`, `storage_pincode`, `storage_contact_no`, `storage_email`, `status`, `created_at`, `branch_id`, `company_id`, `created_by_id`, `storage_state_id`) VALUES
(1, '19/1/17 nabin Chandra das road', 'Kolkata', '700090', 9088856113, 'abcdsa@gmail.com', 1, '2018-05-08 07:21:22.472833', 1, 1, 1, 1),
(2, 'sd sdfsd', 'sdfsd', 'sdfsd', 234234, 'aa@asas.com', 1, '2018-05-09 09:36:35.043212', 4, 1, 1, 2),
(3, 'fvvs wetw', 'werwe', 'werew', 3423432432, 'saas@dfds.com', 1, '2018-05-09 09:38:08.525069', 4, 1, 1, 2),
(4, 'Lorem ipsum', 'kolkata', '700091', 435, 'sss@ff.lk', 1, '2018-05-11 13:08:52.369441', 6, 8, 1, 1),
(5, 'lorem ipsum', 'kolkata', '700091', 123456, 'test@gmail.com', 1, '2018-05-12 05:03:00.256494', 6, 8, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `company_branch_uom`
--

DROP TABLE IF EXISTS `company_branch_uom`;
CREATE TABLE `company_branch_uom` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company_branch_uom`
--

INSERT INTO `company_branch_uom` (`id`, `name`) VALUES
(1, 'PCS'),
(2, 'KG'),
(3, 'CFT'),
(4, 'BAG'),
(5, 'SET'),
(6, 'SQMT');

-- --------------------------------------------------------

--
-- Table structure for table `company_company`
--

DROP TABLE IF EXISTS `company_company`;
CREATE TABLE `company_company` (
  `id` int(11) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `company_url` varchar(200) NOT NULL,
  `company_gst` varchar(50) NOT NULL,
  `company_pan` varchar(50) NOT NULL,
  `company_cin` varchar(50) NOT NULL,
  `company_email` varchar(50) NOT NULL,
  `company_address` varchar(100) NOT NULL,
  `company_contact` bigint(20) NOT NULL,
  `company_city` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `company_state_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `company_pin` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company_company`
--

INSERT INTO `company_company` (`id`, `company_name`, `company_url`, `company_gst`, `company_pan`, `company_cin`, `company_email`, `company_address`, `company_contact`, `company_city`, `status`, `created_at`, `company_state_id`, `created_by_id`, `parent_id`, `company_pin`) VALUES
(1, 'Shyam Steel Industries Limited', 'http://www.shyamsteel.com', '19AAAAA0000A1Z5', 'AAAAA0000A', '15425142ASD', 'contact@shyamsteel.com', 'EN 32, Salt lake, Sector V,  Kolkata-700091', 40074007, 'Kolkata', 1, '2018-05-07 10:21:30.251618', 1, NULL, NULL, '700091'),
(6, 'Shyam Futuretech', 'http://shyamfuture.com/', '19AAAAA00001Z6', 'EAAAA0000', 'CIN78956485', 'future@gmail.com', 'EN 32, Saltlake, Sector V, Kolkata', 8013134344, 'Kolkata', 1, '2018-05-07 10:48:08.514666', 1, 1, 1, '700091'),
(8, 'Shyam Sree Infra', 'http://shyamshreeInfra.com', '19AAAAA00001Z9', 'EAAAA0001', 'CIN78956489', 'triveni@gmail.com', 'Shyam Towers, EN 32, Sector V, Salt Lake, Kolkata700091', 400789574, 'Kolkata', 1, '2018-05-07 12:59:49.390925', 1, 1, 1, '700091'),
(9, 'Shyam Sree ABC', 'http://shyamshreeInfra.com', '19AAAAA00001Z9', 'EAAAA0001', 'CIN78956489', 'triveni@gmail.com', 'Shyam Towers, EN 32, Sector V, Salt Lake, Kolkata700091', 40078957, 'Kolkata', 1, '2018-05-08 11:25:25.595551', 1, 1, 1, '700091'),
(10, 'Shyam Sree BCD', 'http://shyamshreeInfra.com', '19AAAAA00001Z9', 'EAAAA0001', 'CIN78956489', 'triveni@gmail.com', 'Shyam Towers, EN 32, Sector V, Salt Lake, Kolkata700091', 40078957, 'Kolkata', 1, '2018-05-08 11:26:48.432566', 1, 1, 6, '700091'),
(11, 'Shyam Sree ghc', 'http://shyamshreeInfra.com', '19AAAAA00001Z9', 'EAAAA0001', 'CIN78956489', 'triveni@gmail.com', 'Shyam Towers, EN 32, Sector V, Salt Lake, Kolkata700091', 40078957, 'Kolkata', 1, '2018-05-08 11:27:09.934224', 1, 1, 9, '700091'),
(12, 'Shyam Sree XYZ', 'http://shyamshreeInfra.com', '19AAAAA00001Z9', 'EAAAA0001', 'CIN78956489', 'triveni@gmail.com', 'Shyam Towers, EN 32, Sector V, Salt Lake, Kolkata700091', 40078957, 'Kolkata', 1, '2018-05-08 11:27:18.027484', 1, 1, 9, '700091'),
(13, 'hjkhlk', 'http://erp.shyamfuture.com/admin/add-item', '19AAAAA0000A1Z5', 'AAAAA0000A', '15425142ASD', 'contact@shyamsteel.com', 'EN 32, Salt lake, Sector V,  Kolkata-700091', 201423569, 'Kolkata', 1, '2018-05-11 07:19:48.520561', 1, 1, 10, '700091'),
(14, 'JKL', 'http://shyamshreeInfra.com', '19AAAAA00001Z9', 'EAAAA0001', 'CIN78956489', 'triveni@gmail.com', 'Shyam Towers, EN 32, Sector V, Salt Lake, Kolkata700091', 40078957, 'Kolkata', 1, '2018-05-11 07:28:49.974523', 1, 1, 9, '700091'),
(20, 'Test', 'http://www.v.com', '143432', '3dff', 'dsf3525', 'sfs@dd.nm', 'sarwqrwr', 222222, 'rtt', 1, '2018-05-12 08:56:50.153033', 2, 1, 1, 'gg233');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2018-05-07 06:21:14.735108', '1', 'suraj', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1),
(2, '2018-05-07 07:03:35.738139', '1', 'suraj', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]', 4, 1),
(3, '2018-05-07 08:37:39.680592', '3', 'State object (3)', 3, '', 9, 1),
(4, '2018-05-07 08:40:19.259616', '4', 'State object (4)', 3, '', 9, 1),
(5, '2018-05-07 08:41:13.718970', '5', 'State object (5)', 3, '', 9, 1),
(6, '2018-05-07 10:21:30.258434', '1', 'Shyam Steel Industries Limited', 1, '[{\"added\": {}}]', 10, 1),
(7, '2018-05-07 10:41:52.028326', '2', 'Shyam Futuretech', 3, '', 10, 1),
(8, '2018-05-07 10:43:49.786419', '3', 'Shyam Futuretech', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 10, 1),
(9, '2018-05-07 10:45:42.865107', '3', 'Shyam Futuretech', 3, '', 10, 1),
(10, '2018-05-07 10:46:41.425149', '4', 'Shyam Futuretech', 3, '', 10, 1),
(11, '2018-05-07 10:48:05.545148', '5', 'Shyam Futuretech', 3, '', 10, 1),
(12, '2018-05-07 12:52:59.258649', '1', 'Shyam Steel Industries Limited', 2, '[{\"changed\": {\"fields\": [\"company_pin\"]}}]', 10, 1),
(13, '2018-05-07 12:53:07.364067', '6', 'Shyam Futuretech', 2, '[{\"changed\": {\"fields\": [\"company_pin\"]}}]', 10, 1),
(14, '2018-05-07 12:59:30.460959', '7', 'Shyam Sree Infra', 3, '', 10, 1),
(15, '2018-05-08 09:20:59.746122', '1', 'MATLA BDS BRIDGE', 1, '[{\"added\": {}}]', 14, 1),
(16, '2018-05-10 05:33:30.154634', '5', 'Suraj Organization', 3, '', 17, 1),
(17, '2018-05-10 05:33:30.199993', '4', 'Suraj Organization', 3, '', 17, 1),
(18, '2018-05-10 05:33:30.222631', '3', 'Suraj Organization', 3, '', 17, 1),
(19, '2018-05-10 05:33:30.250161', '2', 'Suraj Organization 1', 3, '', 17, 1),
(20, '2018-05-10 05:33:30.260717', '1', 'Suraj Organization', 3, '', 17, 1),
(21, '2018-05-10 05:48:03.749022', '7', 'Suraj Organization', 3, '', 17, 1),
(22, '2018-05-10 05:48:03.780423', '6', 'Suraj Organization', 3, '', 17, 1),
(23, '2018-05-10 07:26:00.183956', '10', 'Suraj Organization', 3, '', 17, 1),
(24, '2018-05-10 07:26:00.216830', '9', 'Suraj Organization', 3, '', 17, 1),
(25, '2018-05-10 07:31:53.083337', '11', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(26, '2018-05-10 07:32:03.328915', '12', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(27, '2018-05-10 08:49:42.947141', '13', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(28, '2018-05-10 08:53:30.624577', '14', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(29, '2018-05-10 08:53:38.497455', '15', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(30, '2018-05-10 08:53:47.312636', '16', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(31, '2018-05-10 08:53:53.778943', '17', 'Suraj Organization 1', 1, '[{\"added\": {}}]', 17, 1),
(32, '2018-05-10 08:54:00.241667', '18', 'Suraj Organization 1', 1, '[{\"added\": {}}]', 17, 1),
(33, '2018-05-10 08:57:04.350831', '19', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(34, '2018-05-10 08:57:09.926108', '20', 'Suraj Organization', 1, '[{\"added\": {}}]', 17, 1),
(35, '2018-05-10 08:57:15.891444', '21', 'Suraj Organization 1', 1, '[{\"added\": {}}]', 17, 1),
(36, '2018-05-11 07:19:48.567442', '13', 'hjkhlk', 1, '[{\"added\": {}}]', 10, 1),
(37, '2018-05-11 07:20:03.275773', '13', 'hjkhlk', 2, '[{\"changed\": {\"fields\": [\"created_by\"]}}]', 10, 1),
(38, '2018-05-11 07:26:48.729567', '2', 'tonmoy', 1, '[{\"added\": {}}]', 4, 1),
(39, '2018-05-11 07:27:32.364302', '2', 'tonmoy', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"is_staff\", \"is_superuser\"]}}]', 4, 1),
(40, '2018-05-11 09:23:45.798625', '1', '<class \'django.db.models.fields.CharField\'>', 3, '', 21, 1),
(41, '2018-05-11 09:28:14.663823', '2', '<class \'django.db.models.fields.CharField\'>', 3, '', 21, 1),
(42, '2018-05-12 07:42:54.239589', '4', 'Mouse', 2, '[{\"changed\": {\"fields\": [\"material_for\"]}}]', 31, 1),
(43, '2018-05-12 07:43:16.470129', '5', 'Chair', 2, '[{\"changed\": {\"fields\": [\"material_for\"]}}]', 31, 1),
(44, '2018-05-12 07:46:26.287573', '5', 'Chair', 2, '[{\"changed\": {\"fields\": [\"tax_for\"]}}]', 30, 1),
(45, '2018-05-12 07:46:36.541434', '5', 'Chair', 2, '[]', 31, 1),
(46, '2018-05-12 08:51:55.549012', '18', 'fdgfdh', 3, '', 10, 1),
(47, '2018-05-12 08:51:55.587066', '17', 'Test23', 3, '', 10, 1),
(48, '2018-05-12 08:51:55.611456', '16', 'Test', 3, '', 10, 1),
(49, '2018-05-12 08:51:55.636303', '15', 'ASDas', 3, '', 10, 1),
(50, '2018-05-12 08:56:17.970072', '19', 'Test', 3, '', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(8, 'authentication', 'state'),
(7, 'authtoken', 'token'),
(10, 'company', 'company'),
(11, 'company_branch', 'companybranch'),
(14, 'company_branch', 'storagebin'),
(12, 'company_branch', 'storagelocation'),
(13, 'company_branch', 'uom'),
(5, 'contenttypes', 'contenttype'),
(21, 'material', 'material'),
(24, 'material', 'materialpurchasegroup'),
(25, 'material', 'materialpurchaseorg'),
(20, 'material', 'materialtype'),
(23, 'material', 'material_tax'),
(22, 'material', 'material_uom'),
(27, 'material_master', 'material'),
(29, 'material_master', 'materialpurchasegroup'),
(28, 'material_master', 'materialpurchaseorg'),
(26, 'material_master', 'materialtype'),
(30, 'material_master', 'material_tax'),
(31, 'material_master', 'material_uom'),
(16, 'purchaseorggroup', 'purchasegroup'),
(15, 'purchaseorggroup', 'purchaseorg'),
(17, 'purchaseorggroup', 'purchaseorgmapping'),
(19, 'salesorg_group', 'salesgroup'),
(18, 'salesorg_group', 'salesorg'),
(6, 'sessions', 'session'),
(9, 'states', 'state');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-05-07 06:03:19.144091'),
(2, 'auth', '0001_initial', '2018-05-07 06:03:22.488078'),
(3, 'admin', '0001_initial', '2018-05-07 06:03:23.253900'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-05-07 06:03:23.316294'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-05-07 06:03:23.785157'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-05-07 06:03:24.066550'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-05-07 06:03:24.425788'),
(8, 'auth', '0004_alter_user_username_opts', '2018-05-07 06:03:24.488298'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-05-07 06:03:24.691601'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-05-07 06:03:24.722693'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-05-07 06:03:24.769572'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-05-07 06:03:25.613634'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-05-07 06:03:26.160535'),
(14, 'authtoken', '0001_initial', '2018-05-07 06:03:26.598085'),
(15, 'authtoken', '0002_auto_20160226_1747', '2018-05-07 06:03:26.957480'),
(16, 'sessions', '0001_initial', '2018-05-07 06:03:27.426137'),
(17, 'authentication', '0001_initial', '2018-05-07 07:03:02.739599'),
(18, 'authentication', '0002_delete_state', '2018-05-07 07:44:00.428173'),
(19, 'states', '0001_initial', '2018-05-07 07:44:00.557777'),
(20, 'states', '0002_state_user', '2018-05-07 08:09:31.431104'),
(21, 'states', '0003_auto_20180507_1503', '2018-05-07 09:33:31.623835'),
(22, 'company', '0001_initial', '2018-05-07 09:38:15.296433'),
(23, 'states', '0004_auto_20180507_1508', '2018-05-07 09:38:15.358783'),
(24, 'states', '0005_auto_20180507_1513', '2018-05-07 09:43:04.746867'),
(25, 'states', '0006_auto_20180507_1514', '2018-05-07 09:44:06.407747'),
(26, 'company', '0002_company_parent', '2018-05-07 09:55:26.896929'),
(27, 'company', '0003_auto_20180507_1615', '2018-05-07 10:45:14.513751'),
(28, 'company', '0004_auto_20180507_1616', '2018-05-07 10:46:15.246079'),
(29, 'company', '0005_company_company_pin', '2018-05-07 12:52:39.894224'),
(30, 'company', '0006_auto_20180507_1824', '2018-05-07 12:54:47.051392'),
(31, 'company_branch', '0001_initial', '2018-05-07 13:13:03.040391'),
(32, 'company_branch', '0002_storagelocation', '2018-05-08 06:57:07.544737'),
(33, 'company_branch', '0003_auto_20180508_1425', '2018-05-08 08:55:23.568528'),
(34, 'company_branch', '0004_auto_20180508_1448', '2018-05-08 09:18:10.455950'),
(35, 'purchaseorggroup', '0001_initial', '2018-05-09 11:02:56.681898'),
(36, 'purchaseorggroup', '0002_purchaseorgmapping', '2018-05-09 11:35:36.762183'),
(37, 'purchaseorggroup', '0003_auto_20180509_1712', '2018-05-09 11:42:21.442694'),
(38, 'company_branch', '0005_auto_20180509_1743', '2018-05-09 12:13:56.242348'),
(39, 'salesorg_group', '0001_initial', '2018-05-09 12:44:01.869472'),
(40, 'material', '0001_initial', '2018-05-11 05:55:30.170298'),
(41, 'material', '0002_auto_20180511_1128', '2018-05-11 05:59:01.858619'),
(42, 'material', '0003_auto_20180511_1140', '2018-05-11 06:10:58.634302'),
(43, 'material', '0004_material', '2018-05-11 06:16:51.102951'),
(44, 'material', '0005_material_tax_material_uom', '2018-05-11 06:47:40.866721'),
(45, 'material', '0006_auto_20180511_1225', '2018-05-11 06:55:24.335388'),
(46, 'material', '0007_auto_20180511_1240', '2018-05-11 07:10:51.555486'),
(47, 'material', '0008_remove_material_created_by', '2018-05-11 09:10:34.823405'),
(48, 'material_master', '0001_initial', '2018-05-11 10:11:26.490010'),
(49, 'material_master', '0002_material_is_sales', '2018-05-11 12:30:34.572454');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1f9vmjnc9pq54mra86i70upzf1hns42k', 'MDkzNTdjOWE4NGFhZTU4MmFlYjY3YTE0NTcyZjI0NDhlZGU0YTkyYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NjMyYTZkNDBlODNmNWU4MmNjMzgxODJhZWMzM2ZlMzg2MjQyYjAzIn0=', '2018-05-24 05:47:27.865712'),
('c9ajjtgbkzfh3nj0j8cnanq5ezmf0qzz', 'MDkzNTdjOWE4NGFhZTU4MmFlYjY3YTE0NTcyZjI0NDhlZGU0YTkyYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NjMyYTZkNDBlODNmNWU4MmNjMzgxODJhZWMzM2ZlMzg2MjQyYjAzIn0=', '2018-05-22 06:58:32.567901'),
('gcuadg3e1s4nhrtqqak016twi5e4565l', 'MDkzNTdjOWE4NGFhZTU4MmFlYjY3YTE0NTcyZjI0NDhlZGU0YTkyYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NjMyYTZkNDBlODNmNWU4MmNjMzgxODJhZWMzM2ZlMzg2MjQyYjAzIn0=', '2018-05-22 09:20:27.021209'),
('im9prxie6rzegvnrf5ijammbqsi059zh', 'MDkzNTdjOWE4NGFhZTU4MmFlYjY3YTE0NTcyZjI0NDhlZGU0YTkyYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NjMyYTZkNDBlODNmNWU4MmNjMzgxODJhZWMzM2ZlMzg2MjQyYjAzIn0=', '2018-05-24 09:13:54.247871');

-- --------------------------------------------------------

--
-- Table structure for table `material_master_material`
--

DROP TABLE IF EXISTS `material_master_material`;
CREATE TABLE `material_master_material` (
  `id` int(11) NOT NULL,
  `material_fullname` varchar(100) NOT NULL,
  `material_code` varchar(25) NOT NULL,
  `description` longtext NOT NULL,
  `is_taxable` tinyint(1) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `material_type_id` int(11) DEFAULT NULL,
  `is_sales` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `material_master_material`
--

INSERT INTO `material_master_material` (`id`, `material_fullname`, `material_code`, `description`, `is_taxable`, `status`, `created_at`, `material_type_id`, `is_sales`) VALUES
(1, 'Pencil', 'P001', 'Demo Desc', 1, 1, '2018-05-11 10:25:08.310290', 1, 0),
(2, 'Rubber', 'P001', 'Demo Desc', 1, 1, '2018-05-11 10:27:21.935408', 1, 0),
(3, 'Phone', 'P001', 'Demo Desc', 1, 1, '2018-05-11 10:28:37.281146', 1, 0),
(4, 'Mouse', 'P001', 'Demo Desc', 1, 1, '2018-05-11 10:32:10.007621', 1, 0),
(5, 'Chair', 'C001', 'Demo Desc', 1, 1, '2018-05-11 10:36:09.186602', 1, 0),
(6, 'AC', 'A001', 'Demo Desc', 1, 1, '2018-05-11 10:48:58.800104', 1, 0),
(7, 'Cooler', 'CL001', 'Demo Desc', 0, 1, '2018-05-11 11:42:35.075615', 1, 0),
(8, 'Shoes', 'SH001', 'Demo Desc', 1, 1, '2018-05-11 13:01:21.651106', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `material_master_materialpurchasegroup`
--

DROP TABLE IF EXISTS `material_master_materialpurchasegroup`;
CREATE TABLE `material_master_materialpurchasegroup` (
  `id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  `pur_group_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `material_master_materialpurchasegroup`
--

INSERT INTO `material_master_materialpurchasegroup` (`id`, `material_id`, `pur_group_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `material_master_materialpurchaseorg`
--

DROP TABLE IF EXISTS `material_master_materialpurchaseorg`;
CREATE TABLE `material_master_materialpurchaseorg` (
  `id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  `pur_org_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `material_master_materialpurchaseorg`
--

INSERT INTO `material_master_materialpurchaseorg` (`id`, `material_id`, `pur_org_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `material_master_materialtype`
--

DROP TABLE IF EXISTS `material_master_materialtype`;
CREATE TABLE `material_master_materialtype` (
  `id` int(11) NOT NULL,
  `material_type` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `material_master_materialtype`
--

INSERT INTO `material_master_materialtype` (`id`, `material_type`, `status`, `created_at`, `created_by_id`) VALUES
(1, 'Finish Good', 1, '2018-05-11 10:20:30.948490', 1),
(2, 'Raw Material', 1, '2018-05-11 10:20:44.282885', 1),
(3, 'Semi Finished Goods', 1, '2018-05-11 10:21:10.780250', 1),
(4, 'Store Item', 1, '2018-05-11 10:21:22.350848', 1);

-- --------------------------------------------------------

--
-- Table structure for table `material_master_material_tax`
--

DROP TABLE IF EXISTS `material_master_material_tax`;
CREATE TABLE `material_master_material_tax` (
  `id` int(11) NOT NULL,
  `tax_for` varchar(1) NOT NULL,
  `igst` decimal(10,2) NOT NULL,
  `cgst` decimal(10,2) NOT NULL,
  `sgst` decimal(10,2) NOT NULL,
  `hsn` varchar(30) NOT NULL,
  `material_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `material_master_material_tax`
--

INSERT INTO `material_master_material_tax` (`id`, `tax_for`, `igst`, `cgst`, `sgst`, `hsn`, `material_id`) VALUES
(6, '1', '18.00', '9.00', '9.00', 'hsn12541542', 6);

-- --------------------------------------------------------

--
-- Table structure for table `material_master_material_uom`
--

DROP TABLE IF EXISTS `material_master_material_uom`;
CREATE TABLE `material_master_material_uom` (
  `id` int(11) NOT NULL,
  `material_for` varchar(1) NOT NULL,
  `unit_per_uom` decimal(10,2) NOT NULL,
  `base_uom_id` int(11) DEFAULT NULL,
  `material_id` int(11) NOT NULL,
  `unit_uom_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `material_master_material_uom`
--

INSERT INTO `material_master_material_uom` (`id`, `material_for`, `unit_per_uom`, `base_uom_id`, `material_id`, `unit_uom_id`) VALUES
(1, '1', '245.00', 1, 1, 1),
(2, '1', '245.00', 1, 2, 1),
(3, '1', '245.00', 1, 3, 1),
(6, '1', '245.00', 1, 6, 1),
(7, '1', '245.00', 1, 7, 1),
(8, '1', '245.00', 1, 8, 1),
(9, '2', '245.00', 1, 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `purchaseorggroup_purchasegroup`
--

DROP TABLE IF EXISTS `purchaseorggroup_purchasegroup`;
CREATE TABLE `purchaseorggroup_purchasegroup` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `purchaseorggroup_purchasegroup`
--

INSERT INTO `purchaseorggroup_purchasegroup` (`id`, `name`, `description`, `status`, `created_at`, `created_by_id`) VALUES
(1, 'Suraj Group', 'Suraj Group Description1', 1, '2018-05-09 11:25:49.251444', 1),
(2, 'Suraj Group 2', 'Suraj Description 1', 1, '2018-05-09 11:57:19.516426', 1),
(3, 'Test', 'lorem ipsum', 1, '2018-05-11 08:59:01.998627', 1),
(4, 'fasdfasdf', 'f', 1, '2018-05-11 08:59:32.386869', 1),
(5, 'sdggddddd', 'gsdgfdsfsgdg', 1, '2018-05-11 08:59:37.317342', 1),
(6, 'adsds', 'hjdfsgsd', 1, '2018-05-11 09:06:22.662097', 1),
(7, 'aaafsdgggs', 'gggfsgfdsgfdg', 1, '2018-05-11 09:06:28.530491', 1),
(8, 'aggggarrgter', 'rgrgerergege', 1, '2018-05-11 09:06:35.719344', 1),
(9, 'agerehgreer', 'erererery', 1, '2018-05-11 09:06:41.467921', 1),
(10, 'hnggfjjjhgjghjghgh', 'kghkghkgkk', 1, '2018-05-11 09:06:49.184249', 1),
(11, 'atyayya', 'ryyyey', 1, '2018-05-11 09:06:55.734917', 1),
(12, 'aayayyayey5ey', 'reyreyeyeye', 1, '2018-05-11 09:07:05.093099', 1),
(13, 'yuiyiti', 'uiuyiuyi', 1, '2018-05-11 09:07:09.877032', 1),
(14, 'afgasg', 'dgsdgsdf', 1, '2018-05-11 10:17:20.098384', 1),
(15, 'aafaffff', 'dfdfdsfg', 1, '2018-05-11 10:17:26.203012', 1);

-- --------------------------------------------------------

--
-- Table structure for table `purchaseorggroup_purchaseorg`
--

DROP TABLE IF EXISTS `purchaseorggroup_purchaseorg`;
CREATE TABLE `purchaseorggroup_purchaseorg` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `purchaseorggroup_purchaseorg`
--

INSERT INTO `purchaseorggroup_purchaseorg` (`id`, `name`, `description`, `status`, `created_at`, `created_by_id`) VALUES
(1, 'Suraj Organization', 'Suraj Organization Description', 1, '2018-05-09 11:21:29.549244', 1),
(2, 'Suraj Organization 1', 'Suraj Organization Description 1', 1, '2018-05-09 11:29:04.999069', 1),
(3, 'fcsdf', 'sdfds', 1, '2018-05-11 07:25:21.199578', 1),
(4, 'Test', 'Lorem ipsum', 1, '2018-05-11 07:26:15.766133', 1),
(5, 'reset2', 'lorem ipsum', 1, '2018-05-11 07:28:08.380016', 1),
(6, 'gdfg', 'fdhdf', 1, '2018-05-11 07:47:40.200015', 1),
(7, 'hhrtrtytry', 'ghfghfgh', 1, '2018-05-11 07:47:49.700441', 1),
(8, 'ss', 'vgfdgg', 1, '2018-05-11 07:47:57.199716', 1),
(9, 'rwerewrew', 'gfgfdhdhh', 1, '2018-05-11 07:48:04.768353', 1),
(10, 'hghfghfghjkhjk', 'gfhfghfghfh', 1, '2018-05-11 07:48:30.055078', 1),
(11, 'gfghfhfg', 'jhgfjfgjfgj', 1, '2018-05-11 07:48:39.586629', 1),
(12, 'jghjgh', 'jhgjghjg', 1, '2018-05-11 07:48:51.961319', 1),
(13, 'fdsgfgd', 'fgfdh', 1, '2018-05-11 07:48:58.641075', 1),
(14, 'ffffsdfsdf', 'dd fg', 1, '2018-05-11 07:50:13.926895', 1),
(15, 'fsssss', 'fggfdgdfgfdg', 1, '2018-05-11 07:50:20.157931', 1),
(16, 'fssss', 'fgfdgfdgfd', 1, '2018-05-11 07:50:25.316462', 1),
(17, 'frrrr', 'frrer', 1, '2018-05-11 07:50:54.901075', 1),
(18, 'ffffgggg', 'sfsdf', 1, '2018-05-11 07:55:05.788243', 1),
(19, 'ffffhhhhhff', 'dfdfgdfdfgd', 1, '2018-05-11 07:55:25.023998', 1);

-- --------------------------------------------------------

--
-- Table structure for table `purchaseorggroup_purchaseorgmapping`
--

DROP TABLE IF EXISTS `purchaseorggroup_purchaseorgmapping`;
CREATE TABLE `purchaseorggroup_purchaseorgmapping` (
  `id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `pur_org_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `purchaseorggroup_purchaseorgmapping`
--

INSERT INTO `purchaseorggroup_purchaseorgmapping` (`id`, `status`, `created_at`, `branch_id`, `created_by_id`, `pur_org_id`) VALUES
(21, 1, '2018-05-10 08:57:15.875572', 2, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `salesorg_group_salesgroup`
--

DROP TABLE IF EXISTS `salesorg_group_salesgroup`;
CREATE TABLE `salesorg_group_salesgroup` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `salesorg_group_salesgroup`
--

INSERT INTO `salesorg_group_salesgroup` (`id`, `name`, `description`, `status`, `created_at`, `created_by_id`) VALUES
(1, 'Sales Group Suraj', 'Demo description', 1, '2018-05-09 12:57:15.088162', 1),
(2, 'test', 'vcvcb', 1, '2018-05-11 10:07:17.343954', 1),
(3, 'bcvxbv', 'vcncvncn', 1, '2018-05-11 10:07:41.632691', 1),
(4, 'ghgfj', 'gfhfghgfhg', 1, '2018-05-11 10:08:08.427971', 1),
(5, 'dfdsg', 'fgfdhdfh', 1, '2018-05-11 10:08:45.240721', 1),
(6, 'hdhh', 'dfhdfh', 1, '2018-05-11 10:08:52.534846', 1),
(7, 'hdfhdh', 'hhhh', 1, '2018-05-11 10:08:59.725064', 1),
(8, 'hdhhhghfghf', 'hdhfgh', 1, '2018-05-11 10:09:15.004271', 1),
(9, 'fasffdgg', 'fdgfdhh', 1, '2018-05-11 10:14:20.359529', 1);

-- --------------------------------------------------------

--
-- Table structure for table `salesorg_group_salesorg`
--

DROP TABLE IF EXISTS `salesorg_group_salesorg`;
CREATE TABLE `salesorg_group_salesorg` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `salesorg_group_salesorg`
--

INSERT INTO `salesorg_group_salesorg` (`id`, `name`, `description`, `status`, `created_at`, `created_by_id`) VALUES
(1, 'Sales Org Suraj', 'Demo Description1', 1, '2018-05-09 12:55:42.665030', 1),
(2, 'asd', 'asdas', 1, '2018-05-09 13:36:42.379266', 1),
(3, '213', '12', 1, '2018-05-09 13:37:15.819630', 1),
(4, 'sAD', 'Dasd', 1, '2018-05-09 13:38:07.515691', 1),
(5, 'adadD', 'DadA', 1, '2018-05-11 09:31:55.737232', 1),
(6, 'DSD', 'ADAF', 1, '2018-05-11 09:32:12.285721', 1),
(7, 'hgfhgfh', 'fjgjfgjf', 1, '2018-05-11 09:32:26.664621', 1),
(8, 'fgjfjfgjfg', 'fjfgjfgjfgjfj', 1, '2018-05-11 09:32:33.285627', 1),
(9, 'jfjfjj', 'fytrytru', 1, '2018-05-11 09:32:40.356582', 1),
(10, 'sdds', '54757uu', 1, '2018-05-11 09:32:46.455274', 1),
(11, 'jfgjfgjfjfjjfjfjfff', 'fgjgjfjfjfjjjf', 1, '2018-05-11 09:32:53.562737', 1),
(12, 'fjfgjfgj', 'jjjjjjjggg', 1, '2018-05-11 09:33:22.204919', 1),
(13, 'fffff', 'hhhhhh', 1, '2018-05-11 09:36:46.440945', 1),
(14, 'ffhhhff', 'hfffhhfh', 1, '2018-05-11 09:36:53.387779', 1),
(15, 'ffffhhfhff', 'fhffhhh', 1, '2018-05-11 09:37:00.253215', 1),
(16, 'ffhhhf', 'fhhfhf', 1, '2018-05-11 09:37:05.923967', 1),
(17, 'fhhfff', 'hhffh', 1, '2018-05-11 09:37:11.579370', 1),
(18, 'ffjjjjj', 'jjfjfjfj', 1, '2018-05-11 09:45:00.753940', 1);

-- --------------------------------------------------------

--
-- Table structure for table `states_state`
--

DROP TABLE IF EXISTS `states_state`;
CREATE TABLE `states_state` (
  `id` int(11) NOT NULL,
  `state_name` varchar(50) NOT NULL,
  `tin_number` int(11) NOT NULL,
  `state_code` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `states_state`
--

INSERT INTO `states_state` (`id`, `state_name`, `tin_number`, `state_code`, `created_at`, `user_id`, `status`) VALUES
(1, 'West Bengal', 665666, 'WB0014', '2018-05-07 07:58:05.287297', 1, 1),
(2, 'Orissa', 111, 'OR001', '2018-05-07 08:00:55.700886', NULL, 1),
(7, 'Test', 1234567, 'WB0023', '2018-05-10 12:43:23.310073', 1, 1),
(20, 'a', 32434, 'fgfdhg', '2018-05-11 06:20:50.552871', 1, 1),
(21, 'ab', 545, 'vgdfgdfg', '2018-05-11 06:21:00.115854', 1, 1),
(22, 'abc', 4546, 'cbvxcbb', '2018-05-11 06:21:14.619382', 1, 1),
(23, 'abcd', 45656547, 'bvcbnvcnb', '2018-05-11 06:21:24.801365', 1, 1),
(24, 'aaa', 46346, 'vbvcnbn', '2018-05-11 06:21:33.224717', 1, 1),
(25, 'aaaaaav', 435436, 'bvcbnvcn', '2018-05-11 06:21:45.488825', 1, 1),
(26, 'aaafff', 23543534, 'cvb vcb', '2018-05-11 06:21:54.650215', 1, 1),
(27, 'aaffff', 53456, 'bcbncvn', '2018-05-11 06:22:03.973580', 1, 1),
(28, 'asssd', 34566, 'bcvbcbn', '2018-05-11 06:22:12.504537', 1, 1),
(29, 'aaaauutyu', 5436, 'bbcvbcvn', '2018-05-11 06:22:24.634733', 1, 1),
(30, 'aaadd', 456564, 'bbcb', '2018-05-11 06:22:33.185041', 1, 1),
(31, 'Chattisgarh', 789, 'C001', '2018-05-11 07:21:09.858456', 1, 1),
(32, 'asdas', 32432, '3424', '2018-05-11 07:25:05.606782', 1, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `company_branch_companybranch`
--
ALTER TABLE `company_branch_companybranch`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_branch_compa_branch_state_id_7d877ac3_fk_states_st` (`branch_state_id`),
  ADD KEY `company_branch_compa_created_by_id_cdfca697_fk_auth_user` (`created_by_id`),
  ADD KEY `company_branch_compa_company_id_8fb9c2a0_fk_company_c` (`company_id`);

--
-- Indexes for table `company_branch_storagebin`
--
ALTER TABLE `company_branch_storagebin`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_branch_stora_branch_id_ea49cf87_fk_company_b` (`branch_id`),
  ADD KEY `company_branch_stora_company_id_6f7bcbe5_fk_company_c` (`company_id`),
  ADD KEY `company_branch_storagebin_created_by_id_fcaa943d_fk_auth_user_id` (`created_by_id`),
  ADD KEY `company_branch_stora_storage_id_934b4732_fk_company_b` (`storage_id`),
  ADD KEY `company_branch_stora_uom_id_0ed574dd_fk_company_b` (`uom_id`);

--
-- Indexes for table `company_branch_storagelocation`
--
ALTER TABLE `company_branch_storagelocation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_branch_stora_branch_id_3cf4d58e_fk_company_b` (`branch_id`),
  ADD KEY `company_branch_stora_company_id_0b3b477c_fk_company_c` (`company_id`),
  ADD KEY `company_branch_stora_created_by_id_fb5d5820_fk_auth_user` (`created_by_id`),
  ADD KEY `company_branch_stora_storage_state_id_8a6697c2_fk_states_st` (`storage_state_id`);

--
-- Indexes for table `company_branch_uom`
--
ALTER TABLE `company_branch_uom`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `company_company`
--
ALTER TABLE `company_company`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_company_company_state_id_76f796cf_fk_states_state_id` (`company_state_id`),
  ADD KEY `company_company_created_by_id_cf02c06b_fk_auth_user_id` (`created_by_id`),
  ADD KEY `company_company_parent_id_3abe3587_fk_company_company_id` (`parent_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `material_master_material`
--
ALTER TABLE `material_master_material`
  ADD PRIMARY KEY (`id`),
  ADD KEY `material_master_mate_material_type_id_d61faaa7_fk_material_` (`material_type_id`);

--
-- Indexes for table `material_master_materialpurchasegroup`
--
ALTER TABLE `material_master_materialpurchasegroup`
  ADD PRIMARY KEY (`id`),
  ADD KEY `material_master_mate_material_id_ec99c87c_fk_material_` (`material_id`),
  ADD KEY `material_master_mate_pur_group_id_1a6bfd7b_fk_purchaseo` (`pur_group_id`);

--
-- Indexes for table `material_master_materialpurchaseorg`
--
ALTER TABLE `material_master_materialpurchaseorg`
  ADD PRIMARY KEY (`id`),
  ADD KEY `material_master_mate_material_id_3e8872df_fk_material_` (`material_id`),
  ADD KEY `material_master_mate_pur_org_id_9a4f6482_fk_purchaseo` (`pur_org_id`);

--
-- Indexes for table `material_master_materialtype`
--
ALTER TABLE `material_master_materialtype`
  ADD PRIMARY KEY (`id`),
  ADD KEY `material_master_mate_created_by_id_0d9a0208_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `material_master_material_tax`
--
ALTER TABLE `material_master_material_tax`
  ADD PRIMARY KEY (`id`),
  ADD KEY `material_master_mate_material_id_25b753a1_fk_material_` (`material_id`);

--
-- Indexes for table `material_master_material_uom`
--
ALTER TABLE `material_master_material_uom`
  ADD PRIMARY KEY (`id`),
  ADD KEY `material_master_mate_base_uom_id_ab4e7358_fk_company_b` (`base_uom_id`),
  ADD KEY `material_master_mate_material_id_24305246_fk_material_` (`material_id`),
  ADD KEY `material_master_mate_unit_uom_id_cd2e4a16_fk_company_b` (`unit_uom_id`);

--
-- Indexes for table `purchaseorggroup_purchasegroup`
--
ALTER TABLE `purchaseorggroup_purchasegroup`
  ADD PRIMARY KEY (`id`),
  ADD KEY `purchaseorggroup_pur_created_by_id_24e2b401_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `purchaseorggroup_purchaseorg`
--
ALTER TABLE `purchaseorggroup_purchaseorg`
  ADD PRIMARY KEY (`id`),
  ADD KEY `purchaseorggroup_pur_created_by_id_5344064c_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `purchaseorggroup_purchaseorgmapping`
--
ALTER TABLE `purchaseorggroup_purchaseorgmapping`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `purchaseorggroup_purchas_pur_org_id_branch_id_5aab0746_uniq` (`pur_org_id`,`branch_id`),
  ADD KEY `purchaseorggroup_pur_branch_id_97aaa2df_fk_company_b` (`branch_id`),
  ADD KEY `purchaseorggroup_pur_created_by_id_71d2402d_fk_auth_user` (`created_by_id`),
  ADD KEY `purchaseorggroup_purchase_pur_org_id_branch_id_5aab0746_idx` (`pur_org_id`,`branch_id`);

--
-- Indexes for table `salesorg_group_salesgroup`
--
ALTER TABLE `salesorg_group_salesgroup`
  ADD PRIMARY KEY (`id`),
  ADD KEY `salesorg_group_salesgroup_created_by_id_7ca90bef_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `salesorg_group_salesorg`
--
ALTER TABLE `salesorg_group_salesorg`
  ADD PRIMARY KEY (`id`),
  ADD KEY `salesorg_group_salesorg_created_by_id_b825d4cf_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `states_state`
--
ALTER TABLE `states_state`
  ADD PRIMARY KEY (`id`),
  ADD KEY `states_state_user_id_08eb8514_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `company_branch_companybranch`
--
ALTER TABLE `company_branch_companybranch`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `company_branch_storagebin`
--
ALTER TABLE `company_branch_storagebin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `company_branch_storagelocation`
--
ALTER TABLE `company_branch_storagelocation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `company_branch_uom`
--
ALTER TABLE `company_branch_uom`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `company_company`
--
ALTER TABLE `company_company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `material_master_material`
--
ALTER TABLE `material_master_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `material_master_materialpurchasegroup`
--
ALTER TABLE `material_master_materialpurchasegroup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `material_master_materialpurchaseorg`
--
ALTER TABLE `material_master_materialpurchaseorg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `material_master_materialtype`
--
ALTER TABLE `material_master_materialtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `material_master_material_tax`
--
ALTER TABLE `material_master_material_tax`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `material_master_material_uom`
--
ALTER TABLE `material_master_material_uom`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `purchaseorggroup_purchasegroup`
--
ALTER TABLE `purchaseorggroup_purchasegroup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `purchaseorggroup_purchaseorg`
--
ALTER TABLE `purchaseorggroup_purchaseorg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `purchaseorggroup_purchaseorgmapping`
--
ALTER TABLE `purchaseorggroup_purchaseorgmapping`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `salesorg_group_salesgroup`
--
ALTER TABLE `salesorg_group_salesgroup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `salesorg_group_salesorg`
--
ALTER TABLE `salesorg_group_salesorg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `states_state`
--
ALTER TABLE `states_state`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `company_branch_companybranch`
--
ALTER TABLE `company_branch_companybranch`
  ADD CONSTRAINT `company_branch_compa_branch_state_id_7d877ac3_fk_states_st` FOREIGN KEY (`branch_state_id`) REFERENCES `states_state` (`id`),
  ADD CONSTRAINT `company_branch_compa_company_id_8fb9c2a0_fk_company_c` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`),
  ADD CONSTRAINT `company_branch_compa_created_by_id_cdfca697_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `company_branch_storagebin`
--
ALTER TABLE `company_branch_storagebin`
  ADD CONSTRAINT `company_branch_stora_branch_id_ea49cf87_fk_company_b` FOREIGN KEY (`branch_id`) REFERENCES `company_branch_companybranch` (`id`),
  ADD CONSTRAINT `company_branch_stora_company_id_6f7bcbe5_fk_company_c` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`),
  ADD CONSTRAINT `company_branch_stora_storage_id_934b4732_fk_company_b` FOREIGN KEY (`storage_id`) REFERENCES `company_branch_storagelocation` (`id`),
  ADD CONSTRAINT `company_branch_stora_uom_id_0ed574dd_fk_company_b` FOREIGN KEY (`uom_id`) REFERENCES `company_branch_uom` (`id`),
  ADD CONSTRAINT `company_branch_storagebin_created_by_id_fcaa943d_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `company_branch_storagelocation`
--
ALTER TABLE `company_branch_storagelocation`
  ADD CONSTRAINT `company_branch_stora_branch_id_3cf4d58e_fk_company_b` FOREIGN KEY (`branch_id`) REFERENCES `company_branch_companybranch` (`id`),
  ADD CONSTRAINT `company_branch_stora_company_id_0b3b477c_fk_company_c` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`),
  ADD CONSTRAINT `company_branch_stora_created_by_id_fb5d5820_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `company_branch_stora_storage_state_id_8a6697c2_fk_states_st` FOREIGN KEY (`storage_state_id`) REFERENCES `states_state` (`id`);

--
-- Constraints for table `company_company`
--
ALTER TABLE `company_company`
  ADD CONSTRAINT `company_company_company_state_id_76f796cf_fk_states_state_id` FOREIGN KEY (`company_state_id`) REFERENCES `states_state` (`id`),
  ADD CONSTRAINT `company_company_created_by_id_cf02c06b_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `company_company_parent_id_3abe3587_fk_company_company_id` FOREIGN KEY (`parent_id`) REFERENCES `company_company` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `material_master_material`
--
ALTER TABLE `material_master_material`
  ADD CONSTRAINT `material_master_mate_material_type_id_d61faaa7_fk_material_` FOREIGN KEY (`material_type_id`) REFERENCES `material_master_materialtype` (`id`);

--
-- Constraints for table `material_master_materialpurchasegroup`
--
ALTER TABLE `material_master_materialpurchasegroup`
  ADD CONSTRAINT `material_master_mate_material_id_ec99c87c_fk_material_` FOREIGN KEY (`material_id`) REFERENCES `material_master_material` (`id`),
  ADD CONSTRAINT `material_master_mate_pur_group_id_1a6bfd7b_fk_purchaseo` FOREIGN KEY (`pur_group_id`) REFERENCES `purchaseorggroup_purchasegroup` (`id`);

--
-- Constraints for table `material_master_materialpurchaseorg`
--
ALTER TABLE `material_master_materialpurchaseorg`
  ADD CONSTRAINT `material_master_mate_material_id_3e8872df_fk_material_` FOREIGN KEY (`material_id`) REFERENCES `material_master_material` (`id`),
  ADD CONSTRAINT `material_master_mate_pur_org_id_9a4f6482_fk_purchaseo` FOREIGN KEY (`pur_org_id`) REFERENCES `purchaseorggroup_purchaseorg` (`id`);

--
-- Constraints for table `material_master_materialtype`
--
ALTER TABLE `material_master_materialtype`
  ADD CONSTRAINT `material_master_mate_created_by_id_0d9a0208_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `material_master_material_tax`
--
ALTER TABLE `material_master_material_tax`
  ADD CONSTRAINT `material_master_mate_material_id_25b753a1_fk_material_` FOREIGN KEY (`material_id`) REFERENCES `material_master_material` (`id`);

--
-- Constraints for table `material_master_material_uom`
--
ALTER TABLE `material_master_material_uom`
  ADD CONSTRAINT `material_master_mate_base_uom_id_ab4e7358_fk_company_b` FOREIGN KEY (`base_uom_id`) REFERENCES `company_branch_uom` (`id`),
  ADD CONSTRAINT `material_master_mate_material_id_24305246_fk_material_` FOREIGN KEY (`material_id`) REFERENCES `material_master_material` (`id`),
  ADD CONSTRAINT `material_master_mate_unit_uom_id_cd2e4a16_fk_company_b` FOREIGN KEY (`unit_uom_id`) REFERENCES `company_branch_uom` (`id`);

--
-- Constraints for table `purchaseorggroup_purchasegroup`
--
ALTER TABLE `purchaseorggroup_purchasegroup`
  ADD CONSTRAINT `purchaseorggroup_pur_created_by_id_24e2b401_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `purchaseorggroup_purchaseorg`
--
ALTER TABLE `purchaseorggroup_purchaseorg`
  ADD CONSTRAINT `purchaseorggroup_pur_created_by_id_5344064c_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `purchaseorggroup_purchaseorgmapping`
--
ALTER TABLE `purchaseorggroup_purchaseorgmapping`
  ADD CONSTRAINT `purchaseorggroup_pur_branch_id_97aaa2df_fk_company_b` FOREIGN KEY (`branch_id`) REFERENCES `company_branch_companybranch` (`id`),
  ADD CONSTRAINT `purchaseorggroup_pur_created_by_id_71d2402d_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `purchaseorggroup_pur_pur_org_id_5898b14c_fk_purchaseo` FOREIGN KEY (`pur_org_id`) REFERENCES `purchaseorggroup_purchaseorg` (`id`);

--
-- Constraints for table `salesorg_group_salesgroup`
--
ALTER TABLE `salesorg_group_salesgroup`
  ADD CONSTRAINT `salesorg_group_salesgroup_created_by_id_7ca90bef_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `salesorg_group_salesorg`
--
ALTER TABLE `salesorg_group_salesorg`
  ADD CONSTRAINT `salesorg_group_salesorg_created_by_id_b825d4cf_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `states_state`
--
ALTER TABLE `states_state`
  ADD CONSTRAINT `states_state_user_id_08eb8514_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

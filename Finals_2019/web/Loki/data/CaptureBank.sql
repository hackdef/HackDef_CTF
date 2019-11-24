CREATE DATABASE IF NOT EXISTS CaptureBankHDF; USE CaptureBankHDF;
--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `age` varchar(3) NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_general_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Daniel','Regalado','dregalado','ab9aef34d88cbd7729e84158fe49bb84','Polanco 5543','5533232323','46'),(2,'Ana','Lopez','alopez','53ab7642bf1024e0906dc40bf7a85b5a','Ecatepec 7','5544223322','23'),(3,'Berenice','Flores','bflores','939249F71730798839DACF0950E3D935','Iztacalco 525','5575845267','28'),(4,'Luis','Noriega','lnoriega','436A30534888AA4679B6C9F8C56C757E','Obrera 525','5245665285','25'),(5,'Juan','Pérez','jperez','hackdef{CF9010E86EB2DAB9387788F354609315}','Coyoacan 2525','5587995288','30'),(6,'Maria','Calderon','mcalderon','B74AE3435CE6BAC35500337A375F594F','Santa Fe 2000','5588774455','19'),(7,'Ulises','Fortress','uF0rtress','D656D89DDCCC83F4A048AA6B44ECD8EB','Insurgentes Sur 3500','5577142255','56'),(8,'Veronica','Espino','vespino','E97525122DDA2DAFC2AB80F11C95F656','Barranca del Muerto 885','5574231595','25'),(9,'Andres','Hernandez','ahernandez','84C14540EADD790A36D1069C1EE3CE93','Universidad 2555','5548526522','65'),(10,'Fernando','Castrejon','fcastrejon','EDBF8D1E3513B7072A05F19F7599323B','Rio los remedios 1','5522114466','80');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cards` (
  `cardId` int(11) NOT NULL AUTO_INCREMENT,
  `cardNum` varchar(50) NOT NULL,
  `expirationDate` varchar(10) NOT NULL,
  `CVV` varchar(5) NOT NULL,
  `userId` int(11) DEFAULT NULL,
  PRIMARY KEY (`cardId`),
  KEY `fk_id` (`userId`),
  CONSTRAINT `fk_id` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_general_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (1,'************4628','01/22','528',1),(2,'************1234','05/20','125',1),(3,'************5852','02/20','111',2),(4,'************7896','05/25','996',3),(5,'************8695','08/22','785',4),(6,'************8695','07/20','255',5),(7,'************7877','02/22','777',6),(8,'************1010','04/26','666',7),(9,'************7411','05/24','739',8),(10,'************7411','08/29','746',9),(11,'************9635','02/23','885',10);
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;
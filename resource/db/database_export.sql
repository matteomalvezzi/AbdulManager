-- MariaDB dump 10.19  Distrib 10.5.9-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: abdulmanager
-- ------------------------------------------------------
-- Server version	10.5.9-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dipendente`
--

DROP TABLE IF EXISTS `dipendente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dipendente` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `sesso` char(1) NOT NULL,
  `data_di_nascita` date NOT NULL,
  `luogo_di_nascita` varchar(45) NOT NULL,
  `codice_fiscale` varchar(16) NOT NULL,
  `impiego` int(3) DEFAULT NULL,
  `data_assunzione` date DEFAULT NULL,
  `stipendio` int(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `impiego` (`impiego`),
  CONSTRAINT `dipendente_ibfk_1` FOREIGN KEY (`impiego`) REFERENCES `impieghi` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dipendente`
--

LOCK TABLES `dipendente` WRITE;
/*!40000 ALTER TABLE `dipendente` DISABLE KEYS */;
INSERT INTO `dipendente` VALUES (1,'Matteo','Malvezzi','M','2003-05-05','Guastalla','MLVMTT03E05E253B',1,'2021-02-20',1400);
/*!40000 ALTER TABLE `dipendente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `impieghi`
--

DROP TABLE IF EXISTS `impieghi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `impieghi` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `impiego` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `impieghi`
--

LOCK TABLES `impieghi` WRITE;
/*!40000 ALTER TABLE `impieghi` DISABLE KEYS */;
INSERT INTO `impieghi` VALUES (1,'Sviluppatore Software'),(2,'Progettista Software'),(3,'Marketer'),(4,'Analista'),(5,'Dirigente vendite'),(6,'Commerciale'),(7,'Rappresentate'),(8,'Amministratore delegato'),(9,'Project Manager'),(10,'Amministratore sistemi aziendali');
/*!40000 ALTER TABLE `impieghi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reparti`
--

DROP TABLE IF EXISTS `reparti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reparti` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `nome_reparto` varchar(45) NOT NULL,
  `id_sede` int(3) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_sede` (`id_sede`),
  CONSTRAINT `reparti_ibfk_1` FOREIGN KEY (`id_sede`) REFERENCES `sedi` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reparti`
--

LOCK TABLES `reparti` WRITE;
/*!40000 ALTER TABLE `reparti` DISABLE KEYS */;
INSERT INTO `reparti` VALUES (1,'Marketing',2),(2,'Vendite',2),(3,'Programmazione software',1),(4,'Sistemi aziendali',3),(5,'Assistenza tecnica',1),(6,'Risorse umane',2),(7,'Progettazione software',1),(8,'Testing Software',1);
/*!40000 ALTER TABLE `reparti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reparto_dipendenti`
--

DROP TABLE IF EXISTS `reparto_dipendenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reparto_dipendenti` (
  `id_dipendente` int(6) NOT NULL,
  `id_reparto` int(3) NOT NULL,
  PRIMARY KEY (`id_dipendente`),
  KEY `id_reparto` (`id_reparto`),
  CONSTRAINT `reparto_dipendenti_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reparto_dipendenti_ibfk_2` FOREIGN KEY (`id_reparto`) REFERENCES `reparti` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reparto_dipendenti`
--

LOCK TABLES `reparto_dipendenti` WRITE;
/*!40000 ALTER TABLE `reparto_dipendenti` DISABLE KEYS */;
INSERT INTO `reparto_dipendenti` VALUES (1,1);
/*!40000 ALTER TABLE `reparto_dipendenti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sedi`
--

DROP TABLE IF EXISTS `sedi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sedi` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `indirizzo` varchar(45) NOT NULL,
  `citta` varchar(45) NOT NULL,
  `provincia` varchar(45) NOT NULL,
  `cap` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sedi`
--

LOCK TABLES `sedi` WRITE;
/*!40000 ALTER TABLE `sedi` DISABLE KEYS */;
INSERT INTO `sedi` VALUES (1,'Via Ivano Martinelli 51 A','Carpi','Modena','41012'),(2,'Via della Repubblica 29','Correggio','Reggio Emilia','42015'),(3,'Via Albricconi 3','Campagnola','Reggio Emilia','42012');
/*!40000 ALTER TABLE `sedi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-17 22:46:57

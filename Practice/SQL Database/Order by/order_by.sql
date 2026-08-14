-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: chinook
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `CustomerId` int NOT NULL,
  `FirstName` varchar(40) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `Company` varchar(80) DEFAULT NULL,
  `Address` varchar(70) DEFAULT NULL,
  `City` varchar(40) DEFAULT NULL,
  `State` varchar(40) DEFAULT NULL,
  `Country` varchar(40) DEFAULT NULL,
  `PostalCode` varchar(10) DEFAULT NULL,
  `Phone` varchar(24) DEFAULT NULL,
  `Fax` varchar(24) DEFAULT NULL,
  `Email` varchar(60) NOT NULL,
  `SupportRepId` int DEFAULT NULL,
  PRIMARY KEY (`CustomerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Luís','Gonçalves','Embraer - Empresa Brasileira de Aeronáutica S.A.','Av. Brigadeiro Faria Lima, 2170','São José dos Campos','SP','Brazil','12227-000','+55 (12) 3923-5555','+55 (12) 3923-5566','luisg@embraer.com.br',3),(2,'Eduardo','Martins','Woodstock Discos','Rua Dr. Falcão Filho, 155','São Paulo','SP','Brazil','01007-010','+55 (11) 3033-5446','+55 (11) 3033-4564','eduardo@woodstock.com.br',4),(3,'Alexandre','Rocha','Banco do Brasil S.A.','Av. Paulista, 2022','São Paulo','SP','Brazil','01310-200','+55 (11) 3055-3278','+55 (11) 3055-8131','alero@uol.com.br',5),(4,'Roberto','Almeida','Riotur','Praça Pio X, 119','Rio de Janeiro','RJ','Brazil','20040-020','+55 (21) 2271-7000','+55 (21) 2271-7070','roberto.almeida@riotur.gov.br',3),(5,'Mark','Philips','Telus','8210 111 ST NW','Edmonton','AB','Canada','T6G 2C7','+1 (780) 434-4554','+1 (780) 434-5565','mphilips12@shaw.ca',5),(6,'Jennifer','Peterson','Rogers Canada','700 W Pender Street','Vancouver','BC','Canada','V6C 1G8','+1 (604) 688-2255','+1 (604) 688-8756','jenniferp@rogers.ca',3);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-14 17:01:35

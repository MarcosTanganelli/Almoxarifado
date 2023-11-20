-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           8.0.34 - MySQL Community Server - GPL
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para almoxarifado
CREATE DATABASE IF NOT EXISTS `almoxarifado` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `almoxarifado`;

-- Copiando estrutura para tabela almoxarifado.estoque
CREATE TABLE IF NOT EXISTS `estoque` (
  `cod_mat` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `material` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `local` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `unidade` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `saldo` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela almoxarifado.estoque: ~0 rows (aproximadamente)
INSERT INTO `estoque` (`cod_mat`, `material`, `local`, `unidade`, `saldo`) VALUES
	('768', 'Adaptador P/ Cx D\'Água, Flange Fixa, 25mm X 3/4', '0', 'PÇ', 7),
	('803', 'Adaptador P/ Cx D\'Água, Flange Fixa, 32mm X 1', '0', 'PÇ', 10),
	('766', 'Adaptador P/ Cx D\'Água, Flange Livre, 40mm', '0', 'PÇ', 129),
	('783', 'Adaptador Sol. Curto P/ Água 25mm X 3/4', '0', 'PÇ', 36),
	('9090', 'Adaptador Solda-Rosca Em Pvc, C/ Flanges Articuladas, 50mm X 1.1/2', '0', 'PÇ', 17),
	('678', 'Adaptador Soldável Curto, 32mm X 1', '0', 'PÇ', 42),
	('686', 'Bóia P/ Caixa D\'Água , Metal, De 3/4', '0', 'PÇ', 9),
	('714', 'Bóia P/ Caixa D\'Água, Metal, De 1', '0', 'PÇ', 17),
	('602', 'Bucha De Redução P/ Esgoto, 100 X 50mm', '0', 'PÇ', 9),
	('9093', 'Bucha De Redução, 32 X 25mm', '0', 'PÇ', 36),
	('680', 'Bucha De Redução, Longa, 40 X 25mm', '0', 'PÇ', 101),
	('789', 'Bucha De Redução. Curta, 50 X 40mm', '0', 'PÇ', 52),
	('763', 'Caixa Sifonada Quadrada C/ 3 Entradas, 100 X 125 X 50mm', '0', 'PÇ', 7),
	('1538', 'Chuveiro Tipo Ducha, 5400w 127v', '0', 'PÇ', 16),
	('750', 'Joelho P/ Esgoto Primário, 45º X 100mm', '0', 'PÇ', 11),
	('760', 'Joelho P/ Esgoto Primário, 45º X 75mm', '0', 'PÇ', 29),
	('652', 'Joelho P/ Esgoto Primário, 90º X 100mm', '0', 'PÇ', 8),
	('727', 'Joelho P/ Esgoto Primário, 90º X 50mm', '0', 'PÇ', 65),
	('733', 'Joelho P/ Esgoto Primário, 90º X 75mm', '0', 'PÇ', 25),
	('739', 'Joelho Soldável C/ Bucha De Latão, 90º X 25mm X 1/2', '0', 'PÇ', 10),
	('653', 'Joelho Soldável C/ Bucha De Latão, 90º X 25mm X 3/4', '0', 'PÇ', 166),
	('670', 'Joelho Soldável P/ Água, 45º X 25mm', '0', 'PÇ', 15),
	('688', 'Joelho Soldável P/ Água, 90º X 25mm', '0', 'PÇ', 84),
	('767', 'Joelho Soldável P/ Água, 90º X 40mm', '0', 'PÇ', 15),
	('801', 'Junção P/ Esgoto Secundário, 45º X 40 Mm', '0', 'PÇ', 65),
	('604', 'Junção Soldável P/ Esgoto, 45º X 100 X 50mm', '0', 'PÇ', 18),
	('605', 'Junção Soldável P/ Esgoto, 45º X 100mm', '0', 'PÇ', 12),
	('603', 'Junção Soldável P/ Esgoto, 45º X 45 X 50mm', '0', 'PÇ', 45),
	('16724', 'Luva De Correr P/ Água, Em Pvc, 32mm', '0', 'PÇ', 150),
	('34032', 'Luva De Correr P/Água, Em Pvc, 25mm.', '0', 'PÇ', 74),
	('27632', 'Luva De Correr P/Água, Em Pvc, 40mm', '0', 'PÇ', 4),
	('27633', 'Luva De Correr, P/Água, Em Pvc, 50mm', '0', 'PÇ', 149),
	('13621', 'Luva De Redução Sol. 25mm X 3/4 C/ Bucha De Latão', '0', 'PÇ', 104),
	('18125', 'Plug Roscável Em Pvc, De 3/4', '0', 'PÇ', 70),
	('30910', 'Registro De Gaveta De 1, S/ Acabamento', '0', 'PÇ', 7),
	('30916', 'Registro De Gaveta De 1.1/2, S/ Acabamento', '0', 'PÇ', 7),
	('30914', 'Registro De Pressão, 3/4', '0', 'PÇ', 1),
	('126849', 'Saboneteira Em Abs, 800ml', '0', 'PÇ', 4),
	('28630', 'Tê De Redução Soldável P/ Água, 90º, 50 X 25mm', '0', 'PÇ', 8),
	('654', 'Tê De Redução Soldável, 90º, 32 X 25mm', '0', 'PÇ', 7),
	('770', 'Tê Em Pvc P/ Esgoto, 40 X 40 X 40mm', '0', 'PÇ', 10),
	('27359', 'Tê Em Pvc P/ Esgoto, 75 X 75 X 75mm', '0', 'PÇ', 5),
	('20503', 'Tê Em Pvc Soldável, 32 X 32 X 32mm', '0', 'PÇ', 46),
	('720', 'Tê Em Pvc Soldavél, 50 X 50 X 50mm', '0', 'PÇ', 40),
	('731', 'Tê P/ Esgoto Primário, 90º, 50 X 50 Mm', '0', 'PÇ', 145),
	('46995', 'Torneira Cromada Para Lavatório (Tipo Longa), Volante No Modelo Bola', '0', 'PÇ', 34),
	('765', 'Torneira Em Metal P/ Jardim, Acionamento Rotativo, S/ Rosca, 3/4', '0', 'PÇ', 39),
	('779', 'Torneira Em Metal P/ Pia, Longa, Acionamento Rotativo, 3/4', '0', 'PÇ', 36),
	('43423', 'Torneira Em Metal P/Jardim,3/4 Acion. Alavanca', '0', 'PÇ', 17),
	('722', 'Torneira P/ Lavatório, Cromada, 1/2', '0', 'PÇ', 2),
	('26450', 'Torneira Plástica Para Bebedouro De Garrafão, Cor Branca/Azul', '0', 'PÇ', 14),
	('33687', 'União Soldável, 25mm', '0', 'PÇ', 60),
	('44702', 'União Soldável, 40mm', '0', 'PÇ', 8),
	('97229', 'Válvula 1" (7/8") P/Lavatório, Cromado, Sem Ladrão Comprimento 76mm', '0', 'PÇ', 54),
	('200001', 'Válvula 2 1/4" Corpo Inox Multiuso: Tanques - Pias - Lavatório', '0', 'PÇ', 0),
	('18978', 'Válvula P/ Lavatório, Em Metal', '0', 'PÇ', 51);

-- Copiando estrutura para tabela almoxarifado.saida
CREATE TABLE IF NOT EXISTS `saida` (
  `chamado_id` varchar(50) DEFAULT NULL,
  `tecnico` varchar(50) DEFAULT NULL,
  `material` varchar(50) DEFAULT NULL,
  `area_atuacao` varchar(50) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `codigo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela almoxarifado.saida: ~0 rows (aproximadamente)
INSERT INTO `saida` (`chamado_id`, `tecnico`, `material`, `area_atuacao`, `data`, `codigo`) VALUES
	('54645645', 'joao', 'teste', 'engenheiro', '2023-09-03', '783');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
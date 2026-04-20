-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cpqd_servidor_teste
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cpqd_servidor_teste
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cpqd_servidor_teste` DEFAULT CHARACTER SET utf8 ;
USE `cpqd_servidor_teste` ;

-- -----------------------------------------------------
-- Table `cpqd_servidor_teste`.`usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_servidor_teste`.`usuario` ;

CREATE TABLE IF NOT EXISTS `cpqd_servidor_teste`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(15) NOT NULL,
  `senha` VARCHAR(25) NOT NULL,
  `cargo` VARCHAR(10) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cpqd_servidor_teste`.`liberacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_servidor_teste`.`liberacao` ;

CREATE TABLE IF NOT EXISTS `cpqd_servidor_teste`.`liberacao` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `placa` VARCHAR(8) NULL,
  `modelo` VARCHAR(45) NULL,
  `cor` VARCHAR(30) NULL,
  `empresa` VARCHAR(25) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

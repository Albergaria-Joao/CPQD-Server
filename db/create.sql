-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cpqd_portaria
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cpqd_portaria` ;

-- -----------------------------------------------------
-- Schema cpqd_portaria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cpqd_portaria` DEFAULT CHARACTER SET utf8 ;
USE `cpqd_portaria` ;

-- -----------------------------------------------------
-- Table `cpqd_portaria`.`usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_portaria`.`usuario` ;

CREATE TABLE IF NOT EXISTS `cpqd_portaria`.`usuario` (
  `id_usuario` VARCHAR(36) NOT NULL,
  `nome_usuario` VARCHAR(20) NULL,
  `senha` VARCHAR(26) NULL,
  `empresa_usuario` VARCHAR(20) NULL,
  `cargo` VARCHAR(10) NULL,
  `status_usuario` VARCHAR(10) NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cpqd_portaria`.`pessoa`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_portaria`.`pessoa` ;

CREATE TABLE IF NOT EXISTS `cpqd_portaria`.`pessoa` (
  `id_pessoa` VARCHAR(36) NOT NULL,
  `nome_pessoa` VARCHAR(80) NULL,
  `rg` VARCHAR(11) NULL,
  `cpf` VARCHAR(12) NULL,
  `tipo_pessoa` VARCHAR(15) NULL,
  PRIMARY KEY (`id_pessoa`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cpqd_portaria`.`carro`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_portaria`.`carro` ;

CREATE TABLE IF NOT EXISTS `cpqd_portaria`.`carro` (
  `id_carro` VARCHAR(36) NOT NULL,
  `placa` VARCHAR(8) NULL,
  `modelo` VARCHAR(45) NULL,
  `cor` VARCHAR(15) NULL,
  `colaborador_id_colaborador` VARCHAR(36) NOT NULL,
  PRIMARY KEY (`id_carro`, `colaborador_id_colaborador`),
  INDEX `fk_carro_colaborador_idx` (`colaborador_id_colaborador` ASC) VISIBLE,
  CONSTRAINT `fk_carro_colaborador`
    FOREIGN KEY (`colaborador_id_colaborador`)
    REFERENCES `cpqd_portaria`.`pessoa` (`id_pessoa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cpqd_portaria`.`liberacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_portaria`.`liberacao` ;

CREATE TABLE IF NOT EXISTS `cpqd_portaria`.`liberacao` (
  `id_liberacao` VARCHAR(36) NOT NULL,
  `status_liberacao` VARCHAR(10) NULL,
  `tipo_liberacao` VARCHAR(15) NULL,
  `inicio` DATETIME NULL,
  `expiracao` DATETIME NULL,
  `empresa_liberacao` VARCHAR(25) NULL,
  `contato_liberacao` VARCHAR(45) NULL,
  `pessoa_id_pessoa` VARCHAR(36) NOT NULL,
  `carro_id_carro` VARCHAR(36) NOT NULL,
  PRIMARY KEY (`id_liberacao`, `pessoa_id_pessoa`, `carro_id_carro`),
  INDEX `fk_liberacao_pessoa1_idx` (`pessoa_id_pessoa` ASC) VISIBLE,
  INDEX `fk_liberacao_carro1_idx` (`carro_id_carro` ASC) VISIBLE,
  CONSTRAINT `fk_liberacao_pessoa1`
    FOREIGN KEY (`pessoa_id_pessoa`)
    REFERENCES `cpqd_portaria`.`pessoa` (`id_pessoa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_liberacao_carro1`
    FOREIGN KEY (`carro_id_carro`)
    REFERENCES `cpqd_portaria`.`carro` (`id_carro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cpqd_portaria`.`historico`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_portaria`.`historico` ;

CREATE TABLE IF NOT EXISTS `cpqd_portaria`.`historico` (
  `id_historico` VARCHAR(36) NOT NULL,
  `horario_historico` DATETIME NULL,
  `descricao` VARCHAR(10) NULL,
  `liberacao_id_liberacao` VARCHAR(36) NOT NULL,
  `liberacao_pessoa_id_pessoa` VARCHAR(36) NOT NULL,
  `liberacao_carro_id_carro` VARCHAR(36) NOT NULL,
  PRIMARY KEY (`id_historico`, `liberacao_id_liberacao`, `liberacao_pessoa_id_pessoa`, `liberacao_carro_id_carro`),
  INDEX `fk_historico_liberacao1_idx` (`liberacao_id_liberacao` ASC, `liberacao_pessoa_id_pessoa` ASC, `liberacao_carro_id_carro` ASC) VISIBLE,
  CONSTRAINT `fk_historico_liberacao1`
    FOREIGN KEY (`liberacao_id_liberacao` , `liberacao_pessoa_id_pessoa` , `liberacao_carro_id_carro`)
    REFERENCES `cpqd_portaria`.`liberacao` (`id_liberacao` , `pessoa_id_pessoa` , `carro_id_carro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cpqd_portaria`.`log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cpqd_portaria`.`log` ;

CREATE TABLE IF NOT EXISTS `cpqd_portaria`.`log` (
  `id_log` VARCHAR(36) NOT NULL,
  `horario_log` DATETIME NULL,
  `acao_log` VARCHAR(100) NULL,
  `usuario_id_usuario` VARCHAR(36) NOT NULL,
  PRIMARY KEY (`id_log`, `usuario_id_usuario`),
  INDEX `fk_log_usuario1_idx` (`usuario_id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_log_usuario1`
    FOREIGN KEY (`usuario_id_usuario`)
    REFERENCES `cpqd_portaria`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

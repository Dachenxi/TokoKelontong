-- Membuat Database tokokelontong;
CREATE DATABASE IF NOT EXISTS tokokelontong;

-- Membuat tabel Kategori;
CREATE TABLE
    `tokokelontong`.`kategori` (
        `idkategori` INT NOT NULL,
        `namaKategori` VARCHAR(25) NOT NULL,
        PRIMARY KEY (`idkategori`)
    );

-- Membuat tabel transaksi;
CREATE TABLE
    `tokokelontong`.`transaksi` (
        `idtransaksi` INT NOT NULL,
        `waktuTransaksi` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `totalBayar` DECIMAL(10, 2) NOT NULL,
        PRIMARY KEY (`idtransaksi`)
    );

-- Membuat tabel supplier;
CREATE TABLE
    `tokokelontong`.`supplier` (
        `idsupplier` INT NOT NULL,
        `namaSupplier` VARCHAR(255) NOT NULL,
        `alamat` VARCHAR(255) NULL,
        `noTelepon` INT NOT NULL,
        `email` VARCHAR(255) NULL,
        PRIMARY KEY (`idsupplier`)
    );

-- Mebuat tabel barang
CREATE TABLE
    `tokokelontong`.`barang` (
        `idBarang` INT NOT NULL,
        `idKategori` INT NULL,
        `idSupplier` INT NULL,
        `namaBarang` VARCHAR(255) NOT NULL,
        `hargaJual` DECIMAL(10, 2) NOT NULL,
        `hargaPack` DECIMAL(10, 2) NULL DEFAULT NULL,
        PRIMARY KEY (`idBarang`),
        INDEX `idKategori_idx` (`idKategori` ASC) VISIBLE,
        INDEX `idSupplier_idx` (`idSupplier` ASC) VISIBLE,
        CONSTRAINT `idKategori` FOREIGN KEY (`idKategori`) REFERENCES `tokokelontong`.`kategori` (`idkategori`) ON DELETE SET NULL ON UPDATE SET NULL,
        CONSTRAINT `idSupplier` FOREIGN KEY (`idSupplier`) REFERENCES `tokokelontong`.`supplier` (`idsupplier`) ON DELETE SET NULL ON UPDATE SET NULL
    );

-- Membuat tabel detailTransaksi
CREATE TABLE
    `tokokelontong`.`detailtransaksi` (
        `idDetailTransaksi` INT NOT NULL,
        `idTransaksi` INT NOT NULL,
        `idBarang` INT NOT NULL,
        `banyakBarang` INT NOT NULL,
        PRIMARY KEY (`idDetailTransaksi`),
        INDEX `idTransaksi_idx` (`idTransaksi` ASC) VISIBLE,
        INDEX `idBarang_idx` (`idBarang` ASC) VISIBLE,
        CONSTRAINT `idTransaksi` FOREIGN KEY (`idTransaksi`) REFERENCES `tokokelontong`.`transaksi` (`idtransaksi`) ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT `idBarang` FOREIGN KEY (`idBarang`) REFERENCES `tokokelontong`.`barang` (`idBarang`) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

-- Membuat tabel detailSupplier
CREATE TABLE
    `tokokelontong`.`detailsupplier` (
        `idDetailSupplier` INT NOT NULL,
        `idSupplier` INT NOT NULL,
        `idBarang` INT NOT NULL,
        `hargaBeli` DECIMAL(10, 2) NOT NULL,
        `waktuTransaksi` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `kuantitas` INT NOT NULL,
        PRIMARY KEY (`idDetailSupplier`),
        INDEX `idSupplier_idx` (`idSupplier` ASC) VISIBLE,
        INDEX `idBarang_idx` (`idBarang` ASC) VISIBLE,
        CONSTRAINT `idSupplierDetail` FOREIGN KEY (`idSupplier`) REFERENCES `tokokelontong`.`supplier` (`idsupplier`) ON DELETE NO ACTION ON UPDATE NO ACTION,
        CONSTRAINT `idBarangDetail` FOREIGN KEY (`idBarang`) REFERENCES `tokokelontong`.`barang` (`idBarang`) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

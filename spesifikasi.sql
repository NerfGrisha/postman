--
-- Struktur dari tabel `spesifikasi`
--

CREATE TABLE `spesifikasi` (
  `spesifikasi_id` int(11) NOT NULL,
  `laptop_id` int(11) DEFAULT NULL,
  `processor` varchar(100) DEFAULT NULL,
  `RAM` varchar(50) DEFAULT NULL,
  `penyimpanan` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `spesifikasi`
--

INSERT INTO `spesifikasi` (`spesifikasi_id`, `laptop_id`, `processor`, `RAM`, `penyimpanan`) VALUES
(1, 120, 'Intel Core i5', '8GB', '256GB SSD'),
(2, 121, 'AMD Ryzen 7', '16GB', '1TB HDD'),
(3, 122, 'Intel Core i7', '12GB', '512GB SSD'),
(4, 123, 'Intel Core i5', '8GB', '1TB HDD'),
(5, 124, 'AMD Ryzen 5', '8GB', '128GB SSD');

-- --------------------------------------------------------
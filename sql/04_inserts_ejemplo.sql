INSERT INTO usuarios (nombre, email) VALUES
('Luisa Espinal', 'luisa.espinal@email.com'),
('José Jaramillo', 'jose.jaramillo@email.com');

INSERT INTO metas_ahorro (id_usuario, meta, plazo, extra, mes_extra, cuota_mensual) VALUES
(1, 1100000, 6, 0, 0, 179925.80),
(2, 5000000, 12, 200000, 6, 381647.32);

INSERT INTO historial_calculos (id_usuario, meta, plazo, extra, mes_extra, cuota_mensual) VALUES
(1, 1100000, 6, 0, 0, 179925.80),
(2, 5000000, 12, 200000, 6, 381647.32);

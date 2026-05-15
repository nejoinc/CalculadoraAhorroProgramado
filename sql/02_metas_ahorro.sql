CREATE TABLE metas_ahorro (
    id_meta INT PRIMARY KEY IDENTITY,
    id_usuario INT REFERENCES usuarios(id_usuario),
    meta DECIMAL(18,2),
    plazo INT,
    extra DECIMAL(18,2) DEFAULT 0,
    mes_extra INT DEFAULT 0,
    tasa DECIMAL(6,4) DEFAULT 0.0075,
    cuota_mensual DECIMAL(18,2),
    fecha_calculo DATETIME DEFAULT GETDATE()
);
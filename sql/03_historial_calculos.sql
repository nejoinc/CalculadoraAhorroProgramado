CREATE TABLE historial_calculos (
    id_historial INT PRIMARY KEY IDENTITY,
    id_usuario INT REFERENCES usuarios(id_usuario),
    meta DECIMAL(18,2),
    plazo INT,
    extra DECIMAL(18,2) DEFAULT 0,
    mes_extra INT DEFAULT 0,
    tasa DECIMAL(6,4) DEFAULT 0.0075,
    valor_futuro_extra DECIMAL(18,2),
    factor_anualidad DECIMAL(18,6),
    cuota_mensual DECIMAL(18,2),
    fecha_calculo DATETIME DEFAULT GETDATE()
);
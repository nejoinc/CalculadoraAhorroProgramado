CREATE TABLE historial_calculos (
    id_historial INT IDENTITY(1,1) PRIMARY KEY,
    id_usuario INT FOREIGN KEY REFERENCES usuarios(id_usuario),
    meta DECIMAL(18,2) NOT NULL,
    plazo INT NOT NULL,
    extra DECIMAL(18,2) DEFAULT 0,
    mes_extra INT DEFAULT 0,
    tasa DECIMAL(6,4) DEFAULT 0.0075,
    valor_futuro_extra DECIMAL(18,2),
    factor_anualidad DECIMAL(18,6),
    cuota_mensual DECIMAL(18,2) NOT NULL,
    fecha_calculo DATETIME DEFAULT GETDATE()
);

def download_ephs(
    year=False,
    path="",
    sleep=30,
):
    import time
    from urllib.error import HTTPError
    from tqdm import tqdm

    ephs = disponibles(year=year)

    for año, onda in tqdm(
        list(zip(ephs.año, ephs.trimestre_u_onda)), desc="Descargando EPHs"
    ):
        try:
            get_microdata(
                year=año, trimester_or_wave=onda, type="hogar", download=True, path=path
            )
        except INDECError:
            print(
                "En el marco de la emergencia estadistica, el INDEC no publicó la base solicitada. Mas información en: https://www.indec.gob.ar/ftp/cuadros/sociedad/anexo_informe_eph_23_08_16.pdf"
            )
        except HTTPError:
            time.sleep(60)
            try:
                get_microdata(
                    year=año,
                    trimester_or_wave=onda,
                    type="hogar",
                    download=True,
                    path=path,
                )
            except HTTPError:
                raise BlockedConnectionError(
                    f"No se pudo descargar la EPH {año}, T{onda}, seguramente porque el sitio haya bloqueado la conexión. Reintentar en unos minutos con un sleep mayor."
                )
        time.sleep(15)  # Para no saturar al servidor


def disponibles(year=False):
    """
    Devuelve la lista de EPHs disponibles para descargar.
    Se puede especificar un año o un rango de años [desde, hasta]"""
    import pandas as pd
    import warnings

    warnings.warn(
        "La lista de EPH disponibles se actualizó el 19/5/23. Seguramente se pueda acceder a bases posteriores si INDEC no cambió el formato de los nombres, pero no está verificado. Probar si andan\n-------------------------------------------------------------------------------------------------",
        stacklevel=3,
    )

    df = pd.DataFrame(
        data=[
            (2022, 4, "Trimestre"),
            (2022, 3, "Trimestre"),
            (2022, 2, "Trimestre"),
            (2022, 1, "Trimestre"),
            (2021, 4, "Trimestre"),
            (2021, 3, "Trimestre"),
            (2021, 2, "Trimestre"),
            (2021, 1, "Trimestre"),
            (2020, 4, "Trimestre"),
            (2020, 3, "Trimestre"),
            (2020, 2, "Trimestre"),
            (2020, 1, "Trimestre"),
            (2019, 4, "Trimestre"),
            (2019, 3, "Trimestre"),
            (2019, 2, "Trimestre"),
            (2019, 1, "Trimestre"),
            (2018, 4, "Trimestre"),
            (2018, 3, "Trimestre"),
            (2018, 2, "Trimestre"),
            (2018, 1, "Trimestre"),
            (2017, 4, "Trimestre"),
            (2017, 3, "Trimestre"),
            (2017, 2, "Trimestre"),
            (2017, 1, "Trimestre"),
            (2016, 4, "Trimestre"),
            (2016, 3, "Trimestre"),
            (2016, 2, "Trimestre"),
            (2016, 1, "Trimestre"),
            (2015, 4, "Trimestre"),
            (2015, 3, "Trimestre"),
            (2015, 2, "Trimestre"),
            (2015, 1, "Trimestre"),
            (2014, 4, "Trimestre"),
            (2014, 3, "Trimestre"),
            (2014, 2, "Trimestre"),
            (2014, 1, "Trimestre"),
            (2013, 4, "Trimestre"),
            (2013, 3, "Trimestre"),
            (2013, 2, "Trimestre"),
            (2013, 1, "Trimestre"),
            (2012, 4, "Trimestre"),
            (2012, 3, "Trimestre"),
            (2012, 2, "Trimestre"),
            (2012, 1, "Trimestre"),
            (2011, 4, "Trimestre"),
            (2011, 3, "Trimestre"),
            (2011, 2, "Trimestre"),
            (2011, 1, "Trimestre"),
            (2010, 4, "Trimestre"),
            (2010, 3, "Trimestre"),
            (2010, 2, "Trimestre"),
            (2010, 1, "Trimestre"),
            (2009, 4, "Trimestre"),
            (2009, 3, "Trimestre"),
            (2009, 2, "Trimestre"),
            (2009, 1, "Trimestre"),
            (2008, 4, "Trimestre"),
            (2008, 3, "Trimestre"),
            (2008, 2, "Trimestre"),
            (2008, 1, "Trimestre"),
            (2007, 4, "Trimestre"),
            (2007, 3, "Trimestre"),
            (2007, 2, "Trimestre"),
            (2007, 1, "Trimestre"),
            (2006, 4, "Trimestre"),
            (2006, 3, "Trimestre"),
            (2006, 2, "Trimestre"),
            (2006, 1, "Trimestre"),
            (2005, 4, "Trimestre"),
            (2005, 3, "Trimestre"),
            (2005, 2, "Trimestre"),
            (2005, 1, "Trimestre"),
            (2004, 4, "Trimestre"),
            (2004, 3, "Trimestre"),
            (2004, 2, "Trimestre"),
            (2004, 1, "Trimestre"),
            (2003, 4, "Trimestre"),
            (2003, 3, "Trimestre"),
            (2003, 2, "Onda"),
            (2003, 1, "Onda"),
            (2002, 2, "Onda"),
            (2002, 1, "Onda"),
            (2001, 2, "Onda"),
            (2001, 1, "Onda"),
            (2000, 2, "Onda"),
            (2000, 1, "Onda"),
            (1999, 2, "Onda"),
            (1999, 1, "Onda"),
            (1998, 2, "Onda"),
            (1998, 1, "Onda"),
            (1997, 2, "Onda"),
            (1997, 1, "Onda"),
            (1996, 2, "Onda"),
            (1996, 1, "Onda"),
        ],
        columns=["año", "trimestre_u_onda", "Tipo"],
    )

    # No data:
    df = df[~((df["año"] == 2007) & (df["trimestre_u_onda"] == 3))]
    df = df[~((df["año"] == 2003) & (df["trimestre_u_onda"] == 2))]
    # Cambio para trimestre/onda de 2003:
    df.loc[(df["año"] == 2003) & (df["trimestre_u_onda"] == 1), "trimestre_u_onda"] = 1
    df.loc[(df["año"] == 2003) & (df["trimestre_u_onda"] == 3), "trimestre_u_onda"] = 3
    df.loc[(df["año"] == 2003) & (df["trimestre_u_onda"] == 4), "trimestre_u_onda"] = 4
    if year:
        try:
            df = df[df["año"].between(year[0], year[1])]
        except:
            df = df[df["año"] == year]

    return df


def get_microdata(
    year, trimester_or_wave, type="hogar", advertencias=True, download=False, path=""
):
    """Genera un DataFrame con los microdatos de la
    Hasta 2018, usa los datos desde la página de Humai (ihum.ai).
    Desde 2019, los descarga desde la página de INDEC (salvo que cambie el formato del nombre de los archivos y links, debería andar para años posteriores, pero se probó hasta 2021)

    Args:
        @year (int): Año de la EPH

        @trimester_or_wave (int): Trimestre (si año >= 2003) u onda (si año < 2003)

        @type (str, optional): Tipo de base (hogar o individual). Default: 'hogar'

        @advertencias (bool, optional): Mostrar advertencias metodológicas de INDEC. Defaults to True.

        @download (bool, optional): Descargar los csv de las EPH (en vez de cargarlos directamente a la RAM). Defaults to False.

        @path (str, optional): Path donde se descargan los archivos. Defaults to ''.

    Returns:
        pandas.DataFrame: DataFrame con los microdatos de la EPH
    """

    from zipfile import ZipFile
    from io import BytesIO
    import os
    import wget
    import fnmatch
    import requests
    import pandas as pd

    handle_exceptions_microdata(year, trimester_or_wave, type, advertencias)

    if year < 2019:
        if year >= 2003 and trimester_or_wave is not None:
            url = f"https://datasets-humai.s3.amazonaws.com/eph/{type}/base_{type}_{year}T{trimester_or_wave}.csv"
            link = url

        elif year < 2003 and trimester_or_wave is not None:
            url = f"https://datasets-humai.s3.amazonaws.com/eph/{type}/base_{type}_{year}O{trimester_or_wave}.csv"
            link = url
        if download:
            filename = url.split("/")[-1]

            if os.path.exists(filename):
                os.remove(filename)

            filename = wget.download(url, out=path)
            df = pd.read_csv(filename, low_memory=False, encoding="unicode_escape")
        else:
            df = pd.read_csv(url, low_memory=False, encoding="unicode_escape")
    elif year >= 2019:
        if trimester_or_wave == 1:
            suffix = "er"
        elif trimester_or_wave == 2:
            suffix = "do"
        elif trimester_or_wave == 3:
            suffix = "er"
        elif trimester_or_wave == 4:
            suffix = "to"

        try:
            query_str = f"https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph/EPH_usu_{trimester_or_wave}_Trim_{year}_txt.zip"
            print(
                "Descomprimiendo...(si tarda mas de 1 min reintentar, seguramente la página de INDEC esté caída)",
                end="\r",
            )
            r = requests.get(query_str)
            files = ZipFile(BytesIO(r.content))
            link = query_str
        except:
            try:
                query_str = f"https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph/EPH_usu_{trimester_or_wave}{suffix}_Trim_{year}_txt.zip"
                print(
                    "Descomprimiendo...(si tarda mas de 1 min reintentar, seguramente la página de INDEC esté caída)",
                    flush=True,
                    end="\r",
                )
                r = requests.get(query_str)
                files = ZipFile(BytesIO(r.content))
                link = query_str
            except:
                try:
                    query_str = f"https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph/EPH_usu_{trimester_or_wave}{suffix}Trim_{year}_txt.zip"
                    print(
                        "Descomprimiendo...(si tarda mas de 1 min reintentar, seguramente la página de INDEC esté caída)",
                        flush=True,
                        sep="",
                        end="\r",
                    )
                    r = requests.get(query_str)
                    files = ZipFile(BytesIO(r.content))
                    link = query_str
                except:
                    raise ValueError(
                        f"No se encontró el archivo de microdatos de la EPH para el año {year} y el trimestre {trimester_or_wave}"
                    )
        try:
            df = pd.read_csv(
                files.open(
                    f"EPH_usu_{trimester_or_wave}{suffix}_Trim_{year}_txt/usu_{type}_T{trimester_or_wave}{str(year)[-2:]}.txt.txt"
                ),
                delimiter=";",
            )
            if download:
                df.to_csv(
                    f"{path}/base_{type}_{year}T{trimester_or_wave}.csv", index=False
                )
            print(f"Se descargó la EPH {year}T{trimester_or_wave} desde {link}")
            return df
        except:
            try:
                for file in files.namelist():
                    if fnmatch.fnmatch(file, f"*{type}*.txt"):
                        df = pd.read_csv(
                            files.open(file), low_memory=False, delimiter=";"
                        )
                        if download:
                            df.to_csv(
                                f"{path}/base_{type}_{year}T{trimester_or_wave}.csv",
                                index=False,
                            )
                        print(
                            f"Se descargó la EPH {year}T{trimester_or_wave} desde {link}"
                        )
                        return df

            except:
                raise ValueError(
                    "No se encontró el archivo de microdatos en la base de INDEC"
                )
    print(f"Se descargó la EPH {year}T{trimester_or_wave} desde {link}")
    return df


def handle_exceptions_microdata(year, trimester_or_wave, type, advertencias):
    import warnings

    if not isinstance(year, int):
        raise YearError("El año tiene que ser un numero")

    if not isinstance(trimester_or_wave, int) and not isinstance(
        trimester_or_wave, int
    ):
        raise TrimesterError(
            "Debe haber trimestre desde 2003 en adelante (1, 2, 3 o 4) \
                        u onda si es antes de 2003 (1 o 2)"
        )

    if (
        isinstance(trimester_or_wave, int) and trimester_or_wave not in [1, 2, 3, 4]
    ) and (year >= 2003):
        raise TrimesterError("Trimestre/Onda inválido (debe ser entre 1 y 4)")

    # if (isinstance(trimester_or_wave,int) and trimester_or_wave not in [1,2]) and (year <= 2003):
    #     raise WaveError("Onda inválida (debe ser 1 o 2)")

    if type not in ["individual", "hogar"]:
        raise TypeError("Seleccione un tipo de base válido: individual u hogar")

    if year == 2007 and trimester_or_wave == 3:
        raise INDECError(
            "\nLa informacion correspondiente al tercer trimestre \
2007 no está disponible ya que los aglomerados Mar del Plata-Batan, \
Bahia Blanca-Cerri y Gran La Plata no fueron relevados por causas \
de orden administrativo, mientras que los datos correspondientes al \
Aglomerado Gran Buenos Aires no fueron relevados por paro del \
personal de la EPH"
        )

    if (year == 2015 and trimester_or_wave in [3, 4]) | (
        year == 2016 and trimester_or_wave == 3
    ):
        raise INDECError(
            "En el marco de la emergencia estadistica, el INDEC no publicó la base solicitada. \
                mas información en: https://www.indec.gob.ar/ftp/cuadros/sociedad/anexo_informe_eph_23_08_16.pdf"
        )

    if year == 2003 and trimester_or_wave in [2]:
        raise INDECError(
            "Debido al cambio metodológico en la EPH, en 2003 la encuesta se realizó para el primer semestre y los dos últimos trimestres"
        )

    if advertencias:
        if year >= 2007 and year <= 2015:
            warnings.warn(
                """\n
Las series estadisticas publicadas con posterioridad a enero 2007 y hasta diciembre \
2015 deben ser consideradas con reservas, excepto las que ya hayan sido revisadas en \
2016 y su difusion lo consigne expresamente. El INDEC, en el marco de las atribuciones \
conferidas por los decretos 181/15 y 55/16, dispuso las investigaciones requeridas para \
establecer la regularidad de procedimientos de obtencion de datos, su procesamiento, \
elaboracion de indicadores y difusion.
Más información en: https://www.indec.gob.ar/ftp/cuadros/sociedad/anexo_informe_eph_23_08_16.pdf 
(Se puede desactivar este mensaje con advertencias=False)\n-------------------------------------------------------------------------------------------------""",
                AdvertenciaINDEC,
                stacklevel=3,
            )


class INDECError(Exception):
    pass


class WaveError(Exception):
    pass


class TrimesterError(Exception):
    pass


class YearError(Exception):
    pass


class BlockedConnectionError(Exception):
    pass


class AdvertenciaINDEC(Warning):
    pass

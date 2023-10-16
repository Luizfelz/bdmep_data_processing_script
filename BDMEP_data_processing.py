import pandas as pd
import tkinter as tk
import webbrowser
import warnings
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkinter import filedialog
warnings.simplefilter("ignore")

file_path = ''

dict_columns_names ={
 'Data Medicao':'date_YYYYMMDD',
 'Hora Medicao':'hour_HHMM',
 'CH (NUVENS ALTAS)(codigo)':'high_clouds_code',
 'CL (NUVENS BAIXAS)(codigo)':'lower_clouds_code',
 'CM (NUVENS MEDIAS)(codigo)':'medium_clouds_code',
 'NEBULOSIDADE, HORARIA(décimos)':'hourly_cloudy_tenth',
 'PRECIPITACAO TOTAL, HORARIO(mm)':'hourly_total_preciptation_mm',
 'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA(mB)':'hourly_atm_pressure_station_level_mB',
 'PRESSAO ATMOSFERICA AO NIVEL DO MAR, HORARIA(mB)':'hourly_atm_pressure_sea_level_mB',
 'TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)':'hourly_dry_bulb_air_temperature_celsius',
 'TEMPERATURA DO AR - BULBO UMIDO, HORARIA(°C)':'hourly_humid_bulb_air_temperature_celsius',
 'TEMPERATURA DO PONTO DE ORVALHO(°C)':'dew_point_temperature_celsius',
 'UMIDADE RELATIVA DO AR, HORARIA(%)':'hourly_relative_air_humidity_percent',
 'VENTO, DIRECAO HORARIA(codigo)':'hourly_wind_direction_code',
 'VENTO, VELOCIDADE HORARIA(m/s)':'hourly_wind_speed_metersPerSec',
 'VISIBILIDADE, HORARIA(codigo)':'hourly_visibility_code',
 'DIRECAO PREDOMINANTE DO VENTO, MENSAL(° (gr))':'monthly_predominant_wind_direction_degrees',
 'EVAPORACAO DO PICHE, MENSAL(mm)':'monthly_piche_evaporation_mm',
 'EVAPOTRANSPIRACAO POTENCIAL, BH MENSAL(mm)':'monthly_potencial_evapotranspiration_mm',
 'EVAPOTRANSPIRACAO REAL, BH MENSAL(mm)':'monthly_real_evapotranspiration_mm',
 'INSOLACAO TOTAL, MENSAL(h)':'monthly_total_insolation_h',
 'NEBULOSIDADE, MEDIA MENSAL(décimos)':'monthly_average_cloudy_tenth',
 'NUMERO DE DIAS COM PRECIP. PLUV, MENSAL(número)':'monthly_number_of_days_with_rainfall_days',
 'PRECIPITACAO TOTAL, MENSAL(mm)':'monthly_total_precipitation_mm',
 'PRESSAO ATMOSFERICA, MEDIA MENSAL(mB)':'monthly_average_atm_pressure_mB',
 'TEMPERATURA MAXIMA MEDIA, MENSAL(°C)':'monthly_average_max_temperature_celsius',
 'TEMPERATURA MEDIA COMPENSADA, MENSAL(°C)':'monthly_compensated_average_temperature_celsius',
 'TEMPERATURA MINIMA MEDIA, MENSAL(°C)':'monthly_average_min_temperature_celsius',
 'UMIDADE RELATIVA DO AR, MEDIA MENSAL(%)':'monthly_average_relative_air_humidity_percent',
 'VENTO, VELOCIDADE MAXIMA MENSAL(m/s)':'monthly_max_wind_speed_metersPerSec',
 'VENTO, VELOCIDADE MEDIA MENSAL(m/s)':'monthly_average_wind_speed_metersPerSec',
 'VISIBILIDADE, MEDIA MENSAL(codigo)':'monthly_average_visibility_code',
 'EVAPORACAO DO PICHE, DIARIA(mm)':'daily_piche_evaporation_mm',
 'INSOLACAO TOTAL, DIARIO(h)':'daily_total_insolation_h',
 'PRECIPITACAO TOTAL, DIARIO(mm)':'daily_total_precipitation_mm',
 'TEMPERATURA MAXIMA, DIARIA(°C)':'daily_max_temperature_celsius',
 'TEMPERATURA MEDIA COMPENSADA, DIARIA(°C)':'daily_compensated_average_temperature_celsius',
 'TEMPERATURA MINIMA, DIARIA(°C)':'daily_min_temperature_celsius',
 'UMIDADE RELATIVA DO AR, MEDIA DIARIA(%)':'daily_average_relative_air_humidity_percent',
 'UMIDADE RELATIVA DO AR, MINIMA DIARIA(%)':'daily_min_relative_air_humidity_percent',
 'VENTO, VELOCIDADE MEDIA DIARIA(m/s)':'daily_average_wind_speed_metersPerSec',
 'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)':'daily_total_precipitation_percent',
 'PRESSAO ATMOSFERICA MEDIA DIARIA (AUT)(mB)':'daily_average_atm_pressure_mB',
 'TEMPERATURA DO PONTO DE ORVALHO MEDIA DIARIA (AUT)(°C)':'daily_average_dew_point_temperature_celsius',
 'TEMPERATURA MAXIMA, DIARIA (AUT)(°C)':'daily_max_temperature_celsius',
 'TEMPERATURA MEDIA, DIARIA (AUT)(°C)':'daily_average_temperature_celsius',
 'TEMPERATURA MINIMA, DIARIA (AUT)(°C)':'daily_min_temperature_celsius',
 'UMIDADE RELATIVA DO AR, MEDIA DIARIA (AUT)(%)':'daily_average_relative_air_humidity_percent',
 'UMIDADE RELATIVA DO AR, MINIMA DIARIA (AUT)(%)':'daily_min_relative_air_humidity_percent',
 'VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)':'daily_max_wind_gust_metersPerSec',
 'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)':'daily_average_wind_speed_metersPerSec',
 'NUMERO DE DIAS COM PRECIP. PLUV, MENSAL (AUT)(número)':'monthly_number_of_days_with_rainfall_days',
 'PRECIPITACAO TOTAL, MENSAL (AUT)(mm)':'monthly_total_precipitation_mm',
 'PRESSAO ATMOSFERICA, MEDIA MENSAL (AUT)(mB)':'monthly_average_atm_pressure_mB',
 'TEMPERATURA MEDIA, MENSAL (AUT)(°C)':'monthly_average_temperature_celsius',
 'VENTO, VELOCIDADE MAXIMA MENSAL (AUT)(m/s)':'monthly_max_wind_speed_metersPerSec',
 'VENTO, VELOCIDADE MEDIA MENSAL (AUT)(m/s)':'monthly_average_wind_speed_metersPerSec',
 'PRESSAO ATMOSFERICA REDUZIDA NIVEL DO MAR, AUT(mB)':'hourly_reduced_atm_pressure_sea_level_mB',
 'PRESSAO ATMOSFERICA MAX.NA HORA ANT. (AUT)(mB)':'hourly_max_atm_pressure_previous_hour_mB',
 'PRESSAO ATMOSFERICA MIN. NA HORA ANT. (AUT)(mB)':'hourly_min_atm_pressure_previous_hour_mB',
 'RADIACAO GLOBAL(Kj/m²)':'hourly_global_radiation_kJPerMeterSquared',
 'TEMPERATURA DA CPU DA ESTACAO(°C)':'hourly_station_cpu_temperature_celsius',
 'TEMPERATURA MAXIMA NA HORA ANT. (AUT)(°C)':'hourly_max_temperature_previous_hour_celsius',
 'TEMPERATURA MINIMA NA HORA ANT. (AUT)(°C)':'hourly_min_temperature_previous_hour_celsius',
 'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT)(°C)':'hourly_max_dew_point_temperature_previous_hour_celsius',
 'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT)(°C)':'hourly_min_dew_point_temperature_previous_hour_celsius',
 'TENSAO DA BATERIA DA ESTACAO(V)':'hourly_station_battery_voltage_Volts',
 'UMIDADE REL. MAX. NA HORA ANT. (AUT)(%)':'hourly_max_relative_air_humidity_previous_hour_percent',
 'UMIDADE REL. MIN. NA HORA ANT. (AUT)(%)':'hourly_min_relative_air_humidity_previous_hour_percent',
 'VENTO, DIRECAO HORARIA (gr)(° (gr))':'hourly_wind_direction_degrees',
 'VENTO, RAJADA MAXIMA(m/s)':'hourly_max_wind_gust_metersPerSec'
}

dict_sheet_names = {
  'allYearsPerMonth':'Returns the average value for each month, considering the complete data series',
  'first10yearsPerMonth':'Returns the average value for each month, considering only the first 10 years of the data series',
  'last10yearsPerMonth':'Returns the average value for each month, considering only the last 10 years of the data series',
  'allYearPerYear':'Returns the average value for each year, considering the complete data series',
  'first10yearsPerYear':'Returns the average value for each year, considering only the first 10 years of the data series',
  'last10yearsPerYear':'Returns the average value for each year, considering only the last 10 years of the data series'
}

def create_dataframe(file_path):
  df = pd.read_csv(file_path, delimiter=';', skiprows=10)
  return df


def get_csv_header_info(file_path):
  df_infos = pd.read_csv(file_path, delimiter=';', nrows=9, header=None, names=['station_infos'])
  return df_infos


def get_instructions_sheet(dict_columns_names):
  df = pd.DataFrame(list(dict_columns_names.items()), columns=['BDMEP_original_variable_name', 'renamed_variable'])
  df = df[['renamed_variable','BDMEP_original_variable_name']]
  df['__________'] = ''
  df_temp = pd.DataFrame(list(dict_sheet_names.items()), columns=['sheet_name','description'])
  df['sheet_name'] = df_temp['sheet_name']
  df['description'] = df_temp['description']
  df.fillna('', inplace=True)
  return df


def remove_unnamed_colum(df):
  for column in df.columns:
    if 'unnamed' in column.lower():
      df = df.drop(column, axis=1) 
  return df


def rename_columns_names(df):
  renamed_df_columns_names = []
  for column in df.columns:
    renamed_df_columns_names.append(dict_columns_names.get(column))
  return renamed_df_columns_names


def rename_columns_in_df(df, renamed_df_columns_names):
  new_columns = dict(zip(df.columns, renamed_df_columns_names))
  df = df.rename(columns=new_columns)
  return df


def create_renamed_df():
  df = create_dataframe(file_path)
  df = remove_unnamed_colum(df)
  renamed_df_columns_names = rename_columns_names(df)
  df = rename_columns_in_df(df, renamed_df_columns_names)
  return df


def get_data_start_date():
  df_temp = create_dataframe(file_path)
  data_start_date = str(df_temp[df_temp.columns[0]].head(1))
  data_start_date = data_start_date.split('-')[0].split(' ')
  data_start_date = data_start_date[-1]
  return data_start_date # returns string year (example: '2010')


def get_data_final_date():
  df_temp = create_dataframe(file_path)
  data_final_date = str(df_temp[df_temp.columns[0]].tail(1))
  data_final_date = data_final_date.split('-')[0].split(' ')
  data_final_date = data_final_date[-1]
  return data_final_date # returns string year (example: '2010')


def calculates_average_values_for_period(df):
  column_names = df.columns
  columns_summed_values = []
  columns_counted_values = []
  for col_name in column_names:
    if ('sum' in col_name):
      columns_summed_values.append(col_name)
    if ('count' in col_name):
      columns_counted_values.append(col_name)
  columns_zipped = list(zip(columns_summed_values, columns_counted_values))
  for column1, column2 in columns_zipped:
    new_column_name = column1.split('_')[0:-1]
    new_column_name = '_'.join(new_column_name)
    df[new_column_name] = df[column1] / df[column2]
  return df


def filters_final_df_columns(df_average_values_calculated):
  filtered_df_columns = [column for column in df_average_values_calculated.columns if 'sum' not in column and 'count' not in column]
  final_result = df_average_values_calculated.select(*filtered_df_columns)
  return final_result


def get_final_result_df():
  df = create_renamed_df()
  df['date_YYYYMMDD'] = pd.to_datetime(df['date_YYYYMMDD'])
  numeric_columns = df.select_dtypes(include=[float, int]).columns
  return df, numeric_columns


def get_final_result_file_name():
  header_complete_info = get_csv_header_info(file_path)
  city_name = header_complete_info.iloc[0][0]
  city_name = city_name.split(':')[1].strip().title()
  city_name = ''.join(city_name.split(' '))
  station_code = header_complete_info.iloc[1][0]
  station_code = station_code.split(':')[1].strip()
  periodicity = header_complete_info.iloc[8][0]
  periodicity = periodicity.split(':')[1].strip().lower()
  prefix_file_path  = file_path.split('/')
  final_result_file_name = '/'.join(prefix_file_path[0:-1]) + f'/{city_name}_station[{station_code}]_periodicity[{periodicity}]'
  return final_result_file_name


def save_all_final_result_to_xlsx_file():
  final_result_file_name = get_final_result_file_name()
  with pd.ExcelWriter(f'{final_result_file_name}.xlsx') as excel_writer: #, engine='openpyxl'
    station_infos = get_csv_header_info(file_path)
    station_infos.to_excel(excel_writer, sheet_name='stationInfos', index=False)
    
    instructions_sheet = get_instructions_sheet(dict_columns_names)
    instructions_sheet.to_excel(excel_writer, sheet_name='instructions', index=False)

    # SQL 1
    df, numeric_columns = get_final_result_df()
    df = sql_complete_series_grouped_by_month(df, numeric_columns)
    df.to_excel(excel_writer, sheet_name='allYearsPerMonth', index=False)

    # SQL 2
    df, numeric_columns = get_final_result_df()
    df = sql_first_ten_years_grouped_by_month(df, numeric_columns)
    df.to_excel(excel_writer, sheet_name='first10yearsPerMonth', index=False)

    #SQL 3
    df, numeric_columns = get_final_result_df()
    df = sql_last_ten_years_grouped_by_month(df, numeric_columns)
    df.to_excel(excel_writer, sheet_name='last10yearsPerMonth', index=False)

    #SQL 4
    df, numeric_columns = get_final_result_df()
    df = sql_complete_series_grouped_by_year(df, numeric_columns)
    df.to_excel(excel_writer, sheet_name='allYearsPerYear', index=False)

    #SQL5
    df, numeric_columns = get_final_result_df()
    df = sql_first_ten_years_grouped_by_year(df, numeric_columns)
    df.to_excel(excel_writer, sheet_name='first10yearsPerYear', index=False)

    #SQL 6
    df, numeric_columns = get_final_result_df()
    df = sql_last_ten_years_grouped_by_year(df, numeric_columns)
    df.to_excel(excel_writer, sheet_name='last10yearsPerYear', index=False)


def main():
  def open_link1():
    webbrowser.open_new('https://github.com/Luizfelz')

  def open_link2():
      webbrowser.open_new('https://www.linkedin.com/in/luizfsf/')

  def open_link3():
      webbrowser.open_new('http://lattes.cnpq.br/2195347611352083')

  def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text='Operation completed! \nResult file saved in the same directory as the csv file!')
    save_all_final_result_to_xlsx_file()

  app = tk.Tk()
  app.title('BDMEP data processing')
  app.geometry('500x250')

  instruction_text = 'Select the CSV file using the "BROWSE" button below.'
  instruction_label = tk.Label(app, text=instruction_text, justify='center', font=('Helvetica', 14))
  instruction_label.pack(pady=(20, 10))

  browse_button = tk.Button(app, text='BROWSE', command=browse_file, bg='#E0E0E0', font=('Helvetica', 12, 'bold'))
  browse_button.pack(pady=20)

  label = tk.Label(app, text='', font=('Helvetica', 14))
  label.pack()

  link_frame = tk.Frame(app)
  link_frame.pack(pady=20)

  made_by_label = tk.Label(link_frame, text='Made by Luiz Fonseca: ', font=('Helvetica', 10, 'bold'))
  made_by_label.pack(side='left', padx=5)

  link1_button = tk.Button(link_frame, text='GitHub', command=open_link1, bg='#838383', font=('Helvetica', 10, 'bold'))
  link1_button.pack(side='left', padx=5)

  link2_button = tk.Button(link_frame, text='Linkedin', command=open_link2, bg='#838383', font=('Helvetica', 10, 'bold'))
  link2_button.pack(side='left', padx=5)

  link3_button = tk.Button(link_frame, text='Lattes', command=open_link3, bg='#838383', font=('Helvetica', 10, 'bold'))
  link3_button.pack(side='left', padx=5)

  app.mainloop()


def sql_complete_series_grouped_by_month(df, numeric_columns):
  df['month'] = df['date_YYYYMMDD'].dt.strftime('%b')
  for col in numeric_columns:
    df[f'{col}_sum'] = df.groupby(['month'])[col].transform('sum')
    df[f'{col}_count'] = df.groupby(['month'])[col].transform('count')
  df = calculates_average_values_for_period(df)
  df = df.drop_duplicates(subset=['month'])
  df = df.filter(regex=f'^(?:(?!.*_sum)(?!.*_count).*$)')
  df = df.drop('date_YYYYMMDD', axis=1)
  df = df[['month'] + [col for col in df.columns if col != 'month']]
  df = df.reset_index(drop=True)
  return df

def sql_first_ten_years_grouped_by_month(df, numeric_columns):
  data_start_date = get_data_start_date()
  data_start_date = datetime.strptime(data_start_date, '%Y').date()
  data_first_ten_years = str(data_start_date + relativedelta(years=10))
  data_first_ten_years = int(data_first_ten_years.split('-')[0])
  df['month'] = df['date_YYYYMMDD'].dt.strftime('%b')
  df['year'] = df['date_YYYYMMDD'].dt.year
  df = df[df['year'] < data_first_ten_years]
  for col in numeric_columns:
    df[f'{col}_sum'] = df.groupby(['month'])[col].transform('sum')
    df[f'{col}_count'] = df.groupby(['month'])[col].transform('count')
  df = calculates_average_values_for_period(df)
  df = df.drop_duplicates(subset=['month'])
  df = df.filter(regex=f'^(?:(?!.*_sum)(?!.*_count).*$)')
  df = df.drop(['date_YYYYMMDD', 'year'], axis=1)
  df = df[['month'] + [col for col in df.columns if col != 'month']]
  df = df.reset_index(drop=True)
  return df

def sql_last_ten_years_grouped_by_month(df, numeric_columns):
  data_final_date = get_data_final_date()
  data_final_date = datetime.strptime(data_final_date, '%Y').date()
  data_last_ten_years = str(data_final_date - relativedelta(years=10))
  data_last_ten_years = int(data_last_ten_years.split('-')[0])
  df['month'] = df['date_YYYYMMDD'].dt.strftime('%b')
  df['year'] = df['date_YYYYMMDD'].dt.year
  df = df[df['year'] > data_last_ten_years]
  for col in numeric_columns:
    df[f'{col}_sum'] = df.groupby(['month'])[col].transform('sum')
    df[f'{col}_count'] = df.groupby(['month'])[col].transform('count')
  df = calculates_average_values_for_period(df)
  df = df.drop_duplicates(subset=['month'])
  df = df.filter(regex=f'^(?:(?!.*_sum)(?!.*_count).*$)')
  df = df.drop(['date_YYYYMMDD', 'year'], axis=1)
  df = df[['month'] + [col for col in df.columns if col != 'month']]
  df = df.reset_index(drop=True)
  return df


def sql_complete_series_grouped_by_year(df, numeric_columns):
  df['year'] = df['date_YYYYMMDD'].dt.year
  for col in numeric_columns:
    df[f'{col}_sum'] = df.groupby(['year'])[col].transform('sum')
    df[f'{col}_count'] = df.groupby(['year'])[col].transform('count')
  df = calculates_average_values_for_period(df)
  df = df.drop_duplicates(subset=['year'])
  df = df.filter(regex=f'^(?:(?!.*_sum)(?!.*_count).*$)')
  df = df.drop('date_YYYYMMDD', axis=1)
  df = df[['year'] + [col for col in df.columns if col != 'year']]
  df = df.reset_index(drop=True)
  return df


def sql_first_ten_years_grouped_by_year(df, numeric_columns):
  data_start_date = get_data_start_date()
  data_start_date = datetime.strptime(data_start_date, '%Y').date()
  data_first_ten_years = str(data_start_date + relativedelta(years=10))
  data_first_ten_years = int(data_first_ten_years.split('-')[0])
  df['year'] = df['date_YYYYMMDD'].dt.year
  df = df[df['year'] < data_first_ten_years]
  for col in numeric_columns:
    df[f'{col}_sum'] = df.groupby(['year'])[col].transform('sum')
    df[f'{col}_count'] = df.groupby(['year'])[col].transform('count')
  df = calculates_average_values_for_period(df)
  df = df.drop_duplicates(subset=['year'])
  df = df.filter(regex=f'^(?:(?!.*_sum)(?!.*_count).*$)')
  df = df.drop('date_YYYYMMDD', axis=1)
  df = df[['year'] + [col for col in df.columns if col != 'year']]
  df = df.reset_index(drop=True)
  return df


def sql_last_ten_years_grouped_by_year(df, numeric_columns):
  data_final_date = get_data_final_date()
  data_final_date = datetime.strptime(data_final_date, '%Y').date()
  data_last_ten_years = str(data_final_date - relativedelta(years=10))
  data_last_ten_years = int(data_last_ten_years.split('-')[0])
  df['year'] = df['date_YYYYMMDD'].dt.year
  df = df[df['year'] > data_last_ten_years]
  for col in numeric_columns:
    df[f'{col}_sum'] = df.groupby(['year'])[col].transform('sum')
    df[f'{col}_count'] = df.groupby(['year'])[col].transform('count')
  df = calculates_average_values_for_period(df)
  df = df.drop_duplicates(subset=['year'])
  df = df.filter(regex=f'^(?:(?!.*_sum)(?!.*_count).*$)')
  df = df.drop('date_YYYYMMDD', axis=1)
  df = df[['year'] + [col for col in df.columns if col != 'year']]
  df = df.reset_index(drop=True)
  return df

main()